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
| Escandallo de un catering con Calc | `cursos/Curso_Escandallo_Catering_SCORM` | 13 módulos, examen de 26 preguntas, banco GIFT de 44 |
| Hoja de cálculo básica con un horario | `cursos/Curso_Horario_Hoja_Calculo_Basico_SCORM` | 14 módulos, examen de 26 preguntas, banco GIFT de 40 |
| LibreOffice: conceptos básicos comunes | `cursos/Curso_LibreOffice_Basico_SCORM` | 13 módulos, examen de 24 preguntas, banco GIFT de 39 |
| Protección de Datos en Hostelería y Restauración | `cursos/Curso_Proteccion_Datos_Hosteleria_SCORM` | 13 módulos, examen de 26 preguntas, banco GIFT de 37 |
| Introducción a Ubuntu para usuarios | `cursos/Curso_Ubuntu_Introduccion_SCORM` | 15 módulos, examen de 31 preguntas, banco GIFT de 46 |

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
