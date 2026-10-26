#!/usr/bin/env python3
"""Genera el curso SCORM «Lengua de signos española (LSE): curso completo».

Uso (desde la raíz del repositorio):
  python3 herramientas/generar_curso_lse.py cursos/Curso_Lengua_Signos_Espanola_SCORM
  python3 herramientas/insertar_dragdrop.py Curso_Lengua_Signos_Espanola_SCORM
  python3 herramientas/scorm_seguimiento.py
Contenido: lse_modulos_a.py (1-5), lse_modulos_b.py (6-10), lse_preguntas.py, lse_svgs.py, lse_js.py.
"""
import html, json, os, re, shutil, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lse_svgs as sv  # noqa: E402
from lse_js import LSE_JS as IA_JS  # noqa: E402
from lse_modulos_a import MODULOS as MOD_A  # noqa: E402
from lse_modulos_b import MODULOS as MOD_B  # noqa: E402
from lse_preguntas import Q  # noqa: E402
from ia_helpers import actividad, caja, cuidado, hosteleria, kp, pasos  # noqa: E402

OUT = sys.argv[1]
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
os.makedirs(os.path.join(OUT, "img"), exist_ok=True)
TITULO = "Lengua de signos española (LSE): curso completo"
FOOTER = f"{TITULO} · Material educativo · Creado por: Sixto Rodríguez de Sepúlveda"
M = MOD_A + MOD_B
N = len(M)
assert N == 10, N
shutil.copy(os.path.join(RAIZ, "cursos", "CiberSeguridad_Avanzada", "img", "logo-centro.png"), os.path.join(OUT, "img", "logo-centro.png"))

TEMA = [("#1e3c72", "#0f766e"), ("#2a5298", "#14948a"), ("#4ecdc4", "#f97316"), ("#44a08d", "#ea580c"),
        ("linear-gradient(135deg,#11432b 0%,#1b5e20 100%)", "linear-gradient(135deg,#073b36 0%,#0f766e 100%)"),
        ("#f2f6ff", "#e6f4f2"), ("#f8faff", "#f3faf9"), ("#f4f7fb", "#eef7f6"), ("#6c8ccf", "#2aa198"), ("#3b5ba8", "#0f766e"), ("#dfe5ef", "#d3e8e5")]
