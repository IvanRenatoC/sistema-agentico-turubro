# Prompt para generar la imagen del repositorio

Para pegar en un generador de imágenes (GPT / DALL·E / Midjourney). Formato pensado como
encabezado del `README.md`: horizontal 16:9.

**Paleta, fija para todas las variantes:**

| Rol | Color | HEX |
|---|---|---|
| Fondo | Negro absoluto | `#000000` |
| Trazo principal | Cobre | `#B87333` (brillos `#E39B5A`) |
| Acento y nodos | Lila eléctrico | `#B36BFF` |

---

## 1. Prompt principal (con etiquetas)

```
Ilustración conceptual horizontal en formato 16:9 para el encabezado de un repositorio de
software. Estilo line art técnico, no fotorrealista.

TEMA: una oficina de servicios profesionales convertida en sistema. Entra un encargo
desordenado por la izquierda, se organiza en el centro y sale un entregable limpio por la
derecha.

FONDO: negro absoluto #000000, con una retícula técnica apenas perceptible en lila oscuro al
8% de opacidad.

PALETA ESTRICTA de solo tres colores: negro de fondo, cobre #B87333 con brillos #E39B5A, y
lila eléctrico #B36BFF. Sin blanco puro salvo destellos mínimos. Ningún otro color.

COMPOSICIÓN, de izquierda a derecha:
1. Izquierda: cinco documentos desordenados y superpuestos, en línea fina cobre, inclinados
   en ángulos distintos como si llegaran de golpe: una hoja escrita, un plano, una
   fotografía, una onda de audio y una planilla de cálculo.
2. Un canal delgado en lila eléctrico los recoge y los ordena en una sola corriente.
3. Centro: un recuadro hexagonal grande de borde lila eléctrico brillante con relleno negro
   —el nodo coordinador—, del que salen líneas finas cobre hacia abajo.
4. Debajo del hexágono: tres tarjetas rectangulares idénticas de borde cobre, cada una con
   tres líneas internas cobre que insinúan texto, conectadas al nodo central por líneas
   lila. Son los especialistas.
5. Derecha: un único documento vertical, limpio y ordenado, de borde lila eléctrico con
   relleno negro, líneas de texto insinuadas en cobre y un sello circular cobre en la
   esquina inferior.
6. Un arco fino cobre punteado vuelve desde ese documento hacia las tres tarjetas, cerrando
   el ciclo.

TEXTO: exactamente cinco etiquetas, en mayúsculas, tipografía sans-serif geométrica, tamaño
pequeño, escritas exactamente así y sin ninguna otra palabra ni número en toda la imagen:
   ENCARGO         — bajo los documentos desordenados, en cobre
   COORDINADOR     — bajo el hexágono, en lila eléctrico
   ESPECIALISTAS   — bajo las tres tarjetas, en cobre
   ENTREGABLE      — bajo el documento final, en lila eléctrico
   APRENDIZAJE     — sobre el arco punteado, en cobre

ESTILO: trazo fino y uniforme de 1 a 2 píxeles, estética de plano de ingeniería cruzada con
circuito impreso, resplandor suave solo en los trazos lila, geometría limpia y simétrica,
mucho espacio negro vacío. Sin sombras realistas, sin degradados sucios, sin texturas, sin
personas, sin rostros, sin logotipos de marcas reales, sin capturas de pantalla.

SENSACIÓN: precisión y orden que emerge del desorden. Sobrio y elegante, trabajo de oficina
técnica de noche. No futurista, no cargado, no "inteligencia artificial genérica".
```

---

## 2. Variante sin texto (la más segura)

Los generadores suelen deformar las palabras. Si las etiquetas salen mal, usa esta versión y
agrega los textos después en Figma, Canva o Keynote.

```
Idéntico al prompt anterior, con un solo cambio: la imagen no contiene NINGÚN texto, ninguna
letra, ninguna palabra y ningún número. Solo formas geométricas, líneas y símbolos. Deja
espacio negro vacío de unos 60 píxeles bajo cada elemento principal, para agregar las
etiquetas después.
```

---

## 3. Variante cuadrada (avatar, redes, portada de presentación)

```
Mismo tema, paleta y estilo del prompt principal, pero en formato cuadrado 1:1 y con una
composición radial en vez de lineal: el hexágono lila eléctrico al centro; seis tarjetas de
borde cobre distribuidas en círculo a su alrededor, conectadas al centro por líneas finas
lila; un anillo exterior cobre punteado que insinúa el ciclo. Sin texto. Mucho espacio negro.
```

---

## 4. Si el resultado no convence

Pide **un solo ajuste por vez**, en este orden de impacto:

1. **Demasiado cargado** → "reduce a la mitad la cantidad de elementos y duplica el espacio
   negro vacío".
2. **Colores apagados o sucios** → "usa cobre #B87333 y lila eléctrico #B36BFF puros y
   saturados sobre negro absoluto, sin mezclarlos entre sí y sin ningún otro color".
3. **Se ve genérico o tipo stock de IA** → "elimina el resplandor exagerado, los circuitos
   decorativos y cualquier cerebro, robot o red neuronal: solo documentos, tarjetas y líneas".
4. **Texto deformado** → cambia a la variante sin texto y agrega las etiquetas a mano.
5. **Muy oscuro al mirarlo pequeño** → "aumenta el grosor de los trazos a 3 píxeles y el
   contraste de los bordes lila".

## 5. Qué debe leerse en la imagen

Es la prueba para aceptarla o rechazarla. Alguien que no conoce el repositorio debería poder
decir, mirándola tres segundos:

- Que **algo desordenado entra y algo ordenado sale**.
- Que en el medio hay **un coordinador y varios especialistas distintos**, no una sola caja
  mágica.
- Que **el resultado vuelve al inicio** como aprendizaje.

Si las tres cosas no se leen, no es un problema de estilo: es un problema de composición.
