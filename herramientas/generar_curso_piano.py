#!/usr/bin/env python3
"""Genera el curso SCORM «Piano: nivel intermedio y avanzado».

Uso (desde la raíz del repositorio):
  python3 herramientas/generar_curso_piano.py cursos/Curso_Piano_Intermedio_Avanzado_SCORM RUTA/abcjs-basic-min.js
  python3 herramientas/scorm_seguimiento.py
  (y para el PDF del cuaderno: node herramientas/piano_pdf.js cursos/Curso_Piano_Intermedio_Avanzado_SCORM)

Partituras: herramientas/piano_partituras.py (notación ABC, dibujadas con abcjs, licencia MIT).
"""
import html, json, math, os, re, shutil, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from piano_partituras import PIEZAS  # noqa: E402
from piano_explicaciones import EXTRA, GLOSARIO, PALABRAS  # noqa: E402

OUT, ABCJS = sys.argv[1], sys.argv[2]
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
for d in ("img", "partituras", "partituras/abc", "licencias"):
    os.makedirs(os.path.join(OUT, d), exist_ok=True)
TITULO = "Piano: nivel intermedio y avanzado"
FOOTER = f"{TITULO} · Material educativo · Creado por: Sixto Rodríguez de Sepúlveda"
N = 14

shutil.copy(ABCJS, os.path.join(OUT, "abcjs-basic-min.js"))
lic = os.path.join(os.path.dirname(ABCJS), "..", "LICENSE.md")
if os.path.exists(lic):
    shutil.copy(lic, os.path.join(OUT, "licencias", "abcjs-LICENSE.md"))
shutil.copy(os.path.join(RAIZ, "cursos", "CiberSeguridad_Avanzada", "img", "logo-centro.png"), os.path.join(OUT, "img", "logo-centro.png"))

# Estilo: base común de los cursos + tema «piano» (azul noche y dorado) -------------------------
base = open(os.path.join(RAIZ, "cursos", "CiberSeguridad_Avanzada", "style.css"), encoding="utf-8").read()
base = base.replace("background:linear-gradient(135deg,#11432b 0%,#1b5e20 100%)", "background:linear-gradient(135deg,#0f1b33 0%,#27375e 100%)")
extra = """
/* Curso de piano */
.shield-icon{background:linear-gradient(45deg,#c9a227,#f3d77a)}
.module h2{border-bottom-color:#c9a227}
.score-box{background:#fff;border:1px solid #e3e6ee;border-radius:14px;padding:14px 14px 10px;margin:22px 0;box-shadow:0 4px 14px rgba(15,27,51,.06)}
.score-box h4{margin:0 0 6px;color:#1e3c72}
.score svg{max-width:100%}
.score-tools{display:flex;flex-wrap:wrap;gap:8px;align-items:center;margin-top:6px}
.score-tools button{background:#1e3c72;color:#fff;border:0;border-radius:20px;padding:7px 14px;cursor:pointer;font-weight:600}
.score-tools button.stop{background:#8a93a3}
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
.beat.on{background:#c9a227}.beat.on.first{background:#e74c3c}
.lect-btns{display:flex;flex-wrap:wrap;gap:8px;margin-top:10px}
.lect-btns button{min-width:62px;padding:10px;border-radius:10px;border:2px solid #1e3c72;background:#fff;font-weight:700;cursor:pointer}
.lect-btns button.ok{background:#4caf50;color:#fff;border-color:#4caf50}.lect-btns button.ko{background:#f44336;color:#fff;border-color:#f44336}
.dl-box{background:#fffaf0;border:2px solid #c9a227;border-radius:12px;padding:14px 18px;margin:18px 0}
.dl-box a{font-weight:700}
.checklist label{display:block;padding:6px 0}.checklist input{width:auto;margin-right:8px}
.palabras{background:#fffaf0;border:2px solid #c9a227;border-radius:14px;padding:14px 18px 10px;margin:4px 0 20px;position:relative}
.palabras p{font-size:1.12em;line-height:1.6;margin:6px 0}
.pal-tag{display:inline-block;background:#c9a227;color:#fff;font-weight:700;font-size:.8em;letter-spacing:.04em;text-transform:uppercase;border-radius:20px;padding:3px 12px}
.practica{background:#eef7ee;border-left:5px solid #4caf50;border-radius:10px;padding:12px 18px;margin:18px 0}
.practica h3{margin-top:4px}
.glosario dt{font-weight:700;color:#1e3c72;margin-top:10px}.glosario dd{margin:2px 0 0 18px;line-height:1.55}
details.glos{border:1px solid #dfe5ef;border-radius:12px;padding:10px 16px;margin:16px 0;background:#f8faff}
details.glos summary{cursor:pointer;font-weight:700;color:#1e3c72;font-size:1.05em}
.module ol{margin:10px 0 14px 28px}.module ol li{line-height:1.7;font-size:1.05em;padding:2px 0}
@media print{.score-tools,.navigation,.progress-container{display:none}}
"""
open(os.path.join(OUT, "style.css"), "w", encoding="utf-8").write(base + extra)

# JavaScript común: dibujar partituras, escucharlas, metrónomo y lectura ------------------------
PIANO_JS = r"""// piano.js · partituras (abcjs), reproducción, metrónomo y entrenador de lectura
var VISUAL = {}, sonando = null;
function dibujarPartituras(){
  if(!window.ABCJS||!window.PARTITURAS)return;
  Object.keys(PARTITURAS).forEach(function(id){
    var el=document.getElementById('p-'+id); if(!el)return;
    VISUAL[id]=ABCJS.renderAbc(el,PARTITURAS[id],{responsive:'resize',add_classes:true,staffwidth:900,wrap:{minSpacing:1.6,maxSpacing:2.6,preferredMeasuresPerLine:4},paddingleft:0,paddingright:0})[0];
  });
}
function msg(id,t){var m=document.getElementById('m-'+id);if(m)m.textContent=t;}
function parar(){ if(sonando){try{sonando.synth.stop();sonando.ctx.close();}catch(e){} msg(sonando.id,''); sonando=null; } }
function tocar(id){
  parar();
  var vis=VISUAL[id]; if(!vis)return;
  if(!ABCJS.synth||!ABCJS.synth.supportsAudio()){msg(id,'Este navegador no permite reproducir sonido.');return;}
  var ctx=new (window.AudioContext||window.webkitAudioContext)();
  var f=parseFloat((document.getElementById('v-'+id)||{value:1}).value);
  var synth=new ABCJS.synth.CreateSynth();
  msg(id,'Cargando sonidos de piano…');
  sonando={synth:synth,ctx:ctx,id:id};
  synth.init({audioContext:ctx,visualObj:vis,millisecondsPerMeasure:vis.millisecondsPerMeasure(vis.getBpm()*f),
              options:{program:0}})
   .then(function(){return synth.prime();})
   .then(function(){ if(sonando&&sonando.synth===synth){synth.start();msg(id,'▶ Sonando…');} })
   .catch(function(){msg(id,'Para escuchar hace falta conexión a Internet: los sonidos del piano se descargan la primera vez.');});
}
// Metrónomo (funciona sin conexión)
var metro={on:false,t:null,n:0,ctx:null};
function metroClick(acento){var c=metro.ctx,o=c.createOscillator(),g=c.createGain();o.frequency.value=acento?1600:1000;
  g.gain.setValueAtTime(0.0001,c.currentTime);g.gain.exponentialRampToValueAtTime(0.6,c.currentTime+0.002);g.gain.exponentialRampToValueAtTime(0.0001,c.currentTime+0.05);
  o.connect(g).connect(c.destination);o.start();o.stop(c.currentTime+0.06);}
function metroPaso(){var tiempos=parseInt(document.getElementById('met-comp').value,10);var i=metro.n%tiempos;
  metroClick(i===0&&tiempos>1);var bs=document.querySelectorAll('#met-beats .beat');
  bs.forEach(function(b,k){b.classList.toggle('on',k===i);b.classList.toggle('first',k===0);});metro.n++;}
function metroPintar(){var tiempos=parseInt(document.getElementById('met-comp').value,10);var c=document.getElementById('met-beats');
  c.innerHTML='';for(var k=0;k<tiempos;k++){var d=document.createElement('div');d.className='beat';c.appendChild(d);}}
function metroToggle(){var b=document.getElementById('met-btn');
  if(metro.on){clearInterval(metro.t);metro.on=false;b.textContent='▶ Iniciar';return;}
  metro.ctx=metro.ctx||new (window.AudioContext||window.webkitAudioContext)();metro.n=0;metroPintar();
  var bpm=parseInt(document.getElementById('met-bpm').value,10);metroPaso();metro.t=setInterval(metroPaso,60000/bpm);metro.on=true;b.textContent='■ Parar';}
function metroBpm(v){document.getElementById('met-val').textContent=v;if(metro.on){metroToggle();metroToggle();}}
// Entrenador de lectura
var LECT={sol:["A,","B,","C","D","E","F","G","A","B","c","d","e","f","g","a","b","c'"],
          fa:["E,,","F,,","G,,","A,,","B,,","C,","D,","E,","F,","G,","A,","B,","C","D","E"]},
    NOMBRE={C:'Do',D:'Re',E:'Mi',F:'Fa',G:'Sol',A:'La',B:'Si'}, lect={nota:null,bien:0,total:0,racha:0};
function lectNueva(){var modo=document.getElementById('lect-clave').value;var clave=modo==='mix'?(Math.random()<.5?'sol':'fa'):modo;
  var lista=LECT[clave],n=lista[Math.floor(Math.random()*lista.length)];lect.nota=n.replace(/[,']/g,'').toUpperCase();
  ABCJS.renderAbc('lect-pent','X:1\nL:1/1\nK:C clef='+(clave==='sol'?'treble':'bass')+'\n'+n+'|',{scale:1.6,staffwidth:150,paddingleft:10});
  document.querySelectorAll('.lect-btns button').forEach(function(b){b.className='';});document.getElementById('lect-fb').textContent='¿Qué nota es?';}
function lectResp(letra,btn){if(!lect.nota)return;lect.total++;var ok=letra===lect.nota;
  if(ok){lect.bien++;lect.racha++;btn.className='ok';}else{lect.racha=0;btn.className='ko';}
  document.getElementById('lect-fb').textContent=(ok?'✅ ¡Bien! ':'❌ Era '+NOMBRE[lect.nota]+'. ')+'Aciertos: '+lect.bien+'/'+lect.total+' · racha: '+lect.racha;
  lect.nota=null;setTimeout(lectNueva,ok?600:1400);}
// Autoevaluaciones
function checkAnswer(btn,ok,id){var p=btn.parentElement;p.querySelectorAll('.option').forEach(function(b){b.classList.remove('correct','incorrect')});
  btn.classList.add(ok?'correct':'incorrect');var fb=document.getElementById('fb-'+id);fb.textContent=ok?'✅ ¡Correcto! '+fb.getAttribute('data-ok'):'❌ No es correcto. Repasa el apartado e inténtalo de nuevo.';}
window.addEventListener('load',dibujarPartituras);
"""
open(os.path.join(OUT, "piano.js"), "w", encoding="utf-8").write(PIANO_JS)

