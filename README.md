# Osiris2 · Cursos SCORM

Cursos en formato **SCORM 1.2** listos para importar en Moodle. Autor: Sixto Rodríguez de Sepúlveda.

| Curso | Carpeta | Contenido |
|---|---|---|
| Curso 2: Ciberseguridad Avanzada y Defensa Digital | `cursos/CiberSeguridad_Avanzada` | 10 módulos, examen de 20 preguntas, banco GIFT de 30 |
| Certificados digitales, firma electrónica y FNMT | `cursos/Curso_Certificado_Digital_FNMT_SCORM` | 15 módulos, examen de 33 preguntas, banco GIFT de 48 |
| Ciberseguridad avanzada para jóvenes | `cursos/Curso_Ciberseguridad_Avanzada_Jovenes_SCORM` | 8 unidades, examen de 8 preguntas, banco GIFT de 8 |
| Ciberseguridad para jóvenes | `cursos/Curso_Ciberseguridad_Jovenes_SCORM` | 10 módulos, examen de 20 preguntas, banco GIFT de 30 |
| Ciberseguridad para jóvenes | `cursos/Curso_Ciberseguridad_Jovenes_SCORM_con_modulo_seguridad_avanzada` | 16 módulos, examen de 34 preguntas, banco GIFT de 51 |
| Ciberseguridad para jóvenes | `cursos/Curso_Ciberseguridad_Jovenes_SCORM_mejorado` | 15 módulos, examen de 32 preguntas, banco GIFT de 46 |
| Ciberseguridad II: redes sociales en profundidad | `cursos/Curso_Ciberseguridad_Redes_Sociales_SCORM` | 15 módulos, examen de 27 preguntas, banco GIFT de 42 |
| Escandallo de un catering con Calc | `cursos/Curso_Escandallo_Catering_SCORM` | 14 módulos (incluye estilos y formato condicional con alarma de antigüedad de precios), examen de 28 preguntas, banco GIFT de 47 |
| Hoja de cálculo básica con un horario | `cursos/Curso_Horario_Hoja_Calculo_Basico_SCORM` | 14 módulos, examen de 26 preguntas, banco GIFT de 40 |
| LibreOffice: conceptos básicos comunes | `cursos/Curso_LibreOffice_Basico_SCORM` | 13 módulos, examen de 24 preguntas, banco GIFT de 39 |
| Protección de Datos en Hostelería y Restauración | `cursos/Curso_Proteccion_Datos_Hosteleria_SCORM` | 13 módulos, examen de 26 preguntas, banco GIFT de 37 |
| Informática básica para jóvenes | `cursos/Curso_Informatica_Basica_Jovenes_SCORM` | 12 módulos con 11 ilustraciones, examen de 24 preguntas, banco GIFT de 36 |
| Matemática Básica | `cursos/Matematica_Basica_SCORM_mejorado` | 10 módulos (regla de tres y porcentajes), repaso de 5 preguntas, examen de 20, banco GIFT de 40 |
| Piano: nivel intermedio y avanzado | `cursos/Curso_Piano_Intermedio_Avanzado_SCORM` | 14 módulos con «En pocas palabras», teoría a fondo (ritmo y compases, intervalos, círculo de quintas, escalas y modos, armonización, progresiones, forma, séptimas, blues, dinámica…), pasos con «Cómo se hace», planes de práctica y errores frecuentes; **planning de 6 meses (1 hora al día)** con PDF imprimible y diario de práctica; **gimnasio de 38 ejercicios prácticos**; 61 partituras interactivas (con audio) y cuaderno PDF, glosario, metrónomo, entrenadores de notas faro, intervalos y armaduras, examen de 42 preguntas, banco GIFT de 97 |
| Saxofón alto: de cero a intermedio | `cursos/Curso_Saxofon_Alto_SCORM` | 14 módulos (el instrumento, montaje y cuidado, postura y respiración, embocadura, digitaciones, articulación, registro agudo, transposición en Mi♭, escalas, ritmo, sonido y afinación, repertorio y blues), 56 partituras con sonido de saxo y acompañamiento, dibujos de digitaciones, entrenadores (lectura, digitaciones, transposición), afinador con micrófono, gimnasio de 40 ejercicios, **planning de 6 meses** con PDF, examen de 35 preguntas, banco GIFT de 59 |
| IA para jóvenes: aprende con Claude | `cursos/Curso_IA_Jovenes_Claude_SCORM` | 12 módulos (qué es la IA, historia en 3 módulos, cómo funciona un modelo de lenguaje, conocer a Claude, prompts, IA en hostelería: atención al cliente / cocina y sala / gestión y marketing, privacidad y ética, futuro), 12 actividades de arrastrar y soltar, constructor de prompts, predictor de palabras, revisor de privacidad, proyecto final, examen de 30 preguntas, banco GIFT de 50 |
| Lengua de signos española (LSE): curso completo | `cursos/Curso_Lengua_Signos_Espanola_SCORM` | 10 módulos (personas sordas y comunidad sorda, historia y derechos, la LSE y sus cinco parámetros, dactilología con entrenador, comunicación sin barreras, primeras conversaciones, gramática, vocabulario, atención accesible en hostelería, seguir aprendiendo con plan de 12 semanas), dibujos de manos del alfabeto manual y de las configuraciones básicas, esquemas, 13 actividades de arrastrar y soltar, proyecto final, examen de 29 preguntas, banco GIFT de 41. Sin vídeos de signos |
| Introducción a Ubuntu para usuarios | `cursos/Curso_Ubuntu_Introduccion_SCORM` | 17 módulos (2 prácticos con simuladores de ventanas y de Archivos), examen de 35 preguntas, banco GIFT de 52 |

