# CLAUDE.md — Cliente: Café Aurora (ejemplo)

> **Esto es un ejemplo de forma, no un cliente real** (regla R11). Muestra cómo se ve una ficha
> completa. Para un cliente nuevo se copia `clientes/_PLANTILLA/`, no esta carpeta. Nadie escribe
> dentro de `_cliente-ejemplo/`.

Este archivo es la **ficha del cliente**. Claude Code lo lee cuando esta carpeta se abre como
proyecto, y lee también, automáticamente, el `CLAUDE.md` de la raíz del repositorio: las reglas de
la oficina siguen mandando. Aquí solo se agrega lo que es **propio de este cliente**.

## Cómo se trabaja desde esta carpeta

- **Esta sesión trabaja para un solo cliente: este.** No se lee, no se cita y no se reutiliza
  nada de otra carpeta de `clientes/` (regla R13). Un hook lo bloquea igual, pero la regla va
  primero.
- **La oficina está dos niveles arriba**, en la raíz del repositorio (`../../`): `staff/`,
  `packs/`, `refs/`, `plantillas/` y `feedback/`. Se leen desde ahí.
- **El expediente está en esta carpeta:** `input/`, `propuestas/`, `runs/` y `notas.md`. Las
  rutas de R5 que empiezan con `clientes/<cliente>/` apuntan aquí.
- **Lo que aprendes de este cliente se queda aquí**, en `notas.md`. A `../../feedback/` solo sube
  lo que serviría con cualquier otro cliente, y sube anonimizado.

---

## Ficha del cliente

- **Nombre y rubro:** Café Aurora. Cafetería de especialidad con dos locales en Valparaíso, 14
  personas. Tuesta su propio grano.
- **Quién decide y quién es el contacto:** decide la dueña, Marcela Soto. El contacto del día a
  día es Tomás, el administrador; no aprueba gastos.
- **Qué le duele:** "la gente nos ve como una cafetería más del cerro". Quiere vender su grano
  envasado en otros locales y la marca actual no lo sostiene.
- **Identidad de marca:** logo dibujado a mano hace ocho años, sin manual. Usa un verde oscuro que
  quiere conservar. Tono cercano, nunca solemne.
- **Preferencias y vetos:** no quiere fotos de banco de imágenes. Rechaza la palabra "artesanal":
  dice que la usa todo el mundo.
- **Condiciones comerciales:** 50 % al aprobar la propuesta, 50 % contra entrega. Sin tarifa
  especial.
- **Historial:** primer contacto el 2026-10-03. Propuesta de rebranding en preparación.

## Confidencialidad de este cliente

Los volúmenes de venta por local que entregó en la reunión no se citan en ningún entregable: los
compartió solo para dimensionar el envasado.
