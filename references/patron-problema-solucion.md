# Patrón Problema–Solución en espejo (genérico)

Estructura de carrusel (y también de reel corto o secuencia de historias) en
la que **una misma queja del cliente se queda fija** y lo que cambia en cada
swipe es la solución. Sirve para mostrar variedad de producto o servicio sin
sonar a venta directa. Complementa a `patron-rompe-creencia.md` (que niega una
creencia) y a `patron-pilares-de-valor.md` (que sostiene la retención): acá no
se niega nada, se responde una duda real con varias salidas.

## Estado

- **Estado:** Nuevo (listo para probar, sin datos propios todavía).
- **Origen:** observado en un carrusel de feed de 4 slides de una tienda de
  ropa de anime de otra cuenta (octubre de 2026). Métricas visibles de esa
  cuenta externa: pocas decenas de interacciones (7 reposts, 18 compartidos),
  es decir, tracción modesta. Lo que vale es la estructura, no una cifra
  probada. Cada negocio debe probarlo con sus propias piezas y subirlo a
  "Probado" en su `config/patrones-propios.md` cuando tenga data.
- **Etapa del embudo:** Consideración (mostrar variedad) y, con quejas bien
  elegidas, Awareness.
- **Formato:** carrusel de 3–6 slides (el natural), reel de 15–30 s con la
  queja fija en pantalla, o 3–4 historias encadenadas.

## Idea central

En cada slide hay dos columnas: **"Tu problema"** a la izquierda y
**"Nuestra solución"** a la derecha. La columna del problema es **idéntica en
todas las slides** (la misma burbuja de chat con la misma queja); solo cambia
la solución de la derecha. Cada deslizada responde la misma duda con una
opción distinta, así quien mira siente que el negocio tiene respuesta para su
caso sin que nadie le haya vendido nada.

## Por qué funciona

- **La queja está en voz del cliente.** Una burbuja de chat con hora se lee
  como un mensaje real de alguien del nicho, no como un anuncio.
- **El ancla fija baja el esfuerzo.** El problema se entiende una sola vez; el
  resto de la pieza es mirar soluciones.
- **Muestra catálogo sin precio ni oferta,** que es lo que pide el contenido
  orgánico.
- **Es barata de producir:** mockups o fotos de producto y una plantilla. No
  requiere filmar, lo que la hace viable con producción liviana.
- **Cada swipe es una mini recompensa:** quien mira quiere ver "cuál sigue".
  Se combina bien con `patron-pilares-de-valor.md`.

## La fórmula

1. **ELEGIR UNA QUEJA** real del buyer persona, dicha como la diría esa
   persona en un chat (corta, informal, con un toque de humor o drama).
2. **PORTADA/SLIDE 1:** columnas "Tu problema" y "Nuestra solución". La
   burbuja de la queja a la izquierda; a la derecha, la primera solución, que
   debería ser la más representativa del negocio.
3. **SLIDES 2 A N−1:** la columna izquierda **no cambia ni un píxel**; a la
   derecha, una solución distinta en cada slide (otro producto, otro estilo,
   otra variante). Ordenar de la más común a la más inesperada para que el
   swipe siga valiendo la pena.
4. **ÚLTIMA SLIDE:** puede repetir el formato con la última solución y dejar
   la invitación en el caption, o cerrar con una slide corta de frase de marca
   + CTA suave (ver Patrón E en `patrones-slides.md`).

## Cómo encontrar una queja que sirva

Una queja funciona si cumple las cuatro:
- La dice el buyer persona de `config/buyer-persona.md`, en su propia voz
  (usar sus hipótesis de dolor/deseo, no inventar una).
- **Es del ambiente, no del lector:** nunca señala ni culpa a quien la lee.
  Habla de algo que le pasa a todos en el nicho.
- Tiene **más de una respuesta posible** en el catálogo (si solo hay una
  solución, no hay carrusel; eso es otra pieza).
- Cabe en una línea corta dentro de la burbuja.

Moldes de queja (adaptar al rubro, uno por pieza):
- "No tengo qué ponerme" / "No sé qué regalar" / "Se me olvidó el cumple".
- "Mi [cosa] se ve aburrida/igual a las de todos".
- "No tengo tiempo para [tarea]".
- "No encuentro nada que sea realmente mío".

