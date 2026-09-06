# PERSONALIZAR.md — Cómo hacer tuyo este repositorio

**Objetivo de este documento:** llevarte, paso a paso, desde el esqueleto que acabas de descargar
hasta una oficina que trabaja con tu criterio y no con criterio genérico. No necesitas saber
programar: todo lo que vas a completar son archivos de texto.

## Cómo se usa esta guía

- Todo lo que aparece **entre `< >` es un espacio para que escribas tú**. Reemplázalo completo,
  incluidos los signos. Ejemplo: `**Nombre:** <nombre de tu oficina>` se convierte en
  `**Nombre:** Talleres del Sur`.
- El resto es instrucción: no necesitas cambiarlo.
- Los bloques de código son **plantillas para copiar y pegar** en el archivo que indica cada paso.
- **Sigue el orden.** Cada paso hace posible el siguiente: sin identidad no hay tono, sin
  especialistas no hay órdenes de trabajo, y sin costos no hay cotización posible.
- Apunta a una **primera versión mínima**, no a la definitiva: un especialista, un servicio, una
  norma. El sistema se afina corriendo encargos reales, no escribiendo más documentación.

> **Regla de oro:** escribe como si estuvieras induciendo a alguien que entra a trabajar contigo
> mañana. Ni folleto de ventas ni manual abstracto: instrucciones que esa persona podría seguir.

## Mapa de lo que vas a completar

| Paso | Archivo | Qué defines | ¿Necesario para la primera corrida? |
|---|---|---|---|
| 1 | `CLAUDE.md` | Identidad, voz, límites, contexto y autonomía | Sí |
| 2 | `staff/<especialista>/` | Quién ejecuta y con qué método y costos | Sí, al menos uno |
| 3 | `packs/<servicio>/detalles.md` | Qué vende la oficina y con qué alcance | Sí, al menos uno |
| 4 | `packs/registry.yaml` | Cómo se reconoce cada encargo | Sí |
| 5 | `refs/INDEX.md` | Qué normas o estándares rigen | Sí, aunque sea breve |
| 6 | `plantillas/estructura-*.md` | La forma de propuestas y entregables | Sí |
| 7 | Tu primer encargo | El sistema funcionando | — |
| 8 | `feedback/` | Cómo el sistema aprende de sus errores | Después de la primera corrida |

---

## Paso 0 — Prepara el terreno

1. Renombra la carpeta del repositorio con el nombre de tu negocio, si quieres.
2. **No borres todavía** las carpetas con prefijo `_`: son moldes y ejemplos de forma
   (`_PLANTILLA/`, `_miembro-1/`, `_pack-1/`, `_id-corrida/`, `_norma.md`). Te sirven de referencia
   mientras completas. Cuando ya tengas tus propias piezas, puedes eliminar las de ejemplo y
   conservar solo los `_PLANTILLA/`.
3. Mira `ejemplos/` para ver dos instanciaciones distintas del mismo esqueleto. Están aplanadas con
   prefijo: `staff-<algo>/` se copia a `staff/<algo>/`.

---

## Paso 1 — La identidad: `CLAUDE.md`

Es el archivo que el agente lee antes que cualquier otro. Tiene seis bloques marcados con
`▶ COMPLETAR`, escritos como bloque citado. **Reemplaza cada bloque citado por tu contenido.**

Plantilla para el primer bloque, el más importante:

```markdown
## Identidad del negocio

- **Nombre:** <nombre con el que te presentas ante un cliente>
- **Rubro:** <en una línea, qué hace esta oficina>
- **Qué vende exactamente:** <horas de especialista / partidas de obra / fases de proyecto /
  retainer mensual / producto cerrado>
- **A quién le vende:** <tipo de cliente, tamaño, quién decide la compra, qué le duele>
- **Qué la distingue:** <la razón por la que te eligen y que un competidor no podría escribir igual>
- **Equipo:** <cuánta gente, qué se hace adentro y qué se subcontrata>
```

