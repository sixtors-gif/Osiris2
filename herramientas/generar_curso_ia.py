#!/usr/bin/env python3
"""Genera el curso SCORM «Inteligencia artificial para jóvenes: aprende con Claude».

Uso (desde la raíz del repositorio):
  python3 herramientas/generar_curso_ia.py cursos/Curso_IA_Jovenes_Claude_SCORM
  python3 herramientas/insertar_dragdrop.py Curso_IA_Jovenes_Claude_SCORM
  python3 herramientas/scorm_seguimiento.py
Contenido: ia_modulos_a.py (1-6), ia_modulos_b.py (7-12), ia_preguntas.py, ia_svgs.py, ia_js.py.
"""
import html, json, os, re, shutil, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ia_svgs as sv  # noqa: E402
from ia_js import IA_JS  # noqa: E402
from ia_modulos_a import MODULOS as MOD_A  # noqa: E402
from ia_modulos_b import MODULOS as MOD_B  # noqa: E402
from ia_preguntas import Q  # noqa: E402
from ia_helpers import actividad, caja, cuidado, hosteleria, kp, pasos  # noqa: E402

OUT = sys.argv[1]
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
os.makedirs(os.path.join(OUT, "img"), exist_ok=True)
TITULO = "Inteligencia artificial para jóvenes: aprende con Claude"
FOOTER = f"{TITULO} · Material educativo · Creado por: Sixto Rodríguez de Sepúlveda"
M = MOD_A + MOD_B
N = len(M)
assert N == 12, N
shutil.copy(os.path.join(RAIZ, "cursos", "CiberSeguridad_Avanzada", "img", "logo-centro.png"), os.path.join(OUT, "img", "logo-centro.png"))

TEMA = [("#1e3c72", "#4b3a8f"), ("#2a5298", "#6a54b8"), ("#4ecdc4", "#f59e0b"), ("#44a08d", "#d98200"),
        ("linear-gradient(135deg,#11432b 0%,#1b5e20 100%)", "linear-gradient(135deg,#241a52 0%,#4b3a8f 100%)"),
        ("#f2f6ff", "#f3effc"), ("#f8faff", "#f8f6fd"), ("#f4f7fb", "#f6f3fc"), ("#6c8ccf", "#8b7bd1"), ("#3b5ba8", "#4b3a8f"), ("#dfe5ef", "#e3ddf3")]
