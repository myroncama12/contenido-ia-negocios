# Contenido IA — Negocios

Este repositorio es la **fuente única de verdad de la metodología** que usa
el skill "Socio Creativo" en todas las cuentas de Claude de los negocios
cliente (Dice & Cards, Pura Vida Gameshop, Geek Vinyl Lab, y los que se
sumen).

## Cómo funciona

Cada negocio tiene, en su propia cuenta de Claude, una copia local del
"shell" del skill: `SKILL.md` + `scripts/` (motor de diseño) + `assets/fonts/`.
Ese shell **no contiene la metodología** — al arrancar cada módulo, le indica
a Claude que descargue la versión actual del archivo de referencia
correspondiente directamente desde este repo (vía `raw.githubusercontent.com`).

```
Cuenta del negocio (Claude.ai)          Este repo (GitHub)
┌────────────────────────────┐          ┌───────────────────────────┐
│ SKILL.md (shell, local)     │  fetch   │ references/*.md           │
│ scripts/ (motor diseño)     │ ───────► │ (framework, ganchos,      │
│ assets/fonts/               │          │  patrones, auditoría,     │
└────────────────────────────┘          │  edición de video, etc.)  │
                                          └───────────────────────────┘
```

**Para actualizar la metodología para TODOS los negocios a la vez**: edita el
archivo correspondiente en `references/`, hacé commit y push a `main`. La
próxima vez que cualquier negocio use ese módulo, Claude va a traer la
versión nueva automáticamente — no hace falta volver a subir nada a ninguna
cuenta cliente.

**Lo único que sí requiere re-subir el `.zip` a cada cuenta cliente** es un
cambio al *motor de diseño* (`scripts/theme.py`, `bg.py`, `helpers.py`,
fuentes) o al propio `SKILL.md`, porque esos viven localmente en cada cuenta
(cambian poco y cada negocio tiene su propio `theme.py` con sus colores).

## Estructura

- `references/config-negocio.md` — qué documentos de configuración necesita
  cada Project cliente (buyer persona, catálogo, objetivos, identidad).
- `references/framework-contenido.md` — embudo, estructura "Doble Caída",
  ejes de contenido semanal. Módulo Estrategia y Copy.
- `references/embudo-contenido.md` — constructor de embudo a pedido: preguntas
  de entrada, modos (producto específico / abierto), pesos por etapa según el
  objetivo y formato de entrega. Se alcanza desde `framework-contenido.md`.
  Módulo Estrategia y Copy.
- `references/ganchos-generico.md` — tipos de gancho, CTAs, tono. Módulo
  Estrategia y Copy.
- `references/patron-pilares-de-valor.md` — estructura de retención
  (preguntas abiertas y mini recompensas) para después del gancho; se
  combina con el patrón rompe-creencia. Módulo Estrategia y Copy.
- `references/patron-problema-solucion.md` — estructura de carrusel (o reel/
  historias) con una queja del cliente fija y una solución distinta en cada
  swipe, para mostrar variedad sin sonar a venta. Estado Nuevo. Módulo
  Estrategia y Copy.
- `references/guia-visual-generica.md` — setup de tema (`theme.py`) por
  negocio. Módulo Diseño Visual.
- `references/patrones-slides.md` — 6 patrones de slide/carrusel (el F es el
  split "Tu problema / Nuestra solución"). Módulo Diseño Visual.
- `references/auditoria-contenido.md` — protocolo de 5 bloques de auditoría
  pre-publicación. Módulo Auditoría.
- `references/edicion-video.md` — flujo de edición de video. Módulo Edición
  de Video.
- `references/ffmpeg-guia.md` — comandos ffmpeg de referencia. Módulo
  Edición de Video.

## Guía de usuario (documentación viva)

Hay una guía para usuarios finales —gente que solo usa el skill, sin tocar
este repo— con ejemplos de pedidos, explicación de cada módulo y preguntas
frecuentes. Existe en dos formas con el mismo contenido:

- **Documento vivo en Claude** (se comparte con un link y se exporta a PDF
  desde la propia interfaz): https://claude.ai/code/artifact/b0b80914-ede2-4582-bac1-3dc24c5c22cb
- **PDF** en este repo: `docs/guia-usuario/Guia-Socio-Creativo.pdf`.

La fuente única es `docs/guia-usuario/guia-usuario.md`. **Cada vez que se
agregue o cambie un patrón, módulo o función que el usuario final note**:

1. Editá `guia-usuario.md`: actualizá la sección que corresponda, sumá una
   fila arriba en "Qué hay de nuevo" con la fecha y cambiá la línea
   "Última actualización".
2. Corré `python3 docs/guia-usuario/build_pdf.py` (necesita `markdown`,
   `wkhtmltopdf`, `pypdf` y `reportlab`) para regenerar el PDF.
3. Reflejá el mismo cambio en el documento vivo de Claude.
4. Hacé commit de los tres.

Ojo: este repo es público, así que todo lo que esté en `docs/` también lo es.
La guía usa un solo ejemplo real (el carrusel de la tienda de ropa geek);
cualquier otro ejemplo debe ser genérico o contar con permiso del negocio.

## Negocios activos usando este sistema

| Negocio | Cuenta administrada por | Estado |
|---|---|---|
| Pura Vida Gameshop | Myron (dueño) | Interno |
| Geek Vinyl Lab | Myron (dueño) | Interno |
| Dice & Cards Hobby Shop | Myron (admin de la cuenta cliente) | Beta (prueba gratis 1 mes) |

## Convención al editar

- Los archivos de `references/` deben seguir siendo **genéricos** — nunca
  metas el nombre, colores o datos de un negocio específico acá. Eso vive en
  el Project de cada cliente, no en este repo.
- Si un cambio es específico de un solo negocio, no va en este repo — va en
  la configuración de su Project.
- Un cambio acá impacta a todos los negocios en su próximo uso, así que
  probalo primero con tu propio negocio (PVG/GVL) antes de confiar en que
  sirve para todos.
