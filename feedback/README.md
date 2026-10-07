# `feedback/` — cómo aprende el sistema

Aquí entra lo que salió mal en el mundo real. **Es tránsito, no bodega:** el destino de una
anotación es desaparecer de acá y aparecer como criterio en `staff/`, `packs/` o `CLAUDE.md`.

Un `feedback/` que solo crece significa que el sistema no está aprendiendo.

## El ciclo

```
corrida  →  error detectado  →  _bruto/  →  destilado a GLOBAL / staff / packs
         →  si se repite  →  promovido al archivo de criterio  →  marcado como incorporado
```

**El agente propone la promoción; la persona la aprueba.** Un sistema que reescribe su propio
criterio sin supervisión deriva sin que nadie note cuándo empezó.

## Qué va en cada archivo

| Ruta | Qué recibe | A dónde se promueve |
|---|---|---|
| `_bruto/` | Notas sin procesar: audios, capturas, un mensaje de WhatsApp | A los tres de abajo |
| `GLOBAL.md` | Lo que aplica a toda la oficina: sesgos, reglas nuevas de la casa | `CLAUDE.md` |
| `staff/<id>.md` | Correcciones a un especialista | Su `rol.md`, `metodologia.md` o `costos.md` |
| `packs/<id>.md` | Correcciones a un servicio: alcance, precio, entregable | Su `detalles.md` o el `registry.yaml` |

Los archivos `staff/_miembro.md` y `packs/_pack.md` son **moldes de anotación**: se copian con el
nombre del especialista o del servicio real. `GLOBAL.md` no se copia: se usa directo.

## Cuándo anotar

- Al cerrar una corrida, siempre: aunque sea para decir qué salió bien.
- Cuando el cliente corrige algo que dimos por cerrado.
- Cuando una propuesta se pierde. **La razón de una propuesta perdida es la información más cara
  que se pierde en una oficina de servicios**, y va a `packs/<id>.md`.
- Cuando un especialista tuvo que preguntar algo que debería haber estado escrito.

## Cómo anotar bien

Una anotación útil responde cuatro cosas: **qué pasó**, **qué debería haber pasado**, **qué
criterio no estaba escrito** y **a qué archivo va la corrección**. Sin la última, la anotación se
queda en queja.

## Lo que no entra aquí: preferencias de un cliente

`feedback/` lo lee **toda corrida, de cualquier cliente**. Por eso, antes de anotar, una pregunta:
**¿esto aplicaría a otro cliente?**

| Si la respuesta es… | Va a… | Ejemplo |
|---|---|---|
| No: es gusto o contexto de ese cliente | `clientes/<cliente>/notas.md` | "No le gustó la paleta café" |
| Sí: es criterio de la oficina | `feedback/`, anonimizado | "Presentar una sola paleta genera más rondas que presentar tres" |

**Anonimizado** significa sin nombre del cliente, sin sus datos y sin el identificador de la
corrida si ese identificador lo nombra. El origen se describe por el tipo de encargo: "rebranding
de cafetería, octubre 2026", no `2026-10-07-rebranding-cafe-aurora`.

Una preferencia de un cliente promovida a `staff/` o `packs/` se convierte en criterio de la casa y
se aplica a todos los demás. Es la forma más silenciosa de contaminar el trabajo de un cliente con
el de otro (regla R13).