base = open(os.path.join(RAIZ, "cursos", "CiberSeguridad_Avanzada", "style.css"), encoding="utf-8").read()
extra = """
/* Curso de IA para jóvenes */
.shield-icon{background:linear-gradient(45deg,#f59e0b,#fcd34d)}
.module h2{border-bottom-color:#f59e0b}
.module h4{color:#4b3a8f;margin:18px 0 6px;font-size:1.05em}
.tabla-wrap{overflow-x:auto;margin:16px 0}
.tabla{border-collapse:collapse;width:100%;font-size:1em}
.tabla th{background:#4b3a8f;color:#fff;padding:8px 10px;text-align:left}
.tabla td{border:1px solid #e3ddf3;padding:8px 10px;vertical-align:top}
.tabla tr:nth-child(even) td{background:#f6f3fc}
.figure img{max-width:100%;height:auto}
.palabras{background:#fffaf0;border:2px solid #f59e0b;border-radius:14px;padding:14px 18px 10px;margin:4px 0 20px}
.palabras p{font-size:1.12em;line-height:1.6;margin:6px 0}
.pal-tag{display:inline-block;background:#f59e0b;color:#fff;font-weight:700;font-size:.8em;letter-spacing:.04em;text-transform:uppercase;border-radius:20px;padding:3px 12px}
.practica{background:#eef7ee;border-left:5px solid #4caf50;border-radius:10px;padding:12px 18px;margin:18px 0}
.como{background:#f3effc;border-left:4px solid #8b7bd1;border-radius:8px;margin:6px 0 10px;font-size:.95em;line-height:1.6}.como>summary{cursor:pointer;padding:7px 12px;font-weight:700;color:#4b3a8f;list-style:none;border-radius:8px}.como>summary::-webkit-details-marker{display:none}.como>summary::before{content:'▸ ';display:inline-block;width:1em}.como[open]>summary::before{content:'▾ '}.como-cuerpo{padding:2px 14px 10px 14px}
.como-ctrl{display:flex;gap:8px;flex-wrap:wrap;margin:0 0 14px}.como-ctrl button{background:#fff;border:1px solid #c9bfe8;border-radius:18px;padding:5px 12px;cursor:pointer;font-size:.9em;color:#4b3a8f;font-weight:600}
.glosario dt{font-weight:700;color:#4b3a8f;margin-top:10px}.glosario dd{margin:2px 0 0 18px;line-height:1.55}
details.glos{border:1px solid #e3ddf3;border-radius:12px;padding:10px 16px;margin:16px 0;background:#f8f6fd}
details.glos summary{cursor:pointer;font-weight:700;color:#4b3a8f;font-size:1.05em}
.module ol{margin:10px 0 14px 28px}.module ol li{line-height:1.7;font-size:1.05em;padding:2px 0}
.prompt{background:#1f1b3a;color:#f4f1ff;border-radius:12px;padding:10px 14px 12px;margin:14px 0;position:relative}
.prompt-t{font-weight:700;color:#fcd34d;margin-bottom:6px;font-size:.95em}
.prompt pre{white-space:pre-wrap;word-wrap:break-word;margin:0 0 8px;font-family:inherit;line-height:1.55;color:#f4f1ff}
.prompt button{background:#f59e0b;color:#1f1b3a;border:0;border-radius:18px;padding:5px 14px;font-weight:700;cursor:pointer}
.respuesta{background:#f3f9f4;border:1px solid #bfdcc4;border-left:5px solid #2e7d32;border-radius:12px;padding:8px 16px;margin:14px 0}
.resp-t{font-weight:700;color:#2e7d32;margin-bottom:4px}
.hosteleria{background:#fff4e0;border:1px solid #f3c77a;border-left:5px solid #f59e0b;border-radius:12px;padding:10px 16px;margin:16px 0;line-height:1.6}
.pb label,.pv label{display:block;margin:8px 0 2px;font-weight:600;color:#4b3a8f}
.pb input[type=text],.pb textarea,.pv textarea{width:100%;box-sizing:border-box;padding:8px;border:1px solid #c9bfe8;border-radius:8px;font:inherit}
.pb textarea{min-height:60px}
.pred-gen{font-size:1.1em;background:#fff;border:1px dashed #8b7bd1;border-radius:8px;padding:8px 12px;min-height:1.5em}
.pv-ok{color:#2e7d32;font-weight:600}.pv-ko{color:#c62828;font-weight:600}
.pv-limpio{white-space:pre-wrap;background:#f6f3fc;border-radius:8px;padding:8px 12px}
.bar-pred{display:flex;align-items:center;gap:8px;margin:3px 0}.bar-pred span.b{display:inline-block;height:14px;background:#8b7bd1;border-radius:7px}
.dl-box{background:#fffaf0;border:2px solid #f59e0b;border-radius:12px;padding:14px 18px;margin:18px 0}
.lect-btns{display:flex;flex-wrap:wrap;gap:8px;margin-top:10px}
.lect-btns button{padding:9px 14px;border-radius:10px;border:2px solid #4b3a8f;background:#fff;font-weight:700;cursor:pointer}
@media print{.navigation,.progress-container,.header img,.footer-autor{display:none}body{background:#fff}.container{max-width:none;box-shadow:none}}
"""
css = base + extra
for a, b in TEMA:
    css = css.replace(a, b)
open(os.path.join(OUT, "style.css"), "w", encoding="utf-8").write(css)

for nombre, svg in (("linea_tiempo.svg", sv.linea_tiempo()), ("red_neuronal.svg", sv.red_neuronal()),
                    ("flujo_llm.svg", sv.flujo_llm()), ("tipos_ia.svg", sv.tipos_ia())):
    open(os.path.join(OUT, "img", nombre), "w", encoding="utf-8").write(svg)
