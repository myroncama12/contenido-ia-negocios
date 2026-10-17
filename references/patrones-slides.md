# Patrones de Slides (genérico)

Cada slide de un carrusel cae normalmente en uno de estos 6 patrones. Elegí
el que corresponda según el guion, en vez de inventar layout desde cero.
Todos los ejemplos asumen que ya hiciste el setup de `theme.py` para el
negocio activo (ver `guia-visual-generica.md`) y que estás en una carpeta
desde la que podés hacer `from bg import make_background` y
`from helpers import *`.

Tamaño de lienzo siempre 1080x1080. Formato de salida: PNG.

---

## Principio de composición: lectura en Z

En slides con más de un elemento, el ojo recorre la imagen en forma de "Z":
arriba-izquierda → arriba-derecha → diagonal → abajo-izquierda → abajo-derecha.
Ubicá logo/eyebrow arriba-izquierda, el elemento de mayor peso visual (foto o
titular) en el centro de ese recorrido, y el CTA/cierre abajo. No hace falta
aplicarlo de forma rígida, pero es el default razonable cuando no hay otra
indicación.

## Patrón A — Portada / Gancho

Uso: primera slide, hook que detiene el scroll. **Regla fija: la portada es
solo texto (sin foto de producto), y el titular + subtítulo van siempre
centrados horizontalmente** — es la slide que más se beneficia de simetría,
a diferencia del resto del carrusel que sigue lectura en Z.

```python
from bg import make_background
from helpers import *
import theme
from PIL import ImageDraw

base = make_background(seed=1).convert("RGBA")
draw = ImageDraw.Draw(base)
add_logo(base, center=(540, 130), diameter=140)  # logo centrado en portada
draw.text((540, 210), theme.BRAND_NAME, font=font(FONT_BODY_BOLD, 30), fill=ACCENT, anchor="mm")

f_h1 = font(FONT_DISPLAY, 78)
draw.text((540, 380), "LÍNEA 1 DEL TITULAR", font=f_h1, fill=WHITE, anchor="mm")
draw.text((540, 465), "LÍNEA 2 EN ACENTO", font=f_h1, fill=ACCENT, anchor="mm")

f_sub = font(FONT_BODY_MED, 34)
sub_lines = wrap_text("Subtítulo de una o dos líneas.", f_sub, 900, draw)
draw_multiline(draw, (60, 570), sub_lines, f_sub, GRAY, line_spacing=1.25, align="center", anchor_x=540)

draw.text((540, 990), "DESLIZÁ »", font=font(FONT_BODY_BOLD, 30), fill=ACCENT, anchor="mm")
base.convert("RGB").save("slide1.png")
```

---

## Patrón B — Foto + titular debajo (problema / contexto / detalle)

Uso: fotos de **contexto o proceso** (no el producto/resultado final) — la
foto va en tarjeta redondeada arriba, el titular va completamente debajo
(nunca solapado ni a caballo del borde).

**Cuando la foto SÍ es el producto o resultado terminado, no uses este
patrón — usá el Patrón D (foto a sangre completa con texto superpuesto).**
Las fotos de tarjeta redondeada funcionan para "iba a explicar algo" y se
sienten chicas/genéricas para "acá está el resultado" — ahí gana el impacto
de la foto ocupando el espacio completo.

```python
from bg import make_background
from helpers import *
import theme
from PIL import Image, ImageDraw

base = make_background(seed=2).convert("RGBA")
draw = ImageDraw.Draw(base)
add_logo(base, center=(90, 90), diameter=120)
draw.text((160, 68), theme.BRAND_NAME, font=font(FONT_BODY_BOLD, 26), fill=ACCENT)
draw.text((60, 175), "TAG DE CONTEXTO", font=font(FONT_BODY_BOLD, 30), fill=GRAY)

photo = Image.open("ruta/a/la/foto.jpg").convert("RGB")
box = (60, 230, 960, 460)  # x, y, w, h — AJUSTAR alto según cuánto texto va después
tmp = Image.new("RGBA", (1080, 1080), (0, 0, 0, 0))
paste_rounded(tmp, photo, box, radius=28)
base = Image.alpha_composite(base, tmp)
draw = ImageDraw.Draw(base)
bx, by, bw, bh = box
draw.rounded_rectangle([bx, by, bx+bw, by+bh], radius=28, outline=(255,255,255,40), width=2)

y = by + bh + 60
f_h1 = font(FONT_DISPLAY, 58)
for line in ["TITULAR LÍNEA 1", "TITULAR LÍNEA 2"]:
    draw.text((60, y), line, font=f_h1, fill=WHITE)
    y += 68

base.convert("RGB").save("slide2.png")
```

**IMPORTANTE — antes de fijar el `box`, calculá que todo el texto que sigue
quepa dentro de 1080px de alto.** Si se pasa de ~1040px, reducí el alto de la
foto o el tamaño de fuente antes de generar, no después de ver el resultado
recortado.