base = open(os.path.join(RAIZ, "cursos", "CiberSeguridad_Avanzada", "style.css"), encoding="utf-8").read()
extra = """
/* Curso de lengua de signos española */
.shield-icon{background:linear-gradient(45deg,#f97316,#fdba74)}
.module h2{border-bottom-color:#f97316}
.module h4{color:#0f766e;margin:18px 0 6px;font-size:1.05em}
.tabla-wrap{overflow-x:auto;margin:16px 0}
.tabla{border-collapse:collapse;width:100%;font-size:1em}
.tabla th{background:#0f766e;color:#fff;padding:8px 10px;text-align:left}
.tabla td{border:1px solid #d3e8e5;padding:8px 10px;vertical-align:top}
.tabla tr:nth-child(even) td{background:#eef7f6}
.figure img{max-width:100%;height:auto}
.palabras{background:#fff7ed;border:2px solid #f97316;border-radius:14px;padding:14px 18px 10px;margin:4px 0 20px}
.palabras p{font-size:1.12em;line-height:1.6;margin:6px 0}
.pal-tag{display:inline-block;background:#f97316;color:#fff;font-weight:700;font-size:.8em;letter-spacing:.04em;text-transform:uppercase;border-radius:20px;padding:3px 12px}
.practica{background:#eef7ee;border-left:5px solid #4caf50;border-radius:10px;padding:12px 18px;margin:18px 0}
.como{background:#e6f4f2;border-left:4px solid #2aa198;border-radius:8px;margin:6px 0 10px;font-size:.95em;line-height:1.6}.como>summary{cursor:pointer;padding:7px 12px;font-weight:700;color:#0f766e;list-style:none;border-radius:8px}.como>summary::-webkit-details-marker{display:none}.como>summary::before{content:'▸ ';display:inline-block;width:1em}.como[open]>summary::before{content:'▾ '}.como-cuerpo{padding:2px 14px 10px 14px}
.como-ctrl{display:flex;gap:8px;flex-wrap:wrap;margin:0 0 14px}.como-ctrl button{background:#fff;border:1px solid #b7dcd7;border-radius:18px;padding:5px 12px;cursor:pointer;font-size:.9em;color:#0f766e;font-weight:600}
.glosario dt{font-weight:700;color:#0f766e;margin-top:10px}.glosario dd{margin:2px 0 0 18px;line-height:1.55}
details.glos{border:1px solid #d3e8e5;border-radius:12px;padding:10px 16px;margin:16px 0;background:#f3faf9}
details.glos summary{cursor:pointer;font-weight:700;color:#0f766e;font-size:1.05em}
.module ol{margin:10px 0 14px 28px}.module ol li{line-height:1.7;font-size:1.05em;padding:2px 0}
.prompt{background:#1f1b3a;color:#f4f1ff;border-radius:12px;padding:10px 14px 12px;margin:14px 0;position:relative}
.prompt-t{font-weight:700;color:#fdba74;margin-bottom:6px;font-size:.95em}
.prompt pre{white-space:pre-wrap;word-wrap:break-word;margin:0 0 8px;font-family:inherit;line-height:1.55;color:#f4f1ff}
.prompt button{background:#f97316;color:#1f1b3a;border:0;border-radius:18px;padding:5px 14px;font-weight:700;cursor:pointer}
.respuesta{background:#f3f9f4;border:1px solid #bfdcc4;border-left:5px solid #2e7d32;border-radius:12px;padding:8px 16px;margin:14px 0}
.resp-t{font-weight:700;color:#2e7d32;margin-bottom:4px}
.hosteleria{background:#fff4e0;border:1px solid #f3c77a;border-left:5px solid #f97316;border-radius:12px;padding:10px 16px;margin:16px 0;line-height:1.6}
.pb label,.pv label{display:block;margin:8px 0 2px;font-weight:600;color:#0f766e}
.pb input[type=text],.pb textarea,.pv textarea{width:100%;box-sizing:border-box;padding:8px;border:1px solid #b7dcd7;border-radius:8px;font:inherit}
.pb textarea{min-height:60px}
.pred-gen{font-size:1.1em;background:#fff;border:1px dashed #2aa198;border-radius:8px;padding:8px 12px;min-height:1.5em}
.pv-ok{color:#2e7d32;font-weight:600}.pv-ko{color:#c62828;font-weight:600}
.pv-limpio{white-space:pre-wrap;background:#eef7f6;border-radius:8px;padding:8px 12px}
.bar-pred{display:flex;align-items:center;gap:8px;margin:3px 0}.bar-pred span.b{display:inline-block;height:14px;background:#2aa198;border-radius:7px}
.letra-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:10px;margin-top:12px}
.letra-card{background:#fff;border:1px solid #b7dcd7;border-radius:12px;padding:8px 10px;font-size:.88em;line-height:1.4}
.letra-card b{display:block;font-size:2em;color:#0f766e;line-height:1.1}
.letra-grande{background:#0f766e;color:#fff;border-radius:14px;padding:12px 18px;margin:10px 0;min-height:70px;display:flex;align-items:center;gap:16px}
.letra-grande b{font-size:3.4em;line-height:1}.letra-grande span{font-size:1.05em}
.jl-desc{font-size:1.15em;background:#fff;border-left:5px solid #f97316;padding:10px 14px;border-radius:8px}
.lect-btns button.ok{background:#4caf50;color:#fff;border-color:#4caf50}.lect-btns button.ko{background:#f44336;color:#fff;border-color:#f44336}
.dl input[type=text]{width:100%;max-width:340px;padding:8px;font-size:1.1em;border:1px solid #b7dcd7;border-radius:8px;text-transform:uppercase}
.dl-box{background:#fff7ed;border:2px solid #f97316;border-radius:12px;padding:14px 18px;margin:18px 0}
.lect-btns{display:flex;flex-wrap:wrap;gap:8px;margin-top:10px}
.lect-btns button{padding:9px 14px;border-radius:10px;border:2px solid #0f766e;background:#fff;font-weight:700;cursor:pointer}
@media print{.navigation,.progress-container,.header img,.footer-autor{display:none}body{background:#fff}.container{max-width:none;box-shadow:none}}
"""
css = base + extra
for a, b in TEMA:
    css = css.replace(a, b)
open(os.path.join(OUT, "style.css"), "w", encoding="utf-8").write(css)

