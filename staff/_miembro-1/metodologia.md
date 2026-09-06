# Metodología — `<nombre del especialista>`

**Objetivo.** El objetivo de este documento es `<producir siempre una partida ejecutable: qué se
hace, cómo, cuánto hay que hacer y bajo qué condiciones>`.

## Pasos, en orden

1. **Verifica qué rige.** `<norma, estándar, especificación del fabricante o criterio interno que
   aplica a este caso>`. Se cita en la partida; sin cita, la especificación es una opinión.
2. **Define el procedimiento.** `<qué método se usa y por qué corresponde a este caso: condiciones,
   material, contexto>`.
3. **Levanta las cantidades.** `<cómo se cuantifica en tu oficio: medición, conteo, cálculo sobre
   plano, estimación por analogía>`. Declara de dónde salió cada cantidad.
4. **Aplica los rendimientos** de tu `costos.md` para traducir cantidad en tiempo y en costo.
5. **Declara las condiciones previas.** Lo que tiene que estar listo antes de empezar, y qué pasa
   si no lo está.
6. **Nombra los riesgos de ejecución** con su medida de control. `<riesgo típico de tu oficio>`
7. **Aplica los controles de calidad** de la lista de abajo antes de cerrar.
8. `<paso propio de tu oficio>`

## Controles de calidad

- Cada cantidad tiene origen declarado: medición, plano, adjunto del cliente o supuesto.
- Cada valor unitario viene de `costos.md`; ninguno inventado.
- El procedimiento cita la norma o el estándar que lo respalda.
- Las condiciones previas están escritas, no sobreentendidas.
- `<verificación obligatoria en tu oficio: inspección, prueba, ensayo, revisión de terminaciones>`

## Criterio de aceptación

La partida está terminada cuando `<alguien de tu oficio podría tomarla y ejecutar el trabajo sin
volver a preguntar nada, salvo lo que está marcado como supuesto>`.

Si al leerla queda una duda sobre **cuánto** o **cómo**, no está terminada.

## Errores típicos a evitar

- **Cuantificar sin medir y no decirlo.** El error no es estimar: es estimar y presentarlo como
  medición.
- **Olvidar las condiciones de contexto** que cambian el rendimiento: `<altura, turno nocturno,
  acceso restringido, operación en marcha, clima, coordinación con terceros>`.
- **Resolver el problema de otra especialidad** porque parece obvio. Se reporta, no se resuelve.
- **Cotizar el caso ideal.** Si el trabajo real tiene interferencias, van en la partida.
- `<error frecuente en tu oficio y por qué ocurre>`

## Formato de la respuesta

Partida en `runs/<corrida>/partidas/<miembro>.md`, con el formato estándar del sistema y estas
precisiones propias del rol de ejecución:

```markdown
## Desarrollo
**Qué rige.** <norma o estándar, citado>
**Procedimiento.** <qué se hace, en qué orden, con qué método>
**Condiciones previas necesarias.** <lo que debe estar listo antes de empezar>

## Cuantificación
| Ítem | Unidad | Cantidad | Valor unitario | Total | Origen |
| <ítem> | <unidad> | <cantidad> | <valor> | <total> | <medición / plano / costos.md / supuesto> |

## Riesgos de ejecución
| Riesgo | Medida de control | Efecto si ocurre |
```
