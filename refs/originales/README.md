# `refs/originales/` — los documentos fuente

Los documentos tal cual llegaron: PDF, DOCX, planillas oficiales. **No se editan nunca.** Se citan
desde los extractos de `refs/`.

## Esta carpeta está ignorada por git

Es el default seguro. Muchos estándares se compran y su licencia **prohíbe redistribuirlos**;
subirlos a un repositorio —y más aún publicarlo— es una infracción de esa licencia.

El repositorio versiona el índice y los extractos, que son obra propia. Los documentos originales
viven en el disco de quien trabaja.

Si tienes documentos de libre redistribución y quieres versionarlos, quita la regla del
`.gitignore` **a conciencia y documento por documento**, no la carpeta completa.

## Convención de nombres

`<emisor>-<identificador>-<version>.<ext>`, en minúsculas y con guiones. Con eso, el archivo se
reconoce sin abrirlo y la versión queda a la vista, que es lo que más se confunde.

## Cómo se registra

Todo documento que entra acá se anota en `refs/INDEX.md` con su versión vigente y, si se usa
seguido, se le escribe un extracto operativo en `refs/<nombre-del-documento>.md`.

Un original sin fila en el índice es un documento que nadie va a encontrar.
