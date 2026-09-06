---
name: ejecutar
description: Ejecuta un encargo aprobado de principio a fin: abre la corrida, entiende, clasifica, planifica, reparte entre especialistas, consolida y deja el trabajo listo para entregar. Úsala cuando el trabajo ya está aprobado y hay que hacerlo. Para cotizar antes de vender, usa proponer; para darle forma final a lo ya ejecutado, usa entregar.
---

# Flujo: ejecutar

**Objetivo.** Convertir un encargo aprobado en trabajo terminado y trazable dentro de
`runs/<corrida>/`, con el criterio escrito de la oficina y no con criterio improvisado.

Es el camino por defecto. Este archivo es **normativo** para el flujo; la sección 4 de
`docs/ARQUITECTURA.md` es su resumen invariante.

## Antes de empezar

1. **Verifica la identidad.** Si `CLAUDE.md` tiene bloques sin completar, o si el pack o el
   especialista que hacen falta no existen, **detente y dilo**. No inventes identidad ni piezas.
2. **Lee el aprendizaje acumulado:** `feedback/GLOBAL.md`, y más adelante los archivos de
   `feedback/staff/` y `feedback/packs/` de las piezas que se activen.
3. **Confirma que el encargo está aprobado.** Si todavía hay que cotizar o convencer, el flujo que
   corresponde es `proponer`.

## Pasos

### 1. Abrir la corrida

- Identificador: `AAAA-MM-DD-<slug-del-encargo>`, minúsculas y guiones. Si hubo propuesta previa,
  **usa el mismo identificador** que en `propuestas/` para poder cruzarlas.
- Archiva el material recibido en `runs/<corrida>/adjuntos/<AAAA-MM-DD>-<lote>/`, **sin modificar
  ningún original**.
- Ejecuta la ingesta a `adjuntos/_texto/`. Lo que no se pueda convertir queda registrado como no
  convertible, con la razón: nada falla en silencio.

### 2. Escribir el brief

El coordinador escribe `brief.md`. Separa **lo que el cliente afirma** de **lo que el material
demuestra**; si se contradicen, queda escrito, no resuelto en silencio. Cierra con lo que quedó
pendiente de confirmar.

### 3. Delegar clasificación y plan

Invoca al **planificador** con el brief. Devuelve `clasificacion.md` y `plan.md`.

**No clasifiques tú.** Dos lecturas independientes del mismo encargo detectan lo que una sola
normaliza.

### 4. Preguntar una sola vez

Junta todo lo que falta —empezando por las entradas mínimas del pack que no llegaron— en **una sola
tanda, priorizada**, antes de emitir órdenes. Si la persona no está disponible, avanza con el
supuesto más conservador y déjalo marcado en el brief; no lo esconda en el consolidado.

### 5. Emitir las órdenes de trabajo

Una por especialista activado, en `ordenes/<miembro>.md`: contexto mínimo, entregable esperado,
entradas que se le entregan, límites y plazo.

**Contexto mínimo es literal.** Nunca le pases el encargo completo: el aislamiento es lo que hace
que las contradicciones entre especialidades aparezcan al integrar.

### 6. Ejecutar

Invoca al **especialista** una vez por miembro. En paralelo cuando el plan no declare dependencias
entre ellos; en serie cuando sí.

Si el pack activa un especialista transversal —revisión, control de calidad—, **va al final**, y su
orden incluye las partidas de los demás como entradas.

### 7. Consolidar

El coordinador escribe `consolidado.md`: integra por unidad de trabajo, resuelve contradicciones
dejando escrito el criterio usado, detecta huecos y dobles conteos, totaliza y lista los supuestos
abiertos. Lo que no puede resolver, lo escala.

### 8. Cerrar

Tres cosas, breves y al final: **qué decidiste por tu cuenta**, **qué debe revisar la persona** y
**qué supuestos quedaron abiertos**. Sin esto la persona solo puede aceptar o rechazar el trabajo,
no dirigirlo.

Si el encargo pide un documento con forma, continúa con el flujo `entregar`.

### 9. Alimentar el aprendizaje

Lo que salió mal se anota en `feedback/`. Cuando una corrección se repite, **propón** promoverla al
`rol.md`, `metodologia.md`, `costos.md` o `CLAUDE.md` que corresponda: proponer, no aplicar.

## Contrato de salida

| Archivo | Autor |
|---|---|
| `runs/<corrida>/brief.md` | coordinador |
| `runs/<corrida>/clasificacion.md`, `plan.md` | planificador |
| `runs/<corrida>/ordenes/<miembro>.md` | coordinador |
| `runs/<corrida>/partidas/<miembro>.md` | cada especialista |
| `runs/<corrida>/consolidado.md` | coordinador |

## Reglas del flujo

- **Ningún número sin procedencia:** `refs/`, un `costos.md`, un adjunto, o supuesto declarado.
- **Nadie escribe fuera de la corrida**, y los originales del cliente no se editan nunca.
- **No se contacta al cliente** ni se envía nada en su nombre: se prepara el borrador.
- **Ningún archivo tiene dos autores.**
- **Si un paso se omite** por el tamaño del encargo, se dice que se omitió y por qué.

## ▶ AJUSTA A TU NEGOCIO

> Opcional. Reemplaza lo que esté entre `< >`; el flujo funciona sin esto.
>
> - **Encargos que pueden saltarse el paso 3:** `<tipos de encargo tan repetidos que la clasificación es evidente>`
> - **Umbral para dividir en fases:** `<tamaño, plazo o monto desde el cual una corrida se parte en varias>`
> - **Revisión transversal obligatoria:** `<siempre / sobre cierto monto / nunca>`
