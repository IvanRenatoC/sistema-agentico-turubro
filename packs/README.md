# `packs/` — el catálogo de lo que vende la oficina

Un **pack** es un servicio vendible: define **qué se ofrece, con qué alcance, qué queda fuera y qué
se le exige al cliente para poder empezar**. Es la unidad comercial del sistema.

No confundir con `staff/`: ahí vive **quién ejecuta**; acá, **qué se vende**. Un mismo especialista
participa en varios packs, y un pack activa a varios especialistas.

## Qué hay en esta carpeta

| Ruta | Qué es | ¿Se borra? |
|---|---|---|
| `registry.yaml` | El índice del sistema: conecta señales de un encargo con packs y staff | **No.** Se reemplaza su contenido por el tuyo. |
| `_PLANTILLA/detalles.md` | El molde limpio para crear un pack nuevo | **No.** Se copia cada vez que agregas un servicio. |
| `_pack-1/detalles.md` | Ejemplo: un servicio de **ejecución** | **Sí**, cuando ya no te sirva de referencia. |
| `_pack-2/detalles.md` | Ejemplo: un servicio de **diagnóstico y definición** | **Sí**, igual. |

Los dos ejemplos existen para mostrar que un servicio que **vende trabajo hecho** y uno que
**vende una decisión** no se escriben igual: cambian las entradas mínimas, los entregables, la
forma de cotizar y los riesgos.

## Cómo se crea un pack

1. Copia `_PLANTILLA/` y renómbrala: `packs/<id-del-servicio>/`.
2. Completa `detalles.md`. **Define el alcance por sus bordes**: lo que queda fuera y lo que se le
   exige al cliente vale más que la descripción de lo que sí se hace. Es lo que evita la discusión
   a mitad del trabajo.
3. Agrega la entrada en `registry.yaml` con sus señales, su staff y sus referencias obligatorias.
4. **Pruébalo:** toma tres encargos reales del año pasado y pide que se clasifiquen. Si acierta los
   tres, el registry está vivo. Si falla, agrega las señales que faltaban **en las palabras que usó
   el cliente**, no en las tuyas.

## Dónde manda el formato

| Lugar | Rol | Naturaleza |
|---|---|---|
| `packs/_PLANTILLA/detalles.md` | La forma de un pack | **Normativo.** Es el molde que se copia. |
| `PERSONALIZAR.md`, paso 3 | Versión abreviada, para orientarse | Guía. |
| `docs/ARQUITECTURA.md` §6 | Esquema y reglas de resolución del `registry.yaml` | **Normativo** para el registry. |
| `_pack-1/`, `_pack-2/` | Cómo se ve un pack escrito | **Ilustrativo.** No manda, y se borra. |
