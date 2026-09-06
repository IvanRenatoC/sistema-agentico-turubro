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