# Dibujos: teclado y círculo de quintas -------------------------------------------------------------
BLANCAS = ["C", "D", "E", "F", "G", "A", "B"]
NEGRAS = {"C": "C#", "D": "D#", "F": "F#", "G": "G#", "A": "A#"}
ESP = {"C": "Do", "D": "Re", "E": "Mi", "F": "Fa", "G": "Sol", "A": "La", "B": "Si"}


def teclado(nombre, titulo, marcas, desde=4, octavas=2, color="#4ecdc4", saltos=(), extra=0):
    """marcas: {'C4': '1', 'F#4': '2'…} → teclas resaltadas con su etiqueta (dedo o nota).
    saltos: [('C4', 'D4', 'T')…] → etiqueta encima del teclado entre dos teclas (tonos y semitonos).
    extra: teclas blancas añadidas tras la última octava (p. ej. 1 para terminar en Do)."""
    W, H, w, h = 26, 120, 16, 74
    top = 30 if saltos else 0
    ancho = (7 * octavas + extra) * W + 2
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {ancho} {H+28+top}" width="{ancho}" height="{H+28+top}" role="img" aria-label="{html.escape(titulo, quote=True)}" font-family="Segoe UI,Tahoma,sans-serif">',
         f'<rect width="{ancho}" height="{H+28+top}" fill="#ffffff"/>', f'<g transform="translate(0,{top})">']
    x = 1
    pos = {}
    blancas = [(b, o) for o in range(desde, desde + octavas) for b in BLANCAS] + [(b, desde + octavas) for b in BLANCAS[:extra]]
    for b, o in blancas:
        k = f"{b}{o}"; pos[k] = x
        on = k in marcas
        s.append(f'<rect x="{x}" y="1" width="{W}" height="{H}" rx="3" fill="{color if on else "#fff"}" stroke="#333"/>')
        if on:
            s.append(f'<text x="{x+W/2}" y="{H-10}" font-size="13" font-weight="700" text-anchor="middle" fill="#0f1b33">{marcas[k]}</text>')
        if b == "C":
            s.append(f'<text x="{x+W/2}" y="{H+20}" font-size="11" text-anchor="middle" fill="#555">Do{o}</text>')
        x += W
    for o in range(desde, desde + octavas):
        for b, n in NEGRAS.items():
            k = f"{n[0]}#{o}"
            bx = pos[f"{b}{o}"] + W - w / 2
            pos[k] = bx - W / 2 + w / 2
            on = k in marcas
            s.append(f'<rect x="{bx}" y="1" width="{w}" height="{h}" rx="2" fill="{"#e67e22" if on else "#1f2937"}"/>')
            if on:
                s.append(f'<text x="{bx+w/2}" y="{h-8}" font-size="11" font-weight="700" text-anchor="middle" fill="#fff">{marcas[k]}</text>')
    s.append("</g>")
    for a, b, txt in saltos:
        xa, xb = pos[a] + W / 2, pos[b] + W / 2
        col = "#c0392b" if txt == "S" else "#1e3c72"
        s.append(f'<path d="M{xa+3} 26 Q{(xa+xb)/2} 6 {xb-3} 26" fill="none" stroke="{col}" stroke-width="1.6"/>')
        s.append(f'<text x="{(xa+xb)/2}" y="14" font-size="12" font-weight="700" text-anchor="middle" fill="{col}">{txt}</text>')
    s.append("</svg>")
    open(os.path.join(OUT, "img", nombre), "w", encoding="utf-8").write("\n".join(s))


teclado("teclado_do_mayor_md.svg", "Escala de Do mayor con la digitación de la mano derecha",
        {"C4": "1", "D4": "2", "E4": "3", "F4": "1", "G4": "2", "A4": "3", "B4": "4", "C5": "1", "D5": "2", "E5": "3", "F5": "1", "G5": "2", "A5": "3", "B5": "4"})
teclado("teclado_re_mayor_md.svg", "Escala de Re mayor con la digitación de la mano derecha",
        {"D4": "1", "E4": "2", "F#4": "3", "G4": "1", "A4": "2", "B4": "3", "C#5": "4", "D5": "5"})
teclado("teclado_acordes.svg", "Do mayor (Do–Mi–Sol) en estado fundamental y Fa mayor en segunda inversión (Do–Fa–La)",
        {"C4": "Do", "E4": "Mi", "G4": "Sol", "C5": "Do", "F5": "Fa", "A5": "La"}, color="#ffd166")
teclado("teclado_rootless.svg", "Voicings sin fundamental: Dm7 (Fa–La–Do–Mi) y G7 (Fa–La–Si–Mi)",
        {"F4": "3", "A4": "5", "C5": "7", "E5": "9"}, color="#a8edea")
teclado("teclado_pasos_do.svg", "Escala de Do mayor con los tonos (T) y semitonos (S) entre sus notas",
        {f"{b}4": ESP[b] for b in BLANCAS} | {"C5": "Do"}, octavas=1, extra=1,
        saltos=[(f"{a}4", f"{b}4" if b != "C" else "C5", t) for a, b, t in zip(BLANCAS, BLANCAS[1:] + ["C"], "TTSTTTS")])
teclado("teclado_3M.svg", "Tercera mayor: de Do a Mi hay cuatro semitonos",
        {"C4": "Do", "C#4": "1", "D4": "2", "D#4": "3", "E4": "Mi 4"}, octavas=1, color="#ffd166")
teclado("teclado_3m.svg", "Tercera menor: de Do a Mi bemol hay tres semitonos",
        {"C4": "Do", "C#4": "1", "D4": "2", "D#4": "3"}, octavas=1, color="#a8edea")
teclado("teclado_blues.svg", "Escala de blues de Do: Do, Mi♭, Fa, Fa♯, Sol, Si♭",
        {"C4": "Do", "D#4": "Mi♭", "F4": "Fa", "F#4": "Fa♯", "G4": "Sol", "A#4": "Si♭", "C5": "Do"}, octavas=1)

MAYORES = ["Do", "Sol", "Re", "La", "Mi", "Si", "Fa♯/Sol♭", "Re♭", "La♭", "Mi♭", "Si♭", "Fa"]
MENORES = ["La m", "Mi m", "Si m", "Fa♯ m", "Do♯ m", "Sol♯ m", "Re♯/Mi♭ m", "Si♭ m", "Fa m", "Do m", "Sol m", "Re m"]
ARM = ["—", "1♯", "2♯", "3♯", "4♯", "5♯", "6♯ / 6♭", "5♭", "4♭", "3♭", "2♭", "1♭"]
c = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 440 440" width="440" height="440" role="img" aria-label="Círculo de quintas con tonalidades mayores, menores relativas y armaduras" font-family="Segoe UI,Tahoma,sans-serif">',
     '<rect width="440" height="440" fill="#fff"/><circle cx="220" cy="220" r="200" fill="#eef2fb" stroke="#1e3c72" stroke-width="2"/>',
     '<circle cx="220" cy="220" r="130" fill="#fffaf0" stroke="#c9a227" stroke-width="2"/><circle cx="220" cy="220" r="72" fill="#1e3c72"/>',
     '<text x="220" y="215" font-size="15" fill="#fff" font-weight="700" text-anchor="middle">Círculo</text><text x="220" y="234" font-size="15" fill="#fff" font-weight="700" text-anchor="middle">de quintas</text>']
