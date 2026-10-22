#!/usr/bin/env python3
"""Genera el curso SCORM «Saxofón alto: de cero a intermedio».

Uso (desde la raíz del repositorio):
  python3 herramientas/generar_curso_saxo.py cursos/Curso_Saxofon_Alto_SCORM RUTA/abcjs-basic-min.js
  python3 herramientas/scorm_seguimiento.py
  (y para los PDF: node herramientas/saxo_pdf.js cursos/Curso_Saxofon_Alto_SCORM)

Partituras: herramientas/saxo_partituras.py (notación ABC, dibujadas con abcjs, licencia MIT).
Contenido: saxo_modulos_a.py, saxo_modulos_b.py; ejercicios y planning: saxo_ejercicios.py.
"""
import html, json, os, re, shutil, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import saxo_digitaciones as dg  # noqa: E402
from saxo_ejercicios import PLAN_JS, ejercicios_html, lista_ejercicios, planning_html  # noqa: E402
from saxo_helpers import partitura  # noqa: E402
from saxo_js import SAXO_JS  # noqa: E402
from saxo_modulos_a import MODULOS as MOD_A  # noqa: E402
from saxo_modulos_b import CLAVES_OPC, MODULOS as MOD_B  # noqa: E402
from saxo_partituras import PIEZAS, silenciar_melodia  # noqa: E402
from saxo_preguntas import Q  # noqa: E402

OUT, ABCJS = sys.argv[1], sys.argv[2]
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
for d in ("img", "partituras", "partituras/abc", "licencias"):
    os.makedirs(os.path.join(OUT, d), exist_ok=True)
TITULO = "Saxofón alto: de cero a intermedio"
FOOTER = f"{TITULO} · Material educativo · Creado por: Sixto Rodríguez de Sepúlveda"
M = MOD_A + MOD_B
N = len(M)
assert N == 14, N

shutil.copy(ABCJS, os.path.join(OUT, "abcjs-basic-min.js"))
lic = os.path.join(os.path.dirname(ABCJS), "..", "LICENSE.md")
if os.path.exists(lic):
    shutil.copy(lic, os.path.join(OUT, "licencias", "abcjs-LICENSE.md"))
shutil.copy(os.path.join(RAIZ, "cursos", "CiberSeguridad_Avanzada", "img", "logo-centro.png"), os.path.join(OUT, "img", "logo-centro.png"))

# Estilo: base común de los cursos con la paleta «latón» ---------------------------------------------
TEMA = [("#1e3c72", "#6b3f0e"), ("#2a5298", "#8a5a14"), ("#4ecdc4", "#c9962b"), ("#44a08d", "#a87a1c"),
        ("linear-gradient(135deg,#11432b 0%,#1b5e20 100%)", "linear-gradient(135deg,#2a1808 0%,#6b3f0e 100%)"),
        ("#f2f6ff", "#fbf5ea"), ("#f8faff", "#fdf9f1"), ("#f4f7fb", "#fbf6ec"), ("#6c8ccf", "#c9962b"), ("#3b5ba8", "#8a5a14"), ("#dfe5ef", "#eadfc9")]