Los otros cinco bloques siguen la misma lógica: **voz** (cómo habla la oficina), **límites** (lo
que nunca se promete y lo que exige firma profesional), **contexto local** (idioma, moneda,
unidades, normativa, calendario), **autonomía** (qué decide el agente solo y qué pregunta siempre)
y **confidencialidad** (qué material es sensible y qué nunca sale del repositorio).

**Cómo saber que quedó bien:** si le pasas solo ese archivo a alguien de otro rubro, debería poder
describir tu negocio sin inventar nada.

---

## Paso 2 — Los especialistas: `staff/`

Copia `staff/_PLANTILLA/` tantas veces como especialistas quieras, y renombra cada copia con un
identificador corto y en minúsculas: `staff/<id-del-especialista>/`.

Empieza por **los dos o tres que participan en casi todo encargo**. Cada uno lleva tres archivos.

### `rol.md` — quién es y qué NO hace

```markdown
# Rol — <nombre del especialista>

**Objetivo del rol.** El objetivo de este especialista es <qué resuelve dentro de la oficina>.

**De qué responde.**
- <responsabilidad concreta>
- <responsabilidad concreta>

**De qué NO responde.**
- <tarea que no le corresponde> → se escala a <quién la asume>
- <tarea que no le corresponde> → se escala a <quién la asume>

**Qué necesita recibir para poder trabajar.**
- <dato, documento o medición sin la cual no puede empezar>

**Con qué criterio decide cuando falta información.**
<regla explícita: por ejemplo, "siempre la opción más conservadora y lo declara como supuesto">
```

La sección de lo que **no** hace es la más valiosa del archivo: es la que evita que el agente
opine fuera de su competencia.

### `metodologia.md` — cómo trabaja

```markdown
# Metodología — <nombre del especialista>

**Objetivo.** El objetivo de este documento es <qué debe producir siempre y con qué calidad>.

**Pasos, en orden.**
1. <primer paso>
2. <segundo paso>
3. <tercer paso>

**Controles de calidad.**
- <qué se verifica antes de entregar>

**Criterio de aceptación.**
<cómo se sabe que el trabajo está bien terminado y no solo terminado>

**Errores típicos a evitar.**
- <error que se comete seguido en tu rubro y por qué>

**Formato de la respuesta.**
<qué secciones entrega, en qué orden, con qué nivel de detalle>
```

### `costos.md` — cómo cuantifica

```markdown
# Costos — <nombre del especialista>

**Unidad de cobro.** <metro lineal / hora hombre / jornada / fase / entregable>

**Tarifas.**

| Concepto | Unidad | Valor | Vigencia |
|---|---|---|---|
| <concepto> | <unidad> | <valor> | <fecha o periodo> |

**Rendimientos.**
- <cuánto se avanza por unidad de tiempo, y en qué condiciones>

**Factores y recargos.**
- <situación que encarece el trabajo> → <factor o porcentaje>

**Qué NO incluye el precio.**
- <lo que se cobra aparte o lo pone el cliente>

**Fuente y vigencia.**
<de dónde salen estos valores y cada cuánto se revisan>
```

**Cómo saber que quedó bien:** con esos tres archivos, alguien que no te conoce debería poder
cotizar un trabajo simple de tu rubro y llegar a un número parecido al tuyo.

---

## Paso 3 — Los servicios: `packs/`

Copia `packs/_PLANTILLA/` una vez por servicio que realmente vendas, y renombra:
`packs/<id-del-servicio>/`.

> El molde completo, con todas las secciones y la explicación de cada una, vive en
> `packs/_PLANTILLA/detalles.md`. La versión de abajo es la abreviada, para orientarte sin
> salir de esta guía.

```markdown
# <nombre comercial del servicio>

**Objetivo.** El objetivo de este servicio es <qué problema del cliente resuelve>.

**Qué incluye.**
- <actividad o entregable incluido>

**Qué NO incluye.**
- <lo que la gente asume que viene incluido y no viene>

**Entradas mínimas exigibles al cliente.**
- <sin esto el trabajo no puede empezar>

**Especialistas que participan.**
- <id-del-especialista> — <en qué parte interviene>

**Entregables.**
- <documento, informe o pieza que recibe el cliente>

**Plazo típico.** <duración y de qué depende>

**Supuestos comerciales y riesgos.**
- <supuesto que, si no se cumple, cambia el precio o el plazo>
```

