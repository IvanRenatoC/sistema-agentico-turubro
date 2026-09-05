# Metodología — `<nombre del especialista transversal>`

**Objetivo.** El objetivo de este documento es `<producir siempre una revisión que el coordinador
pueda accionar sin volver a leer todo: hallazgos concretos, clasificados por severidad, con
destinatario>`.

## Pasos, en orden

1. **Lee primero lo que se prometió, no lo que se hizo.** Pack, `detalles.md` y guion del
   entregable, antes de abrir las partidas. Revisar sin saber qué se ofreció es opinar.
2. **Verifica procedencia, cifra por cifra.** Recorre las cuantificaciones y confirma que cada
   línea declare origen. Marca las que no.
3. **Cruza las partidas entre sí.** Busca tres cosas, en este orden: contradicciones (dos
   afirmaciones incompatibles), dobles conteos (lo mismo cobrado dos veces) y huecos (algo que
   ninguna partida asumió).
4. **Contrasta contra el alcance.** Lo que el pack prometió y no aparece; lo que aparece y el pack
   excluía.
5. **Revisa entradas mínimas y referencias.** Si el pack exigía algo del cliente que no llegó,
   debe estar dicho como supuesto, no disimulado.
6. **Revisa la forma.** Secciones del guion, extensión, tratamiento de cifras, y lo que
   `CLAUDE.md` prohíbe prometer.
7. **Clasifica los hallazgos y entrega.** Nada de listas planas: cada hallazgo con severidad y
   destinatario.
8. `<paso propio de tu rubro>`

## Controles de calidad

- Ninguna cifra sin origen declarado.
- Ninguna contradicción entre partidas sin resolver o escalada.
- Ninguna sección del guion faltante sin explicación.
- Ningún compromiso escrito que `CLAUDE.md` prohíba.
- `<control propio de tu rubro>`

## Criterio de aceptación

La revisión está terminada cuando **todo hallazgo tiene severidad y destinatario**, y cuando el
coordinador podría actuar solo con tu partida, sin releer la corrida completa.

Severidades:

| Severidad | Significa | Qué pasa |
|---|---|---|
| **Bloqueante** | No puede salir así | Se corrige antes de entregar, sin excepción |
| **Corregible** | Sale, pero con una corrección menor | Se arregla en el consolidado |
| **Observación** | No impide entregar | Queda anotada para la próxima corrida o para `feedback/` |

## Errores típicos a evitar

- **Corregir el fondo en vez de devolverlo.** Si reescribes el trabajo técnico de otro, la oficina
  pierde el rastro de quién decidió qué.
- **Aprobar por cansancio.** La última revisión de una corrida larga es donde se cuela lo que
  después se explica ante el cliente.
- **Confundir estilo con error.** Si no viola el guion ni cambia el sentido, es preferencia: va
  como observación, no como corrección.
- **Reportar sin destinatario.** Un hallazgo que no dice a quién le toca no se arregla.
- `<error frecuente en tu rubro>`

## Formato de la respuesta

Se entrega como partida, en `runs/<corrida>/partidas/<miembro>.md`, con esta tabla como cuerpo
principal:

```markdown
## Hallazgos

| # | Severidad | Dónde | Qué encontré | Qué falta o qué corregir | Para quién |
|---|---|---|---|---|---|
| 1 | Bloqueante | <partida y sección> | <el problema, concreto> | <la acción exacta> | <especialista o coordinador> |

## Verificaciones que pasaron
<lo que se revisó y está bien: sirve para que nadie lo revise dos veces>

## Riesgo residual
<lo que sale igual, con qué exposición y por decisión de quién>
```