base = open(os.path.join(RAIZ, "cursos", "CiberSeguridad_Avanzada", "style.css"), encoding="utf-8").read()
extra = """
/* Curso de saxofón alto */
.shield-icon{background:linear-gradient(45deg,#c9962b,#f3d77a)}
.module h2{border-bottom-color:#c9962b}
.score-box{background:#fff;border:1px solid #e3dccb;border-radius:14px;padding:14px 14px 10px;margin:22px 0;box-shadow:0 4px 14px rgba(59,36,16,.07)}
.score-box h4{margin:0 0 6px;color:#1e3c72}
.score svg{max-width:100%}
.score-tools{display:flex;flex-wrap:wrap;gap:8px;align-items:center;margin-top:6px}
.score-tools button{background:#1e3c72;color:#fff;border:0;border-radius:20px;padding:7px 14px;cursor:pointer;font-weight:600}
.score-tools button.stop{background:#8a8379}
.score-tools select{padding:6px;border-radius:8px;border:1px solid #bbb;width:auto}
.score-msg{font-size:.9em;color:#8a5a00}
.score-note{color:#555;font-size:.95em;margin-top:6px}
.tabla-wrap{overflow-x:auto;margin:16px 0}
.tabla{border-collapse:collapse;width:100%;font-size:1em}
.tabla th{background:#1e3c72;color:#fff;padding:8px 10px;text-align:left}
.tabla td{border:1px solid #dfe5ef;padding:8px 10px;vertical-align:top}
.tabla tr:nth-child(even) td{background:#f4f7fb}
.figure img{max-width:100%;height:auto}
.metro{display:flex;flex-wrap:wrap;gap:12px;align-items:center}
.metro input[type=range]{width:220px}
.beats{display:flex;gap:8px;margin-top:10px}
.beat{width:22px;height:22px;border-radius:50%;background:#dfe5ef}
.beat.on{background:#c9962b}.beat.on.first{background:#e74c3c}
.lect-btns{display:flex;flex-wrap:wrap;gap:8px;margin-top:10px}
.lect-btns button{min-width:62px;padding:10px;border-radius:10px;border:2px solid #1e3c72;background:#fff;font-weight:700;cursor:pointer}
.lect-btns button.ok{background:#4caf50;color:#fff;border-color:#4caf50}.lect-btns button.ko{background:#f44336;color:#fff;border-color:#f44336}
.dl-box{background:#fffaf0;border:2px solid #c9962b;border-radius:12px;padding:14px 18px;margin:18px 0}
.dl-box a{font-weight:700}
.checklist label{display:block;padding:6px 0}.checklist input{width:auto;margin-right:8px}
.palabras{background:#fffaf0;border:2px solid #c9962b;border-radius:14px;padding:14px 18px 10px;margin:4px 0 20px;position:relative}
.palabras p{font-size:1.12em;line-height:1.6;margin:6px 0}
.pal-tag{display:inline-block;background:#c9962b;color:#fff;font-weight:700;font-size:.8em;letter-spacing:.04em;text-transform:uppercase;border-radius:20px;padding:3px 12px}
.practica{background:#eef7ee;border-left:5px solid #4caf50;border-radius:10px;padding:12px 18px;margin:18px 0}
.practica h3{margin-top:4px}
.glosario dt{font-weight:700;color:#1e3c72;margin-top:10px}.glosario dd{margin:2px 0 0 18px;line-height:1.55}
details.glos{border:1px solid #dfe5ef;border-radius:12px;padding:10px 16px;margin:16px 0;background:#f8faff}
details.glos summary{cursor:pointer;font-weight:700;color:#1e3c72;font-size:1.05em}
.module h4{color:#1e3c72;margin:18px 0 6px;font-size:1.05em}
.como{background:#f2f6ff;border-left:4px solid #6c8ccf;border-radius:8px;margin:6px 0 10px;font-size:.95em;line-height:1.6}.como>summary{cursor:pointer;padding:7px 12px;font-weight:700;color:#3b5ba8;list-style:none;border-radius:8px}.como>summary::-webkit-details-marker{display:none}.como>summary::before{content:'▸ ';display:inline-block;width:1em}.como[open]>summary::before{content:'▾ '}.como>summary:hover{background:rgba(108,140,207,.12)}.como-cuerpo{padding:2px 14px 10px 14px}.como-ctrl{display:flex;gap:8px;flex-wrap:wrap;margin:0 0 14px}.como-ctrl button{background:#fff;border:1px solid #c7cfe0;border-radius:18px;padding:5px 12px;cursor:pointer;font-size:.9em;color:#3b5ba8;font-weight:600}
.ejercicio{background:#fff;border:1px solid #dfe5ef;border-left:5px solid #1e3c72;border-radius:12px;padding:6px 18px 12px;margin:18px 0}
.ejercicio h4{margin:12px 0 6px;font-size:1.1em;color:#1e3c72}
.ej-id{display:inline-block;background:#1e3c72;color:#fff;border-radius:8px;padding:1px 9px;margin-right:6px;font-size:.9em}
.ej-meta{float:right;font-size:.85em;color:#777;font-weight:400}
.ej-meta-fin{background:#eef7ee;border-radius:8px;padding:8px 12px;margin-top:8px}
.mes{background:#f8faff;border:1px solid #dfe5ef;border-radius:12px;padding:6px 18px 4px;margin:14px 0}
.mes .checklist{list-style:none;padding-left:0;margin:6px 0 12px}
.tabla-plan td,.tabla-plan th{font-size:.92em}
.tabla-plan tr.mes2 td,.tabla-plan tr.mes4 td,.tabla-plan tr.mes6 td{background:#f2f6ff}
.tabla-plan tr.mes1 td,.tabla-plan tr.mes3 td,.tabla-plan tr.mes5 td{background:#fff}
.tabla-plan input{width:20px;height:20px}
.plan-prog{margin:8px 0}.plan-barra{display:inline-block;width:160px;height:10px;background:#dfe5ef;border-radius:6px;margin-left:8px;vertical-align:middle;overflow:hidden}
.plan-barra span{display:block;height:100%;width:0;background:#4caf50}
.tabla-diario td{height:34px}
.lect-btns button.sel{background:#1e3c72;color:#fff}
.module ol{margin:10px 0 14px 28px}.module ol li{line-height:1.7;font-size:1.05em;padding:2px 0}
#dig-svg svg{width:100%;height:auto}
@media print{.score-tools,.navigation,.progress-container,.header img,.dl-box,.footer-autor{display:none}body{background:#fff}.container{max-width:none}.tabla-plan td,.tabla-plan th{font-size:.78em;padding:5px 6px}h2,h3{break-after:avoid}.tabla-plan tr,.ejercicio,.mes{break-inside:avoid}.container{box-shadow:none}}
"""
css = base + extra
for a, b in TEMA:
    css = css.replace(a, b)