**Define el alcance por sus bordes.** Lo que queda fuera y lo que se le exige al cliente vale más
que la descripción de lo que sí se hace: es lo que evita discusiones a mitad del trabajo.

---

## Paso 4 — El índice: `packs/registry.yaml`

Es el archivo que traduce **lo que dice el cliente** en **qué servicio aplica y a quién se
convoca**. Empieza simple: se corrige con el uso.

```yaml
packs:
  - id: <id-del-servicio>              # el nombre de la carpeta en packs/
    nombre: "<nombre comercial>"
    señales:                            # cómo se reconoce este encargo
      - "<palabra o frase que usa el cliente cuando necesita esto>"
      - "<situación típica que lo dispara>"
    staff:                              # carpetas de staff/ que se activan
      - <id-del-especialista>
    refs_obligatorias:                  # lo que siempre se cita en este servicio
      - <archivo de refs/>
    entregable: plantillas/estructura-entregable.md
```

**Cómo saber que quedó bien:** toma tres encargos reales del año pasado, dáselos al agente y pide
que los clasifique. Si acierta los tres, el registry está vivo. Si falla, agrega las señales que
faltaban en las palabras que **usó el cliente**, no en las tuyas.

---

## Paso 5 — La fuente de verdad: `refs/`

No cargues la biblioteca completa. Escribe el índice de lo que **de verdad rige** y deja los
documentos fuente en `refs/originales/`.

`refs/INDEX.md`:

```markdown
# Índice de referencias

| Tema | Qué decide | Documento | Versión vigente | Extracto |
|---|---|---|---|---|
| <tema> | <qué se resuelve mirando esto> | <nombre del documento> | <versión o fecha> | `refs/<archivo>.md` |
```

Y por cada norma o estándar que uses seguido, un extracto operativo:

```markdown
# <nombre de la norma o estándar>

**Objetivo.** El objetivo de este extracto es <qué parte de la norma se aplica en el día a día>.

**Qué exige, en términos prácticos.**
- <requisito aplicado a tu trabajo real>

**Qué queda fuera de este extracto.**
<lo que hay que ir a buscar al documento original>

**Fuente.** <documento, año, versión> — original en `refs/originales/<archivo>`
```

---

## Paso 6 — La forma: `plantillas/`

Aquí vive la firma profesional de la oficina. Los `.potx` son la identidad visual; los dos
`estructura-*.md` son el guion que el agente respeta al construir cada documento.

```markdown
# Estructura de una <propuesta | entregable>

**Objetivo.** El objetivo de este documento es <qué debe lograr en quien lo lee>.

**Secciones, en orden.**
1. <sección> — <qué va acá, en una línea>
2. <sección> — <qué va acá, en una línea>
3. <sección> — <qué va acá, en una línea>

**Reglas de forma.**
- Extensión: <máximo de páginas o láminas>
- Cifras: <cómo se presentan los precios, con o sin impuestos, qué se detalla>
- Lo que nunca aparece: <compromisos, garantías o datos que no se ponen por escrito>
- Cierre: <cómo termina siempre el documento: próximos pasos, validez, firma>
```

---

## Paso 7 — Tu primer encargo

Deja el material crudo en `input/` y escribe un encargo con esta forma. Un buen encargo trae siete
cosas; si faltan las dos últimas, el agente inventa supuestos.

