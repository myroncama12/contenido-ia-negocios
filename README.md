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
- `references/ganchos-generico.md` — tipos de gancho, CTAs, tono. Módulo
  Estrategia y Copy.
- `references/patron-pilares-de-valor.md` — estructura de retención
  (preguntas abiertas y mini recompensas) para después del gancho; se
  combina con el patrón rompe-creencia. Módulo Estrategia y Copy.
- `references/guia-visual-generica.md` — setup de tema (`theme.py`) por
  negocio. Módulo Diseño Visual.
- `references/patrones-slides.md` — 5 patrones de slide/carrusel. Módulo
  Diseño Visual.
- `references/auditoria-contenido.md` — protocolo de 5 bloques de auditoría
  pre-publicación. Módulo Auditoría.
- `references/edicion-video.md` — flujo de edición de video. Módulo Edición
  de Video.
- `references/ffmpeg-guia.md` — comandos ffmpeg de referencia. Módulo
  Edición de Video.

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