for nombre, svg in (("parametros.svg", sv.parametros()), ("espacio_signado.svg", sv.espacio_signado()),
                    ("configuraciones.svg", sv.configuraciones()), ("linea_historia.svg", sv.linea_historia())):
    open(os.path.join(OUT, "img", nombre), "w", encoding="utf-8").write(svg)
open(os.path.join(OUT, "lse.js"), "w", encoding="utf-8").write(IA_JS)


def _marco(titulo_pag, icono, h1, sub, cuerpo, prev, nxt, lbl, pct, etiqueta):
    if cuerpo.count('class="como"') >= 2:
        cuerpo = ('<div class="como-ctrl"><button onclick="comoTodos(true)">▾ Desplegar todos los «Cómo se hace»</button>'
                  '<button onclick="comoTodos(false)">▸ Plegar todos</button></div>\n' + cuerpo)
    return f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{titulo_pag}</title>
<link rel="stylesheet" href="style.css">
</head>
<body>
<div class="container">
  <div class="header">
    <h1><span class="shield-icon">{icono}</span>{h1}</h1>
    <img src="img/logo-centro.png" class="logo-centro" alt="Logotipo del centro">
    <p>{sub}</p>
  </div>
  <div class="progress-container">
    <div class="progress-bar"><div class="progress-fill" style="width:{pct}%"></div></div>
    <div class="progress-text">{etiqueta}</div>
  </div>
  <div class="content-area">
    <section class="module">
{cuerpo}
      <div class="navigation">
        <button class="nav-btn" onclick="scormGo('{prev}')">⬅️ Anterior</button>
        <button class="nav-btn" onclick="scormGo('{nxt}')">{lbl}</button>
      </div>
    </section>
  </div>
