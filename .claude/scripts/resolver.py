#!/usr/bin/env python3
"""resolver.py — resuelve el registry: de señales a packs, staff y referencias.

Contrato (docs/ARQUITECTURA.md §5 y §6):
  Entrada : un texto de encargo, un brief, o una lista explícita de señales.
  Salida  : los packs candidatos, el staff que se activa y las referencias
            obligatorias, cada uno CON LA SEÑAL QUE LO JUSTIFICÓ.

Requisitos que este script cumple, y que hay que preservar al modificarlo:
  1. Lee `packs/registry.yaml` y nada más. No infiere lo que no está declarado.
  2. Devuelve evidencia junto a la conclusión.
  3. Ante empate NO elige: devuelve los candidatos ordenados y deja la decisión
     al planificador, que tiene el brief a la vista.
  4. Cero coincidencias es un resultado válido, no un error.
  5. Valida las referencias del registry antes de resolver: un pack sin
     carpeta, un especialista sin sus tres archivos o una ruta inexistente son
     errores de configuración y se reportan como tales.

Uso:
    python3 .claude/scripts/resolver.py --texto "se rompio una viga del galpon"
    python3 .claude/scripts/resolver.py --brief runs/<corrida>/brief.md
    python3 .claude/scripts/resolver.py --senales "soldadura,estructura"
    python3 .claude/scripts/resolver.py --validar
    python3 .claude/scripts/resolver.py --texto "..." --json

Códigos de salida: 0 = resolvió (incluye cero coincidencias y empates, ambos
informados); 1 = error de uso; 2 = registry inválido.

Sin dependencias externas: usa PyYAML si está instalado y, si no, un parser
interno que cubre el esquema del registry.
"""

import argparse
import json
import pathlib
import re
import sys
import unicodedata

CAMPOS_OBLIGATORIOS = ("id", "nombre", "señales", "staff", "refs_obligatorias", "entregable")
ARCHIVOS_STAFF = ("rol.md", "metodologia.md", "costos.md")


# --------------------------------------------------------------------------- #
# Carga del registry
# --------------------------------------------------------------------------- #
def _sin_comentario(linea):
    fuera, comilla = [], None
    for ch in linea:
        if comilla:
            fuera.append(ch)
            if ch == comilla:
                comilla = None
        elif ch in "\"'":
            comilla = ch
            fuera.append(ch)
        elif ch == "#":
            break
        else:
            fuera.append(ch)
    return "".join(fuera).rstrip()


def _escalar(v):
    v = v.strip()
    if v.startswith("[") and v.endswith("]"):
        cuerpo = v[1:-1].strip()
        return [] if not cuerpo else [_escalar(x) for x in cuerpo.split(",")]
    if len(v) >= 2 and v[0] == v[-1] and v[0] in "\"'":
        return v[1:-1]
    if re.fullmatch(r"-?\d+", v):
        return int(v)
    return v


def parser_interno(texto):
    """Parser mínimo para el esquema de registry.yaml. Sin dependencias."""
    packs, actual, clave_lista = [], None, None
    for cruda in texto.splitlines():
        linea = _sin_comentario(cruda)
        if not linea.strip():
            continue
        sangria = len(linea) - len(linea.lstrip())
        cuerpo = linea.strip()
        if cuerpo == "packs:":
            continue
        if cuerpo.startswith("- ") and ":" in cuerpo and sangria <= 4:
            actual, clave_lista = {}, None
            packs.append(actual)
            cuerpo = cuerpo[2:].strip()
        elif cuerpo.startswith("- "):
            if actual is None or clave_lista is None:
                continue
            actual[clave_lista].append(_escalar(cuerpo[2:]))
            continue
        if actual is None:
            continue
        if ":" in cuerpo:
            clave, _, valor = cuerpo.partition(":")
            clave, valor = clave.strip(), valor.strip()
            if valor == "":
                actual[clave], clave_lista = [], clave
            else:
                actual[clave], clave_lista = _escalar(valor), None
    return {"packs": packs}


