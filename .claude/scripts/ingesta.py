#!/usr/bin/env python3
"""ingesta.py — normaliza los adjuntos de una corrida a texto trazable.

Contrato (docs/ARQUITECTURA.md §5):
  Entrada : runs/<corrida>/adjuntos/<lote>/*
  Salida  : runs/<corrida>/adjuntos/_texto/<archivo>.md  +  _texto/INDEX.md

Requisitos que este script cumple, y que hay que preservar al modificarlo:
  1. No modifica ningún original. Se abren en modo lectura, y nada se escribe
     dentro de la carpeta del lote.
  2. Un archivo de salida por archivo de entrada, con cabecera de procedencia.
  3. Lo que no se puede convertir se registra como NO CONVERTIBLE con la razón:
     nada falla en silencio.
  4. Determinista: la misma entrada produce la misma salida. Por eso la
     cabecera NO lleva la hora de ejecución, sino la fecha del original y su
     sha256.

Uso:
    python3 .claude/scripts/ingesta.py --corrida 2026-09-12-galpon-lo-espejo
    python3 .claude/scripts/ingesta.py --corrida <id> --lote 2026-09-12-fotos
    python3 .claude/scripts/ingesta.py --corrida <id> --dry-run

Códigos de salida: 0 = terminó (los no convertibles se reportan, no fallan);
1 = error de uso o de acceso.

Sin dependencias externas. Para PDF usa `pdftotext` y para imágenes `tesseract`
si están instalados; si no, los reporta como no convertibles con la razón.
"""

import argparse
import datetime as _dt
import hashlib
import html
import html.parser
import json
import pathlib
import re
import shutil
import subprocess
import sys
import zipfile

VERSION = "1.0"

TEXTO_PLANO = {".txt", ".md", ".markdown", ".csv", ".tsv", ".json", ".yaml", ".yml",
               ".xml", ".log", ".rst", ".ini", ".cfg", ".py", ".js", ".sql"}
NO_CONVERTIBLE = {
    ".mp3": "audio: requiere transcripción",
    ".wav": "audio: requiere transcripción",
    ".m4a": "audio: requiere transcripción",
    ".ogg": "audio: requiere transcripción",
    ".mp4": "video: requiere transcripción",
    ".mov": "video: requiere transcripción",
    ".zip": "archivo comprimido: descomprímelo dentro del lote",
    ".rar": "archivo comprimido: descomprímelo dentro del lote",
    ".dwg": "plano CAD: exporta a PDF antes de la ingesta",
    ".dxf": "plano CAD: exporta a PDF antes de la ingesta",
}
IMAGENES = {".png", ".jpg", ".jpeg", ".tif", ".tiff", ".bmp", ".webp"}


class _Texto(html.parser.HTMLParser):
    BLOQUE = {"p", "div", "br", "li", "tr", "h1", "h2", "h3", "h4", "h5", "h6"}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.partes, self._saltar = [], False

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style"):
            self._saltar = True
        elif tag in self.BLOQUE:
            self.partes.append("\n")

    def handle_endtag(self, tag):
        if tag in ("script", "style"):
            self._saltar = False

    def handle_data(self, data):
        if not self._saltar:
            self.partes.append(data)

    def texto(self):
        return re.sub(r"\n{3,}", "\n\n", "".join(self.partes)).strip()


def _sin_tags(xml_bytes):
    txt = xml_bytes.decode("utf-8", "replace")
    txt = re.sub(r"</w:p>|</a:p>|<w:br/>|</text:p>", "\n", txt)
    txt = re.sub(r"<[^>]+>", "", txt)
    return re.sub(r"\n{3,}", "\n\n", html.unescape(txt)).strip()


def _docx(ruta):
    with zipfile.ZipFile(ruta) as z:
        nombres = [n for n in ("word/document.xml", "content.xml") if n in z.namelist()]
        if not nombres:
            raise ValueError("no contiene word/document.xml")
        return _sin_tags(z.read(nombres[0])), "descompresión + limpieza de XML"


def _pptx(ruta):
    with zipfile.ZipFile(ruta) as z:
        slides = sorted(n for n in z.namelist()
                        if re.match(r"ppt/slides/slide\d+\.xml$", n))
        if not slides:
            raise ValueError("no contiene láminas")
        bloques = []
        for i, s in enumerate(slides, 1):
            bloques.append(f"## Lámina {i}\n\n{_sin_tags(z.read(s))}")
        return "\n\n".join(bloques), "descompresión + limpieza de XML"