open(os.path.join(OUT, "ia.js"), "w", encoding="utf-8").write(IA_JS)


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
<script src="ia.js"></script>
<script src="scorm.js"></script>
</body>
</html>
"""


for i, (ic, t, sub, body) in enumerate(M, 1):
    prev = "index.html" if i == 1 else f"modulo{i-1}.html"
    nxt = "proyecto_final.html" if i == N else f"modulo{i+1}.html"
    lbl = "Ir al proyecto final 🎯" if i == N else "Siguiente módulo ➡️"
    nivel = "Fundamentos" if i <= 6 else "Práctica"
    open(os.path.join(OUT, f"modulo{i}.html"), "w", encoding="utf-8").write(
        _marco(f"Módulo {i}: {t}", ic, f"Módulo {i}: {t}", sub, body, prev, nxt, lbl, round(i * 100 / (N + 2)), f"IA con Claude · {nivel} · Módulo {i} de {N}"))
NOMBRES = [m[1] for m in M]

# Proyecto final ------------------------------------------------------------------------------------------
proy = ("<h2>Tu proyecto: un plan de IA para un negocio de hostelería</h2>"
        "<p>Elige un negocio real o inventado (un bar, un hotel, un catering…) y prepara un <b>plan de uso responsable de la IA</b>. Puedes hacerlo por escrito, en una presentación o en una sesión de clase con tu docente.</p>"
        + pasos(["<b>Describe el negocio:</b> tipo, tamaño, público y principales tareas diarias.",
                 "<b>Elige tres tareas</b> donde la IA ayudaría (módulos 8, 9 y 10) y escribe un prompt con los seis ingredientes para cada una.",
                 "<b>Escribe lo que revisará una persona</b> en cada caso (datos, alérgenos, cifras, tono).",
                 "<b>Define tus reglas de privacidad:</b> qué datos nunca se compartirán y cómo se anonimizará (módulo 11).",
                 "<b>Imagina el futuro:</b> qué cambiará en este negocio dentro de cinco años y qué habilidades necesitará el equipo (módulo 12)."])
        + hosteleria("si puedes, enséñaselo a alguien del sector (un familiar, un profesor de cocina o sala, un empresario) y pídele su opinión: seguro que te dice cosas que ninguna IA sabe.")
        + actividad("Borrador del plan", "Escribe aquí el esquema de tu plan (negocio, tres tareas, revisión humana, reglas de privacidad y futuro).", "Negocio: … Tarea 1: … Tarea 2: … Tarea 3: … Reglas de privacidad: … Futuro: …")
        + caja("Criterios para valorarlo:", "claridad de los prompts, honestidad sobre lo que debe comprobarse, cuidado de los datos personales y realismo.")
        + cuidado("Claude.ai está pensado para mayores de 18 años. Si tienes menos, practica con un docente o con tu familia en un entorno autorizado, o con los ejemplos del curso; no necesitas una cuenta propia para hacer este proyecto."))
open(os.path.join(OUT, "proyecto_final.html"), "w", encoding="utf-8").write(_marco(
    "Proyecto final: tu plan de IA", "🎯", "Proyecto final", "Aplica lo aprendido a un negocio de hostelería.", proy,
    f"modulo{N}.html", "examen_final.html", "Ir al examen final 🏁", round((N + 1) * 100 / (N + 2)), "IA con Claude · Proyecto final"))

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


g = ["// Inteligencia artificial para jóvenes: aprende con Claude — Banco de preguntas GIFT para Moodle",
     "// Autor: Sixto Rodríguez de Sepúlveda. Una única respuesta correcta; una categoría por módulo."]
cur, cnt = None, {}
for m, q, opts, ok, _ in QQ:
    if m != cur:
        cur = m
        g += ["", f"$CATEGORY: IA con Claude/Módulo {m:02d} - {gift_esc(NOMBRES[m-1])}"]
    cnt[m] = cnt.get(m, 0) + 1
    g += ["", f"::IA{m:02d}-{cnt[m]}::{gift_esc(q)} {{"] + [f"{'=' if j == ok else '~'}{gift_esc(o)}" for j, o in enumerate(opts)] + ["}"]
open(os.path.join(OUT, "preguntas_moodle.gift"), "w", encoding="utf-8").write("\n".join(g) + "\n")

qs_html = "".join(
    f'<div class="quiz" id="box{i}"><h4>{i}. {html.escape(q)} <span class="small">(Módulo {m})</span></h4><div class="options">'
    + "".join(f'<label class="option"><input type="radio" name="q{i}" value="{j}" style="width:auto;margin-right:8px">{html.escape(o)}</label>' for j, o in enumerate(opts))
    + "</div></div>" for i, (m, q, opts, ok, _) in enumerate(EXAM, 1))
exam = f"""<!DOCTYPE html>
<html lang="es"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Examen final: IA con Claude</title><link rel="stylesheet" href="style.css"></head>
<body><div class="container">
  <div class="header"><h1><span class="shield-icon">🏁</span>Examen final</h1><img src="img/logo-centro.png" class="logo-centro" alt="Logotipo del centro"><p>{TITULO}</p></div>
  <div class="progress-container"><div class="progress-bar"><div class="progress-fill" style="width:100%"></div></div><div class="progress-text">IA con Claude · Examen final</div></div>
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
    ("Agente", "Sistema de IA que realiza tareas usando herramientas, con supervisión humana."), ("Alucinación", "Respuesta falsa que parece verdadera."),
    ("Algoritmo", "Conjunto de pasos para resolver un problema."), ("Anonimizar", "Quitar o sustituir los datos que identifican a una persona."),
    ("Aprendizaje automático", "Forma de IA que aprende patrones a partir de ejemplos."), ("Aprendizaje profundo", "Aprendizaje automático con redes neuronales de muchas capas."),
    ("Contexto (ventana de)", "Cantidad de texto que el modelo puede considerar a la vez."), ("Datos personales", "Información que identifica a una persona."),
    ("IA generativa", "IA que crea texto, imágenes, audio o código nuevos."), ("Modelo de lenguaje (LLM)", "Modelo entrenado con mucho texto para generar lenguaje."),
    ("Prompt", "Instrucción o mensaje que se le escribe a la IA."), ("RGPD", "Reglamento europeo de protección de datos."),
    ("Red neuronal", "Modelo matemático inspirado, de forma muy simplificada, en las neuronas."), ("Sesgo", "Prejuicio que la IA aprende de los datos."),
    ("Temperatura", "Ajuste que hace las respuestas más previsibles o más variadas."), ("Token", "Fragmento de texto que procesa el modelo."),
    ("Transformer", "Arquitectura de 2017 en la que se basan los modelos de lenguaje actuales."),
]
glosario = ('<details class="glos"><summary>📖 Glosario: las palabras del curso explicadas fácil (' + str(len(GLOSARIO)) + ' términos)</summary><dl class="glosario">'
            + "".join(f"<dt>{t}</dt><dd>{d}</dd>" for t, d in sorted(GLOSARIO, key=lambda x: x[0].lower())) + "</dl></details>")