def cargar_registry(ruta, parser="auto"):
    texto = ruta.read_text(encoding="utf-8")
    if parser == "auto":
        try:
            import yaml
            return yaml.safe_load(texto) or {}, "PyYAML"
        except ImportError:
            pass
    return parser_interno(texto), "parser interno"


# --------------------------------------------------------------------------- #
# Coincidencia de señales
# --------------------------------------------------------------------------- #
def normalizar(s):
    s = unicodedata.normalize("NFD", str(s).lower())
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    return re.sub(r"\s+", " ", re.sub(r"[^\w\s]", " ", s)).strip()


def coincidencias(pack, texto_norm):
    return [s for s in pack.get("señales", []) if normalizar(s) and normalizar(s) in texto_norm]


# --------------------------------------------------------------------------- #
# Validación
# --------------------------------------------------------------------------- #
def validar(registry, raiz):
    errores = []
    packs = registry.get("packs") or []
    if not packs:
        errores.append("el registry no declara ningún pack")
    vistos = set()
    for i, p in enumerate(packs, 1):
        pid = p.get("id", f"<sin id en la posición {i}>")
        if pid in vistos:
            errores.append(f"[{pid}] id duplicado")
        vistos.add(pid)
        for campo in CAMPOS_OBLIGATORIOS:
            if campo not in p:
                errores.append(f"[{pid}] falta el campo obligatorio '{campo}'")
        if not (raiz / "packs" / str(pid) / "detalles.md").is_file():
            errores.append(f"[{pid}] no existe packs/{pid}/detalles.md")
        for s in p.get("staff", []) or []:
            faltan = [f for f in ARCHIVOS_STAFF
                      if not (raiz / "staff" / str(s) / f).is_file()]
            if faltan:
                errores.append(f"[{pid}] staff '{s}': falta {', '.join(faltan)}")
        for r in p.get("refs_obligatorias", []) or []:
            if not (raiz / "refs" / str(r)).is_file():
                errores.append(f"[{pid}] no existe refs/{r}")
        ent = p.get("entregable")
        if ent and not (raiz / str(ent)).is_file():
            errores.append(f"[{pid}] no existe el entregable {ent}")
        for otro in p.get("excluye", []) or []:
            if otro not in [q.get("id") for q in packs]:
                errores.append(f"[{pid}] excluye a '{otro}', que no está en el registry")
    return errores


# --------------------------------------------------------------------------- #
# Resolución
# --------------------------------------------------------------------------- #
def resolver(registry, texto):
    texto_norm = normalizar(texto)
    candidatos = []
    for p in registry.get("packs") or []:
        hits = coincidencias(p, texto_norm)
        if hits:
            candidatos.append({
                "id": p.get("id"),
                "nombre": p.get("nombre"),
                "señales_coincidentes": hits,
                "staff": p.get("staff") or [],
                "refs_obligatorias": p.get("refs_obligatorias") or [],
                "entregable": p.get("entregable"),
                "prioridad": p.get("prioridad"),
                "excluye": p.get("excluye") or [],
            })
    candidatos.sort(key=lambda c: (-len(c["señales_coincidentes"]),
                                   c["prioridad"] if isinstance(c["prioridad"], int) else 10**6,
                                   str(c["id"])))
    empate = False
    if len(candidatos) > 1:
        a, b = candidatos[0], candidatos[1]
        empate = (len(a["señales_coincidentes"]) == len(b["señales_coincidentes"])
                  and a["prioridad"] == b["prioridad"])
    conflictos = []
    activos = [c["id"] for c in candidatos]
    for c in candidatos:
        for otro in c["excluye"]:
            if otro in activos:
                conflictos.append(f"{c['id']} excluye a {otro}, y ambos coincidieron")
    return candidatos, empate, conflictos