---

## Patrón C — Solo texto, declaración emocional

Uso: slides intermedias sin foto, para que el copy respire.

```python
from bg import make_background
from helpers import *
from PIL import ImageDraw

base = make_background(seed=3).convert("RGBA")
draw = ImageDraw.Draw(base)
add_logo(base, center=(90, 90), diameter=120)
draw.text((160, 68), theme.BRAND_NAME, font=font(FONT_BODY_BOLD, 26), fill=ACCENT)

f_h1 = font(FONT_DISPLAY, 88)
draw.text((60, 340), "FRASE FUERTE,", font=f_h1, fill=WHITE)
draw.text((60, 440), "EN ACENTO EL", font=f_h1, fill=ACCENT)
draw.text((60, 540), "PUNTO CLAVE...", font=f_h1, fill=ACCENT)

f_h2 = font(FONT_DISPLAY, 58)
draw.text((60, 680), "REMATE EN GRIS", font=f_h2, fill=GRAY)

base.convert("RGB").save("slide3.png")
```

---

## Patrón D — Producto/Resultado y Clímax: foto a sangre completa + texto superpuesto

Uso por default para **mostrar el producto o resultado terminado** (no solo
para la slide de clímax). La foto ocupa la mitad/dos tercios superiores sin
recorte redondeado, con degradado hacia el fondo de marca; el texto va
superpuesto sobre la foto (usando `top_gradient_overlay`/
`bottom_gradient_overlay` detrás para legibilidad) o en la franja de abajo,
nunca en tarjeta redondeada.

```python
from bg import make_background
from helpers import *
from PIL import Image, ImageDraw

base = make_background(seed=4).convert("RGBA")
photo = Image.open("ruta/a/la/foto.jpg").convert("RGB")
box = (0, 0, 1080, 760)
tmp = Image.new("RGBA", (1080, 1080), (0, 0, 0, 0))
paste_rounded(tmp, photo, box, radius=0)
base = Image.alpha_composite(base, tmp)

# degradado de transición foto -> fondo de marca
grad_h = 220
grad = Image.new("L", (1080, grad_h))
for i in range(grad_h):
    grad.putpixel((0, i), int(255 * (i / grad_h)))
grad = grad.resize((1080, grad_h))
bg_block = Image.new("RGBA", (1080, grad_h), BG + (255,))
fade_layer = Image.new("RGBA", (1080, 1080), (0, 0, 0, 0))
fade_layer.paste(bg_block, (0, 760 - grad_h), grad)
base = Image.alpha_composite(base, fade_layer)

add_logo(base, center=(90, 90), diameter=120)
draw = ImageDraw.Draw(base)
f_h1 = font(FONT_DISPLAY, 52)
draw.text((60, 800), "TITULAR BLANCO", font=f_h1, fill=WHITE)
draw.text((60, 866), "TITULAR EN ACENTO", font=f_h1, fill=ACCENT)

base.convert("RGB").save("slide4.png")
```

**OJO con fotos que ya traen un logo incrustado** (fotos promocionales
previas del negocio): recortá la imagen antes de pasarla a `paste_rounded`
para excluir esa zona. Revisá la imagen completa con `view` antes de decidir
el crop.

---

## Patrón E — Cierre + CTA (barra de acento)

Última slide. Frase de marca (sacada de `identidad-marca.md`) + barra de CTA
que invite a interacción — nunca venta dura en contenido orgánico, salvo que
`config/objetivos.md` indique lo contrario para ese negocio.

```python
from bg import make_background
from helpers import *
from PIL import ImageDraw

base = make_background(seed=6).convert("RGBA")
draw = ImageDraw.Draw(base)
add_logo(base, center=(120, 150), diameter=200)

f_h1 = font(FONT_DISPLAY, 92)
draw.text((60, 320), "FRASE DE MARCA", font=f_h1, fill=WHITE)
draw.text((60, 415), "LÍNEA 2", font=f_h1, fill=ACCENT)

f_sub = font(FONT_BODY_MED, 32)
sub_lines = wrap_text("Tagline o filosofía corta del negocio.", f_sub, 900, draw)
draw_multiline(draw, (60, 640), sub_lines, f_sub, GRAY, line_spacing=1.3)

accent_bar(base, draw, xy=(60, 840), w_h=(960, 160),
           text="TU CTA DE INTERACCIÓN AQUÍ",
           fnt=font(FONT_BODY_BOLD, 34), radius=18)

base.convert("RGB").save("slide6.png")
```

---

## Patrón F — Split "Tu problema / Nuestra solución" (queja fija + solución que cambia)