Ejemplos genéricos de aplicación (adaptar con datos reales):
- Pastelería: "Se me olvidó el cumple" → 4 opciones listas en 24 h.
- Accesorios de juego: "Mi mazo se ve igual al de todos" → 4 estilos.
- Servicios: "No tengo tiempo de cocinar" → 4 menús de la semana.

## Reglas duras

- **Una sola queja por pieza.** Las soluciones cambian; la queja no.
- **La queja nunca apunta al lector.** Nada de "estás haciendo mal", "nadie te
  obliga" ni "alguien como vos". Habla de una situación compartida por toda la
  comunidad, para que nadie se sienta excluido.
- **Lo que se muestra debe ser real:** productos, mockups o trabajos que el
  negocio de verdad puede hacer. No inventar productos, resultados ni
  testimonios, ni generar fotos de producto.
- **Sin precio, oferta ni disponibilidad** en contenido orgánico (ver
  `config/restricciones.md`). Si la pieza es de venta explícita, este patrón
  no es el indicado.
- **Si los productos referencian marcas, personajes o franquicias de
  terceros,** el copy no debe sugerir afiliación ni licencia oficial.
- **Sin emojis dibujados dentro de la imagen** (las fuentes bundled no los
  renderizan; ver notas técnicas en `patrones-slides.md`). Si la queja lleva
  emoji, va en el caption, no en la burbuja.
- **Caption corto,** que no repita el copy de las slides: una línea que
  conecte ("Tu problema tiene solución") más una invitación suave a escribir.
  Hashtags en minúscula, máximo 5 (o la convención del negocio).
- **Diseño:** se hace con el Patrón F de `patrones-slides.md`, con el tema
  del negocio activo. Se copia la mecánica, no el estilo visual de la cuenta
  de origen.
- **Producción y marca:** respetar `config/restricciones.md` y
  `config/identidad-marca.md`; siempre mandan sobre este patrón.

## Adaptación por formato

**Carrusel (formato natural)**
- 3–6 slides. Cuatro es un buen punto de partida.
- Misma burbuja, misma posición, mismo texto en todas las slides.
- Orden: de la solución más representativa a la más inesperada.

**Reel / TikTok (15–30 s)**
- Queja fija en pantalla de principio a fin (burbuja en un lado).
- Cada 3–5 s cambia la solución del otro lado; corte seco o deslizamiento.
- Cierre con frase corta + invitación suave.

**Historias**
- Frame 1: la queja con la primera solución. Frames siguientes: misma queja,
  otra solución. El último deja espacio para sticker nativo (caja de
  preguntas: "¿qué querés que resolvamos?").

## Ejemplo de esqueleto (genérico)

```
QUEJA (fija):  "[queja corta del buyer persona]"
SLIDE 1:       [Tu problema] burbuja | [Nuestra solución] opción más representativa
SLIDE 2:       misma burbuja        | opción distinta
SLIDE 3:       misma burbuja        | opción distinta
SLIDE 4:       misma burbuja        | opción inesperada
CAPTION:       1 línea que conecta + invitación a escribir + hasta 5 hashtags
```

## Cómo se combina con el resto

- **Con `patron-pilares-de-valor.md`:** cada slide puede terminar con una mini
  intriga ("y la última es la que más nos piden") para empujar el swipe.
- **Con `patron-rompe-creencia.md`:** son estructuras distintas; no apilarlas
  en la misma pieza. Rompe-creencia = negar una idea del nicho. Problema–
  solución = responder una queja con varias opciones.
- **Con el embudo:** sirve como pieza de Consideración dentro de
  `framework-contenido.md` (mostrar variedad sin cerrar venta).
- No usarlo en banners con precio, preórdenes ni respuestas a DM o
  comentarios.
- Si el negocio tiene un patrón "Probado" en `config/patrones-propios.md`
  para el mismo objetivo, ese manda para el gancho; este se usa como
  alternativa a probar, aclarando que todavía no tiene data propia.

## Chequeo final antes de entregar

1. ¿La queja es del buyer persona y de la comunidad, sin señalar al lector?
2. ¿Es la misma queja, idéntica, en todas las slides?
3. ¿Cada solución es real y producible/entregable por el negocio?
4. ¿Hay más de una solución distinta y ordenadas de la más común a la más
   inesperada?
5. ¿No hay precio, oferta ni disponibilidad, ni emojis dentro de la imagen?
6. ¿Se evitó sugerir afiliación con marcas de terceros?
7. ¿Caption corto, hashtags según la convención del negocio?
