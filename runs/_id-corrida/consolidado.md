# Consolidado — `<AAAA-MM-DD-slug-del-encargo>`

> **EJEMPLO ILUSTRATIVO — no es una corrida real.** Muestra la forma del archivo. El formato
> vigente lo define el **coordinador** en `.claude/agents/coordinador.md`; si algo difiere, manda el
> agente. Nadie escribe dentro de `runs/_id-corrida/`: las corridas reales van en
> `runs/AAAA-MM-DD-<slug>/`. Esta carpeta se puede borrar.

## Integración por unidad de trabajo
| # | Unidad | Especialista | Resultado | Estado |
|---|---|---|---|---|
| 1 | `<unidad>` | `<id>` | `<qué resolvió, en una línea>` | `<completa / condicionada / incompleta>` |

## Contradicciones resueltas
| Entre | Qué se contradecía | Criterio aplicado | Decisión |
|---|---|---|---|
| `<partida A>` y `<partida B>` | `<el conflicto>` | `<la regla usada para decidir>` | `<qué queda>` |

## Huecos y dobles conteos
- `<algo que ninguna partida asumió, o algo contado dos veces>` → `<cómo se resolvió>`

## Totales
| Concepto | Valor | Origen |
|---|---|---|
| `<agrupación>` | `<valor>` | `<suma de partidas X e Y>` |
| **Total** | `<valor>` | — |

`<Deja fuera del total y marcadas como alternativa las partidas que excedan un tope declarado.>`

## Supuestos abiertos
| Supuesto | Quién lo declaró | Efecto si es falso |
|---|---|---|
| `<supuesto>` | `<id del especialista>` | `<qué cambia en precio, plazo o solución>` |

## Escalamientos
- `<lo que requiere decisión de una persona, y de quién>`

## Cierre
- **Decidí por mi cuenta:** `<qué y con qué criterio>`
- **Debes revisar:** `<qué>`
- **Queda abierto:** `<qué>`