## Uso en Moodle

1. Descarga el ZIP del curso desde `paquetes/` (o genéralo, ver abajo).
2. En Moodle, añade una actividad **SCORM** y sube el ZIP sin descomprimir.
3. Para el banco de preguntas: *Banco de preguntas › Importar › Formato GIFT* con el `preguntas_moodle.gift` del curso.

## Seguimiento en Moodle

Todos los cursos tienen un SCO por página. Al abrir una página, el índice de Moodle la marca
como completada; los botones «Siguiente»/«Anterior» piden a Moodle que abra la página vecina
(`nav.event`), y el examen registra la nota y aprobado/suspenso (conservando la mejor nota).
Para saltar a un apartado no consecutivo se usa el índice de Moodle.

Si se añade o cambia una página, ejecuta `python3 herramientas/scorm_seguimiento.py`.

## Regenerar los paquetes

```sh
sh herramientas/empaquetar.sh
```

El Curso 2 (`CiberSeguridad_Avanzada`) se genera con los scripts de `herramientas/`:

```sh
python3 herramientas/generar_ciberseguridad_avanzada_modulos.py cursos/CiberSeguridad_Avanzada
python3 herramientas/generar_ciberseguridad_avanzada_examen.py cursos/CiberSeguridad_Avanzada
python3 herramientas/scorm_seguimiento.py
```

El curso de Piano se genera con `herramientas/generar_curso_piano.py` (partituras en `herramientas/piano_partituras.py`, explicaciones ampliadas en `herramientas/piano_explicaciones.py` y `herramientas/piano_teoria.py` y `herramientas/piano_teoria2.py`, ejercicios y planning en `herramientas/piano_ejercicios.py`, partituras de la ampliación en `herramientas/piano_partituras2.py`, PDF con `herramientas/piano_pdf.js`).
El curso de Saxofón alto se genera con `herramientas/generar_curso_saxo.py` (módulos en `herramientas/saxo_modulos_a.py` y `saxo_modulos_b.py`, partituras en `herramientas/saxo_partituras.py`, digitaciones y dibujos en `herramientas/saxo_digitaciones.py`, ejercicios y planning en `herramientas/saxo_ejercicios.py`, PDF con `herramientas/saxo_pdf.js`). Las partituras están en tono escrito y el audio se transpone a Mi♭ (abcjs `transpose=-9`, timbre de saxo alto).

El curso de IA se genera con `herramientas/generar_curso_ia.py` (módulos en `herramientas/ia_modulos_a.py` y `ia_modulos_b.py`, preguntas en `ia_preguntas.py`, dibujos en `ia_svgs.py`, JavaScript en `ia_js.py`) y después `insertar_dragdrop.py` y `scorm_seguimiento.py`. Los ejemplos de respuestas de IA son ilustrativos (escritos para el curso) y las condiciones de Claude.ai son para mayores de 18 años.

El curso de LSE se genera con `herramientas/generar_curso_lse.py` (módulos en `herramientas/lse_modulos_a.py` y `lse_modulos_b.py`, preguntas en `lse_preguntas.py`, esquemas en `lse_svgs.py`, dibujos de manos en `lse_manos.py` (modelo 3D sencillo de mano proyectado a SVG), JavaScript en `lse_js.py`) y después `insertar_dragdrop.py` y `scorm_seguimiento.py`. No incluye vídeos: las descripciones de letras y signos son orientativas y deben contrastarse con recursos oficiales.

Las actividades de **arrastrar y soltar** (emparejar, clasificar, ordenar, rellenar y etiquetar sobre una imagen) están definidas en `herramientas/dragdrop/<curso>.json` y las inserta `herramientas/insertar_dragdrop.py` (motor en `herramientas/dragdrop/dragdrop.js`). Orden de trabajo: generadores → `python3 herramientas/insertar_dragdrop.py` → `python3 herramientas/scorm_seguimiento.py` → `sh herramientas/empaquetar.sh`. Funcionan con ratón, con el dedo y pulsando ficha y destino.

El curso de Informática básica se genera igual:

```sh
python3 herramientas/generar_informatica_basica.py cursos/Curso_Informatica_Basica_Jovenes_SCORM
python3 herramientas/generar_informatica_basica_imagenes.py cursos/Curso_Informatica_Basica_Jovenes_SCORM
python3 herramientas/scorm_seguimiento.py
```

## Mantener actualizada la carpeta `F:\Temas` (Windows)

Estructura en `F:\Temas`:

```
F:\Temas\<curso>.zip             paquete SCORM listo para Moodle
F:\Temas\extracted\<curso>\     el mismo curso descomprimido
```

1. Clona el repositorio una vez en tu PC:
   `git clone -b claude/focused-franklin-3ugnxv https://github.com/sixtors-gif/Osiris2.git`
2. Cada vez que haya cambios, haz doble clic en `herramientas\actualizar_F_Temas.bat`.
   Descarga la última versión, copia los ZIP a `F:\Temas` y los cursos descomprimidos a
   `F:\Temas\extracted\<curso>` (añade y sobrescribe archivos, pero no borra nada).

## Otros recursos

- [`infraestructura/https_red_local/`](infraestructura/https_red_local/README.md): CA interna del hotel y certificado HTTPS para `horus.com` en la red local, con scripts para generarlos e instalarlos en los puestos (Windows, Linux, macOS, Android e iOS).
