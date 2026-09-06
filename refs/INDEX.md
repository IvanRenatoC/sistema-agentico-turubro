# Índice de referencias

> **Este archivo no se borra: se reemplaza su contenido.** Las filas de abajo son un ejemplo de
> forma. **Bórralas y deja las tuyas.**
>
> Es la puerta de entrada a `refs/`. Los agentes entran por aquí, no por los documentos originales.

## Qué rige

| Tema | Qué decide | Documento | Versión vigente | Extracto | Original |
|---|---|---|---|---|---|
| `<tema del trabajo>` | `<qué pregunta se resuelve mirando esto>` | `<nombre del documento>` | `<versión o año>` | `refs/_norma.md` | `originales/<archivo>` |
| `<otro tema>` | `<qué decide>` | `<documento>` | `<versión>` | `refs/<archivo>.md` | `<enlace o "no versionado">` |

## Cómo se llena

- **Una fila por documento que de verdad rige.** Si mirarlo no cambia ninguna decisión del trabajo,
  no va en el índice.
- **La columna "Qué decide" es la más útil:** es la que permite encontrar la referencia partiendo
  del problema y no del nombre del documento, que nadie recuerda.
- **La versión vigente es obligatoria.** Una cita sin versión no sirve para defender un criterio.
- Si el original no está versionado en el repositorio —lo normal, ver `refs/README.md`—, la última
  columna dice dónde conseguirlo.

## Vigencias por revisar

Los documentos normativos se actualizan y las citas envejecen en silencio. Anota cuándo revisar
cada uno.

| Documento | Última revisión | Próxima revisión | Responsable |
|---|---|---|---|
| `<documento>` | `<fecha>` | `<fecha>` | `<quién>` |

## Qué NO está en `refs/`

Decirlo evita que alguien asuma que el silencio significa "no aplica".

- `<materia que rige pero todavía no está documentada acá>` → `<dónde ir a buscarla mientras tanto>`
- `<lo que es criterio propio de la oficina, no norma externa>` → vive en `staff/` y en `CLAUDE.md`
- `<lo que es material de un solo especialista>` → vive en `staff/<id>/referencias/`
