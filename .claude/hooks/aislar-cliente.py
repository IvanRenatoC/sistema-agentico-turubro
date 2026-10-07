#!/usr/bin/env python3
"""aislar-cliente.py — impide que el trabajo de un cliente lea o escriba en otro.

Contrato (docs/ARQUITECTURA.md §5 y regla R13 de CLAUDE.md):
  Hook PreToolUse de Claude Code. Recibe por stdin el JSON de la herramienta que
  el agente está por usar y decide si la deja pasar.

  - Cliente activo: la carpeta `clientes/<cliente>/` que se abrió como proyecto
    (CLAUDE_PROJECT_DIR) o, en su defecto, el directorio de trabajo.
  - Se bloquea toda ruta dentro de `clientes/<otro>/`.
  - Se bloquea toda búsqueda (Glob, Grep, Bash) cuyo alcance contenga la carpeta
    `clientes/` completa: barrería a todos los clientes a la vez.
  - Si la sesión se abrió en la raíz del repo, no hay cliente activo: se
    bloquea el acceso a cualquier cliente real.

Excepciones, todas deliberadas:
  - Las carpetas con prefijo `_` (`_PLANTILLA/`, `_cliente-ejemplo/`) no son
    clientes reales y se pueden leer desde cualquier sesión.
  - Una carpeta de cliente que todavía no existe se puede crear: no hay nada que
    contaminar.
  - Los archivos sueltos en `clientes/` (su README) se pueden leer.

Requisitos que este hook cumple, y que hay que preservar al modificarlo:
  1. Bloquea con código 2 y explica por qué en stderr: el agente lee el mensaje
     y puede corregir el rumbo.
  2. Ante una entrada que no entiende no bloquea: avisa con código 1 y deja
     pasar. Un hook roto no puede paralizar la oficina.
  3. Sin dependencias externas.

Límite conocido: en Bash la revisión es por las rutas que aparecen escritas en
el comando. Un comando que construye la ruta en tiempo de ejecución no se
detecta. Es una red, no un muro: la regla R13 sigue siendo la que manda.
"""

import json
import os
import pathlib
import re
import shlex
import sys

RAIZ = pathlib.Path(__file__).resolve().parents[2]
CLIENTES = RAIZ / "clientes"
GLOB = re.compile(r"[*?\[{]")
# Comandos de shell que leen contenido o recorren carpetas: solo en ellos un
# directorio amplio (".", "..", la raíz) cuenta como barrido de todos los clientes.
LECTORES = re.compile(r"(^|[\s;|&(])(grep|egrep|rg|ag|ack|find|tree|du|cat|head|tail|less|"
                      r"more|xargs|ls\s+-\w*R|cp\s+-\w*[rR]|rsync|tar|zip)\b")
# Una ficha de shell que tiene forma de ruta: sin comillas, llaves, dos puntos ni variables.
RUTA_SHELL = re.compile(r"^[\w.~/*?\[\]@+,=-]+$")


def cliente_de(ruta):
    """Devuelve el nombre del cliente al que pertenece una ruta, o None."""
    try:
        rel = ruta.relative_to(CLIENTES)
    except ValueError:
        return None
    if not rel.parts:
        return None
    nombre = rel.parts[0]
    if (CLIENTES / nombre).is_file():
        return None
    return nombre


def cubre_clientes(ruta):
    """True si una búsqueda con esta raíz recorrería la carpeta clientes/ completa."""
    return ruta == CLIENTES or ruta in CLIENTES.parents


def resolver(texto, base):
    p = pathlib.Path(os.path.expanduser(texto))
    if not p.is_absolute():
        p = base / p
    return pathlib.Path(os.path.normpath(p))


def rutas_de(herramienta, entrada, base):
    """Las rutas que toca la herramienta, y si cada una es el alcance de una búsqueda."""
    rutas = []
    if herramienta in ("Read", "Write", "Edit", "MultiEdit"):
        if entrada.get("file_path"):
            rutas.append((resolver(entrada["file_path"], base), False))
    elif herramienta == "NotebookEdit":
        if entrada.get("notebook_path"):
            rutas.append((resolver(entrada["notebook_path"], base), False))
    elif herramienta in ("Glob", "Grep"):
        raiz = resolver(entrada.get("path") or ".", base)
        rutas.append((raiz, True))
        patron = entrada.get("pattern", "") if herramienta == "Glob" else ""
        fijo = GLOB.split(patron, 1)[0]
        if "/" in fijo:
            rutas.append((resolver(fijo.rsplit("/", 1)[0] or "/", raiz), True))
    elif herramienta == "Bash":
        comando = entrada.get("command", "")
        lee = bool(LECTORES.search(comando))
        try:
            fichas = shlex.split(comando, posix=True)
        except ValueError:
            fichas = comando.split()
        for f in fichas:
            if not RUTA_SHELL.match(f):  # texto, JSON, variables: no son rutas
                continue
            if "/" in f or f in (".", ".."):
                rutas.append((resolver(GLOB.split(f, 1)[0] or ".", base), lee))
    return rutas


def motivo(ruta, es_alcance, activo):
    if es_alcance and cubre_clientes(ruta):
        return (f"El alcance '{ruta}' incluye la carpeta clientes/ completa y recorrería a "
                f"todos los clientes. Acota la búsqueda: a staff/, packs/, refs/, "
                f"plantillas/ o feedback/ de la oficina, o a la carpeta del cliente activo.")
    otro = cliente_de(ruta)
    if otro is None or otro.startswith("_") or otro == activo:
        return None
    if not (CLIENTES / otro).exists():
        return None
    if activo is None:
        return (f"'{ruta}' pertenece al cliente '{otro}', y esta sesión no está abierta en "
                f"ningún cliente. Para trabajar con él, abre clientes/{otro}/ como proyecto "
                f"en Claude Code (regla R13).")
    return (f"'{ruta}' pertenece al cliente '{otro}', y esta sesión trabaja para "
            f"'{activo}'. El material de un cliente no se usa en otro (regla R13). Si "
            f"necesitas un criterio de ese trabajo, debe estar destilado y anonimizado en "
            f"feedback/, staff/ o packs/.")


def main():
    try:
        datos = json.load(sys.stdin)
        herramienta = datos.get("tool_name", "")
        entrada = datos.get("tool_input") or {}
        base = pathlib.Path(datos.get("cwd") or os.getcwd()).resolve()
    except Exception as e:  # noqa: BLE001 — un hook roto avisa, no paraliza
        print(f"aislar-cliente: no pude leer la entrada del hook ({e}); no se revisó.",
              file=sys.stderr)
        return 1

    proyecto = pathlib.Path(os.environ.get("CLAUDE_PROJECT_DIR") or base).resolve()
    activo = cliente_de(proyecto)
    if activo == "_PLANTILLA":  # el molde no es un cliente: no habilita a nadie
        activo = None

    for ruta, es_alcance in rutas_de(herramienta, entrada, base):
        razon = motivo(ruta, es_alcance, activo)
        if razon:
            print(f"Bloqueado por aislar-cliente: {razon}", file=sys.stderr)
            return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
