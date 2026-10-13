# Osiris2 · Cursos SCORM

Cursos en formato **SCORM 1.2** listos para importar en Moodle. Autor: Sixto Rodríguez de Sepúlveda.

| Curso | Carpeta | Contenido |
|---|---|---|
| Ciberseguridad para jóvenes | `cursos/Curso_Ciberseguridad_Jovenes_SCORM` | 10 módulos, examen y banco GIFT |
| Ciberseguridad para jóvenes (con módulo de seguridad avanzada) | `cursos/Curso_Ciberseguridad_Jovenes_SCORM_con_modulo_seguridad_avanzada` | 16 módulos con vídeos de INCIBE, examen y banco GIFT |
| Ciberseguridad avanzada para jóvenes | `cursos/Curso_Ciberseguridad_Avanzada_Jovenes_SCORM` | 8 unidades, evaluación y banco GIFT |
| **Curso 2: Ciberseguridad Avanzada y Defensa Digital** | `cursos/CiberSeguridad_Avanzada` | 10 módulos, examen de 20 preguntas y banco GIFT de 30 |
| Certificado digital FNMT | `cursos/Curso_Certificado_Digital_FNMT_SCORM` | 15 módulos con capturas, examen y banco GIFT |

## Uso en Moodle

1. Descarga el ZIP del curso desde `paquetes/` (o genéralo, ver abajo).
2. En Moodle, añade una actividad **SCORM** y sube el ZIP sin descomprimir.
3. Para el banco de preguntas: *Banco de preguntas › Importar › Formato GIFT* con el `preguntas_moodle.gift` del curso.

## Regenerar los paquetes

```sh
sh herramientas/empaquetar.sh
```

El Curso 2 (`CiberSeguridad_Avanzada`) se genera con los scripts de `herramientas/`:

```sh
python3 herramientas/generar_ciberseguridad_avanzada_modulos.py cursos/CiberSeguridad_Avanzada
python3 herramientas/generar_ciberseguridad_avanzada_examen.py cursos/CiberSeguridad_Avanzada
```