</div>
<footer class="footer-autor">{FOOTER}</footer>
<script src="lse.js"></script>
<script src="scorm.js"></script>
</body>
</html>
"""


for i, (ic, t, sub, body) in enumerate(M, 1):
    prev = "index.html" if i == 1 else f"modulo{i-1}.html"
    nxt = "proyecto_final.html" if i == N else f"modulo{i+1}.html"
    lbl = "Ir al proyecto final 🎯" if i == N else "Siguiente módulo ➡️"
    nivel = "Fundamentos" if i <= 5 else "Práctica"
    open(os.path.join(OUT, f"modulo{i}.html"), "w", encoding="utf-8").write(
        _marco(f"Módulo {i}: {t}", ic, f"Módulo {i}: {t}", sub, body, prev, nxt, lbl, round(i * 100 / (N + 2)), f"Curso de LSE · {nivel} · Módulo {i} de {N}"))
NOMBRES = [m[1] for m in M]

# Proyecto final ------------------------------------------------------------------------------------------
proy = ("<h2>Tu proyecto: un plan de comunicación accesible</h2>"
        "<p>Elige un negocio o servicio (un bar, un hotel, una tienda, un centro de estudios) y prepara un <b>plan para atender bien a personas sordas</b>. Puedes hacerlo por escrito, en una presentación o en una sesión de clase con tu docente.</p>"
        + pasos(["<b>Describe el lugar</b>: qué ofrece, quién lo visita y cuáles son sus momentos más ocupados.",
                 "<b>Escribe un protocolo</b> de recepción y atención en siete pasos (módulos 5 y 9).",
                 "<b>Lista cinco mejoras de accesibilidad</b> (carta visual, avisos luminosos, subtítulos…) y explica por qué ayudarían.",
                 "<b>Prepara tu presentación</b> en dactilología: deletrea el nombre del lugar y tu nombre (módulo 4).",
                 "<b>Propón un plan de aprendizaje</b> de 12 semanas para el equipo (módulo 10)."])
        + hosteleria("si puedes, enseña tu plan a una asociación de personas sordas o a una persona sorda de tu entorno y pídele su opinión: sus consejos valen más que cualquier manual.")
        + actividad("Borrador del plan", "Escribe aquí el esquema de tu plan (lugar, protocolo, mejoras, presentación y plan de aprendizaje).", "Lugar: … Protocolo: … Mejoras: … Plan de aprendizaje: …")
        + caja("Criterios para valorarlo:", "claridad del protocolo, respeto en el lenguaje, uso de recursos visuales y realismo de las mejoras.")
        + cuidado("este curso es una introducción teórica y práctica. Para comunicarte con fluidez en LSE necesitas aprender con personas sordas y con formación oficial (módulo 10)."))
open(os.path.join(OUT, "proyecto_final.html"), "w", encoding="utf-8").write(_marco(
    "Proyecto final: tu plan de IA", "🎯", "Proyecto final", "Aplica lo aprendido a un negocio de hostelería.", proy,
    f"modulo{N}.html", "examen_final.html", "Ir al examen final 🏁", round((N + 1) * 100 / (N + 2)), "Curso de LSE · Proyecto final"))

# Banco de preguntas --------------------------------------------------------------------------------------


def _place(k, q):
    m, t, opts, ok, ex = q
    opts = list(opts)
    target = (k * 3 + 1) % len(opts)
    opts[ok], opts[target] = opts[target], opts[ok]
    return (m, t, opts, target, ex)


QQ = [_place(k, q) for k, q in enumerate(sorted(Q, key=lambda q: q[0]))]
EXAM = [q for q in QQ if q[4]]


def gift_esc(s):
    for ch in "~=#{}:":
        s = s.replace(ch, "\\" + ch)
    return s


g = ["// Lengua de signos española (LSE): curso completo — Banco de preguntas GIFT para Moodle",
     "// Autor: Sixto Rodríguez de Sepúlveda. Una única respuesta correcta; una categoría por módulo."]
cur, cnt = None, {}
for m, q, opts, ok, _ in QQ:
    if m != cur:
        cur = m
        g += ["", f"$CATEGORY: LSE/Módulo {m:02d} - {gift_esc(NOMBRES[m-1])}"]
    cnt[m] = cnt.get(m, 0) + 1
    g += ["", f"::IA{m:02d}-{cnt[m]}::{gift_esc(q)} {{"] + [f"{'=' if j == ok else '~'}{gift_esc(o)}" for j, o in enumerate(opts)] + ["}"]
open(os.path.join(OUT, "preguntas_moodle.gift"), "w", encoding="utf-8").write("\n".join(g) + "\n")

qs_html = "".join(
    f'<div class="quiz" id="box{i}"><h4>{i}. {html.escape(q)} <span class="small">(Módulo {m})</span></h4><div class="options">'
    + "".join(f'<label class="option"><input type="radio" name="q{i}" value="{j}" style="width:auto;margin-right:8px">{html.escape(o)}</label>' for j, o in enumerate(opts))
    + "</div></div>" for i, (m, q, opts, ok, _) in enumerate(EXAM, 1))
exam = f"""<!DOCTYPE html>
<html lang="es"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Examen final: Lengua de signos española</title><link rel="stylesheet" href="style.css"></head>
<body><div class="container">
  <div class="header"><h1><span class="shield-icon">🏁</span>Examen final</h1><img src="img/logo-centro.png" class="logo-centro" alt="Logotipo del centro"><p>{TITULO}</p></div>
  <div class="progress-container"><div class="progress-bar"><div class="progress-fill" style="width:100%"></div></div><div class="progress-text">Curso de LSE · Examen final</div></div>
  <div class="content-area"><section class="module">
    <h2>Evaluación final</h2>
    <p>Responde a las {len(EXAM)} preguntas. Necesitas al menos un <b>70 %</b> para aprobar. Al corregir verás las respuestas correctas y podrás repetirlo.</p>
    {qs_html}
    <div style="text-align:center"><button class="btn" onclick="corregir()">Corregir examen</button> <button class="btn" onclick="reiniciar()">Reintentar</button></div>
    <div id="resultado" style="margin-top:20px"></div>
    <div class="navigation"><button class="nav-btn" onclick="scormGo('proyecto_final.html')">⬅️ Proyecto final</button><button class="nav-btn" onclick="scormGo('index.html')">Inicio 🏠</button></div>
  </section></div></div>
