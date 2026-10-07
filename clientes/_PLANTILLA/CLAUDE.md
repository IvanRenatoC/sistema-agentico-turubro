# CLAUDE.md — Cliente: <nombre del cliente>

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

## ▶ COMPLETAR — Ficha del cliente

> Reemplaza este bloque. Escríbelo como se lo explicarías a alguien que va a atender a este
> cliente por primera vez. Lo que no sepas todavía, déjalo como pregunta abierta: no lo inventes.
>
> - **Nombre y rubro:** cómo se llama, a qué se dedica, tamaño.
> - **Quién decide y quién es el contacto:** no siempre son la misma persona.
> - **Qué le duele:** el problema por el que llegó, en sus palabras.
> - **Identidad de marca:** colores, tipografías, logo, tono. Si existe un manual, dónde está.
> - **Preferencias y vetos:** lo que le gusta, lo que rechazó antes, palabras que no quiere ver.
> - **Condiciones comerciales:** forma de pago, tarifa especial si la hay, quién la autorizó.
> - **Historial:** primera fecha de contacto y qué se le ha propuesto o entregado.

## Confidencialidad de este cliente

> Opcional. Si este cliente exige algo más estricto que el bloque 6 del `CLAUDE.md` de la raíz
> —un acuerdo de confidencialidad, datos de pacientes, información financiera—, escríbelo aquí.
