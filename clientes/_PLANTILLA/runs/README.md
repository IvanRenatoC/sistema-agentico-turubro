# `runs/` — el expediente de los encargos

Vive dentro de la carpeta de cada cliente: `clientes/<cliente>/runs/`. Una carpeta por encargo
ejecutado, con nombre `AAAA-MM-DD-<slug-del-encargo>`. Todo el estado de
una corrida vive dentro de su carpeta: nada se escribe fuera.

## Qué hay dentro de una corrida

| Ruta | Quién lo escribe | Para quién |
|---|---|---|
| `brief.md` | coordinador | planificador |
| `clasificacion.md` | planificador | coordinador |
| `plan.md` | planificador | coordinador |
| `ordenes/<miembro>.md` | coordinador | ese especialista |
| `partidas/<miembro>.md` | ese especialista | coordinador |
| `consolidado.md` | coordinador | flujo `entregar` |
| `adjuntos/<AAAA-MM-DD>-<lote>/` | coordinador, sin modificar el original | trazabilidad |
| `adjuntos/_texto/` | `ingesta.py` | los especialistas |
| `salida/` | flujo `entregar` | el cliente |

Ningún archivo tiene dos autores. Eso es lo que permite que varios especialistas trabajen en
paralelo sin coordinarse.

## `_id-corrida/` es un ejemplo, no una corrida

La carpeta `clientes/_cliente-ejemplo/runs/_id-corrida/` existe solo para que se vea la forma de una corrida sin tener que
ejecutar una. **Nadie escribe dentro de ella** —ni tú ni los agentes— y puedes borrarla cuando ya
no te sirva de referencia.

## Dónde manda el formato

El mismo formato aparece en tres lugares, con jerarquía explícita:

| Lugar | Rol | Naturaleza |
|---|---|---|
| `.claude/agents/*.md` | El formato de salida de cada rol | **Normativo.** Si algo difiere, manda el agente. |
| `docs/ARQUITECTURA.md` §7 | Secciones mínimas de cada archivo | **Invariante.** La regla corta que no cambia. |
| `clientes/_cliente-ejemplo/runs/_id-corrida/*` | Cómo se ve una corrida | **Ilustrativo.** No manda nunca. |

## Este contenido es derivado

Una corrida se puede reconstruir desde la identidad del negocio (`CLAUDE.md`, `staff/`, `packs/`,
`refs/`) más la ficha del cliente y los adjuntos. Si borras `runs/` completo, el sistema sigue
siendo el mismo.

Qué se versiona y qué no, según la visibilidad del repositorio: ver `clientes/README.md`.