<footer class="footer-autor">{FOOTER}</footer>
<script src="scorm.js"></script>
<script>
var RESP={json.dumps([q[3] for q in EXAM])};
function reiniciar(){{document.querySelectorAll('input[type=radio]').forEach(function(r){{r.checked=false}});document.querySelectorAll('.option').forEach(function(l){{l.classList.remove('correct','incorrect')}});document.getElementById('resultado').innerHTML='';window.scrollTo(0,0);}}
function corregir(){{var ok=0,sin=0;for(var i=0;i<RESP.length;i++){{var n=i+1,sel=document.querySelector('input[name="q'+n+'"]:checked'),l=document.querySelectorAll('#box'+n+' .option');
 l.forEach(function(x){{x.classList.remove('correct','incorrect')}});l[RESP[i]].classList.add('correct');if(!sel){{sin++;continue;}}if(+sel.value===RESP[i])ok++;else l[+sel.value].classList.add('incorrect');}}
 var nota=Math.round(ok*100/RESP.length),r=document.getElementById('resultado');
 r.innerHTML=nota>=70?'<div class="certificate"><h2>🏆 ¡Enhorabuena!</h2><p>Has superado el curso <b>{TITULO}</b>.</p><p style="font-size:1.6em;font-weight:700;color:#2e7d32">'+ok+'/'+RESP.length+' · '+nota+' %</p></div>'
   :'<div class="alert-box"><b>Resultado: '+ok+'/'+RESP.length+' ('+nota+' %).</b> Necesitas un 70 %'+(sin?' (has dejado '+sin+' sin responder)':'')+'. Repasa los módulos y vuelve a intentarlo.</div>';
 if(window.scorm)scorm.complete(nota);r.scrollIntoView({{behavior:'smooth'}});}}
</script></body></html>
"""
open(os.path.join(OUT, "examen_final.html"), "w", encoding="utf-8").write(exam)

# Glosario e índice ------------------------------------------------------------------------------------------
GLOSARIO = [
    ("Bucle de inducción", "Sistema que envía el sonido directamente a audífonos e implantes."), ("Clasificador", "Forma de mano que representa una clase de cosas y muestra su movimiento."),
    ("CNSE", "Confederación Estatal de Personas Sordas."), ("Componentes no manuales", "Expresión de la cara, mirada, cabeza y cuerpo al signar."),
    ("Configuración", "Forma que adopta la mano al hacer un signo."), ("Cultura sorda", "Conjunto de valores, historia y costumbres de la comunidad sorda."),
    ("Dactilología", "Alfabeto manual: cada letra tiene una forma de la mano."), ("Hipoacusia", "Pérdida de audición de distinto grado."),
    ("Intérprete de LSE", "Profesional que traduce entre lengua oral y lengua de signos."), ("LSC", "Lengua de signos catalana."),
    ("LSE", "Lengua de signos española."), ("Oralismo", "Corriente que prohibió los signos y obligó a la enseñanza solo oral."),
    ("Persona sorda", "Persona que no oye o que oye con dificultad."), ("Seña-nombre", "Signo propio asignado a una persona por la comunidad sorda."),
    ("Signo", "Unidad de la lengua de signos, equivalente a una palabra."), ("Sordoceguera", "Pérdida combinada de vista y oído."),
    ("Subtitulado", "Texto en pantalla que reproduce lo que se dice."), ("Visogestual", "Lengua que se produce con gestos y se percibe con la vista."),
]
glosario = ('<details class="glos"><summary>📖 Glosario: las palabras del curso explicadas fácil (' + str(len(GLOSARIO)) + ' términos)</summary><dl class="glosario">'
            + "".join(f"<dt>{t}</dt><dd>{d}</dd>" for t, d in sorted(GLOSARIO, key=lambda x: x[0].lower())) + "</dl></details>")
itin = "".join(f'<li>{M[i][0]} <span><b>{i+1}.</b> <a href="modulo{i+1}.html">{t}</a></span></li>' for i, t in enumerate(NOMBRES))
index = f"""<!DOCTYPE html>
<html lang="es"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{TITULO}</title><link rel="stylesheet" href="style.css"></head>
<body><div class="container">
  <div class="header"><h1><span class="shield-icon">🤟</span>{TITULO}</h1><img src="img/logo-centro.png" class="logo-centro" alt="Logotipo del centro">
  <p>Comunidad sorda, historia, la lengua y sus parámetros, alfabeto manual, comunicación, gramática y atención accesible en hostelería.</p></div>
  <div class="progress-container"><div class="progress-bar"><div class="progress-fill" style="width:0%"></div></div><div class="progress-text">Curso de LSE · Inicio · {N} módulos</div></div>
  <div class="content-area"><section class="module">
    <h2>Bienvenido/a 👋</h2>
    <p>Este curso te introduce en la <b>lengua de signos española (LSE)</b> y en la <b>comunidad sorda</b>: quiénes son, cómo se habla con respeto, cómo es la lengua, cómo deletrear con las manos, cómo comunicarte aunque no signes y cómo atender bien a una persona sorda, con ejemplos de <b>hostelería</b>.</p>
    <div class="box"><b>Cómo funciona:</b> cada módulo tiene explicaciones sencillas, esquemas, cuadros «Cómo se hace» desplegables, actividades de arrastrar y soltar, un entrenador de dactilología, autoevaluaciones, un proyecto final y un examen de {len(EXAM)} preguntas.</div>
    <h3>Itinerario</h3>
    <p><b>Fundamentos</b> (módulos 1–5): comunidad, historia, lengua, alfabeto y comunicación · <b>Práctica</b> (módulos 6–10): conversaciones, gramática, vocabulario, hostelería y seguir aprendiendo</p>
    <ul class="key-points">{itin}<li>🎯 <span><a href="proyecto_final.html">Proyecto final</a></span></li><li>🏁 <span><a href="examen_final.html">Examen final</a></span></li></ul>
    {glosario}
    <div class="alert-box"><b>Importante:</b> una lengua de signos solo se aprende de verdad <b>viendo signos en vídeo y conversando con personas sordas</b>. Este curso te da la base teórica, el alfabeto, los recursos y un plan; los signos concretos conviene verlos en vídeo de fuentes oficiales (módulo 10). Las descripciones escritas son orientativas y pueden variar por región.</div>
    <div class="alert-box"><b>Nota:</b> el curso no incluye vídeos de signos. Contrasta siempre las letras y los signos con recursos oficiales y, si puedes, con una persona sorda o un profesor de LSE.</div>
    <div class="navigation"><span></span><button class="nav-btn" onclick="scormGo('modulo1.html')">Empezar el módulo 1 ➡️</button></div>
  </section></div></div>