def main():
    ap = argparse.ArgumentParser(description="Resuelve el registry: señales -> packs y staff.")
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--texto", help="texto del encargo")
    g.add_argument("--brief", help="ruta a un brief.md")
    g.add_argument("--senales", help="lista explícita separada por comas")
    ap.add_argument("--raiz", default=".", help="raíz del repositorio")
    ap.add_argument("--validar", action="store_true", help="solo validar el registry")
    ap.add_argument("--json", action="store_true", dest="como_json", help="salida en JSON")
    ap.add_argument("--parser", choices=("auto", "interno"), default="auto",
                    help="parser de YAML; 'interno' fuerza el propio, para pruebas")
    a = ap.parse_args()

    raiz = pathlib.Path(a.raiz).resolve()
    ruta = raiz / "packs" / "registry.yaml"
    if not ruta.is_file():
        print(f"ERROR: no existe {ruta}", file=sys.stderr)
        return 1
    registry, motor = cargar_registry(ruta, a.parser)
    errores = validar(registry, raiz)

    if a.validar:
        if a.como_json:
            print(json.dumps({"motor": motor, "errores": errores}, ensure_ascii=False, indent=2))
        else:
            print(f"registry.yaml leído con {motor}: "
                  f"{len(registry.get('packs') or [])} packs declarados.")
            if errores:
                print("\nERRORES DE CONFIGURACIÓN:")
                for e in errores:
                    print(f"  - {e}")
            else:
                print("Todas las referencias existen. Registry consistente.")
        return 2 if errores else 0

    if a.texto:
        texto = a.texto
    elif a.brief:
        p = pathlib.Path(a.brief)
        if not p.is_file():
            print(f"ERROR: no existe {p}", file=sys.stderr)
            return 1
        texto = p.read_text(encoding="utf-8", errors="replace")
    elif a.senales:
        texto = " ".join(s.strip() for s in a.senales.split(","))
    else:
        print("ERROR: indica --texto, --brief, --senales o --validar", file=sys.stderr)
        return 1

    candidatos, empate, conflictos = resolver(registry, texto)
    salida = {
        "motor": motor,
        "errores_de_configuracion": errores,
        "candidatos": candidatos,
        "empate_sin_resolver": empate,
        "conflictos_de_exclusion": conflictos,
        "staff_a_activar": sorted({s for c in candidatos for s in c["staff"]}),
        "refs_obligatorias": sorted({r for c in candidatos for r in c["refs_obligatorias"]}),
    }
    if a.como_json:
        print(json.dumps(salida, ensure_ascii=False, indent=2))
        return 2 if errores else 0

    if errores:
        print("ERRORES DE CONFIGURACIÓN (corrígelos antes de correr nada):")
        for e in errores:
            print(f"  - {e}")
        print()
    if not candidatos:
        print("CERO COINCIDENCIAS. Resultado válido, no un error.")
        print("Significa que el encargo no calza con ningún servicio declarado:")
        print("  - propón declinar o derivar, o")
        print("  - propón un servicio nuevo, o")
        print("  - agrega al registry la señal que faltaba, con las palabras del cliente.")
        return 2 if errores else 0

    print(f"CANDIDATOS ({len(candidatos)}), ordenados por señales coincidentes y prioridad:\n")
    for i, c in enumerate(candidatos, 1):
        print(f"{i}. {c['id']} — {c['nombre']}")
        print(f"   evidencia: {', '.join(repr(s) for s in c['señales_coincidentes'])}")
        print(f"   staff: {', '.join(map(str, c['staff'])) or '(ninguno)'}")
        print(f"   refs: {', '.join(map(str, c['refs_obligatorias'])) or '(ninguna)'}")
        print(f"   entregable: {c['entregable']}\n")
    if empate:
        print("EMPATE SIN RESOLVER entre los dos primeros: mismas señales y misma prioridad.")
        print("No elijo por ti. Decide con el brief a la vista, o declara 'prioridad' en el")
        print("registry. Un empate suele significar que dos servicios se solapan, o que el")
        print("encargo es mixto: ese dato se pierde si se resuelve en silencio.\n")
    for c in conflictos:
        print(f"CONFLICTO DE EXCLUSIÓN: {c}")
    return 2 if errores else 0


if __name__ == "__main__":
    sys.exit(main())