itin = "".join(f'<li>{M[i][0]} <span><b>{i+1}.</b> <a href="modulo{i+1}.html">{t}</a></span></li>' for i, t in enumerate(NOMBRES))
index = f"""<!DOCTYPE html>
<html lang="es"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{TITULO}</title><link rel="stylesheet" href="style.css"></head>
<body><div class="container">
  <div class="header"><h1><span class="shield-icon">🤖</span>{TITULO}</h1><img src="img/logo-centro.png" class="logo-centro" alt="Logotipo del centro">
  <p>Historia de la IA, cómo funciona, cómo usar Claude y qué nos espera, con ejemplos de la hostelería.</p></div>
  <div class="progress-container"><div class="progress-bar"><div class="progress-fill" style="width:0%"></div></div><div class="progress-text">IA con Claude · Inicio · {N} módulos</div></div>
  <div class="content-area"><section class="module">
    <h2>Bienvenido/a 👋</h2>
    <p>Este curso te explica <b>qué es la inteligencia artificial, de dónde viene, cómo funciona y cómo usarla con criterio</b>, tomando como ejemplo a <b>Claude</b>, el asistente de Anthropic. Todos los ejemplos prácticos están pensados para <b>bares, restaurantes, cafeterías y hoteles</b>.</p>
    <div class="box"><b>Cómo funciona:</b> cada módulo tiene explicaciones sencillas, cuadros «Cómo se hace» desplegables, ejemplos de prompts que puedes copiar, actividades de arrastrar y soltar, juegos interactivos (constructor de prompts, predictor de palabras, revisor de privacidad), autoevaluaciones, un proyecto final y un examen de {len(EXAM)} preguntas.</div>
    <h3>Itinerario</h3>
    <p><b>Fundamentos</b> (módulos 1–6): historia, funcionamiento y Claude · <b>Práctica</b> (módulos 7–12): prompts, hostelería, ética y futuro</p>
    <ul class="key-points">{itin}<li>🎯 <span><a href="proyecto_final.html">Proyecto final</a></span></li><li>🏁 <span><a href="examen_final.html">Examen final</a></span></li></ul>
    {glosario}
    <div class="alert-box"><b>Importante:</b> las condiciones de uso de Claude.ai son para <b>mayores de 18 años</b>. Si eres menor, practica con tu docente o tu familia en un entorno autorizado. Todas las actividades del curso funcionan <b>sin cuenta</b> y sin conexión: las respuestas que verás son <b>ejemplos ilustrativos escritos para el curso</b>, no salidas literales de Claude.</div>
    <div class="alert-box"><b>Cuidado con la información:</b> las versiones de los modelos y las funciones de las herramientas cambian muy rápido. Comprueba los datos actuales en la web oficial de Anthropic. En alérgenos, seguridad alimentaria y normativa, consulta siempre fuentes oficiales.</div>
    <div class="navigation"><span></span><button class="nav-btn" onclick="scormGo('modulo1.html')">Empezar el módulo 1 ➡️</button></div>
  </section></div></div>
<footer class="footer-autor">{FOOTER}</footer>
<script src="ia.js"></script>
<script src="scorm.js"></script>
</body></html>
"""
open(os.path.join(OUT, "index.html"), "w", encoding="utf-8").write(index)

