---
name: proponer
description: Convierte un encargo en una propuesta comercial: entiende el problema, clasifica el servicio, estima magnitud y precio con la información disponible, y arma el documento con el guion de la casa. Úsala cuando todavía hay que cotizar o convencer, antes de que el trabajo esté aprobado. Si ya está aprobado, usa ejecutar.
---

# Flujo: proponer

**Objetivo.** Producir una propuesta que se pueda defender: con el alcance claro, el precio
sostenido por supuestos explícitos, y lo que queda fuera dicho antes de firmar.

Este archivo es **normativo** para el flujo; la sección 4 de `docs/ARQUITECTURA.md` es su resumen
invariante.

## La diferencia con `ejecutar`

No es el rigor: es el **nivel de detalle exigible**. Una propuesta se construye con la información
que hay **antes** de tener acceso completo. Por eso la cuantificación es gruesa —magnitud y rango,
no partidas cerradas— y por eso los supuestos que sostienen el precio son la parte más importante
del documento.

Una propuesta que promete un precio cerrado sin las entradas mínimas del pack no es más
competitiva: es más barata de perder.

## Antes de empezar

1. **Verifica la identidad.** Sin `CLAUDE.md` completo no hay voz ni límites, y una propuesta es
   justamente voz y límites. Si falta, detente y dilo.
2. **Lee `feedback/packs/`** del servicio que se va a ofrecer: ahí está lo que no convenció antes.
3. **Confirma que es etapa comercial.** Si el trabajo ya está aprobado, el flujo es `ejecutar`.

## Pasos

### 1. Abrir la carpeta de la propuesta

`propuestas/AAAA-MM-DD-<slug-del-encargo>/`. Este flujo **no abre corrida en `runs/`**: si la
propuesta se aprueba, `ejecutar` abre `runs/` con **el mismo identificador**, y así se puede cruzar
lo ofrecido con lo ejecutado.

### 2. Escribir el brief comercial

`propuestas/<id>/brief.md`, con la misma estructura del brief de una corrida y un énfasis distinto:
qué problema dice tener el cliente, qué muestra el material, **quién decide la compra** y qué
tendría que ser verdad para que este servicio sea la respuesta.

### 3. Clasificar

Invoca al **planificador**. Interesa sobre todo una cosa: **qué entradas mínimas del pack no están
cubiertas**. Eso define si se puede cotizar cerrado, por rango, o si primero hay que vender un
levantamiento.

### 4. Estimar

Invoca a los **especialistas** que el pack active, con órdenes que pidan explícitamente
**estimación gruesa**: magnitud, rango y los supuestos que la sostienen. Nada de partidas cerradas
con información incompleta.

Si el detalle del cálculo merece quedar escrito, va en `propuestas/<id>/estimacion.md`.

**Ningún valor inventado.** Lo que no está en un `costos.md` se declara como supuesto y se avisa.

### 5. Armar el documento

Con el guion de `plantillas/estructura-propuesta.md` y la identidad visual de
`plantillas/propuesta.potx`. El guion se respeta: si una sección no aplica, se dice por qué en vez
de eliminarla en silencio.

Verifica contra `CLAUDE.md` que no aparezca ningún compromiso prohibido: plazos garantizados,
precios cerrados sin visita, resultados de negocio asegurados.

### 6. Cerrar

- **Los supuestos que sostienen el precio**, listados, y **qué lo cambiaría**.
- **Qué se le pide al cliente** para poder empezar, con fecha.
- **Validez de la propuesta.**
- Y para la persona, no para el cliente: qué decidiste por tu cuenta y qué debe revisar.

La propuesta enviada queda archivada como `propuestas/<id>/propuesta.pdf`: es la versión firmada en
el tiempo, y no se edita después.

### 7. Registrar el desenlace

Cuando la propuesta se resuelve —aprobada, rechazada o sin respuesta—, el aprendizaje va a
`feedback/packs/<pack>.md`: qué se ofreció, qué pasó y por qué. Alcance mal definido, precio fuera
de mercado, entregable que no convenció.

**Una propuesta perdida sin razón anotada es la información más cara que se pierde en una oficina de
servicios.**

## Contrato de salida

| Archivo | Contenido |
|---|---|
| `propuestas/<id>/brief.md` | El encargo entendido en etapa comercial |
| `propuestas/<id>/estimacion.md` | Opcional: el detalle del cálculo grueso y sus supuestos |
| `propuestas/<id>/propuesta.pdf` | El documento enviado |

## Reglas del flujo

- **Nada se promete fuera de lo que el pack incluye.** El alcance del documento es el alcance del
  pack, no lo que el cliente quisiera oír.
- **Toda cifra declara si es cerrada o estimada.** Mezclarlas es la forma más común de perder plata.
- **No se envía nada al cliente:** se deja el documento listo para revisión y firma de una persona.
- **Si el encargo no calza con ningún pack**, esa es la conclusión: propón declinar o crear un
  servicio nuevo, en vez de estirar uno existente.

## ▶ AJUSTA A TU NEGOCIO

> Opcional. Reemplaza lo que esté entre `< >`.
>
> - **Validez por defecto de una propuesta:** `<días>`
> - **Cuándo se cotiza cerrado y cuándo por rango:** `<condición: por ejemplo, cerrado solo con visita previa>`
> - **Descuentos o condiciones que puedes ofrecer sin autorización:** `<ninguno / cuáles>`
> - **Qué se adjunta siempre:** `<referencias, trabajos previos, certificados, seguros>`
