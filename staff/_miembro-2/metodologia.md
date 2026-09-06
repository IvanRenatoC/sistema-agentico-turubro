# Metodología — `<nombre del especialista>`

**Objetivo.** El objetivo de este documento es `<producir siempre una decisión defendible: con
evidencia, con alternativas descartadas y con la renuncia declarada>`.

## Pasos, en orden

1. **Lee el problema antes de la solución.** `<qué se revisa primero en tu rubro: los datos del
   negocio, el estado real del activo, el registro histórico>`. Nunca al revés: si empiezas por la
   solución, encuentras evidencia para justificarla.
2. **Separa lo afirmado de lo demostrado.** Dos columnas: lo que dice el cliente y lo que muestran
   los datos. Las contradicciones son el hallazgo, no un estorbo.
3. **Mapea el contexto.** `<qué hay alrededor que condiciona la decisión: competencia, entorno
   físico, normativa, capacidades internas, historial>`.
4. **Formula al menos `<número>` hipótesis** de solución o de causa. Una sola hipótesis no es
   análisis: es preferencia.
5. **Contrasta cada hipótesis con evidencia.** Lo que no se puede contrastar queda marcado como
   supuesto con su dato faltante.
6. **Elige una y declara la renuncia.** Qué se gana y qué se deja de hacer o de ser al tomar ese
   camino.
7. **Traduce la decisión en instrucciones ejecutables:** lo que los especialistas de ejecución
   necesitan recibir para trabajar sin volver a preguntar.
8. `<paso propio de tu rubro>`

## Controles de calidad

- Cada afirmación sobre el contexto tiene fuente; lo que no la tiene está marcado como supuesto.
- Hay al menos una opción descartada, con su razón escrita.
- La recomendación declara explícitamente lo que se sacrifica.
- La definición para ejecución está completa: `<qué campos no pueden faltar en tu rubro>`.
- `<verificación obligatoria en tu rubro>`

## Criterio de aceptación

Dos pruebas, y hay que pasar las dos:

- **Prueba de la renuncia.** Si la recomendación no dice qué se deja de hacer, no está terminada.
- **Prueba del competidor.** Si la misma recomendación la podría firmar cualquier competidor sin
  cambiar una palabra, todavía es genérica: falta decidir.

## Errores típicos a evitar

- **Confirmar la primera intuición.** El paso 4 existe para eso: obliga a formular alternativas
  reales, no adornos.
- **Confundir el síntoma con la causa.** `<síntoma típico de tu rubro que se confunde con la
  causa>`.
- **Entregar diagnóstico sin decisión.** Un informe que describe y no recomienda deja el trabajo
  difícil en manos del cliente.
- **Recomendar sin considerar quién lo ejecuta.** Si nadie de la oficina puede hacerlo, hay que
  decirlo en la misma partida.
- `<error frecuente en tu rubro>`

## Formato de la respuesta

Partida en `runs/<corrida>/partidas/<miembro>.md`, con el formato estándar del sistema y estas
precisiones propias del rol de diagnóstico:

```markdown
## Desarrollo
**Lo que el cliente afirma vs. lo que muestran los datos.**
| Afirmación | Evidencia | ¿Coinciden? |

**Hipótesis evaluadas.**
| # | Hipótesis | Evidencia a favor | Evidencia en contra | Estado |

**Recomendación.** <el camino elegido>
**Criterio de la elección.** <por qué este y no los otros>
**Lo que se sacrifica.** <la renuncia, explícita>

## Definición para ejecución
<lo que cada especialista de ejecución necesita recibir para poder trabajar>

## Supuestos y dato faltante
| Supuesto | Qué dato lo confirma o lo derriba | Efecto si es falso |
```
