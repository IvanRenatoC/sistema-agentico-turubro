# Estimación — `<AAAA-MM-DD-slug-del-encargo>`

> **EJEMPLO ILUSTRATIVO — no es una estimación real.** Archivo **opcional**: se escribe cuando el
> detalle del cálculo grueso merece quedar registrado. El formato vigente lo define el flujo
> **proponer** en `.claude/skills/proponer/SKILL.md`. Esta carpeta se puede borrar.

**Nivel de detalle.** Estimación gruesa: magnitud y rango. **No son partidas cerradas.**

## Estimación por unidad de trabajo

| # | Unidad | Especialista | Magnitud | Rango de valor | Confianza |
|---|---|---|---|---|---|
| 1 | `<unidad de trabajo>` | `<id>` | `<cantidad aproximada y unidad>` | `<mínimo – máximo>` | `<alta / media / baja>` |

**Total estimado.** `<rango>` · **Total que se ofrece.** `<valor o rango>` ·
**Condición.** `<cerrado / sujeto a visita / sujeto a medición>`

## Supuestos que sostienen el precio

Lo más importante del archivo: si uno de estos cae, el precio cambia.

| Supuesto | En qué se basa | Efecto si es falso |
|---|---|---|
| `<supuesto>` | `<costos.md / dato del cliente / experiencia declarada>` | `<cuánto y en qué dirección se mueve>` |

## Qué cambiaría el precio

- **Hacia arriba:** `<qué hallazgo o condición lo encarece>`
- **Hacia abajo:** `<qué información permitiría cotizar más fino>`

## Qué queda fuera del total
- `<partida marcada como alternativa por exceder el tope declarado>`
- `<lo que se cotiza aparte al confirmarse>`

## Origen de los valores
| Concepto | Origen |
|---|---|
| `<concepto>` | `<costos.md de <id> / refs/ / supuesto declarado>` |

`<Ningún valor inventado: lo que no está en un costos.md va como supuesto y se avisa.>`
