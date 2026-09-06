# `.claude/scripts/` — el trabajo determinista

Un script existe **solo cuando el resultado debe ser idéntico cada vez que se ejecuta**. Lo que
requiere criterio es trabajo de un agente: convertirlo en reglas rígidas lo degrada. Y al revés, lo
mecánico se degrada si se deja al criterio.

Sin dependencias externas: solo la biblioteca estándar de Python 3.

| Script | Qué hace | Contrato |
|---|---|---|
| `ingesta.py` | Normaliza los adjuntos de una corrida a texto trazable | `docs/ARQUITECTURA.md` §5 |
| `resolver.py` | Traduce señales de un encargo en packs, staff y referencias | `docs/ARQUITECTURA.md` §5 y §6 |

## `ingesta.py`

```bash
python3 .claude/scripts/ingesta.py --corrida 2026-09-12-galpon-lo-espejo
python3 .claude/scripts/ingesta.py --corrida <id> --lote 2026-09-12-fotos
python3 .claude/scripts/ingesta.py --corrida <id> --dry-run
```

Lee `runs/<corrida>/adjuntos/<lote>/` y escribe un `.md` por archivo en `adjuntos/_texto/`, más un
`INDEX.md`. Cada salida abre con cabecera de procedencia: archivo original, lote, bytes, sha256 y
fecha del original.

**No lleva la hora de ejecución a propósito:** el contrato exige que sea determinista, y un reloj lo
rompería. La trazabilidad la da el sha256.

Formatos: texto plano, CSV/TSV, JSON, HTML, `.docx`, `.pptx`, `.xlsx` con la biblioteca estándar;
PDF con `pdftotext` e imágenes con `tesseract` **si están instalados**. Lo que no se puede convertir
—audio, video, CAD, un PDF escaneado sin OCR— genera igual su archivo, marcado `NO CONVERTIBLE` y
con la razón. Nada falla en silencio.

Salidas: `0` terminó (los no convertibles se reportan, no fallan) · `1` error de uso o de acceso.

## `resolver.py`

```bash
python3 .claude/scripts/resolver.py --texto "se rompió una viga del galpón"
python3 .claude/scripts/resolver.py --brief runs/<corrida>/brief.md
python3 .claude/scripts/resolver.py --senales "soldadura,estructura"
python3 .claude/scripts/resolver.py --validar
python3 .claude/scripts/resolver.py --texto "..." --json
```

Lee `packs/registry.yaml` y nada más. Devuelve los candidatos **con la señal que los justificó**,
ordenados por cantidad de coincidencias y luego por `prioridad`.

Tres comportamientos que son parte del contrato, no limitaciones:

- **Ante empate no elige.** Devuelve los candidatos e informa el empate. Un empate suele significar
  que dos servicios se solapan o que el encargo es mixto, y ese dato se pierde si se resuelve en
  silencio.
- **Cero coincidencias es un resultado válido**, no un error: significa declinar, crear un servicio
  nuevo, o agregar la señal que faltaba con las palabras del cliente.
- **Valida antes de resolver:** pack sin `detalles.md`, especialista sin sus tres archivos, ruta de
  `refs/` o de entregable inexistente, ids duplicados y exclusiones a packs que no existen.

La comparación ignora mayúsculas, tildes y puntuación. Usa PyYAML si está instalado y, si no, un
parser interno que cubre el esquema del registry; `--parser interno` lo fuerza, para probarlo.

Salidas: `0` resolvió · `1` error de uso · `2` registry inválido.

## Al modificarlos

Los requisitos del contrato están escritos como comentario al inicio de cada archivo. Si tocas uno,
esa lista es lo que hay que seguir cumpliendo: no modificar originales, cabecera de procedencia,
determinismo, evidencia junto a la conclusión y no desempatar solo.
