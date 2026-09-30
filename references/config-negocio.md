# Configuración del negocio — qué buscar en el Project

Este skill es genérico: no tiene ninguna marca hardcodeada. Toda la
información específica del negocio vive en el **Project** donde se activa
(en la sección de conocimiento/knowledge del Project en Claude.ai), no en el
skill. Al empezar cualquier tarea, revisá si el Project tiene estos
documentos (los nombres exactos pueden variar, buscá por contenido si el
nombre no calza exacto):

| Documento esperado | Contenido | De dónde sale |
|---|---|---|
| `buyer-persona.md` | Perfil(es) de cliente: edad, motivaciones, dolores, dónde están en redes | Sección 2 del Formulario de Onboarding |
| `catalogo.md` | Categorías de producto, rango de precios, productos estrella, disponibilidad/reposición | Sección 3 |
| `objetivos.md` | Qué busca lograr el negocio con el contenido, métricas que le importan | Sección 4 |
| `identidad-marca.md` | Paleta de colores (hex), tipografías, tono de voz, filosofía/diferenciador, competencia | Secciones 1 y 5 |
| `estado-redes.md` | Qué ha funcionado o no antes en sus redes | Sección 6 |
| `restricciones.md` | Qué no mostrar/decir, lineamientos de marcas de terceros que revenden | Sección 8 |

**Nota sobre `restricciones.md`:** además de lo que pida el negocio
explícitamente, preguntá siempre si hay información operativa que prefieran
no revelar en contenido público — de dónde sacan proveedores, cómo logran
una ventaja de producto/precio, procesos internos — porque eso le da pistas
fáciles a la competencia. Cuando el negocio anuncie una mejora de producto
sin querer explicar el "cómo", enmarcalo como "ya lo tenemos" sin detallar el
proceso detrás.

Si falta alguno de estos documentos y la tarea lo necesita, **decilo
explícitamente y pedí el dato puntual** en vez de inventar un buyer persona o
una paleta de colores — a diferencia de los skills de marca única (como los
que existían antes de generalizar este), este skill no tiene un fallback de
marca real al que recurrir.

## Cómo se usa esta configuración en cada módulo

- **Estrategia y copy** (`framework-contenido.md`, `ganchos-generico.md`):
  lee buyer-persona, catalogo, objetivos e identidad-marca.
- **Diseño de carrusel** (`patrones-slides.md`, `guia-visual-generica.md`):
  lee identidad-marca para paleta/tipografía/logo — ver esa guía para cómo
  trasladar esos datos a `scripts/theme.py`.
- **Auditoría** (`auditoria-contenido.md`): lee buyer-persona e
  identidad-marca para validar tono y segmentación.
- **Edición de video** (`edicion-video.md`): lee identidad-marca para la
  paleta de subtítulos.

## Un Project por negocio

Cada negocio tiene su propio Project en la cuenta de Claude donde se instaló
este skill, con su propia carpeta de configuración. El skill nunca cambia
entre negocios — lo que cambia es el Project activo. Si en algún momento no
está claro para qué negocio se está trabajando (por ejemplo, si el mismo
skill está instalado también fuera de cualquier Project), preguntá antes de
asumir cuál configuración usar.