open(os.path.join(OUT, "style.css"), "w", encoding="utf-8").write(css)

# Dibujos ------------------------------------------------------------------------------------------------
def guardar_svg(nombre, svg):
    open(os.path.join(OUT, "img", nombre), "w", encoding="utf-8").write(svg)


guardar_svg("saxo_partes.svg", dg.svg_partes())
guardar_svg("saxo_familia.svg", dg.svg_familia())
guardar_svg("saxo_partes_mudo.svg", dg.svg_partes(etiquetas=False))   # sin textos: para la actividad de arrastrar y soltar
guardar_svg("dig_basicas_mudo.svg", dg.svg_digitaciones(["Si4", "La4", "Sol4"], "Digitaciones sin nombre", con_nombre=False))
guardar_svg("dig_derecha_mudo.svg", dg.svg_digitaciones(["Fa4", "Mi4", "Re4"], "Digitaciones sin nombre", con_nombre=False))
for nombre, notas, titulo in (
        ("dig_basicas.svg", ["Si4", "La4", "Sol4"], "Si, La y Sol"),
        ("dig_derecha.svg", ["Fa4", "Mi4", "Re4"], "Fa, Mi y Re"),
        ("dig_do.svg", ["Do5", "Do♯5"], "Do y Do♯"),
        ("dig_alteradas.svg", ["Fa♯4", "Si♭4", "Sol♯4", "Mi♭4"], "Fa♯, Si♭, Sol♯ y Mi♭"),
        ("dig_graves.svg", ["Do4", "Do♯4", "Si3", "Si♭3"], "Do, Do♯, Si y Si♭ graves"),
        ("dig_agudo1.svg", ["Re5", "Mi5", "Fa♯5", "Sol5", "La5", "Si5"], "Re5, Mi5, Fa♯5, Sol5, La5 y Si5"),
        ("dig_agudo2.svg", ["Do6", "Do♯6", "Mi♭5", "Sol♯5", "Si♭5", "Fa5"], "Do6, Do♯6, Mi♭5, Sol♯5, Si♭5 y Fa5")):
    guardar_svg(nombre, dg.svg_digitaciones(notas, "Digitaciones de " + titulo))

