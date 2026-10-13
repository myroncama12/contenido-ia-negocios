# Constructor de Embudo de Contenido (genérico)

Este archivo define **cómo armar un embudo de contenido a pedido**. Las 4 etapas
(Awareness, Consideración, Decisión, Fidelización), los 4 ejes semanales y la
Doble Caída ya están definidos en `framework-contenido.md`: acá no se redefinen,
se usan. Este archivo no contiene datos de ningún negocio; todo lo específico
sale de `config/*.md` del Project.

**Cuándo usarlo:** el usuario pide un embudo, una secuencia de contenido para
vender algo, o un plan de piezas que empuje hacia una meta concreta.

## Paso 1 — Leer la config antes de preguntar

Leé `config/buyer-persona.md`, `config/catalogo.md`, `config/objetivos.md` e
`config/identidad-marca.md`. Lo que la config ya responde se confirma en una
línea, no se vuelve a preguntar. Si falta un dato que el embudo necesita, pedí
solo ese dato puntual; nunca lo inventes.

## Paso 2 — Preguntas de entrada

Hacé solo las que falten, todas juntas en un mismo mensaje (máximo 4) y con
opciones sugeridas para que responder sea rápido. Si el usuario ya dio un dato
en su pedido, no lo repreguntes.

**1. Modo del embudo**
- **A. Producto u oferta específica:** embudo con principio y fin alrededor de
  un producto, lanzamiento, promo o preorden.
- **B. Abierto / complemento semanal:** embudo continuo que acompaña el
  contenido normal de la semana, sin una oferta puntual.

**2. Objetivo(s)** — elegir 1 o 2 (más de 2 diluye el embudo)
- Que más gente nos conozca
- Generar confianza y que nos vean como referente
- Que nos escriban (conversaciones por mensaje)
- Vender un producto o servicio
- Que los clientes vuelvan y recomienden

**3. Ventana de tiempo**
- Modo A: fecha de inicio y fecha clave (lanzamiento, cierre de preorden, fin de
  promo). Si no hay fechas, proponer 2 semanas.
- Modo B: cuántas semanas cubrir. Si no se dice, proponer 1.

**4. Capacidad de producción y canal de cierre**
- Cuántas piezas por semana se pueden producir y en qué formatos (video a
  cámara, solo foto, carrusel, etc.). Salen de `config-negocio.md` si ya está.
- Dónde cierra la venta (WhatsApp, DM, tienda física, web). Sale de la config
  si ya está.

## Paso 3 — Definir el peso de cada etapa según el objetivo

Punto de partida orientativo: porcentaje de piezas por etapa. Ajustalo con el
criterio del caso, no es una regla fija.

| Objetivo | Awareness | Consideración | Decisión | Fidelización |
|---|---|---|---|---|
| Que más gente nos conozca | 60% | 25% | 10% | 5% |
| Generar confianza | 25% | 50% | 15% | 10% |
| Que nos escriban | 25% | 40% | 30% | 5% |
| Vender | 15% | 35% | 45% | 5% |
| Que vuelvan y recomienden | 10% | 20% | 10% | 60% |

Con dos objetivos, dale más peso al primero que mencionó el usuario (ej. 60/40)
y combiná las filas.

## Paso 4 — Armar según el modo

### Modo A — Producto u oferta específica

Estructurá el embudo en tres fases alrededor de la fecha clave:

- **Antes (calentamiento):** crear contexto y deseo sin vender todavía.
  Principalmente Awareness y Consideración.
- **Durante (ventana de venta):** Decisión. Mostrar el producto, responder
  objeciones y abrir el canal de cierre.
- **Después (cierre):** prueba social, agradecimiento y qué pasó. Fidelización.

Reglas:
- El producto sale de `catalogo.md`. El ángulo sale del buyer persona (qué siente,
  qué desea), no de la lista de características.
- Cada pieza indica qué etapa trabaja y qué deseo u objeción toca.
- Debe haber al menos una pieza que responda las objeciones más comunes antes
  del CTA directo.
- El CTA escala: suave al inicio, directo solo en la fase "Durante".
- Si hay urgencia (cupo limitado, preorden con fecha), tiene que ser real. Nunca
  inventada.

### Modo B — Abierto / complemento semanal

- Partí de los 4 ejes semanales de `framework-contenido.md` y asignale a cada
  pieza una etapa según el peso del objetivo (Paso 3).
- El resultado debe ser una semana equilibrada: no todas las piezas en la misma
  etapa.
- Rotá estructuras (Doble Caída y las alternativas que apliquen) en lugar de
  repetir la misma.
- Incluí al menos una pieza "puente" por semana: que lleve al espectador a la
  siguiente etapa, para que nunca se quede sin próximo paso.
- Si hay un producto que impulsar sin ser un lanzamiento, mantené pocas piezas
  de Decisión por semana y que el resto construya confianza.

## Paso 5 — Formato de entrega

Una tabla con una fila por pieza:

| Día | Plataforma | Formato | Etapa | Idea / ángulo | Tipo de gancho | CTA | Qué mide |
|---|---|---|---|---|---|---|---|

Debajo de la tabla, tres líneas:
1. Objetivo y modo elegidos.
2. La lógica del embudo en una frase (cómo se mueve la persona de pieza en pieza).
3. La pieza más importante y por qué.

El embudo es el **mapa**: no escribas los guiones completos en este paso salvo
que el usuario lo pida. Cerrá con un próximo paso concreto (ej. "¿escribo el
guion de la pieza 1?").

## Reglas generales

1. Toda pieza tiene una etapa y un propósito. Si no lo tiene, sobra.
2. No arrastres ejemplos, nombres ni resultados de otros negocios.
3. Si existe `config/patrones-propios.md` con patrones en estado "Probado" que
   encajen con la etapa, usalos como punto de partida para ganchos y
   estructuras (ver `patrones-propios.md`).
4. No prometas resultados. Pesos y frecuencias son un punto de partida que se
   ajusta con lo que el negocio observe.
5. Si la capacidad de producción es menor a lo que pide el embudo, recortá
   piezas, no etapas: protegé la etapa clave del objetivo.
6. El embudo resultante se guarda en el Project del negocio, nunca en el repo.

## Revisión al cierre de la ventana

Sugerí revisar con los KPI de cada etapa (ver `framework-contenido.md`) en cuál
se atoró la gente: si hubo alcance pero no guardados, falla Consideración; si
hubo mensajes pero no ventas, falla Decisión. Con esa respuesta se ajusta el
siguiente embudo.
