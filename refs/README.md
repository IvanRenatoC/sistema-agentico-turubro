# `refs/` — la fuente de verdad transversal

Aquí vive **lo que rige independiente de quién haga el trabajo**: normas, estándares, reglamentos,
manuales de marca, tarifarios oficiales, criterios de la autoridad. Es lo que un especialista no
puede decidir por su cuenta porque no le pertenece: lo aplica y lo cita.

## La diferencia con `staff/<miembro>/referencias/`

| Carpeta | Qué contiene | Ejemplo de pregunta que responde |
|---|---|---|
| `refs/` | Lo que obliga a **toda** la oficina | ¿Qué exige la norma en este caso? |
| `staff/<id>/referencias/` | Material propio de **un** especialista | ¿Qué rendimiento tiene este equipo? |

Si dos especialistas distintos necesitan el mismo documento, va en `refs/`.

## Qué hay en esta carpeta

| Ruta | Qué es | ¿Se borra? |
|---|---|---|
| `INDEX.md` | La puerta de entrada: qué documento rige qué tema y en qué versión | **No.** Se reemplazan sus filas. |
| `_norma.md` | Ejemplo de extracto operativo | **Sí**, cuando escribas los tuyos. |
| `<nombre-del-documento>.md` | Un extracto operativo por documento que uses seguido | — |
| `originales/` | Los documentos fuente tal cual llegaron | **No** se edita nunca. |

## La regla más importante: extracto propio, no copia

**Los documentos normativos tienen derechos de autor.** Muchos estándares se compran y su licencia
prohíbe expresamente redistribuirlos. Copiar el texto de una norma a este repositorio —y más aún
publicarlo— es una infracción, no un atajo.

Lo que se escribe en `refs/<documento>.md` es un **extracto operativo propio**:

- Con **tus palabras**, describiendo cómo se aplica esa exigencia en tu trabajo real.
- **Citando** el documento, la versión y la sección, para que quien necesite el detalle vaya a la
  fuente.
- **Sin transcribir** el texto normativo, ni sus tablas completas, ni sus figuras.

El extracto no reemplaza la norma: **la hace usable en el día a día y deja el rastro para ir a
buscarla.**

## Los originales y el `.gitignore`

`refs/originales/` está **ignorado por git de forma predeterminada**, justamente por lo anterior: es
el default seguro para un repositorio que puede volverse público. Los documentos viven en el disco
de quien trabaja, y el repositorio guarda el índice y los extractos, que sí son obra propia.

Si tienes documentos de libre redistribución y quieres versionarlos, quita esa regla del
`.gitignore` a conciencia, documento por documento.

## Cómo se usa en una corrida

1. El **planificador** lee `INDEX.md` y declara en `clasificacion.md` qué referencias son
   obligatorias para el pack que aplica.
2. Cada **especialista** lee solo los extractos que su orden declara, y **cita** en su partida.
3. El **transversal** verifica que lo citado corresponda a la versión vigente del `INDEX.md`.

Nadie entra por `originales/`: se entra por `INDEX.md`. Un índice de diez líneas bien curado sirve
más que cuarenta PDF sin leer.

## Reglas de mantención

- **Nunca se cita de memoria.** Si no está en `refs/`, se declara como supuesto.
- **La versión vigente se declara** en `INDEX.md`. Una norma citada sin versión no es una cita.
- **Si el documento cambió**, se actualiza el extracto y se anota la fecha en su historial. Las
  corridas anteriores no se recalculan: quedan como testimonio de lo que regía entonces.
- **Si el extracto no cambia ninguna decisión**, no debería existir. `refs/` no es una biblioteca:
  es una lista de lo que obliga.