# JavaScript común (con las digitaciones del entrenador) --------------------------------------------------
dig_svgs = {n: dg.svg_digitaciones([n], "Digitación de " + n) for n in dg.REGISTRO_GRAVE + dg.REGISTRO_AGUDO}
open(os.path.join(OUT, "saxo.js"), "w", encoding="utf-8").write(SAXO_JS.replace("__DIG__", json.dumps(dig_svgs, ensure_ascii=False)))

# Páginas ---------------------------------------------------------------------------------------------------


def _marco(titulo_pag, icono, h1, sub, cuerpo, prev, nxt, lbl, pct, etiqueta, script_final=""):
    if cuerpo.count('class="como"') >= 2:  # botones para desplegar o plegar todos los «Cómo se hace»
        cuerpo = ('<div class="como-ctrl"><button onclick="comoTodos(true)">▾ Desplegar todos los «Cómo se hace»</button>'
                  '<button onclick="comoTodos(false)">▸ Plegar todos</button></div>\n' + cuerpo)
    claves = re.findall(r'id="p-(\w+)"', cuerpo)
    datos = json.dumps({k: PIEZAS[k]["abc"] for k in claves}, ensure_ascii=False)
    acomp = json.dumps({k: silenciar_melodia(PIEZAS[k]["abc"]) for k in claves if PIEZAS[k]["acomp"]}, ensure_ascii=False)
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
<script>var PARTITURAS={datos};var PARTITURAS_ACOMP={acomp};</script>
<script src="abcjs-basic-min.js"></script>
<script src="saxo.js"></script>
<script src="scorm.js"></script>
{script_final}
</body>
</html>
"""


LECT_BTNS = "".join(f'<button onclick="lectResp(\'{l}\',this)">{n}</button>' for l, n in (("C", "Do"), ("D", "Re"), ("E", "Mi"), ("F", "Fa"), ("G", "Sol"), ("A", "La"), ("B", "Si")))


def arreglar(cuerpo):
    cuerpo = cuerpo.replace("__LECT_BTNS__", LECT_BTNS).replace("__CLAVES__", CLAVES_OPC)
    assert "__LECT_BTNS__" not in cuerpo and "__CLAVES__" not in cuerpo
    return cuerpo


def pagina(n, icono, titulo, sub, cuerpo):
    prev = "planificacion.html" if n == 1 else f"modulo{n-1}.html"
    nxt = "ejercicios.html" if n == N else f"modulo{n+1}.html"
    lbl = "Ir al gimnasio de ejercicios 🏋️" if n == N else "Siguiente módulo ➡️"
    nivel = "Fundamentos" if n <= 7 else "Desarrollo"
    return _marco(f"Módulo {n}: {titulo}", icono, f"Módulo {n}: {titulo}", sub, arreglar(cuerpo), prev, nxt, lbl,
                  round(n * 100 / (N + 2)), f"Saxofón alto · {nivel} · Módulo {n} de {N}")


for i, (ic, t, sub, body) in enumerate(M, 1):
    open(os.path.join(OUT, f"modulo{i}.html"), "w", encoding="utf-8").write(pagina(i, ic, t, sub, body))
NOMBRES = [m[1] for m in M]

# Gimnasio de ejercicios -----------------------------------------------------------------------------------
N_EJ = len(lista_ejercicios())
open(os.path.join(OUT, "ejercicios.html"), "w", encoding="utf-8").write(_marco(
    "Gimnasio: ejercicios prácticos", "🏋️", "Gimnasio de ejercicios prácticos",
    "Ejercicios con partitura, pasos, tiempo y una meta medible para cada día.",
    "<h2>Ejercicios prácticos</h2>\n" + ejercicios_html(partitura), f"modulo{N}.html", "examen_final.html", "Ir al examen final 🏁",
    round((N + 1) * 100 / (N + 2)), "Saxofón alto · Gimnasio de ejercicios"))

# Cuaderno de partituras (para imprimir y generar el PDF) --------------------------------------------------
orden = list(PIEZAS)
bloques = "".join(f'<section class="pieza"><h2>{i}. {PIEZAS[k]["titulo"]}</h2><div id="p-{k}"></div><p>{PIEZAS[k]["nota"]}</p></section>' for i, k in enumerate(orden, 1))
cuaderno = f"""<!DOCTYPE html>
<html lang="es"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Cuaderno de partituras · {TITULO}</title>
<style>
body{{font-family:'Segoe UI',Tahoma,sans-serif;max-width:820px;margin:0 auto;padding:16px;color:#222;background:#fff}} .pieza div{{width:100%}}
header{{text-align:center;border-bottom:3px solid #c9962b;margin-bottom:20px}} h1{{color:#6b3f0e}}
.pieza{{page-break-inside:avoid;break-inside:avoid;margin-bottom:26px}} .pieza h2{{color:#6b3f0e;font-size:1.1em;margin-bottom:0}}
.pieza p{{font-size:.9em;color:#555;margin-top:2px}} footer{{text-align:center;font-size:.8em;color:#777}}
</style></head><body>
<header><h1>Cuaderno de partituras para saxo alto</h1><p>{TITULO}<br>Todas las partituras están en el tono ESCRITO del saxo alto (clave de Sol). Los acordes, también en tono escrito.<br>
Ejercicios originales del curso y melodías tradicionales de dominio público.</p></header>
{bloques}
<footer>{FOOTER} · Partituras dibujadas con abcjs (licencia MIT)</footer>
<script>var PARTITURAS={json.dumps({k: PIEZAS[k]["abc"] for k in orden}, ensure_ascii=False)};</script>
<script src="../abcjs-basic-min.js"></script>
<script>Object.keys(PARTITURAS).forEach(function(k){{var op={{responsive:'resize',staffwidth:900,wrap:{{minSpacing:1.6,maxSpacing:2.6,preferredMeasuresPerLine:4}},paddingleft:0,paddingright:0}};if(/^% sin-ajuste/m.test(PARTITURAS[k])){{delete op.wrap;op.paddingright=30;}}ABCJS.renderAbc('p-'+k,PARTITURAS[k],op);}});document.title+=' ';window.LISTO=true;</script>
</body></html>
"""
open(os.path.join(OUT, "partituras", "cuaderno.html"), "w", encoding="utf-8").write(cuaderno)
for i, k in enumerate(orden, 1):
    open(os.path.join(OUT, "partituras", "abc", f"{i:02d}_{k}.abc"), "w", encoding="utf-8").write(PIEZAS[k]["abc"])

# Banco de preguntas --------------------------------------------------------------------------------------


def _place(k, q):
    m, t, opts, ok, ex = q
    opts = list(opts); target = (k * 3 + 1) % len(opts)
    opts[ok], opts[target] = opts[target], opts[ok]
    return (m, t, opts, target, ex)


QQ = sorted(Q, key=lambda q: q[0])
QQ = [_place(k, q) for k, q in enumerate(QQ)]
EXAM = [q for q in QQ if q[4]]


def gift_esc(s):
    for ch in "~=#{}:":
        s = s.replace(ch, "\\" + ch)
    return s


g = ["// Saxofón alto: de cero a intermedio — Banco de preguntas GIFT para Moodle",
     "// Autor: Sixto Rodríguez de Sepúlveda. Una única respuesta correcta; una categoría por módulo."]
cur, cnt = None, {}
for m, q, opts, ok, _ in QQ:
    if m != cur:
        cur = m
        g += ["", f"$CATEGORY: Saxofón alto/Módulo {m:02d} - {gift_esc(NOMBRES[m-1])}"]
    cnt[m] = cnt.get(m, 0) + 1
    g += ["", f"::SAX{m:02d}-{cnt[m]}::{gift_esc(q)} {{"] + [f"{'=' if j == ok else '~'}{gift_esc(o)}" for j, o in enumerate(opts)] + ["}"]
open(os.path.join(OUT, "preguntas_moodle.gift"), "w", encoding="utf-8").write("\n".join(g) + "\n")

qs_html = "".join(
    f'<div class="quiz" id="box{i}"><h4>{i}. {html.escape(q)} <span class="small">(Módulo {m})</span></h4><div class="options">'
    + "".join(f'<label class="option"><input type="radio" name="q{i}" value="{j}" style="width:auto;margin-right:8px">{html.escape(o)}</label>' for j, o in enumerate(opts))
    + "</div></div>" for i, (m, q, opts, ok, _) in enumerate(EXAM, 1))
exam = f"""<!DOCTYPE html>
<html lang="es"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Examen final: Saxofón alto</title><link rel="stylesheet" href="style.css"></head>
<body><div class="container">
  <div class="header"><h1><span class="shield-icon">🏁</span>Examen final</h1><img src="img/logo-centro.png" class="logo-centro" alt="Logotipo del centro"><p>{TITULO}</p></div>
  <div class="progress-container"><div class="progress-bar"><div class="progress-fill" style="width:100%"></div></div><div class="progress-text">Saxofón alto · Examen final</div></div>
  <div class="content-area"><section class="module">
    <h2>Evaluación final</h2>
    <p>Responde a las {len(EXAM)} preguntas. Necesitas al menos un <b>70 %</b> para aprobar. Al corregir verás las respuestas correctas y podrás repetirlo.</p>
    {qs_html}
    <div style="text-align:center"><button class="btn" onclick="corregir()">Corregir examen</button> <button class="btn" onclick="reiniciar()">Reintentar</button></div>
    <div id="resultado" style="margin-top:20px"></div>
    <div class="navigation"><button class="nav-btn" onclick="scormGo('ejercicios.html')">⬅️ Gimnasio</button><button class="nav-btn" onclick="scormGo('index.html')">Inicio 🏠</button></div>
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
   :'<div class="alert-box"><b>Resultado: '+ok+'/'+RESP.length+' ('+nota+' %).</b> Necesitas un 70 %'+(sin?' (has dejado '+sin+' sin responder)':'')+'. Repasa los módulos indicados y vuelve a intentarlo.</div>';
 if(window.scorm)scorm.complete(nota);r.scrollIntoView({{behavior:'smooth'}});}}
</script></body></html>
"""
open(os.path.join(OUT, "examen_final.html"), "w", encoding="utf-8").write(exam)

# Planning ---------------------------------------------------------------------------------------------------
open(os.path.join(OUT, "planificacion.html"), "w", encoding="utf-8").write(_marco(
    "Planning de 6 meses (45 minutos al día)", "📅", "Planning de 6 meses · 45 minutos al día",
    "26 semanas: qué estudiar cada día, cada semana y cada mes.",
    "<h2>Tu planning de estudio</h2>\n" + planning_html(len(EXAM)), "index.html", "modulo1.html", "Empezar el módulo 1 ➡️",
    round(100 / (N + 2)), "Saxofón alto · Planning de 6 meses", script_final="<script>" + PLAN_JS + "</script>"))

# Glosario y portada -------------------------------------------------------------------------------------------
GLOSARIO = [
    ("Abrazadera", "Anillo con tornillos que sujeta la caña a la boquilla."), ("Afinación", "Ajuste de la altura de las notas a una referencia común (La = 440 Hz)."),
    ("Arpegio", "Notas de un acorde tocadas una tras otra."), ("Articulación", "Forma de empezar, unir y terminar las notas: ligado, picado, acento…"),
    ("Blues", "Forma de 12 compases con tres acordes, base del jazz."), ("Boquilla", "Pieza sobre la que vibra la caña."),
    ("Caña", "Lengüeta de caña que vibra contra la boquilla."), ("Cents", "Centésimas de semitono; se usan para medir la afinación."),
    ("Compás", "Grupo de pulsos que se repite, con el primero más fuerte."), ("Concierto (tono de)", "La altura real que suena, la que lee un piano."),
    ("Cuello (tudel)", "Tubo curvo entre la boquilla y el cuerpo."), ("Embocadura", "Posición de los labios y los dientes sobre la boquilla."),
    ("Escala cromática", "Escala que avanza por semitonos."), ("Escrito (tono)", "La nota que se lee en la partitura del saxo, distinta de la que suena."),
    ("Frase", "Idea musical completa, como una oración; se respira entre frases."), ("Legato", "Notas unidas, sin cortes."),
    ("Llave de octava", "Llave del pulgar izquierdo que hace sonar la nota una octava más aguda."), ("Mi♭ (saxo en)", "El saxo alto suena una sexta mayor más grave que lo escrito."),
    ("Nota azul", "Nota de paso de la escala de blues que da su color."), ("Pulso", "Latido constante de la música."),
    ("Registro", "Zona del instrumento: grave o agudo."), ("Staccato", "Notas cortadas, más breves que su valor."),
    ("Swing", "Corcheas desiguales («largas-cortas») típicas del jazz."), ("Tempo", "Velocidad de la música, en pulsos por minuto."),
    ("Transposición", "Cambio de una música a otra tonalidad."), ("Vibrato", "Oscilación regular de la altura de una nota."),
]
glosario = ('<details class="glos"><summary>📖 Glosario: las palabras del curso explicadas fácil (' + str(len(GLOSARIO)) + ' términos)</summary><dl class="glosario">'
            + "".join(f"<dt>{t}</dt><dd>{d}</dd>" for t, d in sorted(GLOSARIO, key=lambda x: x[0].lower())) + "</dl></details>")
itin = ('<li>📅 <span><a href="planificacion.html"><b>Planning de 6 meses</b></a> (45 minutos al día): qué estudiar cada día y cada semana</span></li>'
        + "".join(f'<li>{"🎷" if i < 7 else "🎼"} <span><b>{i+1}.</b> <a href="modulo{i+1}.html">{t}</a></span></li>' for i, t in enumerate(NOMBRES)))
index = f"""<!DOCTYPE html>
<html lang="es"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{TITULO}</title><link rel="stylesheet" href="style.css"></head>
<body><div class="container">
  <div class="header"><h1><span class="shield-icon">🎷</span>{TITULO}</h1><img src="img/logo-centro.png" class="logo-centro" alt="Logotipo del centro">
  <p>Del montaje y el primer sonido a las escalas, la lectura, la afinación y la improvisación, con partituras que puedes escuchar e imprimir.</p></div>
  <div class="progress-container"><div class="progress-bar"><div class="progress-fill" style="width:0%"></div></div><div class="progress-text">Saxofón alto · Inicio · {N} módulos</div></div>
  <div class="content-area"><section class="module">
    <h2>Bienvenido/a 👋</h2>
    <p>Este curso es para quien <b>nunca ha tocado el saxofón</b> (aunque sepas algo de música, mejor): empieza por conocer y montar el instrumento y termina tocando melodías, escalas y un blues. Aprenderás <b>sonido, embocadura, respiración, digitaciones, articulación, lectura, transposición, afinación e improvisación</b>.</p>
    <div class="box"><b>Cómo funciona:</b> cada módulo tiene explicaciones paso a paso, dibujos de digitaciones, <b>partituras interactivas con sonido de saxo y acompañamiento</b> (pulsa «▶ Escuchar»), ejercicios y autoevaluaciones. Además hay un <b>gimnasio con {N_EJ} ejercicios</b>, un <b>planning de 6 meses</b> y un examen final de {len(EXAM)} preguntas.</div>
    <div class="dl-box">📥 <b>Partituras para imprimir:</b> <a href="partituras/Cuaderno_de_partituras.pdf" target="_blank" rel="noopener">Cuaderno de partituras (PDF)</a> con las {len(PIEZAS)} partituras del curso (en tono escrito para saxo alto).</div>
    <h3>Itinerario</h3>
    <p><b>Fundamentos</b> (módulos 1–7) · <b>Desarrollo</b> (módulos 8–14)</p>
    <ul class="key-points">{itin}<li>🏋️ <span><a href="ejercicios.html"><b>Gimnasio de ejercicios prácticos</b></a>: {N_EJ} ejercicios con partitura, pasos y meta</span></li><li>🏁 <span><a href="examen_final.html">Examen final</a></span></li></ul>
    {glosario}
    <div class="alert-box"><b>Qué necesitas:</b> un saxo alto en buen estado (o alquilado), boquilla, cañas, correa, paño y escobillón. Si es posible, <b>un/a profesor/a</b> que corrija tu postura y tu embocadura, que son difíciles de ver por uno mismo. Para escuchar las partituras hace falta conexión a Internet la primera vez (se descargan los sonidos); el resto de los recursos funcionan sin conexión.</div>
    <div class="alert-box"><b>Cuida tu salud:</b> descansa los labios cada pocos minutos, bebe agua y para si notas dolor en los labios, el cuello, las muñecas o la espalda.</div>
    <div class="navigation"><span></span><button class="nav-btn" onclick="scormGo('planificacion.html')">Ver el planning y comenzar ➡️</button></div>
  </section></div></div>
<footer class="footer-autor">{FOOTER}</footer>
<script src="scorm.js"></script>
</body></html>
"""
open(os.path.join(OUT, "index.html"), "w", encoding="utf-8").write(index)

if not os.path.exists(os.path.join(OUT, "imsmanifest.xml")):
    open(os.path.join(OUT, "imsmanifest.xml"), "w", encoding="utf-8").write(
        f'<?xml version="1.0" encoding="UTF-8"?>\n<manifest identifier="saxo-alto-iniciacion" version="1.0" xmlns="http://www.imsproject.org/xsd/imscp_rootv1p1p2">'
        f'<organizations default="ORG_1"><organization identifier="ORG_1"><title>{TITULO}</title></organization></organizations><resources/></manifest>\n')
if not os.path.exists(os.path.join(OUT, "scorm.js")):
    open(os.path.join(OUT, "scorm.js"), "w", encoding="utf-8").write("")

open(os.path.join(OUT, "README.txt"), "w", encoding="utf-8").write(f"""SAXOFÓN ALTO: DE CERO A INTERMEDIO — Paquete SCORM 1.2
Autor: Sixto Rodríguez de Sepúlveda

{N} módulos: el instrumento y sus partes, montaje, cuidado y mantenimiento, postura y respiración, embocadura y primer
sonido, primeras notas (Si-La-Sol), notas graves y medias con alteraciones, articulación con la lengua, registro agudo
y llave de octava, lectura y transposición (el saxo en Mi♭), escalas y arpegios, ritmo y fraseo, sonido y afinación,
repertorio y tocar con otros, y jazz, blues e improvisación.

Contenido:
- {len(PIEZAS)} partituras interactivas (notación ABC dibujada con abcjs, licencia MIT, en licencias/): se escuchan con timbre de
  saxo alto y acompañamiento (modos: saxo + acompañamiento, solo saxo, solo acompañamiento) a 50/75/100 %.
  Requiere Internet la primera vez para descargar los sonidos. Las partituras están en TONO ESCRITO (el audio suena en
  tono de concierto, una sexta mayor más grave).
- partituras/Cuaderno_de_partituras.pdf (para imprimir) y partituras/abc/*.abc (fuentes ABC).
- Dibujos de digitaciones del saxo alto y esquemas del instrumento.
- planificacion.html y Planning_6_meses_saxo.pdf: planning de 6 meses (26 semanas, 45 min al día) con diario imprimible.
- ejercicios.html: gimnasio con {N_EJ} ejercicios prácticos (partitura, pasos, tiempo y meta medible).
- Herramientas integradas: metrónomo, entrenadores (lectura, digitaciones, transposición), convertidor de tonalidades,
  tono de referencia, afinador con micrófono y temporizador de práctica.
- examen_final.html: {len(EXAM)} preguntas (aprobado 70 %); preguntas_moodle.gift: {len(QQ)} preguntas.
- Seguimiento SCORM: un SCO por página; el índice de Moodle se marca al avanzar.

Melodías tradicionales de dominio público; el resto de piezas y ejercicios son originales del curso.
Las digitaciones corresponden al saxo alto estándar; algunos modelos tienen digitaciones alternativas.
""")
print("ok", N, "módulos,", len(PIEZAS), "partituras,", N_EJ, "ejercicios,", len(EXAM), "preguntas de examen,", len(QQ), "GIFT")