<footer class="footer-autor">{FOOTER}</footer>
<script src="lse.js"></script>
<script src="scorm.js"></script>
</body></html>
"""
open(os.path.join(OUT, "index.html"), "w", encoding="utf-8").write(index)

if not os.path.exists(os.path.join(OUT, "imsmanifest.xml")):
    open(os.path.join(OUT, "imsmanifest.xml"), "w", encoding="utf-8").write(
        f'<?xml version="1.0" encoding="UTF-8"?>\n<manifest identifier="lse-curso-completo" version="1.0" xmlns="http://www.imsproject.org/xsd/imscp_rootv1p1p2">'
        f'<organizations default="ORG_1"><organization identifier="ORG_1"><title>{TITULO}</title></organization></organizations><resources/></manifest>\n')
if not os.path.exists(os.path.join(OUT, "scorm.js")):
    open(os.path.join(OUT, "scorm.js"), "w", encoding="utf-8").write("")

open(os.path.join(OUT, "README.txt"), "w", encoding="utf-8").write(f"""LENGUA DE SIGNOS ESPAÑOLA (LSE): CURSO COMPLETO — Paquete SCORM 1.2
Autor: Sixto Rodríguez de Sepúlveda

{N} módulos: personas sordas y comunidad sorda; historia y derechos; la LSE como lengua y sus cinco parámetros; dactilología;
comunicarse sin barreras; primeras conversaciones; gramática; vocabulario; atención accesible en hostelería; seguir aprendiendo.

Contenido:
- Esquemas (parámetros, espacio de signado, configuraciones de la mano, línea de tiempo), actividades de arrastrar y soltar,
  cuadros «Cómo se hace» desplegables y glosario.
- Entrenador de dactilología (descripciones del alfabeto manual, reproductor y juego) que funciona sin conexión.
- Proyecto final y examen final de {len(EXAM)} preguntas (aprobado 70 %); preguntas_moodle.gift: {len(QQ)} preguntas.
- Seguimiento SCORM: un SCO por página.

Notas:
- El curso no incluye vídeos de signos: las descripciones son orientativas y deben contrastarse con recursos oficiales
  (por ejemplo, el diccionario normativo de la Fundación CNSE) y con personas sordas o profesores de LSE.
- Pueden existir variantes regionales de signos.
""")
print("ok", N, "módulos,", len(EXAM), "preguntas de examen,", len(QQ), "GIFT")
