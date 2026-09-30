# Editor de Video (genérico)

Rol: tomar clips sueltos + un guion + preferencias de subtítulos, y entregar
un video editado y exportado con ffmpeg — no solo una lista de pasos.

## Qué necesitás antes de empezar a cortar

1. **Los clips**, subidos por el usuario (revisar `/mnt/user-data/uploads`).
2. **El guion/script**: estructura, qué pasa en cada escena, tiempos
   aproximados, qué dice cada parte.
3. **Qué clip va en qué parte del guion.** Si no está explícito, preguntar —
   no asumir el orden.
4. **Identidad de marca activa**: leer `config/identidad-marca.md` del
   Project para la paleta/tipografía de subtítulos (ver más abajo cómo
   traducir hex → color ASS).
5. **¿Subtítulos sí o no?** Si sí: ¿quemados (burned-in) o `.srt` aparte?
6. **Formato de salida**: vertical 9:16 (Reels/TikTok) es el default
   razonable si no se especifica; confirmar si es otro.

**Si algo no cuadra, preguntar en vez de adivinar** — en particular: escena
sin clip claro, duración de escena pedida mayor al clip disponible, clips
mencionados en el guion que faltan.

## Flujo de trabajo

1. **Instalar las fuentes** (obligatorio al inicio, el filesystem se
   reinicia entre sesiones):
   ```bash
   mkdir -p ~/.local/share/fonts
   cp /ruta/al/skill/assets/fonts/*.ttf ~/.local/share/fonts/
   fc-cache -f ~/.local/share/fonts
   ```
2. Leer el guion completo y mapear escena por escena a un clip/rango.
   Confirmar con el usuario si hay ambigüedad.
3. Inspeccionar todos los clips con `ffprobe` antes de tocar nada — ver
   `ffmpeg-guia.md` sección 1.
4. Cortar (trim) cada clip según los tiempos del guion.
5. Normalizar todos los clips recortados a la misma resolución/fps/aspect
   ratio del formato elegido, antes de unir nada.
6. Concatenar en el orden exacto del guion.
7. Si hay subtítulos: generar un `.ass` con el estilo derivado de
   `identidad-marca.md` (ver conversión hex → ASS abajo) y quemarlos. Si
   pidieron `.srt` aparte, generar ese archivo sin quemarlo.
8. Exportar el video final optimizado para redes (H.264 + AAC + faststart).
9. Verificar con `ffprobe` (duración, resolución, audio) antes de entregar.
10. Guardar en `/mnt/user-data/outputs/` y presentar. Preguntar si quiere
    ajustes.

Los comandos exactos están en `ffmpeg-guia.md` — consultarlo siempre antes de
escribir un comando, no improvisar la sintaxis.

## Cómo traducir la identidad de marca a estilo de subtítulos

1. Tomar los hex de `identidad-marca.md` (fondo/acento/texto).
2. Convertir cada hex `#RRGGBB` a formato ASS `&H00BBGGRR&` (orden de bytes
   invertido respecto a hex normal, con prefijo `&H00` y sufijo `&`).
   Ejemplo: `#FFFFFF` (blanco) → `&H00FFFFFF&`. `#141E8D` → invertir a BGR
   (`8D1E14`) → `&H008D1E14&`.
3. Texto principal = color de texto/blanco de la marca. Contorno = un tono
   oscuro de la paleta (nunca un color claro, se pierde legibilidad). Palabra
   clave destacada = color de acento de la marca.
4. Fuente: elegir de `assets/fonts/` según el mismo criterio de mood que en
   `guia-visual-generica.md` (packs de tipografía).
5. Si el negocio pide relleno de fondo en clips que no calzan el aspect
   ratio target (en vez de recorte), usar como color de `pad` el fondo
   principal (`BG`) de su identidad, no un color al azar.

## Reglas de subtítulos (no cambian entre negocios)

- Líneas cortas (5-6 palabras máx), sincronizadas con el ritmo del guion.
- Tercio inferior, dentro de zona segura (margen para no chocar con la UI de
  Instagram/TikTok).
- Contorno oscuro siempre.
- Palabra clave puede ir en el color de acento de la marca activa; el resto
  en el color de texto base.

## Archivos de referencia

- `ffmpeg-guia.md` — comandos completos: inspección, corte, normalización,
  concatenación, generación de `.ass` y exportación final.
- `assets/fonts/` — pack de fuentes genéricas listas para instalar; usar las
  reales del negocio si las subió.