if not os.path.exists(os.path.join(OUT, "imsmanifest.xml")):
    open(os.path.join(OUT, "imsmanifest.xml"), "w", encoding="utf-8").write(
        f'<?xml version="1.0" encoding="UTF-8"?>\n<manifest identifier="ia-jovenes-claude" version="1.0" xmlns="http://www.imsproject.org/xsd/imscp_rootv1p1p2">'
        f'<organizations default="ORG_1"><organization identifier="ORG_1"><title>{TITULO}</title></organization></organizations><resources/></manifest>\n')
if not os.path.exists(os.path.join(OUT, "scorm.js")):
    open(os.path.join(OUT, "scorm.js"), "w", encoding="utf-8").write("")

open(os.path.join(OUT, "README.txt"), "w", encoding="utf-8").write(f"""INTELIGENCIA ARTIFICIAL PARA JÓVENES: APRENDE CON CLAUDE — Paquete SCORM 1.2
Autor: Sixto Rodríguez de Sepúlveda

{N} módulos: qué es la IA; historia de la IA (3 módulos); cómo funciona un modelo de lenguaje; conocer a Claude; escribir buenos
prompts; IA en hostelería (atención al cliente, cocina y sala, gestión y marketing); privacidad, ética y límites; y el futuro.

Contenido:
- Actividades de arrastrar y soltar, cuadros «Cómo se hace» desplegables, prompts para copiar, glosario.
- Herramientas que funcionan en el navegador, sin conexión y sin enviar datos: constructor de prompts, predictor de la
  siguiente palabra (con temperatura), simulador de ventana de contexto y revisor de privacidad.
- Proyecto final y examen final de {len(EXAM)} preguntas (aprobado 70 %); preguntas_moodle.gift: {len(QQ)} preguntas.
- Seguimiento SCORM: un SCO por página.

Notas:
- Las respuestas de IA que aparecen son ejemplos ilustrativos redactados para el curso, no salidas literales.
- Las condiciones de Claude.ai son para mayores de 18 años; el curso no requiere cuenta.
- Las versiones de modelos y funciones cambian rápido: verificar en la web oficial de Anthropic.
""")
print("ok", N, "módulos,", len(EXAM), "preguntas de examen,", len(QQ), "GIFT")
