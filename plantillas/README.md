# `plantillas/` — la forma de lo que sale de la casa

Aquí vive **la firma profesional de la oficina**: el orden en que se cuentan las cosas y cómo se
ven. Dos capas distintas:

| Capa | Archivos | Qué define | Quién la usa |
|---|---|---|---|
| **Guion** | `estructura-propuesta.md`, `estructura-entregable.md` | Qué secciones van, en qué orden y qué va en cada una | Los flujos `proponer` y `entregar` |
| **Identidad visual** | `propuesta.potx`, `entregable.potx` | Tipografías, colores, portada, pie, logotipo | La persona, al armar el documento final |

El guion pesa más que el diseño. Un documento feo y bien estructurado se defiende; uno bonito con
las secciones desordenadas, no.

## Los dos `.potx` no vienen en el repositorio

**Los creas tú**, en PowerPoint o Keynote, y los guardas acá con esos nombres. Un archivo binario
vacío no enseña nada y se rompe al abrirlo, así que no los dejamos como marcador.

Lo mínimo que debe traer cada plantilla:

- **Portada** con `<nombre de la oficina>`, título del documento, cliente y fecha.
- **Página maestra** con pie: `<oficina>` · `<identificador de la corrida>` · número de página.
- **Estilos definidos** para título, subtítulo, cuerpo, tabla y nota al pie. Que estén definidos
  como estilos, no como formato manual, es lo que evita que cada documento se vea distinto.
- **Una lámina de tabla** ya formateada: es donde se rompen todos los documentos de servicios.
- **Los colores y tipografías** que declaraste en el bloque de voz de `CLAUDE.md`.

Si tu oficina entrega en Word o en PDF armado a mano, cambia la extensión y deja acá lo que
corresponda: `propuesta.dotx`, `entregable.dotx`. Lo que importa es que exista **un** archivo de
identidad visual por tipo de documento, y que los guiones lo mencionen.

## Regla de uso

El guion se respeta. Si una sección no aplica a un encargo, **se dice por qué en el documento**, no
se elimina en silencio. Esa es la regla R12 del `CLAUDE.md` y la verifica el flujo `entregar`.