```text
Encargo nuevo: <título del encargo>.

Cliente: <nombre>. Contacto: <persona y cargo>.
El problema, en palabras del cliente: "<lo que dijo tal cual>".
En input/ dejé: <lista de lo que hay y qué es cada archivo>.
Fecha comprometida: <fecha>.

Trabajo que necesito, en este orden:
1. Procesa input/ y abre la corrida en runs/<AAAA-MM-DD>-<slug-del-encargo>. En el brief.md deja
   explícito lo que no quedó claro del material.
2. Clasifica contra packs/registry.yaml: qué pack aplica, qué staff se activa y qué entradas
   mínimas del pack NO están cubiertas. Si falta un dato que cambia el resultado, pregúntame
   ANTES de planificar.
3. Emite las órdenes de trabajo y ejecútalas. Cada partida debe declarar sus supuestos.
4. Consolida y deja el entregable en runs/<corrida>/salida/ según plantillas/estructura-entregable.md.

Restricciones del encargo:
- <restricción operativa real: turnos, accesos, plazos, condiciones de terreno>
- <restricción normativa: qué norma rige y si debe citarse>
- <restricción comercial: tope de presupuesto, política de precios, qué no se ofrece>

Al final, dime en tres líneas qué decisiones tomaste por tu cuenta y cuáles debo revisar yo.
```

---

## Paso 8 — Cerrar el ciclo: `feedback/`

Después de cada corrida, anota lo que falló. Las notas sin procesar van a `feedback/_bruto/`; lo
destilado, a estos archivos.

```markdown
## <fecha> — <corrida donde ocurrió>

**Qué salió mal o faltó.** <descripción concreta, con el dato o la frase exacta>
**Qué debería haber pasado.** <el resultado correcto>
**Por qué ocurrió.** <qué criterio no estaba escrito>
**A qué archivo va la corrección.** <staff/<id>/metodologia.md | packs/<id>/detalles.md | CLAUDE.md>
**Estado.** <pendiente | incorporado el <fecha>>
```

El feedback es **tránsito, no bodega**: cuando una corrección se repite, se escribe en el archivo
que corresponde y se marca como incorporada. Un `feedback/` que solo crece significa que el
sistema no está aprendiendo.

---

## Cómo saber que la personalización quedó bien

Cuatro pruebas rápidas, todas sobre una corrida de prueba:

1. **Prueba del extraño.** Dale solo `CLAUDE.md` a alguien de otro rubro. Si no puede explicar qué
   vendes y a quién, falta el paso 1.
2. **Prueba del número.** Pide una cotización simple. Si aparece una cifra sin fuente —que no venga
   de `costos.md`, de `refs/` o de un adjunto—, falta el paso 2.
3. **Prueba de la promesa.** Lee la propuesta que genere. Si un competidor podría firmarla tal cual,
   falta el "qué la distingue" del paso 1.
4. **Prueba del no.** Pídele algo fuera de tu alcance. Si no dice "esto no lo hacemos" y te deriva,
   faltan los límites del bloque 3.

## Errores comunes al personalizar

- **Escribir el repositorio completo antes de correr un encargo.** La documentación no se valida
  sola: se valida con trabajo real. Un especialista, un servicio y una corrida enseñan más que
  veinte archivos perfectos.
- **Describir el rol en positivo solamente.** Sin la lista de lo que **no** hace, el especialista
  se expande hasta opinar de todo.
- **Dejar los costos "para después".** Sin `costos.md` el sistema no puede cotizar, y cotizar es la
  mitad del valor.
- **Confundir tono con criterio.** El bloque de voz define cómo suena la oficina; el criterio vive
  en las metodologías. Un tono impecable sobre criterio vacío produce documentos que se leen bien
  y no sirven.
- **Cargar `refs/` con todo.** Un índice de diez líneas con lo que rige es más útil que cuarenta
  PDF sin curar.

## Lista final

- [ ] Los seis bloques de `CLAUDE.md`, completados.
- [ ] Al menos un especialista en `staff/`, con sus tres archivos.
- [ ] Al menos un servicio en `packs/`, con su `detalles.md`.
- [ ] `packs/registry.yaml` clasificando bien tres encargos reales del pasado.
- [ ] `refs/INDEX.md` con lo que de verdad rige.
- [ ] Los dos guiones de `plantillas/`.
- [ ] Una corrida de prueba completa, de principio a fin.
- [ ] Primera anotación en `feedback/`, aunque sea para decir qué salió bien.

Cuando termines, el repositorio dejó de ser un esqueleto y pasó a ser tu oficina. A partir de ahí
el trabajo no es escribir documentación: es correr encargos y corregir lo que aparezca.