for i in range(12):
    a = math.radians(i * 30 - 90)
    for r, txt, size, col in ((172, MAYORES[i], 16, "#1e3c72"), (103, MENORES[i], 12, "#8a5a00"), (148, ARM[i], 11, "#555")):
        x, y = 220 + r * math.cos(a), 220 + r * math.sin(a) + 5
        c.append(f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" font-weight="700" fill="{col}" text-anchor="middle">{txt}</text>')
    x1, y1 = 220 + 130 * math.cos(a + math.radians(15)), 220 + 130 * math.sin(a + math.radians(15))
    x2, y2 = 220 + 200 * math.cos(a + math.radians(15)), 220 + 200 * math.sin(a + math.radians(15))
    c.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="#c7cfe0"/>')
c.append("</svg>")
open(os.path.join(OUT, "img", "circulo_quintas.svg"), "w", encoding="utf-8").write("\n".join(c))

# Utilidades de página ----------------------------------------------------------------------------


def fig(img, alt, cap):
    return f'<div class="figure"><img src="img/{img}" alt="{html.escape(alt, quote=True)}"><div class="figure-caption">{cap}</div></div>'


def kp(items, ico):
    return '<ul class="key-points">' + "".join(f"<li>{ico} <span>{i}</span></li>" for i in items) + "</ul>"


def tabla(cab, filas):
    return ('<div class="tabla-wrap"><table class="tabla"><tr>' + "".join(f"<th>{x}</th>" for x in cab) + "</tr>"
            + "".join("<tr>" + "".join(f"<td>{x}</td>" for x in f) + "</tr>" for f in filas) + "</table></div>")


def quiz(qid, q, opts, ok, why):
    b = "".join(f'<button class="option" onclick="checkAnswer(this,{str(j == ok).lower()},\'{qid}\')">{chr(65+j)}. {o}</button>' for j, o in enumerate(opts))
    return f'<div class="quiz"><h4>🧩 {q}</h4><div class="options">{b}</div><p class="feedback" id="fb-{qid}" data-ok="{html.escape(why, quote=True)}"></p></div>'


def actividad(t, txt, ph):
    return f'<div class="activity"><h3>🎹 {t}</h3><p>{txt}</p><textarea placeholder="{ph}"></textarea></div>'


def imslp(obra):
    return f'<a href="https://imslp.org/index.php?search={obra.replace(" ", "+")}" target="_blank" rel="noopener">IMSLP ↗</a>'


def partitura(clave):
    p = PIEZAS[clave]
    return (f'<div class="score-box"><h4>🎼 {p["titulo"]}</h4><div class="score" id="p-{clave}"></div>'
            f'<div class="score-tools"><button onclick="tocar(\'{clave}\')">▶ Escuchar</button><button class="stop" onclick="parar()">■ Parar</button>'
            f'<label>Velocidad <select id="v-{clave}"><option value="0.5">50 %</option><option value="0.75">75 %</option><option value="1" selected>100 %</option></select></label>'
            f'<span class="score-msg" id="m-{clave}"></span></div>'
            + (f'<p class="score-note">{p["nota"]}</p>' if p["nota"] else "") + "</div>")


def pagina(n, icono, titulo, sub, cuerpo):
    prev = "index.html" if n == 1 else f"modulo{n-1}.html"
    nxt = "examen_final.html" if n == N else f"modulo{n+1}.html"
    lbl = "Ir al examen final 🏁" if n == N else "Siguiente módulo ➡️"
    nivel = "Nivel intermedio" if n <= 8 else "Nivel avanzado"
    # Cada página lleva solo las partituras que muestra
    datos = json.dumps({k: PIEZAS[k]["abc"] for k in re.findall(r'id="p-(\w+)"', cuerpo)}, ensure_ascii=False)
    return f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Módulo {n}: {titulo}</title>
<link rel="stylesheet" href="style.css">
</head>
<body>
<div class="container">
  <div class="header">
    <h1><span class="shield-icon">{icono}</span>Módulo {n}: {titulo}</h1>
    <img src="img/logo-centro.png" class="logo-centro" alt="Logotipo del centro">
    <p>{sub}</p>
  </div>
  <div class="progress-container">
    <div class="progress-bar"><div class="progress-fill" style="width:{round(n*100/(N+1))}%"></div></div>
    <div class="progress-text">Piano · {nivel} · Módulo {n} de {N}</div>
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
<script>var PARTITURAS={datos};</script>
<script src="abcjs-basic-min.js"></script>
<script src="piano.js"></script>
<script src="scorm.js"></script>
</body>
</html>
"""


DESCARGA = '<div class="dl-box">📥 <b>Partituras para imprimir:</b> todas las del curso están en el <a href="partituras/Cuaderno_de_partituras.pdf" target="_blank" rel="noopener">Cuaderno de partituras (PDF)</a>.</div>'

M = []
# 1 ------------------------------------------------------------------------------------------------
M.append(("⏱️", "Cómo estudiar: método, rutina y metrónomo", "Estudiar mejor rinde más que estudiar más horas.", f"""
      <h2>Bienvenido/a al nivel intermedio</h2>
      <p>En este nivel ya lees partituras sencillas y tocas con las dos manos. Lo que marca la diferencia a partir de aquí no es cuántas horas pasas al piano, sino <b>cómo</b> las usas. Este módulo te da un método que aplicarás en todo el curso.</p>
      <h3>1. La práctica deliberada</h3>
      {kp(["<b>Objetivo concreto por sesión:</b> «compases 9-12 a negra = 72 sin errores», no «estudiar la pieza».",
           "<b>Lento y sin errores:</b> el cerebro aprende lo que repites, también los errores. Si fallas, el tempo es demasiado rápido.",
           "<b>Fragmentos cortos:</b> 1–2 compases, con la primera nota del siguiente compás como «puente».",
           "<b>Manos separadas</b> en los pasajes difíciles; después juntas, aún más lento.",
           "<b>Subida gradual con metrónomo:</b> de 4 en 4 o de 5 en 5 bpm cuando consigas 3 repeticiones limpias seguidas.",
           "<b>Descansos:</b> 5 minutos cada 25–30. La concentración rinde más que la resistencia."], "🎯")}
      <h3>2. Una rutina de 60 minutos</h3>
      {tabla(["Bloque", "Tiempo", "Contenido"], [["Calentamiento", "10 min", "Escalas y arpegios del día (módulos 3 y 4)"], ["Técnica", "10 min", "Un ejercicio técnico concreto (octavas, terceras, polirritmia…)"], ["Repertorio: trabajo lento", "25 min", "Fragmentos difíciles con metrónomo"], ["Repertorio: pasada completa", "10 min", "Tocar seguido sin parar, como en un concierto"], ["Lectura a primera vista", "5 min", "Algo nuevo y fácil, sin detenerte"]])}
      <h3>3. Tu metrónomo</h3>
      <p>Este metrónomo funciona dentro del curso, también sin conexión. El primer tiempo de cada compás suena más agudo.</p>
      <div class="activity"><div class="metro">
        <button class="btn" id="met-btn" onclick="metroToggle()">▶ Iniciar</button>
        <label>Tempo: <b id="met-val">72</b> bpm <input id="met-bpm" type="range" min="40" max="208" value="72" oninput="metroBpm(this.value)"></label>
        <label>Compás: <select id="met-comp" onchange="metroPintar()"><option value="2">2/4</option><option value="3">3/4</option><option value="4" selected>4/4</option><option value="6">6/8 (en corcheas)</option></select></label>
      </div><div class="beats" id="met-beats"></div></div>
      <div class="box tip"><b>Truco:</b> pon el metrónomo a la mitad de la velocidad final y cuenta una nota por clic. Cuando sea fácil, sube 4 bpm. Al llegar al tempo final, bájalo otra vez y deja que el clic marque solo el tiempo fuerte.</div>
      {quiz("m1a", "Fallas siempre en el mismo compás. ¿Qué haces?", ["Tocar la pieza entera muchas veces seguidas", "Aislar ese compás, bajar el tempo hasta tocarlo sin errores y subir poco a poco", "Tocarlo más deprisa para pasarlo rápido"], 1, "Aislar, ralentizar y subir de forma gradual es la base de la práctica deliberada.")}
      {quiz("m1b", "¿Cuándo subes el metrónomo?", ["Cuando lo toco tres veces seguidas sin errores", "Cada cinco minutos, aunque falle", "Nunca: hay que tocar siempre a tempo"], 0, "Solo se sube cuando el tempo actual está consolidado.")}
      {actividad("Tu plan semanal", "Escribe tu objetivo concreto para esta semana y cómo repartirás tu tiempo de estudio.", "Lunes: escalas de Do y Sol… Objetivo: …")}
      <div class="summary-box"><b>Resumen:</b> objetivos concretos, lento sin errores, fragmentos cortos, metrónomo gradual y una pasada completa al final.</div>
"""))
# 2 ------------------------------------------------------------------------------------------------
M.append(("👁️", "Lectura avanzada: claves, ritmos y compases", "Leer con fluidez libera la cabeza para pensar en la música.", f"""
      <h2>Leer más rápido y con más seguridad</h2>
      <h3>1. Notas de referencia</h3>
      <p>No leas nota a nota contando líneas: memoriza unas pocas notas «faro» y calcula las demás por intervalos.</p>
      {tabla(["Clave", "Notas faro", "Truco"], [["Sol (M.D.)", "Do4 (1.ª línea adicional abajo), Sol4 (2.ª línea), Do5 (3.er espacio), Sol5 (encima del pentagrama)", "Las líneas adicionales de arriba: La5, Do6, Mi6…"], ["Fa (M.I.)", "Fa3 (4.ª línea), Do3 (2.º espacio), Do4 (1.ª línea adicional arriba), Sol2 (1.ª línea)", "Do4 está a la misma distancia del pentagrama en las dos claves"]])}
      <h3>2. Entrenador de lectura</h3>
      <p>Aparece una nota en clave de Sol o de Fa, incluidas las líneas adicionales. Responde lo más rápido que puedas.</p>
      <div class="activity">
        <label>Clave: <select id="lect-clave" onchange="lectNueva()"><option value="mix">Sol y Fa mezcladas</option><option value="sol">Solo clave de Sol</option><option value="fa">Solo clave de Fa</option></select></label>
        <div id="lect-pent" style="max-width:260px"></div>
        <p class="feedback" id="lect-fb">Pulsa «Empezar».</p>
        <div class="lect-btns">{''.join(f'<button onclick="lectResp(\'{l}\',this)">{ESP[l]}</button>' for l in BLANCAS)}</div>
        <button class="btn" onclick="lectNueva()">Empezar / otra nota</button>
      </div>
      <h3>3. Ritmos que aparecen a partir de ahora</h3>
      {tabla(["Elemento", "Qué es", "Cómo contarlo"], [["Tresillo", "Tres notas en el tiempo de dos iguales", "«tri-o-la» por pulso"], ["Síncopa", "Acento en la parte débil, prolongado a la fuerte", "Cuenta las subdivisiones en voz alta"], ["Puntillo doble", "Añade la mitad y la cuarta parte del valor", "Negra con doble puntillo = negra + corchea + semicorchea"], ["Compás compuesto (6/8, 9/8, 12/8)", "El pulso es una negra con puntillo dividida en 3 corcheas", "6/8 se siente en <b>2</b> pulsos: «1-2-3, 4-5-6»"]])}
      <div class="box tip"><b>Lectura a primera vista:</b> antes de tocar, 30 segundos de «escaneo»: tonalidad, compás, notas más agudas y más graves, ritmos raros y cambios de clave. Después, toca sin parar aunque falles.</div>
      {quiz("m2a", "¿Cuántos pulsos se sienten en un compás de 6/8 a velocidad normal?", ["6", "2", "3"], 1, "6/8 tiene 2 pulsos de negra con puntillo, cada uno dividido en 3 corcheas.")}
      {quiz("m2b", "Un tresillo de corcheas ocupa el tiempo de…", ["Tres corcheas", "Dos corcheas (una negra)", "Una corchea"], 1, "Son tres notas que se reparten el tiempo de dos.")}
      <div class="summary-box"><b>Resumen:</b> notas faro + intervalos, entrenamiento diario de lectura y control de los ritmos compuestos.</div>
"""))
# 3 ------------------------------------------------------------------------------------------------
M.append(("🎼", "Escalas en todas las tonalidades", "La gimnasia diaria del pianista… y el mapa de la armonía.", f"""
      <h2>Escalas: técnica y teoría a la vez</h2>
      <p>Las escalas desarrollan la igualdad de los dedos y el paso del pulgar, y te enseñan las tonalidades. El <b>círculo de quintas</b> las ordena: cada paso a la derecha añade un sostenido y cada paso a la izquierda, un bemol.</p>
      {fig("circulo_quintas.svg", "Círculo de quintas", "Tonalidades mayores (exterior), relativas menores (interior) y número de alteraciones de la armadura.")}
      <h3>1. Do mayor, la referencia</h3>
      {fig("teclado_do_mayor_md.svg", "Teclado con la escala de Do mayor y su digitación", "Mano derecha: 1-2-3, pasa el pulgar, 1-2-3-4, pasa el pulgar… y el 5 solo en la nota final.")}
      {partitura("escala_do")}
      <h3>2. Reglas de digitación</h3>
      {kp(["El <b>pulgar no toca teclas negras</b> (salvo casos muy concretos).", "Los dedos se agrupan en <b>1-2-3</b> y <b>1-2-3-4</b>: los grupos se ajustan para que los dedos largos caigan en las teclas negras.", "El pulgar pasa por debajo <b>sin mover el codo</b>; prepara el paso girando ligeramente el antebrazo.", "Estudia siempre <b>manos separadas primero</b>: los «pasos de pulgar» de cada mano no coinciden."], "🖐️")}
      {fig("teclado_re_mayor_md.svg", "Teclado con la escala de Re mayor y su digitación", "Re mayor: misma digitación que Do (1-2-3-1-2-3-4-5) porque Fa♯ y Do♯ caen en dedos largos.")}
      <h3>3. Digitaciones estándar (una octava)</h3>
      {tabla(["Tonalidad", "Mano derecha", "Mano izquierda"], [
        ["Do, Sol, Re, La, Mi", "1 2 3 1 2 3 4 5", "5 4 3 2 1 3 2 1"],
        ["Si", "1 2 3 1 2 3 4 5", "4 3 2 1 4 3 2 1"],
        ["Fa", "1 2 3 4 1 2 3 4", "5 4 3 2 1 3 2 1"],
        ["Si♭", "4 1 2 3 1 2 3 4", "3 2 1 4 3 2 1 3"],
        ["Mi♭", "3 1 2 3 4 1 2 3", "3 2 1 4 3 2 1 3"],
        ["La♭", "3 4 1 2 3 1 2 3", "3 2 1 4 3 2 1 3"],
        ["Re♭", "2 3 1 2 3 4 1 2", "3 2 1 4 3 2 1 3"],
        ["Fa♯ / Sol♭", "2 3 4 1 2 3 1 2", "4 3 2 1 3 2 1 4"]])}
      <p class="small">Digitaciones de uso habitual en los métodos tradicionales; algunas ediciones proponen variantes.</p>
      <h3>4. Escalas menores</h3>
      {tabla(["Tipo", "Fórmula (desde La)", "Rasgo"], [["Natural", "La Si Do Re Mi Fa Sol La", "Misma armadura que su relativa mayor (Do)"], ["Armónica", "La Si Do Re Mi Fa <b>Sol♯</b> La", "7.º grado elevado: crea la sensible"], ["Melódica", "Sube con <b>Fa♯ y Sol♯</b>; baja como la natural", "Suaviza el salto de la armónica"]])}
      {partitura("escala_lam")}
      {quiz("m3a", "¿Qué alteración caracteriza a la escala de La menor armónica?", ["Fa♯", "Sol♯", "Si♭"], 1, "La menor armónica eleva el 7.º grado: Sol♯.")}
      {quiz("m3b", "¿Cuántas alteraciones tiene la armadura de Re mayor?", ["Dos sostenidos", "Un bemol", "Tres sostenidos"], 0, "Re mayor lleva Fa♯ y Do♯.")}
      {DESCARGA}
      <div class="summary-box"><b>Resumen:</b> círculo de quintas, pulgar fuera de las teclas negras, manos separadas primero y las tres formas de la escala menor.</div>
"""))
# 4 ------------------------------------------------------------------------------------------------
M.append(("🌊", "Arpegios, acordes e inversiones", "Los acordes, desplegados o en bloque, son el esqueleto de casi toda la música.", f"""
      <h2>De la escala al acorde</h2>
      <p>Un <b>acorde tríada</b> se forma apilando terceras: fundamental, tercera y quinta. Según la tercera sea mayor o menor obtienes un acorde mayor o menor.</p>
      {tabla(["Tipo", "Intervalos desde la fundamental", "Ejemplo en Do", "Cifrado"], [["Mayor", "3.ª mayor + 5.ª justa", "Do–Mi–Sol", "C"], ["Menor", "3.ª menor + 5.ª justa", "Do–Mi♭–Sol", "Cm"], ["Disminuido", "3.ª menor + 5.ª disminuida", "Do–Mi♭–Sol♭", "Cdim / C°"], ["Aumentado", "3.ª mayor + 5.ª aumentada", "Do–Mi–Sol♯", "Caug / C+"]])}
      <h3>1. Inversiones</h3>
      <p>Si la nota más grave no es la fundamental, el acorde está <b>invertido</b>. Las inversiones permiten enlazar acordes moviendo poco las manos.</p>
      {fig("teclado_acordes.svg", "Teclado con Do mayor y Fa mayor en segunda inversión", "Do mayor en estado fundamental (izquierda) y Fa mayor en 2.ª inversión, Do–Fa–La (derecha).")}
      {partitura("inversiones")}
      <h3>2. Arpegios</h3>
      {kp(["Digitación de Do mayor (M.D., dos octavas): <b>1-2-3-1-2-3-5</b>; (M.I.): <b>5-4-2-1-4-2-1</b>.", "La muñeca y el antebrazo <b>acompañan lateralmente</b>: el pulgar no «se estira» por debajo.", "Practica primero el arpegio <b>en bloque</b> (acorde plaqué) para que la mano aprenda la forma."], "🌊")}
      {partitura("arpegio_do")}
      {quiz("m4a", "¿Qué notas forman la 1.ª inversión de Do mayor?", ["Do–Mi–Sol", "Mi–Sol–Do", "Sol–Do–Mi"], 1, "En la 1.ª inversión la tercera (Mi) está en el bajo.")}
      {quiz("m4b", "¿Qué tipo de acorde es Re–Fa–La?", ["Mayor", "Menor", "Disminuido"], 1, "Re–Fa es una 3.ª menor y Re–La una 5.ª justa: Re menor.")}
      {actividad("Inversiones en todas las tonalidades", "Toca la tríada de cada tonalidad del círculo de quintas en estado fundamental, 1.ª y 2.ª inversión, subiendo y bajando. Anota las que te cuesten.", "Me cuestan: …")}
      <div class="summary-box"><b>Resumen:</b> cuatro tipos de tríada, tres posiciones y arpegios con el brazo acompañando.</div>
"""))
# 5 ------------------------------------------------------------------------------------------------
M.append(("🧭", "Armonía funcional aplicada al teclado", "Entender por qué suena lo que suena.", f"""
      <h2>Grados y funciones</h2>
      <p>Cada acorde de una tonalidad tiene una <b>función</b>: reposo, alejamiento o tensión que pide resolver.</p>
      {tabla(["Grado (Do mayor)", "Acorde", "Función"], [["I", "C (Do mayor)", "<b>Tónica</b>: reposo"], ["ii", "Dm (Re menor)", "Subdominante"], ["iii", "Em (Mi menor)", "Tónica (débil)"], ["IV", "F (Fa mayor)", "<b>Subdominante</b>: alejamiento"], ["V / V7", "G / G7 (Sol 7)", "<b>Dominante</b>: tensión que resuelve en I"], ["vi", "Am (La menor)", "Tónica relativa"], ["vii°", "Bdim (Si disminuido)", "Dominante"]])}
      <h3>1. Cadencias</h3>
      {kp(["<b>Perfecta (auténtica):</b> V–I. Conclusión total.", "<b>Plagal:</b> IV–I. El «amén».", "<b>Semicadencia:</b> termina en V. Suspense, pide continuación.", "<b>Rota (de engaño):</b> V–vi. Sorpresa: esperas I y suena vi."], "🎯")}
      {partitura("cadencia")}
      <h3>2. Conducción de voces</h3>
      {kp(["Mantén las <b>notas comunes</b> entre acordes.", "Mueve las demás por el <b>camino más corto</b> (grado conjunto).", "La <b>sensible</b> (Si en Do mayor) sube a la tónica.", "La <b>7.ª del acorde</b> de dominante (Fa en Sol7) baja por grado."], "🔗")}
      <h3>3. Cifrado americano</h3>
      <p>Letras: A = La, B = Si, C = Do, D = Re, E = Mi, F = Fa, G = Sol. «m» = menor; «7» = séptima menor; «maj7» = séptima mayor; «/» = bajo distinto (C/E = Do con Mi en el bajo).</p>
      {quiz("m5a", "En Do mayor, ¿cuál es el acorde de dominante con séptima (V7)?", ["Fa mayor", "Sol7 (Sol–Si–Re–Fa)", "La menor"], 1, "El V grado de Do es Sol; con la 7.ª: Sol–Si–Re–Fa.")}
      {quiz("m5b", "Esperas el acorde de Do al final y suena La menor. ¿Qué cadencia es?", ["Perfecta", "Plagal", "Rota (de engaño)"], 2, "V–vi es la cadencia rota.")}
      {actividad("Transporte", "Toca la cadencia I–IV–V7–I del ejemplo en Sol mayor y en Fa mayor. Escribe los acordes que usas.", "Sol mayor: G – C – D7 – G …")}
      <div class="summary-box"><b>Resumen:</b> tónica, subdominante y dominante; cadencias y conducción de voces suave.</div>
"""))
# 6 ------------------------------------------------------------------------------------------------
M.append(("🤲", "Independencia de manos y acompañamientos", "Que cada mano cuente su propia historia.", f"""
      <h2>Dos manos, dos papeles</h2>
      <p>En casi toda la música para piano una mano lleva la <b>melodía</b> y la otra el <b>acompañamiento</b>. La clave es que la melodía «cante» por encima: la mano del acompañamiento toca más suave.</p>
      <h3>1. Patrones de acompañamiento</h3>
      {tabla(["Patrón", "Estilo", "Esquema (Do mayor)"], [["Bajo Alberti", "Clasicismo (Mozart, Haydn, Clementi)", "Do–Sol–Mi–Sol"], ["Arpegio abierto", "Romanticismo", "Do–Sol–Mi'–Sol (amplio, con pedal)"], ["Vals (bajo–acorde–acorde)", "Danza 3/4", "Do · [Mi Sol] · [Mi Sol]"], ["Stride", "Jazz clásico, ragtime", "Bajo grave en 1 y 3; acorde medio en 2 y 4"], ["Boogie", "Blues, rock and roll", "Do–Sol, Do–La, Do–Si♭, Do–La (módulo 12)"]])}
      {partitura("alberti")}
      <h3>2. Cómo trabajar la independencia</h3>
      <ol class="steps">
        <li>Cada mano por separado, hasta que sea automática.</li>
        <li>Juntas, muy lento, <b>compás a compás</b>.</li>
        <li>Toca el acompañamiento <i>piano</i> y la melodía <i>mezzoforte</i>: el balance se entrena aparte.</li>
        <li>Canta la melodía mientras tocas solo el acompañamiento.</li>
      </ol>
      {quiz("m6a", "¿Qué es el bajo Alberti?", ["Un acompañamiento que arpegia el acorde en el orden grave–agudo–medio–agudo", "Un pedal que se mantiene toda la obra", "Una escala cromática en la mano izquierda"], 0, "Por ejemplo, Do–Sol–Mi–Sol.")}
      {quiz("m6b", "La melodía queda tapada por el acompañamiento. ¿Qué haces?", ["Tocar el acompañamiento más suave y dar más peso a la melodía", "Tocar todo más fuerte", "Quitar el acompañamiento"], 0, "El balance entre manos se trabaja de forma consciente.")}
      <div class="summary-box"><b>Resumen:</b> melodía que canta, acompañamiento suave y trabajo por capas.</div>
"""))
# 7 ------------------------------------------------------------------------------------------------
M.append(("🦶", "El pedal", "El pedal es parte del sonido, no un efecto añadido.", f"""
      <h2>Los tres pedales</h2>
      {tabla(["Pedal", "Qué hace", "Uso"], [["Derecho (de resonancia)", "Levanta todos los apagadores: las cuerdas siguen sonando", "Legato, color y resonancia"], ["Central (sostenuto)", "Mantiene solo las notas que estaban pulsadas al pisarlo (en pianos de cola y algunos verticales)", "Bajos largos sin emborronar el resto"], ["Izquierdo (una corda)", "Suaviza el sonido y cambia el timbre", "Pasajes <i>pp</i> o de color especial"]])}
      <h3>1. Pedal sincopado (legato)</h3>
      <p>Es la técnica básica: el pedal se cambia <b>después</b> de tocar el acorde nuevo, nunca a la vez.</p>
      <ol class="steps"><li>Toca el acorde con el pedal pisado.</li><li>Al tocar el acorde siguiente, <b>levanta</b> el pedal en ese instante…</li><li>…y <b>vuelve a pisarlo</b> justo después, con el acorde nuevo ya sonando.</li></ol>
      {partitura("pedal")}
      <h3>2. Pedal según el estilo</h3>
      {kp(["<b>Barroco:</b> muy poco o nada (el clave no tenía pedal). La claridad viene de los dedos.", "<b>Clásico:</b> breve, para unir y dar color; nunca para tapar las escalas.", "<b>Romántico:</b> abundante y cambiado con cada armonía.", "<b>Impresionismo:</b> medios pedales y mezclas de armonías buscadas."], "🎨")}
      <div class="box tip"><b>Escucha antes que la vista:</b> si el sonido se emborrona, cambia el pedal; si se corta, cámbialo más tarde. Las marcas de la partitura son una guía, el oído decide.</div>
      {quiz("m7a", "¿Cuándo se cambia el pedal en el pedal sincopado?", ["Antes de tocar el acorde nuevo", "Justo al tocar el acorde nuevo: se levanta y se vuelve a pisar inmediatamente", "Solo al final de la obra"], 1, "Así los acordes se enlazan sin mezclarse.")}
      {quiz("m7b", "¿Qué pedal sostiene solo las notas que estaban pulsadas al pisarlo?", ["El izquierdo", "El central (sostenuto)", "El derecho"], 1, "El sostenuto mantiene solo esas notas.")}
      <div class="summary-box"><b>Resumen:</b> pedal sincopado, adaptado al estilo y controlado por el oído.</div>
"""))
# 8 ------------------------------------------------------------------------------------------------
M.append(("📜", "Repertorio intermedio: analizar antes de tocar", "Dos obras clásicas para aplicar todo lo aprendido.", f"""
      <h2>Estudiar una obra como un profesional</h2>
      <ol class="steps"><li><b>Escucha</b> varias versiones grabadas.</li><li><b>Analiza:</b> tonalidad, forma (secciones que se repiten), armonía y pasajes difíciles.</li><li><b>Decide la digitación</b> y escríbela antes de tocar.</li><li><b>Trabaja por secciones</b>, empezando por la más difícil.</li><li>Une las secciones y haz <b>pasadas completas</b>.</li></ol>
      <h3>1. J. S. Bach · Preludio en Do mayor, BWV 846</h3>
      <p>Primera pieza de <i>El clave bien temperado</i> (libro I, 1722). Toda la obra es un mismo patrón de arpegio sobre una sucesión de acordes: es perfecta para practicar <b>análisis armónico</b> y <b>regularidad</b>.</p>
      {partitura("bach846")}
      {kp(["Escribe el acorde de cada compás de toda la obra (está en IMSLP) y toca la reducción en bloques.", "Mantén un sonido igual y <i>legato</i> sin pedal; si lo usas, cambio en cada compás.", "Obra completa: " + imslp("Bach Well-Tempered Clavier Book 1")], "🎼")}
      <h3>2. L. van Beethoven · <i>Para Elisa</i>, WoO 59</h3>
      <p>Rondó en La menor (forma A–B–A–C–A). El tema A requiere un <b>legato</b> fluido entre las dos manos: la mano izquierda continúa el arpegio que empieza la derecha.</p>
      {partitura("elise")}
      {kp(["Las semicorcheas Mi–Re♯ deben sonar sin acentos: relaja el 4.º y 5.º dedo.", "Pedal: uno por compás en los arpegios; levántalo en el compás de la melodía sola.", "Obra completa: " + imslp("Für Elise Beethoven")], "🎼")}
      {quiz("m8a", "El Preludio en Do mayor BWV 846 pertenece a…", ["Las Variaciones Goldberg", "El clave bien temperado, libro I", "Las Invenciones a dos voces"], 1, "Es el primer preludio del libro I.")}
      {quiz("m8b", "¿En qué compás está escrita «Para Elisa»?", ["3/8", "4/4", "6/8"], 0, "Está en 3/8, con anacrusa de dos semicorcheas.")}
      {actividad("Análisis", "Escribe el acorde de los compases 5 a 11 del Preludio BWV 846 (descárgalo de IMSLP).", "Compás 5: …")}
      {DESCARGA}
      <div class="summary-box"><b>Resumen:</b> escuchar, analizar, digitar, trabajar por secciones y unir.</div>
"""))
# 9 ------------------------------------------------------------------------------------------------
M.append(("💪", "Técnica avanzada: octavas, terceras y adornos", "Potencia y agilidad sin tensión.", f"""
      <h2>Comienza el nivel avanzado</h2>
      <div class="alert-box"><b>Salud primero:</b> la técnica avanzada exige fuerza, pero nunca dolor. Si notas molestia en la muñeca, el antebrazo o la espalda, para. Calienta antes, estudia en sesiones cortas y consulta a un profesional si el dolor persiste.</div>
      <h3>1. Octavas</h3>
      {kp(["Pulgar abajo; arriba el <b>5.º en teclas blancas y el 4.º en negras</b> (en octavas legato se alternan 3-4-5).", "El movimiento sale de la <b>muñeca</b>, con el brazo sosteniendo el peso y la mano como un «arco» firme.", "Empieza a tempo lento y forte suave; la velocidad llega con la relajación."], "🖐️")}
      {partitura("octavas")}
      <h3>2. Terceras dobles</h3>
      {partitura("terceras")}
      <h3>3. Adornos</h3>
      {tabla(["Adorno", "Signo", "Realización habitual (Barroco–Clasicismo)"], [["Trino", "tr", "Alterna la nota con la superior, empezando por la superior"], ["Mordente", "Signo con raya vertical", "Nota real – inferior – real"], ["Mordente superior (pralltriller)", "Signo sin raya", "Nota real – superior – real"], ["Grupeto", "~ tumbado", "Superior – real – inferior – real"], ["Apoyatura", "Nota pequeña", "Toma parte del valor de la nota principal"]])}
      {partitura("adornos")}
      <p class="small">En el Romanticismo los trinos suelen empezar por la nota real; consulta siempre una edición crítica.</p>
      {quiz("m9a", "En el Barroco y el Clasicismo, ¿por qué nota empieza normalmente el trino?", ["Por la nota real", "Por la nota superior", "Por la nota inferior"], 1, "Empieza por la superior, que actúa como apoyatura.")}
      {quiz("m9b", "Octavas en la mano derecha: ¿qué dedo va arriba en las teclas negras?", ["El 4.º", "El 2.º", "El pulgar"], 0, "5.º en blancas y 4.º en negras.")}
      <div class="summary-box"><b>Resumen:</b> muñeca libre en las octavas, terceras por capas y adornos según el estilo.</div>
"""))
# 10 ---------------------------------------------------------------------------------------------
M.append(("🔀", "Polirritmia: 3 contra 2 y 4 contra 3", "Dos ritmos a la vez, cada uno en su mano.", f"""
      <h2>Contar en una cuadrícula común</h2>
      <p>Para tocar 3 notas en una mano contra 2 en la otra, piensa en el <b>mínimo común múltiplo</b>: 6 subdivisiones. Cada mano toca en sus puntos y solo coinciden en el primero.</p>
      {tabla(["Subdivisión", "1", "2", "3", "4", "5", "6"], [["Mano derecha (3)", "●", "", "●", "", "●", ""], ["Mano izquierda (2)", "●", "", "", "●", "", ""], ["Resultado", "juntas", "", "M.D.", "M.I.", "M.D.", ""]])}
      <p>Dicho en voz alta: «<b>jun</b>-tas, de-re-cha, iz-quier-da, de-re-cha». Empieza muy lento, sobre la mesa, dando palmadas.</p>
      {partitura("poli32")}
      <h3>4 contra 3</h3>
      <p>Cuadrícula de <b>12</b>: la mano de 4 toca en 1-4-7-10 y la de 3 en 1-5-9.</p>
      {partitura("poli43")}
      <div class="box tip"><b>En el repertorio:</b> el 3 contra 2 aparece constantemente en Chopin (por ejemplo, la <i>Fantasía-Impromptu</i>, que usa 4 contra 3) y en Debussy. Cuando lo domines, deja de contar: siente la mano lenta como el pulso y la rápida «fluyendo» por encima.</div>
      {quiz("m10a", "¿Cuántas subdivisiones tiene la cuadrícula común de 3 contra 2?", ["5", "6", "12"], 1, "El mínimo común múltiplo de 3 y 2 es 6.")}
      {quiz("m10b", "En 3 contra 2, ¿en qué subdivisiones coinciden las dos manos?", ["En todas", "Solo en la primera", "En la 1.ª y la 4.ª"], 1, "Solo coinciden al principio de cada grupo.")}
      <div class="summary-box"><b>Resumen:</b> cuadrícula común, practicar fuera del piano y, al final, sentirlo sin contar.</div>
"""))
# 11 ---------------------------------------------------------------------------------------------
M.append(("🎷", "Armonía avanzada: séptimas, tensiones y voicings", "El lenguaje del jazz y de la música moderna.", f"""
      <h2>Acordes de cuatro notas</h2>
      {tabla(["Tipo", "Fórmula", "En Do", "Cifrado"], [["Séptima mayor", "1 – 3 – 5 – 7", "Do–Mi–Sol–Si", "Cmaj7 / CΔ"], ["Séptima de dominante", "1 – 3 – 5 – ♭7", "Do–Mi–Sol–Si♭", "C7"], ["Menor séptima", "1 – ♭3 – 5 – ♭7", "Do–Mi♭–Sol–Si♭", "Cm7"], ["Semidisminuido", "1 – ♭3 – ♭5 – ♭7", "Do–Mi♭–Sol♭–Si♭", "Cm7♭5 / Cø"], ["Disminuido", "1 – ♭3 – ♭5 – ♭♭7", "Do–Mi♭–Sol♭–Si♭♭ (La)", "C°7"]])}
      <h3>1. Tensiones</h3>
      <p>Por encima de la 7.ª se añaden <b>tensiones</b>: 9.ª, 11.ª y 13.ª (las notas 2, 4 y 6 una octava más arriba). Dan el color «moderno» a los acordes.</p>
      <h3>2. Voicings sin fundamental (rootless)</h3>
      <p>En un grupo, el bajista toca la fundamental; el pianista toca 3.ª, 7.ª y tensiones. Así el acorde suena lleno y las manos casi no se mueven.</p>
      {fig("teclado_rootless.svg", "Voicing sin fundamental de Dm7", "Dm7 sin fundamental: Fa–La–Do–Mi (3.ª, 5.ª, 7.ª y 9.ª). Para pasar a G7 solo baja el Do a Si.")}
      {partitura("iivi")}
      {kp(["La <b>3.ª y la 7.ª</b> definen el acorde (shell voicing): con solo esas dos notas ya se reconoce.", "En el ii–V–I, la 7.ª de cada acorde baja por grado y se convierte en la 3.ª del siguiente.", "Practica el ii–V–I en las 12 tonalidades siguiendo el círculo de quintas."], "🎹")}
      {quiz("m11a", "¿Qué notas forman Cmaj7?", ["Do–Mi–Sol–Si♭", "Do–Mi–Sol–Si", "Do–Mi♭–Sol–Si♭"], 1, "Séptima mayor: Si natural.")}
      {quiz("m11b", "¿Qué dos notas definen mejor un acorde de séptima?", ["La fundamental y la 5.ª", "La 3.ª y la 7.ª", "La 5.ª y la 9.ª"], 1, "Por eso los «shell voicings» usan 3.ª y 7.ª.")}
      <div class="summary-box"><b>Resumen:</b> cinco tipos de séptima, tensiones y voicings que conectan las voces de forma suave.</div>
"""))
# 12 ---------------------------------------------------------------------------------------------
M.append(("🎶", "Improvisación: blues y reharmonización", "Crear música propia con lo que ya sabes.", f"""
      <h2>El blues de 12 compases</h2>
      <p>Es la forma más usada para aprender a improvisar: corta, repetitiva y con tres acordes.</p>
      {tabla(["Compases", "1–4", "5–6", "7–8", "9", "10", "11", "12"], [["Acordes en Do", "C7", "F7", "C7", "G7", "F7", "C7", "G7 (vuelta)"], ["Grados", "I7", "IV7", "I7", "V7", "IV7", "I7", "V7"]])}
      {partitura("blues")}
      <h3>1. La escala de blues</h3>
      {fig("teclado_blues.svg", "Escala de blues de Do", "Escala de blues de Do: Do, Mi♭, Fa, Fa♯, Sol, Si♭. Funciona sobre los tres acordes del blues.")}
      <ol class="steps"><li>Toca el bajo boogie con la mano izquierda hasta que sea automático.</li><li>Con la derecha, improvisa frases cortas de 2 compases usando solo 3 notas de la escala.</li><li>Deja silencios: pregunta (2 compases) y respuesta (2 compases).</li><li>Amplía a toda la escala y añade la «nota azul» Mi♭ resolviendo a Mi.</li></ol>
      <h3>2. Reharmonizar</h3>
      <p>Reharmonizar es <b>cambiar los acordes</b> de una melodía conservándola. Recursos sencillos:</p>
      {kp(["Sustituir I por vi o iii (comparten dos notas).", "Preparar cualquier acorde con su propio dominante (dominante secundario): antes de Dm, toca A7.", "Convertir V en ii–V (G7 → Dm7–G7).", "Sustitución tritonal: G7 → D♭7 (comparten la 3.ª y la 7.ª)."], "🔄")}
      {quiz("m12a", "¿Qué notas forman la escala de blues de Do?", ["Do–Re–Mi–Sol–La", "Do–Mi♭–Fa–Fa♯–Sol–Si♭", "Do–Re–Mi–Fa–Sol–La–Si"], 1, "Es la pentatónica menor con la 5.ª disminuida añadida.")}
      {quiz("m12b", "¿Qué acorde suena en el compás 5 del blues en Do?", ["C7", "F7", "G7"], 1, "Los compases 5 y 6 van al IV7.")}
      {actividad("Tu primer coro de blues", "Graba con el móvil un coro (12 compases) de blues improvisado y escribe qué frase te ha gustado más.", "Me ha gustado…")}
      <div class="summary-box"><b>Resumen:</b> forma de 12 compases, escala de blues, pregunta–respuesta y sustituciones básicas.</div>
"""))
# 13 ---------------------------------------------------------------------------------------------
M.append(("🎭", "Interpretación y estilos", "Tocar las notas es el principio; hacer música, el objetivo.", f"""
      <h2>Del texto al sonido</h2>
      {kp(["<b>Fraseo:</b> agrupa las notas en frases como en una conversación; respira al final de cada una.", "<b>Dinámica:</b> <i>pp, p, mp, mf, f, ff</i>. Los <i>crescendo</i> se planifican: empieza más suave para tener margen.", "<b>Articulación:</b> legato, staccato, tenuto y acentos cambian el carácter.", "<b>Rubato:</b> flexibilidad del tempo, acelerando y frenando, sin perder el pulso general."], "🎨")}
      <h3>1. Los grandes estilos</h3>
      {tabla(["Estilo", "Rasgos", "Repertorio recomendado (dominio público)"], [
        ["Barroco (1600–1750)", "Contrapunto, articulación clara, pedal mínimo, adornos", "Bach: <i>Invenciones a dos voces</i>, <i>Preludios y fugas</i> " + imslp("Bach Inventions")],
        ["Clasicismo (1750–1820)", "Frases equilibradas, bajo Alberti, dinámicas contrastadas", "Mozart: <i>Sonata K. 545</i>; Beethoven: <i>Sonata «Patética»</i>, 2.º mov. " + imslp("Beethoven Pathetique")],
        ["Romanticismo (1820–1900)", "Melodía cantabile, rubato, pedal abundante", "Chopin: <i>Nocturno op. 9 n.º 2</i>, <i>Preludios op. 28</i>; Schumann: <i>Escenas de niños</i> " + imslp("Chopin Nocturnes Op.9")],
        ["Impresionismo (1890–1920)", "Color, armonías flotantes, medios pedales", "Debussy: <i>Clair de lune</i>; Satie: <i>Gymnopédies</i> " + imslp("Debussy Suite bergamasque")],
        ["Ragtime y primer jazz", "Bajo stride, síncopas", "Joplin: <i>The Entertainer</i>, <i>Maple Leaf Rag</i> " + imslp("Joplin Entertainer")]])}
      <div class="box tip"><b>Ediciones:</b> en IMSLP elige ediciones «Urtext» o críticas cuando las haya: respetan lo que escribió el compositor y distinguen los añadidos del editor.</div>
      {quiz("m13a", "¿Qué es el rubato?", ["Tocar siempre con metrónomo", "Flexibilidad expresiva del tempo sin perder el pulso general", "Un tipo de pedal"], 1, "Se «roba» tiempo a unas notas para dárselo a otras.")}
      {quiz("m13b", "¿Qué compositor es representativo del impresionismo pianístico?", ["Claude Debussy", "J. S. Bach", "Scott Joplin"], 0, "Debussy, junto a Ravel, es el gran referente del impresionismo.")}
      <div class="summary-box"><b>Resumen:</b> fraseo, dinámica, articulación y rubato, adaptados a cada estilo.</div>
"""))
# 14 ---------------------------------------------------------------------------------------------
M.append(("🏆", "Preparar una obra y tocar en público", "Proyecto final: de la partitura al escenario.", f"""
      <h2>Plan de 4 semanas para una obra</h2>
      {tabla(["Semana", "Objetivo"], [["1", "Escucha, análisis, digitación y lectura lenta por secciones"], ["2", "Pasajes difíciles con metrónomo; unir secciones; primeras decisiones de dinámica"], ["3", "Tempo final; pedal y fraseo definitivos; memorización"], ["4", "Pasadas completas, grabarte y simular la actuación ante otras personas"]])}
      <h3>1. Memorizar de forma fiable</h3>
      {kp(["<b>Analítica:</b> saber qué acorde y qué sección vienen.", "<b>Visual:</b> recordar la página y la forma de la mano.", "<b>Auditiva:</b> poder cantar la música.", "<b>Motriz:</b> la memoria de los dedos (la menos fiable si va sola).", "Crea <b>puntos de entrada</b> cada 4–8 compases para poder retomar desde ahí."], "🧠")}
      <h3>2. Los nervios</h3>
      {kp(["Simula la actuación: ropa, saludo, toca para familia o amigos y grábate.", "Respiración lenta antes de empezar y elige un tempo inicial cómodo.", "Si te equivocas, <b>no pares</b>: mantén el pulso y entra en el siguiente punto de entrada."], "🫁")}
      <div class="activity checklist"><h3>✔️ Proyecto final</h3><p>Elige una obra del módulo 13 (o una de tu profesor/a) y completa:</p>
        <label><input type="checkbox" class="chk"> Análisis de forma y tonalidad escrito</label>
        <label><input type="checkbox" class="chk"> Digitación anotada en la partitura</label>
        <label><input type="checkbox" class="chk"> Plan de 4 semanas en el calendario</label>
        <label><input type="checkbox" class="chk"> Tempo final alcanzado con metrónomo</label>
        <label><input type="checkbox" class="chk"> Memorizada con puntos de entrada</label>
        <label><input type="checkbox" class="chk"> Grabación completa escuchada con lápiz en mano</label>
        <label><input type="checkbox" class="chk"> Interpretada ante público</label>
        <button class="btn" onclick="var c=document.querySelectorAll('.chk:checked').length,t=document.querySelectorAll('.chk').length;document.getElementById('prog').textContent=c===t?'🏆 ¡Proyecto completado!':'Llevas '+c+' de '+t+'.'">Ver mi progreso</button><p class="feedback" id="prog"></p></div>
      {quiz("m14a", "¿Qué técnica de memorización es más fiable?", ["Solo la memoria de los dedos", "Combinar memoria analítica, visual, auditiva y motriz", "Tocarla muchas veces deprisa"], 1, "Varias memorias se respaldan entre sí.")}
      {quiz("m14b", "Te equivocas tocando en público. ¿Qué haces?", ["Paro y empiezo de nuevo", "Sigo manteniendo el pulso y entro en el siguiente punto seguro", "Pido disculpas al público"], 1, "El público casi nunca nota un error si la música sigue.")}
      {DESCARGA}
      <div class="summary-box"><b>¡Enhorabuena!</b> Has completado los 14 módulos. Ahora puedes hacer el examen final.</div>
"""))
assert len(M) == N


def ampliar(i, body):
    """Añade «En pocas palabras» al principio y las explicaciones extra antes de la primera autoevaluación."""
    extra = re.sub(r"\[\[partitura:(\w+)\]\]", lambda m: partitura(m.group(1)), EXTRA[i])
    extra = re.sub(r"\[\[fig:([^|\]]+)\|([^|\]]+)\|([^\]]+)\]\]", lambda m: fig(*m.groups()), extra)
    assert "[[" not in extra, i
    pos = body.find('<div class="quiz">')
    pos = len(body) if pos < 0 else pos
    return PALABRAS[i] + body[:pos] + extra + "\n" + body[pos:]


M = [(ic, t, sub, ampliar(i, body)) for i, (ic, t, sub, body) in enumerate(M, 1)]
for i, (ic, t, sub, body) in enumerate(M, 1):
    open(os.path.join(OUT, f"modulo{i}.html"), "w", encoding="utf-8").write(pagina(i, ic, t, sub, body))

# Cuaderno de partituras (para imprimir y generar el PDF) ------------------------------------------
orden = ["escala_do", "escala_lam", "arpegio_do", "inversiones", "cadencia", "alberti", "pedal", "bach846", "elise",
         "octavas", "terceras", "adornos", "poli32", "poli43", "iivi", "blues",
         "pulso_68", "ritmos", "escala_sol", "escala_fa", "cadencia_sol", "vals", "blues_frase"]
assert set(orden) == set(PIEZAS)
bloques = "".join(f'<section class="pieza"><h2>{i}. {PIEZAS[k]["titulo"]}</h2><div id="p-{k}"></div><p>{PIEZAS[k]["nota"]}</p></section>' for i, k in enumerate(orden, 1))
cuaderno = f"""<!DOCTYPE html>
<html lang="es"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Cuaderno de partituras · {TITULO}</title>
<style>
body{{font-family:'Segoe UI',Tahoma,sans-serif;max-width:820px;margin:0 auto;padding:16px;color:#222;background:#fff}} .pieza div{{width:100%}}
header{{text-align:center;border-bottom:3px solid #c9a227;margin-bottom:20px}} h1{{color:#1e3c72}}
.pieza{{page-break-inside:avoid;break-inside:avoid;margin-bottom:26px}} .pieza h2{{color:#1e3c72;font-size:1.1em;margin-bottom:0}}
.pieza p{{font-size:.9em;color:#555;margin-top:2px}} footer{{text-align:center;font-size:.8em;color:#777}}
</style></head><body>
<header><h1>Cuaderno de partituras</h1><p>{TITULO}<br>Ejercicios originales del curso y fragmentos de obras de dominio público (J. S. Bach, L. van Beethoven).</p></header>
{bloques}
<footer>{FOOTER} · Partituras dibujadas con abcjs (licencia MIT)</footer>
<script>var PARTITURAS={json.dumps({k: PIEZAS[k]["abc"] for k in orden}, ensure_ascii=False)};</script>
<script src="../abcjs-basic-min.js"></script>
<script>Object.keys(PARTITURAS).forEach(function(k){{ABCJS.renderAbc('p-'+k,PARTITURAS[k],{{responsive:'resize',staffwidth:900,wrap:{{minSpacing:1.6,maxSpacing:2.6,preferredMeasuresPerLine:4}},paddingleft:0,paddingright:0}});}});document.title+=' ';window.LISTO=true;</script>
</body></html>
"""
open(os.path.join(OUT, "partituras", "cuaderno.html"), "w", encoding="utf-8").write(cuaderno)
for i, k in enumerate(orden, 1):
    open(os.path.join(OUT, "partituras", "abc", f"{i:02d}_{k}.abc"), "w", encoding="utf-8").write(PIEZAS[k]["abc"])

# Banco de preguntas: (módulo, enunciado, opciones, índice correcto, va al examen) ------------------
Q = [
 (1, "¿En qué consiste la práctica lenta deliberada?", ["Tocar a un tempo en el que no cometes errores y subirlo poco a poco con metrónomo", "Tocar la obra entera muchas veces a tempo", "Tocar solo lo que ya sale bien", "Practicar sin partitura desde el primer día"], 0, True),
 (1, "Al estudiar un pasaje difícil, ¿qué tamaño de fragmento conviene?", ["Fragmentos cortos de 1–2 compases, con la nota de unión al siguiente", "La página entera", "Toda la obra de principio a fin", "Una sola nota"], 0, True),
 (1, "¿Cuándo conviene subir el tempo del metrónomo?", ["Cuando el tempo actual sale limpio varias veces seguidas", "Cada cinco minutos", "Cuando te aburres", "Nunca"], 0, False),
 (2, "En un compás de 6/8 a velocidad normal, ¿cuántos pulsos se sienten?", ["2 pulsos de negra con puntillo", "6 pulsos de corchea", "3 pulsos de negra", "4 pulsos de corchea"], 0, True),
 (2, "Un tresillo de corcheas ocupa el tiempo de…", ["Dos corcheas (una negra)", "Tres corcheas", "Una corchea", "Una blanca"], 0, True),
 (2, "¿Qué nota está en la primera línea adicional por debajo del pentagrama en clave de Sol?", ["Do4 (Do central)", "La3", "Mi4", "Si3"], 0, False),
 (3, "¿Qué regla de digitación de escalas es correcta?", ["El pulgar no suele tocar teclas negras", "El pulgar toca siempre las teclas negras", "Se usan siempre los cinco dedos seguidos", "La mano izquierda copia la digitación de la derecha"], 0, True),
 (3, "¿Qué alteración caracteriza a la escala de La menor armónica?", ["Sol♯", "Fa♯", "Si♭", "Do♯"], 0, True),
 (3, "¿Cuántas alteraciones tiene la armadura de Re mayor?", ["Dos sostenidos (Fa♯ y Do♯)", "Un sostenido", "Dos bemoles", "Ninguna"], 0, False),
 (4, "¿Qué notas forman la 1.ª inversión de Do mayor?", ["Mi–Sol–Do", "Do–Mi–Sol", "Sol–Do–Mi", "Do–Fa–La"], 0, True),
 (4, "¿Qué digitación se usa habitualmente en el arpegio de Do mayor con la mano derecha (dos octavas)?", ["1-2-3-1-2-3-5", "1-2-4-1-2-4-5", "1-3-5-1-3-5-5", "5-4-2-1-4-2-1"], 0, True),
 (4, "Re–Fa–La es un acorde…", ["Menor", "Mayor", "Disminuido", "Aumentado"], 0, False),
 (5, "En Do mayor, ¿cuál es el acorde de dominante con séptima (V7)?", ["Sol7: Sol–Si–Re–Fa", "Fa mayor: Fa–La–Do", "Do7: Do–Mi–Sol–Si♭", "Re menor: Re–Fa–La"], 0, True),
 (5, "¿Qué es una cadencia perfecta (auténtica)?", ["El enlace V–I", "El enlace IV–I", "Terminar en el V grado", "El enlace V–vi"], 0, True),
 (5, "En cifrado americano, «Am» significa…", ["La menor", "La mayor", "La séptima", "Mi menor"], 0, False),
 (6, "¿Qué es el bajo Alberti?", ["Un acompañamiento que arpegia el acorde en el orden grave–agudo–medio–agudo", "Un acorde mantenido con pedal", "Una escala en octavas", "Un adorno barroco"], 0, True),
 (6, "La melodía queda tapada por el acompañamiento. ¿Qué haces?", ["Tocar el acompañamiento más suave y dar más peso a la melodía", "Tocar las dos manos más fuerte", "Quitar el pedal siempre", "Tocar más deprisa"], 0, True),
 (6, "¿Qué patrón sigue el bajo boogie en Do?", ["Do–Sol, Do–La, Do–Si♭, Do–La", "Do–Mi–Sol–Do", "Do–Re–Mi–Fa", "Do–Sol–Mi–Sol"], 0, False),
 (7, "¿Qué es el pedal sincopado (legato)?", ["Levantar el pedal justo al tocar el acorde nuevo y volver a pisarlo inmediatamente después", "Pisar el pedal toda la obra", "Cambiar el pedal antes del acorde nuevo", "Usar solo el pedal izquierdo"], 0, True),
 (7, "¿Qué pedal sostiene solo las notas que estaban pulsadas al pisarlo?", ["El central (sostenuto)", "El derecho", "El izquierdo", "Ninguno"], 0, True),
 (7, "¿Para qué sirve el pedal izquierdo (una corda)?", ["Para suavizar y cambiar el timbre", "Para mantener todas las notas", "Para afinar el piano", "Para tocar más fuerte"], 0, False),
 (8, "El Preludio en Do mayor BWV 846 pertenece a…", ["El clave bien temperado, libro I, de J. S. Bach", "Las sonatas de Beethoven", "Los nocturnos de Chopin", "Las Invenciones de Bach"], 0, True),
 (8, "¿En qué compás está escrita «Para Elisa» de Beethoven?", ["3/8", "4/4", "2/4", "6/8"], 0, True),
 (8, "¿Cuál es el primer paso recomendable para estudiar una obra nueva?", ["Escucharla y analizar forma, tonalidad y pasajes difíciles", "Tocarla a tempo desde el principio", "Memorizarla sin leerla", "Tocar solo el final"], 0, False),
 (9, "En el Barroco y el Clasicismo, ¿por qué nota empieza normalmente el trino?", ["Por la nota superior", "Por la nota real", "Por la nota inferior", "Por la tónica"], 0, True),
 (9, "Al tocar octavas con la mano derecha, ¿qué dedo va arriba en las teclas negras?", ["El 4.º", "El 2.º", "El pulgar", "El 3.º siempre"], 0, True),
 (9, "Notas molestias en la muñeca estudiando octavas. ¿Qué haces?", ["Paro, descanso y reviso la técnica; si persiste, consulto a un profesional", "Sigo hasta que se pase", "Toco más fuerte", "Subo el tempo"], 0, False),
 (10, "¿Cuántas subdivisiones tiene la cuadrícula común de un 3 contra 2?", ["6", "5", "3", "12"], 0, True),
 (10, "En 3 contra 2, ¿en qué subdivisiones coinciden las dos manos?", ["Solo en la primera", "En todas", "En la 1.ª y la 3.ª", "En ninguna"], 0, True),
 (10, "¿Cuántas subdivisiones tiene la cuadrícula común de un 4 contra 3?", ["12", "7", "6", "16"], 0, False),
 (11, "¿Qué notas forman Cmaj7?", ["Do–Mi–Sol–Si", "Do–Mi–Sol–Si♭", "Do–Mi♭–Sol–Si♭", "Do–Mi♭–Sol♭–Si♭"], 0, True),
 (11, "¿Qué notas tiene un voicing sin fundamental de Dm7 (3.ª, 5.ª, 7.ª y 9.ª)?", ["Fa–La–Do–Mi", "Re–Fa–La–Do", "Fa–La–Si–Mi", "Mi–Sol–Si–Re"], 0, True),
 (11, "¿Qué dos notas definen mejor un acorde de séptima (shell voicing)?", ["La 3.ª y la 7.ª", "La fundamental y la 5.ª", "La 5.ª y la 9.ª", "La 9.ª y la 13.ª"], 0, False),
 (12, "¿Qué notas forman la escala de blues de Do?", ["Do–Mi♭–Fa–Fa♯–Sol–Si♭", "Do–Re–Mi–Sol–La", "Do–Re–Mi–Fa–Sol–La–Si", "Do–Mi–Sol–Si♭"], 0, True),
 (12, "En un blues de 12 compases en Do, ¿qué acorde suena en los compases 5 y 6?", ["F7", "C7", "G7", "Am"], 0, True),
 (12, "Reharmonizar consiste en…", ["Cambiar los acordes de una melodía conservando la melodía", "Cambiar la melodía conservando los acordes", "Tocar más rápido", "Transportar a otra tonalidad"], 0, False),
 (13, "¿Qué es el rubato?", ["Flexibilidad expresiva del tempo sin perder el pulso general", "Tocar siempre con metrónomo", "Un tipo de pedal", "Un adorno barroco"], 0, True),
 (13, "¿Qué compositor es representativo del impresionismo pianístico?", ["Claude Debussy", "J. S. Bach", "W. A. Mozart", "Scott Joplin"], 0, True),
 (13, "En la música barroca para teclado, el pedal…", ["Se usa muy poco o nada", "Se usa en cada nota", "Es obligatorio en las fugas", "Se sustituye por el izquierdo"], 0, False),
 (14, "¿Qué técnica de memorización es más fiable?", ["Combinar memoria analítica, visual, auditiva y motriz", "Solo la memoria de los dedos", "Tocarla muchas veces deprisa", "Leerla sin tocar"], 0, True),
 (14, "Te equivocas tocando en público. ¿Qué haces?", ["Sigues manteniendo el pulso y entras en el siguiente punto seguro", "Paras y empiezas de nuevo", "Te disculpas con el público", "Tocas más deprisa para terminar"], 0, True),
 (14, "¿Qué ayuda a controlar los nervios antes de actuar?", ["Simular la actuación ante otras personas varias veces", "No tocar la obra la semana anterior", "Cambiar la digitación el día antes", "Subir el tempo el mismo día"], 0, False),
]

# Preguntas de la ampliación (solo banco GIFT); se ordenan por módulo para agrupar las categorías
Q += [
 (2, "¿Cómo se cuenta un compás de 6/8 a velocidad normal?", ["En dos pulsos, cada uno dividido en tres: «1-y-a 2-y-a»", "En seis pulsos iguales y fuertes", "En tres pulsos, como un 3/4", "En cuatro pulsos"], 0, False),
 (3, "¿Cuál es el patrón de tonos (T) y semitonos (S) de toda escala mayor?", ["T–T–S–T–T–T–S", "T–S–T–T–S–T–T", "S–T–T–T–S–T–T", "T–T–T–S–T–T–S"], 0, False),
 (3, "¿Qué alteración lleva la armadura de Fa mayor?", ["Si♭", "Fa♯", "Mi♭", "Do♯"], 0, False),
 (4, "¿Cuántos semitonos tiene una tercera mayor (por ejemplo, Do–Mi)?", ["4", "3", "2", "5"], 0, False),
 (5, "En Sol mayor, ¿qué acorde es la dominante (V)?", ["Re mayor", "Do mayor", "La menor", "Mi menor"], 0, False),
 (6, "En un vals con acompañamiento de mano izquierda, ¿qué se toca normalmente en el tiempo 1?", ["El bajo (la nota grave)", "El acorde en el registro medio", "Un silencio", "La melodía"], 0, False),
 (12, "¿Qué es una frase de «pregunta y respuesta» al improvisar?", ["Una idea corta seguida de otra que la contesta y cierra, a menudo en la tónica", "Tocar la escala de arriba abajo", "Repetir la misma nota todo el compás", "Cambiar de tonalidad en cada compás"], 0, False),
]
Q.sort(key=lambda q: q[0])


def _place(k, q):
    m, t, opts, ok, ex = q
    opts = list(opts); target = (k * 3 + 1) % len(opts)
    opts[ok], opts[target] = opts[target], opts[ok]
    return (m, t, opts, target, ex)


Q = [_place(k, q) for k, q in enumerate(Q)]
EXAM = [q for q in Q if q[4]]
NOMBRES = [m[1] for m in M]


def gift_esc(s):
    for ch in "~=#{}:":
        s = s.replace(ch, "\\" + ch)
    return s


g = ["// Piano: nivel intermedio y avanzado — Banco de preguntas GIFT para Moodle",
     "// Autor: Sixto Rodríguez de Sepúlveda. Una única respuesta correcta; una categoría por módulo."]
cur, cnt = None, {}
for m, q, opts, ok, _ in Q:
    if m != cur:
        cur = m
        g += ["", f"$CATEGORY: Piano intermedio y avanzado/Módulo {m:02d} - {gift_esc(NOMBRES[m-1])}"]
    cnt[m] = cnt.get(m, 0) + 1
    g += ["", f"::PIA{m:02d}-{cnt[m]}::{gift_esc(q)} {{"] + [f"{'=' if j == ok else '~'}{gift_esc(o)}" for j, o in enumerate(opts)] + ["}"]
open(os.path.join(OUT, "preguntas_moodle.gift"), "w", encoding="utf-8").write("\n".join(g) + "\n")

qs_html = "".join(
    f'<div class="quiz" id="box{i}"><h4>{i}. {html.escape(q)} <span class="small">(Módulo {m})</span></h4><div class="options">'
    + "".join(f'<label class="option"><input type="radio" name="q{i}" value="{j}" style="width:auto;margin-right:8px">{html.escape(o)}</label>' for j, o in enumerate(opts))
    + "</div></div>" for i, (m, q, opts, ok, _) in enumerate(EXAM, 1))
exam = f"""<!DOCTYPE html>
<html lang="es"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Examen final: Piano intermedio y avanzado</title><link rel="stylesheet" href="style.css"></head>
<body><div class="container">
  <div class="header"><h1><span class="shield-icon">🏁</span>Examen final</h1><img src="img/logo-centro.png" class="logo-centro" alt="Logotipo del centro"><p>{TITULO}</p></div>
  <div class="progress-container"><div class="progress-bar"><div class="progress-fill" style="width:100%"></div></div><div class="progress-text">Piano · Examen final</div></div>
  <div class="content-area"><section class="module">
    <h2>Evaluación final</h2>
    <p>Responde a las {len(EXAM)} preguntas. Necesitas al menos un <b>70 %</b> para aprobar. Al corregir verás las respuestas correctas y podrás repetirlo.</p>
    {qs_html}
    <div style="text-align:center"><button class="btn" onclick="corregir()">Corregir examen</button> <button class="btn" onclick="reiniciar()">Reintentar</button></div>
    <div id="resultado" style="margin-top:20px"></div>
    <div class="navigation"><button class="nav-btn" onclick="scormGo('modulo{N}.html')">⬅️ Módulo {N}</button><button class="nav-btn" onclick="scormGo('index.html')">Inicio 🏠</button></div>
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

# Portada ---------------------------------------------------------------------------------------
itin = "".join(f'<li>{"🎹" if i < 8 else "🎼"} <span><b>{i+1}.</b> <a href="modulo{i+1}.html">{t}</a></span></li>' for i, t in enumerate(NOMBRES))
glosario = ('<details class="glos"><summary>📖 Glosario: las palabras del curso explicadas fácil (' + str(len(GLOSARIO)) + ' términos)</summary><dl class="glosario">'
            + "".join(f"<dt>{t}</dt><dd>{d}</dd>" for t, d in sorted(GLOSARIO, key=lambda x: x[0].lower())) + "</dl></details>")
index = f"""<!DOCTYPE html>
<html lang="es"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{TITULO}</title><link rel="stylesheet" href="style.css"></head>
<body><div class="container">
  <div class="header"><h1><span class="shield-icon">🎹</span>{TITULO}</h1><img src="img/logo-centro.png" class="logo-centro" alt="Logotipo del centro">
  <p>Técnica, armonía, lectura, improvisación e interpretación, con partituras que puedes escuchar e imprimir.</p></div>
  <div class="progress-container"><div class="progress-bar"><div class="progress-fill" style="width:0%"></div></div><div class="progress-text">Piano · Inicio · {N} módulos</div></div>
  <div class="content-area"><section class="module">
    <h2>Bienvenido/a 👋</h2>
    <p>Este curso es para quien ya lee partituras sencillas y toca con las dos manos, y quiere dar el salto: tocar con <b>método</b>, entender la <b>armonía</b>, dominar la <b>técnica</b> avanzada, <b>improvisar</b> y preparar obras para tocarlas en público.</p>
    <div class="box"><b>Cómo funciona:</b> cada módulo tiene explicaciones, <b>partituras interactivas</b> (pulsa «▶ Escuchar» y elige la velocidad), ejercicios para el piano y autoevaluaciones. Al final hay un examen de {len(EXAM)} preguntas.</div>
    <div class="dl-box">📥 <b>Partituras para imprimir:</b> <a href="partituras/Cuaderno_de_partituras.pdf" target="_blank" rel="noopener">Cuaderno de partituras (PDF)</a> con los {len(PIEZAS)} ejercicios y fragmentos del curso. Las obras completas, en <a href="https://imslp.org" target="_blank" rel="noopener">IMSLP</a> (biblioteca libre de partituras de dominio público).</div>
    {glosario}
    <h3>Itinerario</h3>
    <p><b>Nivel intermedio</b> (módulos 1–8) · <b>Nivel avanzado</b> (módulos 9–14)</p>
    <ul class="key-points">{itin}<li>🏁 <span><a href="examen_final.html">Examen final</a></span></li></ul>
    <div class="alert-box"><b>Requisitos:</b> un piano o teclado de 88 teclas (mínimo 61) con teclas sensibles a la velocidad y pedal. Para escuchar las partituras hace falta conexión a Internet la primera vez (se descargan los sonidos del piano); el resto del curso funciona sin conexión.</div>
    <div class="navigation"><span></span><button class="nav-btn" onclick="scormGo('modulo1.html')">Comenzar ➡️</button></div>
  </section></div></div>
<footer class="footer-autor">{FOOTER}</footer>
<script src="scorm.js"></script>
</body></html>
"""
open(os.path.join(OUT, "index.html"), "w", encoding="utf-8").write(index)

if not os.path.exists(os.path.join(OUT, "imsmanifest.xml")):
    open(os.path.join(OUT, "imsmanifest.xml"), "w", encoding="utf-8").write(
        f'<?xml version="1.0" encoding="UTF-8"?>\n<manifest identifier="piano-intermedio-avanzado" version="1.0" xmlns="http://www.imsproject.org/xsd/imscp_rootv1p1p2">'
        f'<organizations default="ORG_1"><organization identifier="ORG_1"><title>{TITULO}</title></organization></organizations><resources/></manifest>\n')
if not os.path.exists(os.path.join(OUT, "scorm.js")):
    open(os.path.join(OUT, "scorm.js"), "w", encoding="utf-8").write("")

open(os.path.join(OUT, "README.txt"), "w", encoding="utf-8").write(f"""PIANO: NIVEL INTERMEDIO Y AVANZADO — Paquete SCORM 1.2
Autor: Sixto Rodríguez de Sepúlveda

{N} módulos (1–8 intermedio, 9–14 avanzado): método de estudio y metrónomo, lectura avanzada con
entrenador de notas, escalas y círculo de quintas, arpegios e inversiones, armonía funcional,
independencia de manos, pedal, repertorio (Bach BWV 846, Beethoven WoO 59), octavas/terceras/adornos,
polirritmia, armonía de jazz y voicings, blues e improvisación, estilos e interpretación, y preparación
de una actuación (proyecto final).

Contenido:
- {len(PIEZAS)} partituras interactivas (notación ABC dibujada con abcjs, licencia MIT, en licencias/):
  se pueden escuchar a 50/75/100 % (requiere Internet la primera vez para los sonidos).
- partituras/Cuaderno_de_partituras.pdf (para imprimir) y partituras/abc/*.abc (fuentes ABC,
  se abren con MuseScore u otros editores con soporte ABC).
- Ilustraciones: teclados con digitaciones y círculo de quintas.
- Metrónomo y entrenador de lectura integrados (sin conexión).
- examen_final.html: {len(EXAM)} preguntas (aprobado 70 %); preguntas_moodle.gift: {len(Q)} preguntas.
- Seguimiento SCORM: un SCO por página; el índice de Moodle se marca al avanzar.

Obras de dominio público: solo fragmentos; las obras completas se enlazan a IMSLP.
""")
print("ok", N, "módulos,", len(EXAM), "preguntas de examen,", len(Q), "GIFT")
