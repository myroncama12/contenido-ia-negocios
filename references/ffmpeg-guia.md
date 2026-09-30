# Guía técnica ffmpeg (genérico)

ffmpeg ya está instalado en el entorno (`/usr/bin/ffmpeg`, con soporte
`libass` para subtítulos). No hace falta instalar nada salvo las fuentes.

## 0. Setup de fuentes (siempre al inicio de una sesión de edición)

```bash
mkdir -p ~/.local/share/fonts
cp /ruta/al/skill/assets/fonts/*.ttf ~/.local/share/fonts/
fc-cache -f ~/.local/share/fonts
```

## 1. Inspeccionar cada clip antes de procesar

```bash
ffprobe -v error -select_streams v:0 \
  -show_entries stream=width,height,r_frame_rate,duration,codec_name \
  -of default=noprint_wrappers=1 clip.mp4
```

Revisar TODOS los clips subidos antes de armar el plan de edición. Si un
clip está en horizontal y el guion pide vertical (o viceversa), avisar antes
de decidir cómo recortarlo/rellenarlo.

## 2. Cortar (trim) un clip según el guion

```bash
ffmpeg -i input.mp4 -ss 00:00:03.500 -to 00:00:08.200 \
  -c:v libx264 -preset fast -crf 18 -c:a aac -b:a 192k \
  clip_recortado.mp4
```

## 3. Normalizar resolución/aspect ratio/fps antes de concatenar

| Formato | Resolución | Filtro de escalado |
|---|---|---|
| Vertical 9:16 (Reels/TikTok) — default | 1080x1920 | `scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920` |
| Horizontal 16:9 (YouTube) | 1920x1080 | `scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080` |
| Cuadrado 1:1 | 1080x1080 | `scale=1080:1080:force_original_aspect_ratio=increase,crop=1080:1080` |

```bash
ffmpeg -i clip_recortado.mp4 \
  -vf "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,fps=30,setsar=1" \
  -c:v libx264 -preset fast -crf 18 -pix_fmt yuv420p \
  -ar 48000 -ac 2 -c:a aac -b:a 192k \
  clip_normalizado.mp4
```

Si un clip original es mucho más angosto que el target y `crop` recorta
contenido importante, usar `pad` con el color de fondo de la marca activa (ver
`edicion-video.md`) en vez de `crop`, y avisar que se usó relleno en vez de
recorte.

## 4. Concatenar los clips normalizados en el orden del guion

```bash
cat > lista.txt << 'EOF'
file 'clip1_normalizado.mp4'
file 'clip2_normalizado.mp4'
file 'clip3_normalizado.mp4'
EOF

ffmpeg -f concat -safe 0 -i lista.txt -c copy video_unido.mp4
```

## 5. Subtítulos — generar archivo .ass con el estilo de marca activo

```
[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, OutlineColour, Bold, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV
Style: Default,<FontFamily>,64,<PrimaryColourASS>,<OutlineColourASS>,1,1,4,0,2,80,80,300

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Text
Dialogue: 0,0:00:00.00,0:00:02.50,Default,,0,0,0,PRIMERA LÍNEA DE TEXTO
Dialogue: 0,0:00:02.50,0:00:05.00,Default,,0,0,0,SEGUNDA LÍNEA DE TEXTO
```

Notas clave:
- `<FontFamily>` debe ser el nombre EXACTO que reporta `fc-list` (ej.
  `Montserrat`, `Rajdhani`, `Bebas Neue`) — no el nombre del archivo.
- `<PrimaryColourASS>` / `<OutlineColourASS>`: ver conversión hex→ASS en
  `edicion-video.md`.
- `Alignment: 2` = centrado abajo. `MarginV: 300` empuja el texto hacia
  arriba para no chocar con la UI de Instagram/TikTok.
- Líneas cortas (5-6 palabras máx) sincronizadas con el guion.
- Palabra clave destacada en otro color: `{\c&H<ColorASS>&}PALABRA{\r}`
  dentro del texto del `Dialogue`.

## 6. Quemar los subtítulos en el video

```bash
ffmpeg -i video_unido.mp4 -vf "ass=subtitulos.ass" \
  -c:v libx264 -preset medium -crf 18 -pix_fmt yuv420p \
  -c:a copy \
  video_con_subtitulos.mp4
```

Si pidieron `.srt` aparte en vez de quemado, generar un `.srt` simple (sin
estilo) como archivo adicional, sin tocar el video.

## 7. Exportación final optimizada para redes sociales

```bash
ffmpeg -i video_con_subtitulos.mp4 \
  -c:v libx264 -preset medium -crf 20 -pix_fmt yuv420p \
  -c:a aac -b:a 192k -ar 48000 \
  -movflags +faststart \
  /mnt/user-data/outputs/video_final.mp4
```

## 8. Verificación final

Antes de presentar el archivo, correr `ffprobe` sobre el resultado final y
confirmar: resolución correcta, duración esperada, que tenga audio, tamaño de
archivo razonable. Si algo no cuadra, revisar antes de entregar.
