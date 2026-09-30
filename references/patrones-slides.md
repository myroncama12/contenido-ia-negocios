# Patrones de Slides (genérico)

Cada slide de un carrusel cae normalmente en uno de estos 5 patrones. Elegí
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