def _xlsx(ruta):
    with zipfile.ZipFile(ruta) as z:
        compartidas = []
        if "xl/sharedStrings.xml" in z.namelist():
            crudo = z.read("xl/sharedStrings.xml").decode("utf-8", "replace")
            for si in re.findall(r"<si>(.*?)</si>", crudo, re.S):
                compartidas.append(html.unescape(
                    "".join(re.findall(r"<t[^>]*>(.*?)</t>", si, re.S))))
        hojas = sorted(n for n in z.namelist()
                       if re.match(r"xl/worksheets/sheet\d+\.xml$", n))
        if not hojas:
            raise ValueError("no contiene hojas")
        bloques = []
        for i, h in enumerate(hojas, 1):
            crudo = z.read(h).decode("utf-8", "replace")
            filas = []
            for fila in re.findall(r"<row[^>]*>(.*?)</row>", crudo, re.S):
                celdas = []
                for celda in re.findall(r"<c[^>]*>.*?</c>|<c[^>]*/>", fila, re.S):
                    v = re.search(r"<v>(.*?)</v>", celda, re.S)
                    t_inline = re.search(r"<is>.*?<t[^>]*>(.*?)</t>", celda, re.S)
                    if 't="s"' in celda and v:
                        idx = int(v.group(1))
                        celdas.append(compartidas[idx] if idx < len(compartidas) else "")
                    elif t_inline:
                        celdas.append(html.unescape(t_inline.group(1)))
                    elif v:
                        celdas.append(html.unescape(v.group(1)))
                    else:
                        celdas.append("")
                if any(c.strip() for c in celdas):
                    filas.append("\t".join(celdas))
            bloques.append(f"## Hoja {i}\n\n" + "\n".join(filas))
        return "\n\n".join(bloques), "descompresión + limpieza de XML"


def _pdf(ruta):
    if not shutil.which("pdftotext"):
        raise ValueError("PDF: falta la herramienta pdftotext (poppler-utils)")
    r = subprocess.run(["pdftotext", "-layout", "-enc", "UTF-8", str(ruta), "-"],
                       capture_output=True)
    if r.returncode != 0:
        raise ValueError(f"pdftotext falló: {r.stderr.decode('utf-8', 'replace')[:200]}")
    texto = r.stdout.decode("utf-8", "replace").strip()
    if not texto:
        raise ValueError("PDF sin texto extraíble: probablemente escaneado, requiere OCR")
    return texto, "pdftotext -layout"


def _imagen(ruta):
    if not shutil.which("tesseract"):
        raise ValueError("imagen: requiere OCR y falta la herramienta tesseract")
    r = subprocess.run(["tesseract", str(ruta), "stdout"], capture_output=True)
    texto = r.stdout.decode("utf-8", "replace").strip()
    if r.returncode != 0 or not texto:
        raise ValueError("OCR no devolvió texto legible")
    return texto, "tesseract OCR — REQUIERE REVISIÓN HUMANA"


def _plano(ruta):
    return ruta.read_text(encoding="utf-8", errors="replace").strip(), "lectura directa"


def _html(ruta):
    p = _Texto()
    p.feed(ruta.read_text(encoding="utf-8", errors="replace"))
    return p.texto(), "limpieza de HTML"


def extraer(ruta):
    """Devuelve (texto, método). Lanza ValueError si no es convertible."""
    ext = ruta.suffix.lower()
    if ext in NO_CONVERTIBLE:
        raise ValueError(NO_CONVERTIBLE[ext])
    if ext in TEXTO_PLANO:
        return _plano(ruta)
    if ext in (".html", ".htm"):
        return _html(ruta)
    if ext == ".docx":
        return _docx(ruta)
    if ext == ".pptx":
        return _pptx(ruta)
    if ext == ".xlsx":
        return _xlsx(ruta)
    if ext == ".pdf":
        return _pdf(ruta)
    if ext in IMAGENES:
        return _imagen(ruta)
    raise ValueError(f"extensión no soportada: {ext or 'sin extensión'}")


def sha256(ruta):
    h = hashlib.sha256()
    with ruta.open("rb") as f:
        for bloque in iter(lambda: f.read(65536), b""):
            h.update(bloque)
    return h.hexdigest()


def fecha_original(ruta):
    return _dt.datetime.utcfromtimestamp(int(ruta.stat().st_mtime)).strftime("%Y-%m-%d %H:%M:%S UTC")