Uso: carruseles del patrón `patron-problema-solucion.md`. Es el único layout
de dos columnas: la columna izquierda ("problema") es **idéntica en todas las
slides del carrusel** y la derecha ("solución") trae un producto distinto en
cada una. Fondo claro o plano del tema; el producto va sobre su propio fondo
limpio (mockup o foto recortada), sin recorte redondeado ni degradado.

Reglas de composición:
- Misma burbuja, misma posición y mismo texto en todas las slides: generar la
  columna izquierda **una sola vez** (función o variable) y reutilizarla.
- Encabezados en dos niveles ("TU" arriba pequeño en bold, "problema" abajo
  grande en acento; igual a la derecha con "NUESTRA" / "solución"). Usar
  `FONT_DISPLAY` para ambos o la tipografía de títulos del tema.
- Línea divisoria vertical centrada (x=540) entre las dos columnas.
- El producto ocupa el ~60 % de la altura de la columna derecha, centrado.
- La burbuja de chat va a la altura media de la columna izquierda, con una
  hora pequeña (ej. "20:21") dentro. **Sin emojis dentro de la burbuja.**
- Marca (logo) discreto en una esquina, no compite con los encabezados.

```python
from bg import make_background
from helpers import *
import theme
from PIL import Image, ImageDraw

PROBLEMA = "No tengo qué ponerme"   # una sola queja, igual en todas las slides
HORA = "20:21"
PRODUCTOS = ["producto1.png", "producto2.png", "producto3.png", "producto4.png"]

def columna_problema(base):
    draw = ImageDraw.Draw(base)
    f_eyebrow = font(FONT_BODY_BOLD, 54)
    f_title = font(FONT_DISPLAY, 86)
    draw.text((270, 215), "TU", font=f_eyebrow, fill=WHITE, anchor="mm")
    draw.text((270, 290), "problema", font=f_title, fill=ACCENT, anchor="mm")
    # burbuja de chat
    bx, by, bw, bh = 20, 520, 480, 120
    draw.rounded_rectangle([bx, by, bx + bw, by + bh], radius=40, fill=ACCENT)
    draw.polygon([(bx + 6, by + bh - 20), (bx - 14, by + bh + 12), (bx + 60, by + bh - 6)], fill=ACCENT)
    f_msg = font(FONT_BODY_BOLD, 32)
    lines = wrap_text(PROBLEMA, f_msg, bw - 70, draw)
    draw_multiline(draw, (bx + 36, by + 30), lines, f_msg, WHITE, line_spacing=1.15)
    draw.text((bx + bw - 20, by + bh - 22), HORA, font=font(FONT_BODY_MED, 20), fill=WHITE, anchor="rm")

def columna_solucion(base, ruta_producto):
    draw = ImageDraw.Draw(base)
    draw.text((810, 215), "NUESTRA", font=font(FONT_BODY_BOLD, 54), fill=WHITE, anchor="mm")
    draw.text((810, 290), "solución", font=font(FONT_DISPLAY, 86), fill=ACCENT, anchor="mm")
    prod = Image.open(ruta_producto).convert("RGBA")
    prod.thumbnail((500, 640))
    x = 810 - prod.width // 2
    y = 360 + (640 - prod.height) // 2
    base.alpha_composite(prod, (x, y))

for i, ruta in enumerate(PRODUCTOS, start=1):
    base = make_background(seed=7).convert("RGBA")
    columna_problema(base)
    columna_solucion(base, ruta)
    draw = ImageDraw.Draw(base)
    draw.line([(540, 230), (540, 1000)], fill=GRAY, width=4)
    add_logo(base, center=(70, 1010), diameter=70)
    base.convert("RGB").save(f"slide_f{i}.png")
```

**Notas:**
- Las fotos de producto deben ser reales (mockups o fotos del negocio); nunca
  generadas. Recortar el fondo antes de pegarlas si no son PNG con
  transparencia.
- Revisá cada slide con `view` para confirmar que la burbuja y los
  encabezados quedaron en el mismo lugar en todas.
- Si los colores del tema tienen poco contraste sobre el fondo claro (ej. el
  acento sobre `Chalk White`), usar el color de texto oscuro del tema para
  "TU"/"NUESTRA" y reservar el acento para "problema"/"solución" y la burbuja.

---

## Notas técnicas comunes a todos los patrones

- **Emojis**: las fuentes bundled NO tienen glifos de emoji — se renderizan
  como cuadro vacío ("tofu"). No incluir emojis en texto dibujado con
  `draw.text`.
- **Flechas**: usar `»` o `>` en vez de `→`/`➤`.
- **Tildes y "ñ"**: funcionan bien en todas las fuentes bundled.
- **Fotos de baja resolución**: preferí mostrarlas en tarjeta más pequeña en
  vez de a sangre completa.
- Guardá cada slide como `slideN.png` y usá `present_files` para mostrarlas
  todas juntas al final.
