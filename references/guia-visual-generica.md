# Guía Visual Genérica — Carruseles

Este skill no tiene una identidad visual fija — la construye a partir de
`config/identidad-marca.md` del Project, y la traslada a `scripts/theme.py`
**una vez por negocio**, no en cada carrusel.

## Paso 1 — Setup del tema (primera vez que se trabaja con un negocio nuevo)

1. Copiá `scripts/` y `assets/` de este skill a tu carpeta de trabajo.
2. Leé `identidad-marca.md` del Project y sacá:
   - Colores hex → convertí a RGB y reemplazá `BG`, `BG2`, `ACCENT`, `ACCENT2`
     en tu copia de `theme.py`.
   - Nombre del negocio → `BRAND_NAME`.
   - Mood de marca → elegí un pack de tipografías de `assets/fonts/` (ver
     tabla abajo) y actualizá las rutas `FONT_*`.
3. Si el negocio ya subió su logo (PNG, fondo transparente): guardalo como
   `assets/logo_activo.png` en tu copia de trabajo. Si no lo subió, avisá que
   las slides van a salir sin logo hasta que lo compartan, y seguí sin
   bloquear el resto del trabajo.
4. Si el negocio subió tipografías reales (`.ttf`/`.otf` con licencia de uso
   fuera de diseño): guardalas en `assets/fonts/` y apuntá `FONT_*` a esos
   archivos en vez de las genéricas.
5. Confirmá el tema generando un fondo de prueba (`bg.py` standalone) y
   mirándolo con `view` antes de armar slides reales.

**No repitas este paso en cada carrusel** — una vez que `theme.py` está
configurado para ese negocio, todos los patrones lo usan automáticamente. Si
cambiás de negocio en la misma sesión (poco común, pero puede pasar), volvé
a hacer el setup para el nuevo antes de generar.

## Paso 2 — Packs de tipografía disponibles (mood → fuentes)

| Mood de marca | Display (titulares) | Body (subtítulos/CTA) |
|---|---|---|
| Gamer / competitivo / alto impacto | `Anton-Regular.ttf` o `BebasNeue-Regular.ttf` | `Poppins-Bold/Medium/Regular.ttf` |
| Tech / futurista / gaming digital | `BebasNeue-Regular.ttf` | `Rajdhani-Bold/SemiBold/Regular.ttf` |
| Adulto refinado / lifestyle | `PlayfairDisplay.ttf` (títulos) | `Inter.ttf` o `DMSans.ttf` |
| Cercano / cálido / cotidiano | `Montserrat.ttf` (bold como display) | `Montserrat.ttf` / `Montserrat-Italic.ttf` |
| Retro / pixel / arcade | `PressStart2P-Regular.ttf` (solo para acentos cortos, es muy angosta para párrafos) | `Poppins-Regular.ttf` |

Esto es un punto de partida razonable, no una regla fija — si el negocio ya
tiene una identidad tipográfica definida en Canva u otro lado, replicá el
"rol" (cuál es display, cuál es body) con el sustituto más parecido de la
lista, igual que se hizo para marcas anteriores con Lastica/Horizon → Anton/
Poppins.

## Paso 3 — Estilo de fondo

`theme.BACKGROUND_STYLE`:
- `"bokeh_oscuro"` (default): funciona bien para estética gamer/geek/nocturna.
- `"plano"`: fondo sólido sin bokeh, mejor para marcas minimalistas o cuando
  el negocio pide algo más limpio/editorial.

Si ninguno de los dos calza con la marca (ej. fondo claro/pastel), avisá que
`bg.py` necesitaría un tercer modo y proponé el ajuste antes de forzar un
estilo que no corresponde.

## Reglas que no cambian entre negocios

- Formato: 1080x1080, salida PNG.
- Nunca generar/alucinar fotos de producto — siempre pedirlas reales al
  negocio, igual que con cualquier producto con derechos de autor de
  terceros (ver `config/restricciones.md`).
- Nunca usar emojis en el texto dibujado con Pillow (no se renderizan con
  estas fuentes) — usar `»` en vez de `→`.
- Revisar cada imagen generada con `view` antes de darla por buena.
