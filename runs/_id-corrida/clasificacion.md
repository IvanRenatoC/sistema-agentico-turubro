# Clasificación — `<AAAA-MM-DD-slug-del-encargo>`

> **EJEMPLO ILUSTRATIVO — no es una corrida real.** Muestra la forma del archivo. El formato
> vigente lo define el **planificador** en `.claude/agents/planificador.md`; si algo difiere, manda
> el agente. Nadie escribe dentro de `runs/_id-corrida/`: las corridas reales van en
> `runs/AAAA-MM-DD-<slug>/`. Esta carpeta se puede borrar.

## Pack que aplica
`<id-del-pack>` — `<nombre comercial>`
**Evidencia.** `<señal encontrada>`, en `<de dónde salió: frase del cliente, adjunto, dato>`

## Packs descartados
| Pack | Por qué se descartó |
|---|---|
| `<id>` | `<razón concreta, no "no aplica">` |

## Especialistas que se activan
| Especialista | En qué parte interviene | Por qué es necesario |
|---|---|---|
| `<id>` | `<parte del trabajo>` | `<qué se pierde si no participa>` |

## Entradas mínimas del pack
| Entrada exigida | ¿Está? | Dónde está o qué falta |
|---|---|---|
| `<entrada del detalles.md>` | `<sí / no / parcial>` | `<ruta del adjunto o qué pedirle al cliente>` |

## Normativa y referencias obligatorias
| Referencia | Qué decide en este encargo |
|---|---|
| `<archivo de refs/>` | `<qué resuelve mirar esto>` |

## Conflictos detectados
`<empate entre packs, especialidad sin responsable, o "ninguno">`
