# `propuestas/` — lo que se ofreció, antes de ejecutar

Una carpeta por propuesta, con el mismo formato de identificador que una corrida:
`AAAA-MM-DD-<slug-del-encargo>`. Es el archivo comercial de la oficina: **qué se ofreció, a qué
precio y sobre qué supuestos**.

La escribe el flujo `proponer`. No abre corrida en `runs/`.

## La relación con `runs/`

**El identificador es el puente.** Si la propuesta se aprueba, `ejecutar` abre
`runs/<mismo-identificador>/` y reutiliza el brief.

| | `propuestas/<id>/` | `runs/<id>/` |
|---|---|---|
| Cuándo | Antes de vender | Después de aprobar |
| Detalle | Magnitud y rango | Partidas cerradas |
| Pregunta que responde | ¿Qué ofrecimos y por qué? | ¿Qué hicimos y cómo? |

Poder cruzar las dos carpetas por el mismo identificador es lo que permite responder la pregunta
que más cuesta contestar en una oficina de servicios: **¿en qué se nos fue la mano al cotizar?**

## Qué hay dentro de una propuesta

| Ruta | Qué es | Obligatorio |
|---|---|---|
| `brief.md` | El encargo entendido en etapa comercial | Sí |
| `estimacion.md` | El detalle del cálculo grueso y sus supuestos | Opcional |
| `propuesta.pdf` | El documento tal como se envió | Sí, cuando se envía |

El documento final lleva la extensión que use tu oficina —`.pdf`, `.pptx`, `.docx`—. En la carpeta
de ejemplo no hay ninguno: un archivo binario vacío no enseña nada.

## Reglas

- **El documento enviado no se edita.** Es la versión firmada en el tiempo. Una corrección genera
  un archivo nuevo: `propuesta-v2.pdf`, conservando el anterior.
- **Toda cifra declara si es cerrada o estimada.** Mezclarlas es la forma más común de perder plata.
- **Nada se promete fuera de lo que el pack incluye.** El alcance del documento es el alcance del
  pack, no lo que el cliente quisiera oír.
- **No se envía desde acá.** El sistema deja el documento listo; el envío lo hace una persona.

## Registrar el desenlace

Cuando la propuesta se resuelve —aprobada, rechazada o sin respuesta— el aprendizaje va a
`feedback/packs/<pack>.md`, no a esta carpeta. Ahí es donde sirve: alcance mal definido, precio
fuera de mercado, entregable que no convence.

**Una propuesta perdida sin razón anotada es la información más cara que se pierde en una oficina de
servicios.**

## Privacidad y `.gitignore`

Estas carpetas contienen nombres de clientes y precios. La decisión depende de la visibilidad de tu
repositorio, y es tuya:

- **Repositorio privado:** versiona todo. La trazabilidad de lo ofrecido vale más que el peso.
- **Repositorio público:** agrega `propuestas/*` al `.gitignore` con excepción de la carpeta de
  ejemplo. La regla está escrita y comentada al final del `.gitignore`, lista para activar.

La diferencia con `refs/originales/` —que se ignora por defecto— es que ahí el problema es legal
(licencias de terceros) y aquí es de confidencialidad, que depende de dónde publiques.
