---
name: entregar
description: Toma el trabajo ya consolidado y lo convierte en el entregable final con la forma y la voz de la casa, verificando el guion sección por sección. Úsala cuando la ejecución está lista y hay que darle forma de documento, o cuando hay que rehacer el formato de un entregable sin repetir el trabajo técnico.
---

# Flujo: entregar

**Objetivo.** Convertir `consolidado.md` en el documento que recibe el cliente, con la forma de la
casa y sin perder ni agregar nada en el camino.

Este archivo es **normativo** para el flujo; la sección 4 de `docs/ARQUITECTURA.md` es su resumen
invariante.

## Por qué es un flujo aparte

Porque **la forma se rehace más veces que el fondo**. Cambiar el formato de un entregable, ajustar
la extensión o rearmarlo para otra audiencia no debería obligar a repetir el trabajo técnico. Si
esto viviera dentro de `ejecutar`, cada cambio de formato sería una corrida nueva.

## Antes de empezar

1. **Exige un consolidado.** Sin `consolidado.md` no hay nada que dar forma: el flujo que
   corresponde es `ejecutar`.
2. **Identifica la audiencia y el guion.** `plantillas/estructura-entregable.md` para trabajo
   ejecutado; `estructura-propuesta.md` si lo que se arma es comercial.
3. **Lee la voz** en `CLAUDE.md`: tono, tratamiento, extensión por defecto y lo que nunca se pone
   por escrito.

## Pasos

### 1. Recorrer el guion, sección por sección

Para cada sección del guion, una de tres cosas:

- **Tiene contenido** en el consolidado → se traslada.
- **No tiene contenido pero corresponde** → se marca como faltante y se pide. No se rellena con
  texto de relleno.
- **No aplica a este encargo** → se dice por qué. **Nunca se elimina en silencio.**

### 2. Trasladar sin reinterpretar

El entregable **no es una segunda opinión**. Traslada lo que dice el consolidado; si algo no se
entiende o parece equivocado, se devuelve al coordinador en vez de arreglarlo de paso.

Las cifras se copian con su condición: cerrada o estimada, y con sus supuestos visibles. Un total
que en el consolidado tenía tres supuestos no puede aparecer limpio en el entregable.

### 3. Traducir a la audiencia, no al gusto

Ajusta el lenguaje a quién lee —según `CLAUDE.md`— sin cambiar el fondo. Si la audiencia no es
técnica, se explica; no se simplifica hasta que deje de ser cierto.

### 4. Verificar antes de cerrar

- Todas las secciones del guion, presentes o justificadas.
- Ningún compromiso que `CLAUDE.md` prohíba.
- Todo lo que requiere firma profesional, marcado como pendiente de firma.
- Los supuestos abiertos, visibles: **si el cliente tiene que saberlo, va en el documento**, no
  solo en el consolidado.
- Extensión y forma dentro de lo que define el guion.

### 5. Dejar el entregable y cerrar

En `runs/<corrida>/salida/`. Cierra con las tres líneas de siempre: qué decidiste por tu cuenta,
qué debe revisar la persona, qué queda abierto.

**No se envía al cliente.** Queda listo para que una persona lo revise, lo asuma y lo firme.

## Contrato de salida

| Archivo | Contenido |
|---|---|
| `runs/<corrida>/salida/<entregable>` | El documento con la forma de la casa |
| Cierre en el chat | Faltantes pedidos, secciones justificadas y qué debe revisarse |

## Reglas del flujo

- **No se agrega contenido nuevo.** Todo lo que aparece en el entregable existe en el consolidado o
  en una partida.
- **No se borra una sección del guion sin decirlo.**
- **No se limpian los supuestos** para que el documento se vea más sólido: eso es exactamente lo
  que después no se puede defender.
- **El entregable enviado no se edita.** Una corrección genera una versión nueva.

## ▶ AJUSTA A TU NEGOCIO

> Opcional. Reemplaza lo que esté entre `< >`.
>
> - **Formato de salida por defecto:** `<presentación / informe / planilla / PDF>`
> - **Qué se anexa siempre:** `<planos, fotos, memoria de cálculo, fuentes>`
> - **Numeración de versiones:** `<v1, v2 / fecha / código propio>`
> - **Quién firma y cómo aparece la firma:** `<nombre, cargo, registro profesional>`
