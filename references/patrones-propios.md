# Patrones Propios — biblioteca de patrones validados con data real (genérico)

Este archivo explica el **mecanismo**, no trae patrones ya hechos. Cada
negocio construye su propia biblioteca a partir de lo que realmente le
funcionó — un patrón copiado de otro negocio, sin datos propios que lo
respalden, no tiene el mismo peso.

## Por qué existe esto aparte de `ganchos-generico.md` y `patron-rompe-creencia.md`

Los ganchos y estructuras de esos archivos son puntos de partida razonables
para cualquier negocio. Pero con el tiempo, cada negocio va a descubrir
formatos específicos que le funcionan mejor que el default genérico —
basados en reproducciones, alcance a no-seguidores, guardados, o cualquier
métrica real de sus propias cuentas. Esos hallazgos valen más que la teoría
genérica para ese negocio en particular, y merecen quedar documentados en
un lugar fijo del Project: `config/patrones-propios.md`.

## Cuándo un patrón propio manda sobre la estructura genérica

Si `config/patrones-propios.md` del negocio tiene un patrón con **estado
"Probado"** (ver plantilla abajo) que encaja con el objetivo de la pieza que
se está armando (misma etapa de embudo, mismo tipo de contenido), ese
patrón es el punto de partida — no la estructura genérica de
`framework-contenido.md` o `patron-rompe-creencia.md`. Los patrones en
estado "Candidato" se pueden proponer como alternativa a probar, dejando
claro que todavía no tienen data propia detrás.

Esto no reemplaza las reglas de marca (`identidad-marca.md`,
`restricciones.md`) — esas mandan siempre, sobre cualquier patrón.

## Cómo detectar un patrón propio nuevo (durante el trabajo normal)

Si en la conversación el negocio menciona que una pieza concreta tuvo un
resultado fuera de lo común (una cifra de reproducciones/alcance que él
mismo señala como alta, un formato que "funcionó varias veces"), vale la
pena proponerle documentarlo como patrón propio en vez de dejarlo perdido
en el chat. No hace falta esperar a que lo pida.

## Plantilla para cada patrón (usar esta estructura en `config/patrones-propios.md`)

```
### <Nombre del patrón>

- **Estado:** Probado (con datos propios) / Nuevo (listo para probar, sin
  datos aún) / Candidato (mencionado como funcional, sin métricas
  registradas)
- **Etapa del embudo:** Awareness / Consideración / Decisión / Fidelización
- **Duración / formato:** (ej. 5-8s reel, carrusel de 6 slides, historia
  única)
- **Cuándo usarlo:** una frase — qué objetivo cumple
- **Estructura:** los beats/pasos concretos con segundos o slides
- **Datos que lo respaldan:** (si es Probado) la cifra y de dónde sale —
  ej. "2641 reproducciones, 87.5% no-seguidores, [fecha]"
- **Ejemplo real:** una pieza concreta ya hecha con este patrón, si existe
```

## Restricciones que cualquier patrón propio debe respetar

Todo patrón documentado acá debe seguir cumpliendo:
- Las restricciones de producción reales del negocio
  (`config/restricciones.md` — actores disponibles, locaciones,
  información operativa que no se revela).
- Nada de precio/oferta/disponibilidad en contenido orgánico, salvo que sea
  explícitamente una pieza de venta.
- El tono de marca definido en `config/identidad-marca.md`.

## Si el negocio todavía no tiene `patrones-propios.md`

Es normal, sobre todo al empezar — no es un documento obligatorio como los
6 de `config-negocio.md`. Seguir con la estructura genérica
(`framework-contenido.md`, `ganchos-generico.md`, `patron-rompe-creencia.md`,
`historias-generico.md`) hasta que el negocio acumule resultados reales que
valga la pena documentar.