def cabecera(ruta, lote, metodo, estado, razon=""):
    campos = {
        "archivo_original": ruta.name,
        "ruta_original": f"adjuntos/{lote}/{ruta.name}",
        "lote": lote,
        "bytes": ruta.stat().st_size,
        "sha256": sha256(ruta),
        "fecha_del_original": fecha_original(ruta),
        "estado": estado,
        "metodo": metodo,
        "generado_por": f"ingesta.py v{VERSION}",
    }
    if razon:
        campos["razon"] = razon
    lineas = ["---"] + [f"{k}: {v}" for k, v in campos.items()] + ["---", ""]
    return "\n".join(lineas)


def slug(nombre):
    base = re.sub(r"[^a-zA-Z0-9._-]+", "-", nombre).strip("-")
    return base or "sin-nombre"


def main():
    ap = argparse.ArgumentParser(description="Normaliza los adjuntos de una corrida a texto.")
    ap.add_argument("--corrida", required=True, help="identificador de la corrida (carpeta en runs/)")
    ap.add_argument("--lote", help="procesar solo este lote; por omisión, todos")
    ap.add_argument("--raiz", default=".", help="raíz del repositorio (por omisión, el directorio actual)")
    ap.add_argument("--dry-run", action="store_true", help="no escribe nada, solo informa")
    a = ap.parse_args()

    raiz = pathlib.Path(a.raiz).resolve()
    adjuntos = raiz / "runs" / a.corrida / "adjuntos"
    if not adjuntos.is_dir():
        print(f"ERROR: no existe {adjuntos}", file=sys.stderr)
        return 1

    lotes = ([adjuntos / a.lote] if a.lote else
             sorted(d for d in adjuntos.iterdir() if d.is_dir() and d.name != "_texto"))
    lotes = [d for d in lotes if d.is_dir()]
    if not lotes:
        print(f"ERROR: no hay lotes que procesar en {adjuntos}", file=sys.stderr)
        return 1

    destino = adjuntos / "_texto"
    if not a.dry_run:
        destino.mkdir(exist_ok=True)

    filas, convertidos, fallidos = [], 0, 0
    for lote in lotes:
        for origen in sorted(p for p in lote.rglob("*") if p.is_file()):
            if origen.name.startswith("."):
                continue
            nombre_salida = f"{slug(origen.stem)}{origen.suffix.lower().replace('.', '-')}.md"
            try:
                texto, metodo = extraer(origen)
                cuerpo = cabecera(origen, lote.name, metodo, "convertido") + texto + "\n"
                estado, detalle = "convertido", metodo
                convertidos += 1
            except Exception as e:  # noqa: BLE001 — cualquier fallo se reporta, no se oculta
                razon = str(e)
                cuerpo = (cabecera(origen, lote.name, "ninguno", "NO CONVERTIBLE", razon) +
                          f"# NO CONVERTIBLE\n\n**Razón.** {razon}\n\n"
                          f"El original está en `adjuntos/{lote.name}/{origen.name}` y no fue "
                          f"modificado. Si este archivo contiene información necesaria para la "
                          f"corrida, hay que revisarlo a mano y anotar lo relevante.\n")
                estado, detalle = "NO CONVERTIBLE", razon
                fallidos += 1
            if not a.dry_run:
                (destino / nombre_salida).write_text(cuerpo, encoding="utf-8")
            filas.append((lote.name, origen.name, estado, detalle, nombre_salida))

    filas.sort()
    indice = ["# Índice de adjuntos convertidos", "",
              f"Generado por `ingesta.py` v{VERSION}. "
              f"{convertidos} convertidos · {fallidos} no convertibles.", "",
              "| Lote | Archivo original | Estado | Método o razón | Texto |",
              "|---|---|---|---|---|"]
    for lote, nombre, estado, detalle, salida in filas:
        indice.append(f"| `{lote}` | `{nombre}` | {estado} | {detalle} | `{salida}` |")
    indice += ["", "Los originales no fueron modificados.", ""]
    if not a.dry_run:
        (destino / "INDEX.md").write_text("\n".join(indice), encoding="utf-8")

    print(f"{convertidos} convertidos, {fallidos} no convertibles.")
    for lote, nombre, estado, detalle, _ in filas:
        if estado != "convertido":
            print(f"  NO CONVERTIBLE: {lote}/{nombre} — {detalle}")
    if a.dry_run:
        print("(dry-run: no se escribió nada)")
    else:
        print(f"Salida en runs/{a.corrida}/adjuntos/_texto/ — revisa INDEX.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())
