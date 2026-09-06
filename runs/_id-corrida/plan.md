# Plan — `<AAAA-MM-DD-slug-del-encargo>`

> **EJEMPLO ILUSTRATIVO — no es una corrida real.** Muestra la forma del archivo. El formato
> vigente lo define el **planificador** en `.claude/agents/planificador.md`; si algo difiere, manda
> el agente. Nadie escribe dentro de `runs/_id-corrida/`: las corridas reales van en
> `runs/AAAA-MM-DD-<slug>/`. Esta carpeta se puede borrar.

## Unidades de trabajo
| # | Unidad | Especialista | Entrada que necesita | Entregable |
|---|---|---|---|---|
| 1 | `<unidad con un solo responsable>` | `<id>` | `<qué debe recibir>` | `<qué produce, verificable>` |

## Secuencia y dependencias
- **En paralelo:** `<unidades que no se bloquean entre sí>`
- **En serie:** `<unidad>` antes de `<unidad>`, porque `<razón>`

## Riesgos
| Riesgo | Probabilidad | Qué hacemos si ocurre |
|---|---|---|
| `<riesgo concreto>` | `<alta / media / baja>` | `<plan B; un riesgo sin respuesta es decoración>` |

## Criterio de cierre
`<cómo se sabe que la corrida está terminada y no solo entregada>`

## Preguntas abiertas, priorizadas
1. `<la que más cambia el resultado>` — afecta `<qué>`
2. `<la siguiente>` — afecta `<qué>`
