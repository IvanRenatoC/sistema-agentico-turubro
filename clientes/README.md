# `clientes/` — una carpeta aislada por cliente

La oficina (`staff/`, `packs/`, `refs/`, `plantillas/`, `feedback/`) es una sola y la comparten
todos los clientes. Lo que es **de un cliente** —su ficha, su material, sus propuestas y sus
corridas— vive en su propia carpeta y no se mezcla con ningún otro (regla R13 de `CLAUDE.md`).

```text
clientes/
├── README.md
├── _PLANTILLA/            Molde. Se copia para cada cliente nuevo; nunca se trabaja dentro.
├── _cliente-ejemplo/      Ejemplo de forma (Café Aurora, ficticio). Nadie escribe dentro.
└── <slug-del-cliente>/    Un cliente real.
    ├── CLAUDE.md          Su ficha: marca, colores, tono, quién decide, vetos, historial.
    ├── notas.md           Lo aprendido con él que solo vale para él.
    ├── .claude/           Permisos y el hook de aislamiento para la sesión de este cliente.
    ├── input/             Bandeja de entrada de su material. Zona de paso, no se versiona.
    ├── propuestas/        Lo que se le ofreció, antes de ejecutar. Una carpeta por propuesta.
    └── runs/              Lo que se le hizo. Una carpeta por corrida.
```

## Dar de alta un cliente

1. Copia `clientes/_PLANTILLA/` a `clientes/<slug-del-cliente>/`, en minúsculas y con guiones:
   `clientes/cafe-aurora/`, `clientes/peluqueria-la-reina/`. Copia también la carpeta oculta
   `.claude/`.
2. Completa su `CLAUDE.md` con lo que sepas. Lo que no sepas, déjalo como pregunta abierta.
3. Abre **esa carpeta** como proyecto en Claude Code (en la app de escritorio, al elegir la
   carpeta del proyecto). Desde ahí se usan `/proponer`, `/ejecutar` y `/entregar` como siempre.

## Por qué una sesión por cliente

Porque lo que un agente tiene a la vista termina influyendo en lo que hace. Si en la misma sesión
leyó el rebranding de una cafetería, el sitio web de una peluquería puede salir con su paleta o su
tono sin que nadie lo haya pedido. Abrir la carpeta del cliente hace tres cosas a la vez:

- **Carga su ficha automáticamente.** Claude Code lee el `CLAUDE.md` de la carpeta abierta y el de
  la raíz del repositorio: reglas de la oficina más contexto del cliente, y nada más.
- **Activa el hook de aislamiento.** `.claude/hooks/aislar-cliente.py` bloquea cualquier lectura o
  escritura en la carpeta de otro cliente, y cualquier búsqueda que recorra `clientes/` completo.
- **Empieza con contexto limpio.** Una sesión nueva no arrastra la conversación de otro cliente.

Cambiar de cliente es cambiar de carpeta, no seguir en la misma conversación.

## Lo que sí cruza entre clientes

El aprendizaje que sirve para cualquier cliente: que un tipo de entregable genera más rondas de
corrección, que un rendimiento estaba subestimado, que un alcance quedó mal definido. Ese
aprendizaje cruza **por `feedback/`**, escrito sin el nombre del cliente ni datos que lo
identifiquen. Lo que solo vale para un cliente se queda en su `notas.md`.

La pregunta que decide: **¿esto aplicaría a otro cliente?**

## Privacidad y `.gitignore`

Esta carpeta contiene nombres de clientes, precios y material que te entregaron:

- **Repositorio privado:** versiona todo. La trazabilidad vale más que el peso.
- **Repositorio público:** activa las reglas comentadas al final del `.gitignore`, que ignoran
  `clientes/*` y conservan solo `_PLANTILLA/` y `_cliente-ejemplo/`.

El material crudo de `input/` no se versiona nunca, en ningún caso.
