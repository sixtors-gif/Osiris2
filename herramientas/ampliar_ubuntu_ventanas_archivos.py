#!/usr/bin/env python3
"""Amplía el curso de Ubuntu con dos módulos prácticos (migración de una sola vez):

  · Nuevo módulo 8:  Práctica: abrir, organizar y cerrar ventanas (con simulador de escritorio).
  · Nuevo módulo 10: Práctica: copiar, pegar, mover, renombrar y borrar archivos (con simulador de Archivos).

Los módulos antiguos 8…15 pasan a ser 9, 11…17. Se actualizan barra de progreso, navegación,
referencias cruzadas, portada, examen (2 preguntas nuevas por módulo), banco GIFT y README.
Después hay que ejecutar herramientas/scorm_seguimiento.py y herramientas/empaquetar.sh.

Uso: python3 herramientas/ampliar_ubuntu_ventanas_archivos.py cursos/Curso_Ubuntu_Introduccion_SCORM
"""
import json, os, re, sys

D = sys.argv[1]
if os.path.exists(os.path.join(D, "modulo17.html")):
    sys.exit("El curso ya está ampliado (existe modulo17.html). No se hace nada.")

TOTAL = 17
CURSO = "Introducción a Ubuntu para usuarios"
MAPA = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 9, 9: 11, 10: 12, 11: 13, 12: 14, 13: 15, 14: 16, 15: 17}
rd = lambda f: open(os.path.join(D, f), encoding="utf-8").read()
def wr(f, s): open(os.path.join(D, f), "w", encoding="utf-8").write(s)


def sub1(s, old, new, f):
    assert s.count(old) == 1, (f, old, s.count(old))
    return s.replace(old, new)


# 1. Renombrar los módulos existentes (de mayor a menor para no pisar archivos) -----------------
for viejo in sorted(MAPA, reverse=True):
    if MAPA[viejo] != viejo:
        os.rename(os.path.join(D, f"modulo{viejo}.html"), os.path.join(D, f"modulo{MAPA[viejo]}.html.tmp"))
for viejo in MAPA:
    if MAPA[viejo] != viejo:
        os.rename(os.path.join(D, f"modulo{MAPA[viejo]}.html.tmp"), os.path.join(D, f"modulo{MAPA[viejo]}.html"))


def cabecera_y_nav(s, n, f):
    s = re.sub(r"Módulo \d+ de 15", f"Módulo {n} de {TOTAL}", s)
    s = re.sub(r'(class="progress-fill" style="width:)\d+%', lambda m: f"{m.group(1)}{round(n * 100 / (TOTAL + 1))}%", s)
    prev = "index.html" if n == 1 else f"modulo{n-1}.html"
    nxt = "examen_final.html" if n == TOTAL else f"modulo{n+1}.html"
    nav = re.search(r'<div class="navigation">.*?</div>', s, re.S)
    botones = re.findall(r"scormGo\('[^']+'\)", nav.group(0))
    nuevo = nav.group(0)
    if len(botones) == 2:
        nuevo = nuevo.replace(botones[0], f"scormGo('{prev}')", 1)
        nuevo = nuevo[::-1].replace(botones[1][::-1], f"scormGo('{nxt}')"[::-1], 1)[::-1]
    else:  # el último módulo solo tenía «Anterior»
        nuevo = nuevo.replace(botones[0], f"scormGo('{prev}')", 1)
        if n < TOTAL:
            nuevo = nuevo.replace("</div>", f'<button class="nav-btn" onclick="scormGo(\'{nxt}\')">Siguiente ➡️</button></div>', 1)
    return s.replace(nav.group(0), nuevo)


for viejo, n in MAPA.items():
    f = f"modulo{n}.html"
    s = cabecera_y_nav(rd(f), n, f)
    if viejo == 14:
        s = sub1(s, "(módulo 11)", "(módulo 13)", f)
    if viejo == 15:
        s = sub1(s, "el simulador del módulo 13", "el simulador del módulo 15", f)
    wr(f, s)

# 2. Plantilla de página (misma estructura que el resto del curso) ------------------------------
PICKC = """<script>
function pickc(el,uid,ok){var box=document.getElementById('opt_'+uid);box.querySelectorAll('.option').forEach(function(x){x.classList.remove('correct','incorrect')});
el.classList.add(ok?'correct':'incorrect');var e=document.getElementById('fb_'+uid);e.className='feedback-box '+(ok?'good':'bad');
e.textContent=(ok?'✅ Correcto. ':'❌ No exactamente. ')+e.getAttribute('data-exp');}
</script>"""


def ejercicio(uid, titulo, preg, opciones, ok, exp):
    ops = "".join(f'<div class="option" onclick="pickc(this,\'{uid}\',{1 if i == ok else 0})">{o}</div>' for i, o in enumerate(opciones))
    return (f'<div class="exercise"><h3>🧩 {titulo}</h3><p>{preg}</p><div class="options" id="opt_{uid}">{ops}</div>'
            f'<div id="fb_{uid}" class="feedback-box" data-exp="{exp}"></div></div>')


def pagina(n, icono, titulo, sub, cuerpo, extra_js=""):
    return f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{titulo}</title>
<link rel="stylesheet" href="style.css">
</head>
<body>
<div class="container">
  <div class="header">
    <h1><span class="badge-icon">{icono}</span>{titulo}</h1>
    <img src="img/logo-centro.png" class="logo-centro" alt="Logotipo del centro">
    <p>{sub}</p>
  </div>
  <div class="progress-container">
    <div class="progress-bar"><div class="progress-fill" style="width:{round(n * 100 / (TOTAL + 1))}%"></div></div>
    <div class="progress-text">{CURSO} · Módulo {n} de {TOTAL}</div>
  </div>
  <div class="content-area">
    <section class="module">
      <h2>{titulo}</h2>
{cuerpo}
      <div class="navigation"><button class="nav-btn" onclick="scormGo('modulo{n-1}.html')">⬅️ Anterior</button><button class="nav-btn" onclick="scormGo('modulo{n+1}.html')">Siguiente ➡️</button></div>
    </section>
  </div>
</div>
<footer class="footer-autor">{CURSO} · Material educativo · Creado por: Sixto Rodríguez de Sepúlveda</footer>
<script src="scorm.js"></script>
{PICKC}
{extra_js}
</body>
</html>
"""


K = lambda *teclas: " + ".join(f"<kbd>{t}</kbd>" for t in teclas)

# Esquema de una ventana con sus partes (dibujo ilustrativo) ----------------------------------
VENTANA_SVG = """<svg viewBox="0 0 640 300" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Partes de una ventana en Ubuntu: barra de título, botones minimizar, maximizar y cerrar, y bordes para cambiar el tamaño" font-family="Segoe UI,Tahoma,sans-serif">
<rect x="70" y="40" width="420" height="230" rx="12" fill="#ffffff" stroke="#9aa4bd" stroke-width="2"/>
<path d="M70,52 a12,12 0 0 1 12,-12 h396 a12,12 0 0 1 12,12 v34 h-420 z" fill="#ebebeb"/>
<text x="280" y="68" font-size="15" font-weight="700" fill="#333" text-anchor="middle">Documentos</text>
<circle cx="410" cy="63" r="11" fill="#d4d4d4"/><line x1="405" y1="63" x2="415" y2="63" stroke="#333" stroke-width="2"/>
<circle cx="437" cy="63" r="11" fill="#d4d4d4"/><rect x="432" y="58" width="10" height="10" fill="none" stroke="#333" stroke-width="2"/>
<circle cx="464" cy="63" r="11" fill="#E95420"/><path d="M459,58 l10,10 M469,58 l-10,10" stroke="#fff" stroke-width="2.2"/>
<rect x="90" y="105" width="110" height="145" rx="6" fill="#f4f4f4"/>
<g fill="#cfd6e4"><rect x="220" y="110" width="250" height="14" rx="4"/><rect x="220" y="134" width="210" height="14" rx="4"/><rect x="220" y="158" width="230" height="14" rx="4"/><rect x="220" y="182" width="180" height="14" rx="4"/></g>
<rect x="476" y="256" width="14" height="14" fill="none" stroke="#E95420" stroke-width="2" stroke-dasharray="3 2"/>
<g font-size="13" font-weight="700" fill="#1f3a63">
<line x1="150" y1="63" x2="150" y2="20" stroke="#6b7280"/><text x="150" y="15" text-anchor="middle">Barra de título: arrastrar para mover · doble clic para maximizar</text>
<line x1="410" y1="75" x2="545" y2="110" stroke="#6b7280"/><text x="550" y="114">Minimizar</text>
<line x1="437" y1="75" x2="545" y2="140" stroke="#6b7280"/><text x="550" y="144">Maximizar</text>
<line x1="464" y1="75" x2="545" y2="170" stroke="#6b7280"/><text x="550" y="174">Cerrar</text>
<line x1="490" y1="270" x2="545" y2="250" stroke="#6b7280"/><text x="550" y="246">Bordes y</text><text x="550" y="262">esquinas:</text><text x="550" y="278">cambiar tamaño</text>
</g></svg>"""

# 3. Nuevo módulo 8: ventanas -------------------------------------------------------------------
SIM_VENTANAS = """
<div class="sim" id="simv">
  <div class="sim-top"><span>Actividades</span><span id="simv-hora">10:00</span><span>🔊 🔋</span></div>
  <div class="sim-body">
    <div class="sim-dock" id="simv-dock"></div>
    <div class="sim-desk" id="simv-desk"><div class="sim-hint">Haz clic en un icono del Dock para abrir una aplicación</div></div>
  </div>
</div>
<div class="missions-box"><b>🎯 Misiones</b><ul class="checks" id="simv-mis"></ul><p class="small" id="simv-msg"></p>
<button class="btn" onclick="simvReset()">Empezar de nuevo</button></div>
"""
JS_VENTANAS = r"""<script>
(function(){
var APPS=[{id:'files',ico:'📁',name:'Archivos'},{id:'web',ico:'🌐',name:'Firefox'},{id:'text',ico:'📝',name:'Editor de texto'}];
var MIS=[['abrir2','Abre dos aplicaciones distintas desde el Dock'],['max','Maximiza una ventana (botón ▢ o doble clic en la barra de título)'],
['mover','Mueve una ventana arrastrando su barra de título'],['min','Minimiza una ventana (botón –)'],
['rec','Recupera la ventana minimizada haciendo clic en su icono del Dock'],['cerrar','Cierra todas las ventanas (botón ✕)']];
var st,z=1,desk=document.getElementById('simv-desk'),dock=document.getElementById('simv-dock'),mis=document.getElementById('simv-mis');
function done(k){if(!st.done[k]){st.done[k]=1;pinta();}}
function pinta(){mis.innerHTML=MIS.map(function(m){return '<li class="'+(st.done[m[0]]?'ok':'')+'">'+(st.done[m[0]]?'✅ ':'⬜ ')+m[1]+'</li>'}).join('');
 var n=MIS.filter(function(m){return st.done[m[0]]}).length;document.getElementById('simv-msg').textContent=n===MIS.length?'🏆 ¡Todas las misiones completadas!':'Misiones: '+n+' de '+MIS.length;
 dock.innerHTML='';APPS.forEach(function(a){var b=document.createElement('button');b.className='sim-app'+(st.win[a.id]?' abierta':'');b.title=a.name;b.innerHTML=a.ico;b.onclick=function(){abrir(a)};dock.appendChild(b)});}
function abrir(a){var w=st.win[a.id];
 if(w){if(w.style.display==='none'){w.style.display='';done('rec');}w.style.zIndex=++z;return;}
 w=document.createElement('div');w.className='sim-win';var n=Object.keys(st.win).length;w.style.left=(30+n*40)+'px';w.style.top=(20+n*30)+'px';w.style.zIndex=++z;
 w.innerHTML='<div class="sim-title"><span>'+a.ico+' '+a.name+'</span><span class="sim-btns"><button title="Minimizar">–</button><button title="Maximizar">▢</button><button class="x" title="Cerrar">✕</button></span></div><div class="sim-cont">'+({files:'📂 Documentos · 📂 Descargas · 📂 Imágenes',web:'🔒 https://ubuntu.com',text:'Escribe aquí tus apuntes…'})[a.id]+'</div>';
 var bt=w.querySelectorAll('.sim-btns button');
 bt[0].onclick=function(e){e.stopPropagation();w.style.display='none';done('min');};
 bt[1].onclick=function(e){e.stopPropagation();maxi(w);};
 bt[2].onclick=function(e){e.stopPropagation();w.remove();delete st.win[a.id];if(!Object.keys(st.win).length&&st.done.abrir2)done('cerrar');pinta();};
 var t=w.querySelector('.sim-title');t.ondblclick=function(){maxi(w)};
 t.onpointerdown=function(e){if(e.target.tagName==='BUTTON'||w.classList.contains('max'))return;w.style.zIndex=++z;var r=desk.getBoundingClientRect(),ox=e.clientX-w.offsetLeft,oy=e.clientY-w.offsetTop,moved=0;
  t.setPointerCapture(e.pointerId);t.onpointermove=function(ev){w.style.left=Math.max(0,Math.min(r.width-80,ev.clientX-ox))+'px';w.style.top=Math.max(0,Math.min(r.height-30,ev.clientY-oy))+'px';moved++;};
  t.onpointerup=function(){t.onpointermove=null;if(moved>3)done('mover');};};
 w.onpointerdown=function(){w.style.zIndex=++z;};
 desk.appendChild(w);st.win[a.id]=w;var h=desk.querySelector('.sim-hint');if(h)h.style.display='none';
 if(Object.keys(st.win).length>=2)done('abrir2');pinta();}
function maxi(w){w.classList.toggle('max');if(w.classList.contains('max'))done('max');}
window.simvReset=function(){desk.querySelectorAll('.sim-win').forEach(function(w){w.remove()});st={win:{},done:{}};var h=desk.querySelector('.sim-hint');if(h)h.style.display='';pinta();};
simvReset();
})();
</script>"""

M8 = f"""
<div class="activity"><h3>🪟 De la teoría a la práctica</h3>
<p>En el módulo anterior viste los atajos. Ahora vas a practicar, paso a paso, lo que harás decenas de veces al día: <b>abrir</b> aplicaciones, <b>mover y ordenar</b> sus ventanas, <b>minimizarlas</b> y <b>cerrarlas</b> correctamente. Al final tienes un <b>simulador</b> para practicar aunque no tengas Ubuntu delante.</p></div>

<h3>1. Abrir una aplicación: tres caminos</h3>
<ol class="steps">
<li><b>Desde el Dock</b> (la barra de iconos de la izquierda): un clic sobre el icono. Bajo el icono aparece un <b>punto</b>: indica que la aplicación está abierta.</li>
<li><b>Buscándola:</b> pulsa {K("Super")}, escribe las primeras letras (por ejemplo <code>calc</code>) y pulsa {K("Intro")}. Es la forma más rápida cuando te acostumbras.</li>
<li><b>Desde la cuadrícula de aplicaciones:</b> el botón de los nueve cuadrados, abajo del todo en el Dock, muestra <b>todas</b> las aplicaciones instaladas.</li>
</ol>
<div class="tip-box">💡 <b>¿Quieres otra ventana de la misma aplicación</b> (por ejemplo, dos documentos)? Clic derecho sobre su icono del Dock ▸ <b>Nueva ventana</b>, o dentro de la aplicación {K("Ctrl", "N")}.</div>

<h3>2. Las partes de una ventana</h3>
<div class="figure">{VENTANA_SVG}<div class="figure-caption">Esquema ilustrativo de una ventana de Ubuntu. En Ubuntu los botones están arriba a la <b>derecha</b> y el de cerrar es naranja.</div></div>

<h3>3. Mover, maximizar y cambiar el tamaño</h3>
<table class="tbl"><tr><th>Quiero…</th><th>Con el ratón</th><th>Con el teclado</th></tr>
<tr><td>Mover la ventana</td><td>Arrastra la <b>barra de título</b></td><td>—</td></tr>
<tr><td>Maximizar / restaurar</td><td>Botón ▢, o <b>doble clic</b> en la barra de título</td><td>{K("Super", "↑")} / {K("Super", "↓")}</td></tr>
<tr><td>Ocupar media pantalla</td><td>Arrastra la ventana al borde izquierdo o derecho</td><td>{K("Super", "←")} / {K("Super", "→")}</td></tr>
<tr><td>Cambiar el tamaño</td><td>Arrastra un <b>borde</b> o una <b>esquina</b> (el puntero cambia a una flecha doble)</td><td>—</td></tr>
<tr><td>Traer al frente una ventana tapada</td><td>Clic en cualquier parte visible de ella, o en su icono del Dock</td><td>{K("Alt", "Tab")}</td></tr></table>

<h3>4. Minimizar y recuperar</h3>
<p>Minimizar <b>esconde</b> la ventana sin cerrarla: la aplicación sigue abierta y conserva lo que estabas haciendo.</p>
<ul class="key-points"><li>➖ <span>Para minimizar: botón <b>–</b> de la barra de título.</span></li>
<li>↩️ <span>Para recuperarla: clic en su icono del <b>Dock</b>, {K("Alt", "Tab")}, o {K("Super")} y elegirla entre las ventanas.</span></li>
<li>🖥️ <span>Para ver el escritorio un momento: {K("Super", "D")} esconde todas; repítelo para que vuelvan.</span></li></ul>

<h3>5. Cerrar bien: ventana, pestaña o aplicación</h3>
<table class="tbl"><tr><th>Acción</th><th>Cómo</th><th>Qué cierra</th></tr>
<tr><td>Cerrar la ventana</td><td>Botón ✕ naranja, o {K("Alt", "F4")}</td><td>Esa ventana</td></tr>
<tr><td>Cerrar una pestaña o documento</td><td>{K("Ctrl", "W")}</td><td>Solo la pestaña o el documento activo</td></tr>
<tr><td>Salir de la aplicación</td><td>{K("Ctrl", "Q")}, o clic derecho en su icono del Dock ▸ <b>Salir</b></td><td>La aplicación entera, con todas sus ventanas</td></tr></table>
<div class="alert-box">⚠️ <b>Si hay cambios sin guardar</b>, la aplicación te preguntará antes de cerrar. Lee el aviso: normalmente ofrece <b>Guardar</b>, <b>Cerrar sin guardar</b> o <b>Cancelar</b>. Si dudas, elige <b>Cancelar</b> y guarda primero con {K("Ctrl", "S")}.</div>

<h3>6. Si una aplicación se queda colgada</h3>
<ol class="steps">
<li>Espera unos segundos: a veces solo está ocupada.</li>
<li>Si Ubuntu muestra el aviso <b>«… no responde»</b>, puedes elegir <b>Esperar</b> o <b>Forzar salida</b>. Forzar la salida la cierra de inmediato y se pierde lo que no estuviera guardado.</li>
<li>Si no aparece el aviso, abre <b>Resources</b> (el monitor del sistema), busca la aplicación y fuerza su cierre.</li>
</ol>
<div class="ms-box"><span class="mbadge">Si vienes de Windows</span> Es lo mismo que «Finalizar tarea» en el Administrador de tareas. {K("Ctrl", "Alt", "Supr")} en Ubuntu sirve para <b>cerrar la sesión</b>, no abre un administrador de tareas.</div>

<h3>7. Practica en el simulador</h3>
<p>Este escritorio es una <b>simulación simplificada</b> para practicar con el ratón (o con el dedo en una tableta). Completa las misiones.</p>
{SIM_VENTANAS}

{ejercicio("u8a", "Doble clic", "¿Qué ocurre al hacer doble clic en la barra de título de una ventana?", ["Se cierra", "Se maximiza, o vuelve a su tamaño si ya estaba maximizada", "Se minimiza al Dock", "Se mueve a otro espacio de trabajo"], 1, "El doble clic en la barra de título alterna entre maximizar y restaurar.")}
{ejercicio("u8b", "Recuperar una ventana", "Has minimizado el editor de texto. ¿Cómo lo recuperas?", ["Lo vuelvo a instalar", "No se puede: minimizar es cerrar", "Hago clic en su icono del Dock o uso Alt + Tab", "Reinicio el ordenador"], 2, "Minimizar solo esconde la ventana; su icono del Dock la trae de vuelta.")}
{ejercicio("u8c", "Cerrar todo", "Quieres cerrar Firefox entero, con todas sus ventanas. ¿Qué atajo usas?", ["Ctrl + W", "Ctrl + Q", "Super + D", "Ctrl + N"], 1, "Ctrl + Q sale de la aplicación; Ctrl + W cierra solo la pestaña o el documento actual.")}
{ejercicio("u8d", "Aplicación colgada", "Una aplicación no responde y aparece un aviso. ¿Qué botón la cierra a la fuerza?", ["Esperar", "Forzar salida", "Minimizar", "Maximizar"], 1, "Forzar salida la cierra inmediatamente (se pierde lo no guardado).")}
<div class="summary-box">🎯 <b>Idea clave:</b> abre desde el Dock o con {K("Super")} + nombre; ordena con la barra de título y {K("Super")} + flechas; minimizar no es cerrar; {K("Ctrl", "W")} cierra un documento y {K("Ctrl", "Q")} la aplicación.</div>
"""

# 4. Nuevo módulo 10: archivos ------------------------------------------------------------------
SIM_ARCHIVOS = """
<div class="sim" id="sima" tabindex="0">
  <div class="sim-top"><span>📁 Archivos</span><span id="sima-ruta">Carpeta personal</span><span></span></div>
  <div class="sim-tools">
    <button data-a="copiar">📄 Copiar <small>Ctrl+C</small></button><button data-a="cortar">✂️ Cortar <small>Ctrl+X</small></button>
    <button data-a="pegar">📋 Pegar <small>Ctrl+V</small></button><button data-a="renombrar">✏️ Renombrar <small>F2</small></button>
    <button data-a="carpeta">➕ Nueva carpeta</button><button data-a="borrar">🗑️ A la papelera <small>Supr</small></button>
    <button data-a="restaurar">♻️ Restaurar</button>
  </div>
  <div class="sim-fm"><div class="sim-side" id="sima-side"></div><div class="sim-files" id="sima-files"></div></div>
  <div class="sim-status" id="sima-status">Haz clic en un archivo para seleccionarlo. Ctrl + clic selecciona varios.</div>
</div>
<div class="missions-box"><b>🎯 Misiones</b><ul class="checks" id="sima-mis"></ul><p class="small" id="sima-msg"></p>
<button class="btn" onclick="simaReset()">Empezar de nuevo</button></div>
"""
JS_ARCHIVOS = r"""<script>
(function(){
var CARP=['Documentos','Descargas','Imágenes','USB','Papelera'],ICO={Documentos:'📄',Descargas:'⬇️',Imágenes:'🖼️',USB:'💾',Papelera:'🗑️'};
var MIS=[['m1','Copia «foto_playa.jpg» de Imágenes al USB (debe seguir también en Imágenes)'],
['m2','Mueve «apuntes.odt» de Descargas a Documentos (que ya no quede en Descargas)'],
['m3','Renombra «documento1.odt» (en Documentos) como «trabajo_historia.odt»'],
['m4','Crea una carpeta llamada «Clase» en Documentos'],
['m5','Manda «borrador.txt» (en Documentos) a la Papelera… y después restáuralo']];
var st,box=document.getElementById('sima');
function nuevo(){return {cur:'Imágenes',sel:[],clip:null,origen:{},done:{},borrado:false,fs:{
 Documentos:['documento1.odt','borrador.txt','horario.ods'],Descargas:['apuntes.odt','instalador.deb'],
 Imágenes:['foto_playa.jpg','captura.png'],USB:['musica.mp3'],Papelera:[]}}}
function ico(n){return n.indexOf('.')<0?'📂':{jpg:'🖼️',png:'🖼️',odt:'📝',ods:'📊',txt:'🗒️',mp3:'🎵',deb:'📦'}[n.split('.').pop()]||'📄'}
function msg(t){document.getElementById('sima-status').textContent=t}
function comprueba(){var f=st.fs;
 if(f.USB.indexOf('foto_playa.jpg')>=0&&f['Imágenes'].indexOf('foto_playa.jpg')>=0)st.done.m1=1;
 if(f.Documentos.indexOf('apuntes.odt')>=0&&f.Descargas.indexOf('apuntes.odt')<0)st.done.m2=1;
 if(f.Documentos.indexOf('trabajo_historia.odt')>=0&&f.Documentos.indexOf('documento1.odt')<0)st.done.m3=1;
 if(f.Documentos.indexOf('Clase')>=0)st.done.m4=1;
 if(f.Papelera.indexOf('borrador.txt')>=0)st.borrado=true;
 if(st.borrado&&f.Documentos.indexOf('borrador.txt')>=0)st.done.m5=1;}
function pinta(){comprueba();
 document.getElementById('sima-side').innerHTML=CARP.map(function(c){return '<button class="'+(c===st.cur?'on':'')+'" data-c="'+c+'">'+ICO[c]+' '+c+'</button>'}).join('');
 var fl=st.fs[st.cur];document.getElementById('sima-files').innerHTML=fl.length?fl.map(function(n){return '<button class="sim-file'+(st.sel.indexOf(n)>=0?' sel':'')+'" data-f="'+n+'"><span>'+ico(n)+'</span>'+n+'</button>'}).join(''):'<p class="small">Esta carpeta está vacía.</p>';
 document.getElementById('sima-ruta').textContent=st.cur==='USB'?'USB (memoria externa)':(st.cur==='Papelera'?'Papelera':'Carpeta personal › '+st.cur);
 document.getElementById('sima-mis').innerHTML=MIS.map(function(m){return '<li class="'+(st.done[m[0]]?'ok':'')+'">'+(st.done[m[0]]?'✅ ':'⬜ ')+m[1]+'</li>'}).join('');
 var n=MIS.filter(function(m){return st.done[m[0]]}).length;document.getElementById('sima-msg').textContent=n===MIS.length?'🏆 ¡Todas las misiones completadas!':'Misiones: '+n+' de '+MIS.length;}
function libre(c,n){if(st.fs[c].indexOf(n)<0)return n;var p=n.lastIndexOf('.'),b=p>0?n.slice(0,p):n,e=p>0?n.slice(p):'',i=1,c2;
 do{c2=b+' (copia'+(i>1?' '+i:'')+')'+e;i++}while(st.fs[c].indexOf(c2)>=0);return c2}
function accion(a){var f=st.fs,c=st.cur;
 if(a==='copiar'||a==='cortar'){if(!st.sel.length)return msg('Primero selecciona uno o varios archivos.');st.clip={modo:a,de:c,items:st.sel.slice()};
  msg((a==='copiar'?'Copiado':'Cortado')+': '+st.sel.join(', ')+'. Ahora ve a la carpeta de destino y pulsa Pegar.');}
 else if(a==='pegar'){if(!st.clip)return msg('No hay nada copiado ni cortado.');if(c==='Papelera')return msg('No se puede pegar en la Papelera: usa «A la papelera».');
  var hechos=[];st.clip.items.forEach(function(n){if(st.fs[st.clip.de].indexOf(n)<0)return;
   if(st.clip.modo==='cortar'&&st.clip.de===c)return;var dest=libre(c,n);f[c].push(dest);hechos.push(dest);
   if(st.clip.modo==='cortar')f[st.clip.de].splice(f[st.clip.de].indexOf(n),1);});
  msg(hechos.length?(st.clip.modo==='copiar'?'Copiado aquí: ':'Movido aquí: ')+hechos.join(', ')+(hechos.some(function(h){return h.indexOf('(copia')>=0})?' · Ya había uno con ese nombre: se ha creado una copia con otro nombre.':''):'Nada que pegar aquí.');
  if(st.clip.modo==='cortar')st.clip=null;st.sel=hechos;}
 else if(a==='renombrar'){if(st.sel.length!==1)return msg('Selecciona un solo archivo para renombrarlo.');if(c==='Papelera')return msg('Restaura el archivo antes de renombrarlo.');
  var v=st.sel[0],nn=prompt('Nuevo nombre para «'+v+'»:',v);if(!nn||nn===v)return;nn=nn.trim();
  if(/[\/]/.test(nn))return msg('El nombre no puede contener «/».');if(f[c].indexOf(nn)>=0)return msg('Ya existe un archivo con ese nombre en esta carpeta.');
  f[c][f[c].indexOf(v)]=nn;st.sel=[nn];msg('Renombrado: «'+v+'» → «'+nn+'».');}
 else if(a==='carpeta'){if(c==='Papelera')return msg('No se pueden crear carpetas dentro de la Papelera.');var nc=prompt('Nombre de la nueva carpeta:','Nueva carpeta');if(!nc)return;nc=nc.trim();
  if(f[c].indexOf(nc)>=0)return msg('Ya existe algo con ese nombre.');f[c].push(nc);st.sel=[nc];msg('Carpeta «'+nc+'» creada en '+c+'.');}
 else if(a==='borrar'){if(!st.sel.length)return msg('Selecciona lo que quieres mandar a la Papelera.');if(c==='Papelera')return msg('Ya está en la Papelera. En Ubuntu, «Vaciar papelera» lo borraría para siempre.');
  st.sel.forEach(function(n){f[c].splice(f[c].indexOf(n),1);f.Papelera.push(n);st.origen[n]=c;});msg('Movido a la Papelera: '+st.sel.join(', ')+'. Puedes restaurarlo desde la Papelera.');st.sel=[];}
 else if(a==='restaurar'){if(c!=='Papelera'||!st.sel.length)return msg('Entra en la Papelera, selecciona el archivo y pulsa Restaurar.');
  st.sel.forEach(function(n){var o=st.origen[n]||'Documentos';f.Papelera.splice(f.Papelera.indexOf(n),1);f[o].push(libre(o,n));});msg('Restaurado a su carpeta original: '+st.sel.join(', ')+'.');st.sel=[];}
 pinta();}
box.addEventListener('click',function(e){var b=e.target.closest('button');if(!b)return;
 if(b.dataset.c){st.cur=b.dataset.c;st.sel=[];msg('Estás en '+st.cur+'.');pinta();}
 else if(b.dataset.f){var n=b.dataset.f;if(e.ctrlKey||e.metaKey){var i=st.sel.indexOf(n);if(i>=0)st.sel.splice(i,1);else st.sel.push(n);}else st.sel=[n];msg('Seleccionado: '+st.sel.join(', '));pinta();}
 else if(b.dataset.a)accion(b.dataset.a);
 box.focus({preventScroll:true});});
box.addEventListener('keydown',function(e){var k=e.key.toLowerCase(),m={c:'copiar',x:'cortar',v:'pegar'};
 if((e.ctrlKey||e.metaKey)&&m[k]){e.preventDefault();accion(m[k]);}
 else if((e.ctrlKey||e.metaKey)&&k==='a'){e.preventDefault();st.sel=st.fs[st.cur].slice();msg('Seleccionado todo.');pinta();}
 else if(e.key==='F2'){e.preventDefault();accion('renombrar');}else if(e.key==='Delete'){e.preventDefault();accion('borrar');}});
window.simaReset=function(){st=nuevo();msg('Haz clic en un archivo para seleccionarlo. Ctrl + clic selecciona varios.');pinta();};
simaReset();
})();
</script>"""

M10 = f"""
<div class="activity"><h3>📁 Manos a la obra con tus archivos</h3>
<p>En el módulo anterior conociste cómo se organizan las carpetas en Ubuntu. Ahora vas a aprender, paso a paso, las operaciones que harás constantemente en la aplicación <b>Archivos</b>: <b>seleccionar</b>, <b>copiar</b>, <b>mover</b>, <b>renombrar</b>, <b>borrar</b> y <b>recuperar</b>. Al final hay un <b>simulador</b> con misiones.</p></div>

<h3>1. Seleccionar</h3>
<table class="tbl"><tr><th>Quiero seleccionar…</th><th>Cómo</th></tr>
<tr><td>Un archivo</td><td>Un clic sobre él</td></tr>
<tr><td>Varios sueltos</td><td>Mantén {K("Ctrl")} y haz clic en cada uno</td></tr>
<tr><td>Varios seguidos</td><td>Clic en el primero, mantén {K("Mayús")} y clic en el último</td></tr>
<tr><td>Todos los de la carpeta</td><td>{K("Ctrl", "A")}</td></tr>
<tr><td>Un grupo con el ratón</td><td>Empieza a arrastrar desde un hueco vacío y dibuja un recuadro</td></tr></table>

<h3>2. Copiar y pegar (el original se queda donde estaba)</h3>
<ol class="steps">
<li>Selecciona el archivo o los archivos.</li>
<li>Pulsa {K("Ctrl", "C")} o haz clic derecho ▸ <b>Copiar</b>.</li>
<li>Entra en la carpeta de destino (por ejemplo, desde la barra lateral).</li>
<li>Pulsa {K("Ctrl", "V")} o haz clic derecho en un <b>hueco vacío</b> ▸ <b>Pegar</b>.</li>
</ol>

<h3>3. Mover: cortar y pegar (el original desaparece de su sitio)</h3>
<ol class="steps">
<li>Selecciona y pulsa {K("Ctrl", "X")} (o clic derecho ▸ <b>Cortar</b>).</li>
<li>Ve a la carpeta de destino y pulsa {K("Ctrl", "V")}.</li>
</ol>
<div class="tip-box">💡 <b>Con el ratón:</b> arrastra el archivo hasta otra carpeta. <b>Dentro del mismo disco se mueve</b>; si lo sueltas en otro disco (por ejemplo, un USB) <b>se copia</b>. Si mantienes pulsada {K("Ctrl")} al soltar, se copia en lugar de moverse. También puedes usar clic derecho ▸ <b>Copiar a…</b> o <b>Mover a…</b> para elegir el destino en una ventana.</div>

<h3>4. ¿Y si ya existe un archivo con ese nombre?</h3>
<ul class="key-points"><li>📄 <span>Si pegas en la <b>misma carpeta</b>, Archivos crea una copia con otro nombre, por ejemplo <code>foto (copia).jpg</code>.</span></li>
<li>⚠️ <span>Si en la carpeta de destino ya hay uno con el mismo nombre, te pregunta qué hacer: <b>reemplazarlo</b> (se pierde el que había), <b>omitir</b> ese archivo, o ponerle <b>otro nombre</b>. Lee el aviso antes de pulsar.</span></li></ul>

<h3>5. Renombrar</h3>
<ol class="steps">
<li>Selecciona el archivo y pulsa {K("F2")} (o clic derecho ▸ <b>Renombrar…</b>).</li>
<li>Escribe el nuevo nombre. Archivos selecciona solo el nombre, <b>sin la extensión</b> (<code>.odt</code>, <code>.jpg</code>…), para que no la borres sin querer.</li>
<li>Pulsa {K("Intro")}.</li>
</ol>
<p>Si seleccionas <b>varios</b> archivos y pulsas {K("F2")}, puedes renombrarlos todos a la vez (por ejemplo, <code>viaje_1.jpg</code>, <code>viaje_2.jpg</code>…).</p>

<h3>6. Crear carpetas</h3>
<p>Clic derecho en un hueco ▸ <b>Nueva carpeta…</b>, o {K("Ctrl", "Mayús", "N")}. Escribe el nombre y pulsa {K("Intro")}.</p>

<h3>7. Borrar y recuperar</h3>
<table class="tbl"><tr><th>Acción</th><th>Cómo</th><th>¿Se puede recuperar?</th></tr>
<tr><td>Mandar a la Papelera</td><td>{K("Supr")} o clic derecho ▸ <b>Mover a la papelera</b></td><td>✅ Sí</td></tr>
<tr><td>Deshacer justo después</td><td>Botón <b>Deshacer</b> del aviso que aparece abajo, o {K("Ctrl", "Z")}</td><td>✅ Sí</td></tr>
<tr><td>Restaurar desde la Papelera</td><td>Abre <b>Papelera</b> en la barra lateral ▸ clic derecho ▸ <b>Restaurar desde la papelera</b></td><td>✅ Vuelve a su carpeta original</td></tr>
<tr><td>Vaciar la Papelera</td><td>En la Papelera, botón <b>Vaciar</b></td><td>❌ No</td></tr>
<tr><td>Borrar directamente</td><td>{K("Mayús", "Supr")} (pide confirmación)</td><td>❌ No</td></tr></table>

<h3>8. Más cosas útiles con el clic derecho</h3>
<ul class="key-points">
<li>📂 <span><b>Abrir con…</b>: elige con qué aplicación abrir el archivo (por ejemplo, una foto con el editor en lugar del visor).</span></li>
<li>🗜️ <span><b>Comprimir…</b>: junta varios archivos en un <code>.zip</code> para enviarlos. Para abrir un <code>.zip</code> recibido: clic derecho ▸ <b>Extraer</b>.</span></li>
<li>ℹ️ <span><b>Propiedades</b>: tamaño, ubicación, fecha y permisos.</span></li>
<li>⭐ <span><b>Destacar</b>: lo añade a «Destacados» en la barra lateral para encontrarlo rápido.</span></li></ul>

<h3>9. Copiar a una memoria USB</h3>
<ol class="steps">
<li>Conecta el USB: aparece en la barra lateral de Archivos.</li>
<li>Copia los archivos con {K("Ctrl", "C")} y pégalos dentro del USB con {K("Ctrl", "V")} (o arrástralos: al ser otro disco, se copian).</li>
<li>Espera a que termine la copia (verás el progreso arriba a la derecha).</li>
<li>Pulsa el botón de <b>expulsar</b> ⏏ junto al nombre del USB y retíralo cuando desaparezca.</li>
</ol>

<h3>10. Practica en el simulador</h3>
<p>Este explorador es una <b>simulación simplificada</b> de Archivos. Usa los botones o, con el simulador seleccionado, los atajos {K("Ctrl", "C")}, {K("Ctrl", "X")}, {K("Ctrl", "V")}, {K("Ctrl", "A")}, {K("F2")} y {K("Supr")}.</p>
{SIM_ARCHIVOS}

{ejercicio("u10a", "Copiar o mover", "Quieres llevar una foto a otra carpeta y que siga también en la original. ¿Qué haces?", ["Cortar (Ctrl + X) y pegar", "Copiar (Ctrl + C) y pegar (Ctrl + V) en la carpeta de destino", "Pulsar Mayús + Supr", "Renombrarla con F2"], 1, "Copiar deja el original en su sitio; cortar lo quita.")}
{ejercicio("u10b", "Varios sueltos", "¿Cómo seleccionas varios archivos que no están seguidos?", ["Con doble clic en cada uno", "Manteniendo pulsada Ctrl mientras haces clic en cada uno", "Pulsando F2", "Con Alt + F4"], 1, "Ctrl + clic añade o quita archivos de la selección uno a uno.")}
{ejercicio("u10c", "Recuperar", "Has mandado un archivo a la Papelera por error. ¿Cómo lo recuperas?", ["No se puede recuperar", "Reinstalando Ubuntu", "Abriendo la Papelera, clic derecho sobre él ▸ Restaurar desde la papelera", "Pulsando Mayús + Supr"], 2, "Mientras no vacíes la Papelera, el archivo se puede restaurar a su carpeta original.")}
{ejercicio("u10d", "Arrastrar al USB", "Arrastras un archivo desde Documentos hasta tu memoria USB. ¿Qué ocurre?", ["Se mueve y desaparece de Documentos", "Se copia: al ser otro disco, el original se queda en Documentos", "Se borra", "Se comprime"], 1, "Entre discos distintos, arrastrar copia; dentro del mismo disco, mueve.")}
<div class="summary-box">🎯 <b>Idea clave:</b> {K("Ctrl", "C")} copia, {K("Ctrl", "X")} corta, {K("Ctrl", "V")} pega; {K("F2")} renombra; {K("Supr")} manda a la Papelera, de donde aún puedes restaurar. Antes de vaciarla o de pulsar {K("Mayús", "Supr")}, piénsalo dos veces.</div>
"""

wr("modulo8.html", pagina(8, "🖱️", "Práctica: abrir, organizar y cerrar ventanas",
                           "Paso a paso y con un simulador: abrir aplicaciones, mover, maximizar, minimizar y cerrar ventanas.", M8, JS_VENTANAS))
wr("modulo10.html", pagina(10, "📋", "Práctica: copiar, pegar, mover, renombrar y borrar archivos",
                            "Paso a paso y con un simulador: todo lo que harás a diario en la aplicación Archivos.", M10, JS_ARCHIVOS))

# 5. Estilos de los simuladores -----------------------------------------------------------------
css = rd("style.css")
if ".sim{" not in css:
    css += """
/* Simuladores de escritorio y de Archivos (módulos 8 y 10) */
.sim{border-radius:12px;overflow:hidden;border:1px solid #444;margin:16px 0;background:#2c001e;user-select:none;outline:none}
.sim:focus{box-shadow:0 0 0 3px #E95420}
.sim-top{display:flex;justify-content:space-between;background:#111;color:#eee;font-size:13px;padding:5px 12px}
.sim-body{display:flex;height:340px}
.sim-dock{width:58px;background:rgba(0,0,0,.55);display:flex;flex-direction:column;gap:6px;padding:8px 6px}
.sim-app{width:46px;height:46px;border:0;border-radius:10px;background:rgba(255,255,255,.12);font-size:24px;cursor:pointer;position:relative}
.sim-app:hover{background:rgba(255,255,255,.25)}
.sim-app.abierta:after{content:"";position:absolute;left:-4px;top:19px;width:5px;height:8px;border-radius:3px;background:#E95420}
.sim-desk{flex:1;position:relative;overflow:hidden;background:linear-gradient(135deg,#77216F,#2c001e)}
.sim-hint{color:#fff;opacity:.85;text-align:center;margin-top:140px;font-size:15px}
.sim-win{position:absolute;width:300px;max-width:85%;background:#fff;border-radius:10px;box-shadow:0 8px 24px rgba(0,0,0,.45);overflow:hidden}
.sim-win.max{left:0!important;top:0!important;width:100%;max-width:100%;height:100%;border-radius:0}
.sim-title{display:flex;justify-content:space-between;align-items:center;background:#ebebeb;padding:6px 8px;font-weight:700;font-size:14px;cursor:move;touch-action:none}
.sim-btns button{width:24px;height:24px;border-radius:50%;border:0;background:#d4d4d4;margin-left:4px;cursor:pointer;font-size:12px;line-height:24px;padding:0}
.sim-btns button.x{background:#E95420;color:#fff}
.sim-cont{padding:18px 14px;font-size:14px;color:#333;min-height:90px}
.sim-tools{display:flex;flex-wrap:wrap;gap:4px;background:#ebebeb;padding:6px}
.sim-tools button{border:1px solid #c8c8c8;background:#fff;border-radius:6px;padding:5px 8px;cursor:pointer;font-size:13px}
.sim-tools button small{color:#888}
.sim-fm{display:flex;background:#fff;min-height:220px}
.sim-side{width:150px;background:#f4f4f4;padding:6px;display:flex;flex-direction:column;gap:2px}
.sim-side button{text-align:left;border:0;background:none;padding:7px 8px;border-radius:6px;cursor:pointer;font-size:14px}
.sim-side button.on{background:#E95420;color:#fff}
.sim-files{flex:1;display:flex;flex-wrap:wrap;align-content:flex-start;gap:8px;padding:10px}
.sim-file{width:110px;border:2px solid transparent;background:none;border-radius:8px;padding:6px;cursor:pointer;font-size:12px;word-break:break-all}
.sim-file span{display:block;font-size:30px}
.sim-file.sel{background:#fbe1d6;border-color:#E95420}
.sim-status{background:#f4f4f4;border-top:1px solid #ddd;color:#333;font-size:13px;padding:6px 10px;min-height:20px}
.missions-box{background:#fff8f3;border:2px solid #E95420;border-radius:12px;padding:12px 16px;margin:10px 0 20px}
.missions-box .checks{list-style:none;margin:8px 0;padding:0}
.missions-box .checks li{padding:3px 0}
.missions-box .checks li.ok{color:#2e7d32;font-weight:600}
@media (max-width:600px){.sim-side{width:96px}.sim-side button{font-size:12px;padding:6px 4px}.sim-file{width:84px}.sim-body{height:300px}}
"""
    wr("style.css", css)

# 6. Portada: itinerario ------------------------------------------------------------------------
s = rd("index.html")
titulos = {n: re.search(r"<title>(.*?)</title>", rd(f"modulo{n}.html")).group(1) for n in range(1, TOTAL + 1)}
lista = "".join(f'<li><span><b>{n}.</b></span><span><a href="modulo{n}.html">{titulos[n]}</a></span></li>' for n in range(1, TOTAL + 1))
viejo = re.search(r'(<h3>Contenido</h3>\s*<ul class="key-points">)(.*?)(</ul>)', s, re.S)
fin = re.search(r'<li><span>🏁.*?</li>', viejo.group(2))
s = s.replace(viejo.group(0), viejo.group(1) + lista + (fin.group(0) if fin else "") + viejo.group(3))
s = sub1(s, "<div class=\"app-tile\"><div class=\"app-ico\">🖥️</div><b>Usar</b><span>Escritorio, ventanas, archivos</span></div>",
         "<div class=\"app-tile\"><div class=\"app-ico\">🖥️</div><b>Usar</b><span>Ventanas y archivos, con simuladores</span></div>", "index.html")
wr("index.html", s)

# 7. Examen: dos preguntas por módulo nuevo ------------------------------------------------------
s = rd("examen_final.html")
qs = json.loads(re.search(r"const qs=(\[.*?\]);", s, re.S).group(1))
p8 = [["¿Qué ocurre al hacer doble clic en la barra de título de una ventana?", "Se maximiza, o vuelve a su tamaño si ya estaba maximizada", "Se cierra", "Se minimiza al Dock", "Se mueve a otro espacio de trabajo"],
      ["¿Qué diferencia hay entre Ctrl + W y Ctrl + Q?", "Ctrl + W cierra la pestaña o documento actual y Ctrl + Q sale de la aplicación entera", "Son exactamente iguales", "Ctrl + W guarda y Ctrl + Q imprime", "Ctrl + Q cierra solo una pestaña"]]
p10 = [["Quieres llevar una foto a otra carpeta y que siga también en la original. ¿Qué haces?", "Copiar (Ctrl + C) y pegar (Ctrl + V) en la carpeta de destino", "Cortar (Ctrl + X) y pegar", "Pulsar Mayús + Supr", "Renombrarla con F2"],
       ["Has mandado un archivo a la Papelera por error. ¿Cómo lo recuperas?", "Abres la Papelera, clic derecho sobre él y «Restaurar desde la papelera»", "No se puede recuperar", "Reinstalando Ubuntu", "Pulsando Mayús + Supr"]]
i7 = next(i for i, q in enumerate(qs) if q[1] == "Super + flecha izquierda")
i8 = next(i for i, q in enumerate(qs) if q[1] == "Ctrl + H")
qs = qs[:i7 + 1] + p8 + qs[i7 + 1:i8 + 1] + p10 + qs[i8 + 1:]
nuevo_js = "const qs=" + json.dumps(qs, ensure_ascii=False).replace('], [', '],\n  [') + ";"
s = re.sub(r"const qs=\[.*?\];", lambda m: nuevo_js, s, count=1, flags=re.S)
s = s.replace("scormGo('modulo15.html')", f"scormGo('modulo{TOTAL}.html')")
s = re.sub(r"(⬅️[^<]*?)15", lambda m: m.group(1) + str(TOTAL), s, count=1)
s = re.sub(r"\b31 preguntas\b", f"{len(qs)} preguntas", s)
wr("examen_final.html", s)

# 8. Banco GIFT --------------------------------------------------------------------------------
g = rd("preguntas_moodle.gift")
def cat(m):
    n = int(m.group(1))
    return f"$CATEGORY: Curso Ubuntu/Módulo {MAPA[n]} - "
g = re.sub(r"\$CATEGORY: Curso Ubuntu/Módulo (\d+) - ", cat, g)
def bloque(n, titulo, preguntas, inicio):
    out = [f"$CATEGORY: Curso Ubuntu/Módulo {n} - {titulo}", ""]
    for k, (q, ok, *mal) in enumerate(preguntas):
        esc = lambda t: re.sub(r"([~=#{}:])", r"\\\1", t)
        out += [f"::UB{inicio + k}::{esc(q)} {{", f"={esc(ok)}"] + [f"~{esc(x)}" for x in mal] + ["}", ""]
    return "\n".join(out)
num = max(int(x) for x in re.findall(r"::UB(\d+)::", g)) + 1
b8 = bloque(8, "Práctica - abrir, organizar y cerrar ventanas", p8 + [["Una aplicación no responde y aparece un aviso. ¿Qué botón la cierra a la fuerza?", "Forzar salida", "Esperar", "Minimizar", "Maximizar"]], num)
b10 = bloque(10, "Práctica - copiar, pegar, mover, renombrar y borrar archivos", p10 + [["¿Cómo seleccionas varios archivos que no están seguidos?", "Manteniendo pulsada Ctrl mientras haces clic en cada uno", "Con doble clic en cada uno", "Pulsando F2", "Con Alt + F4"]], num + 3)
g = sub1(g, "$CATEGORY: Curso Ubuntu/Módulo 9 - Archivos y carpetas", b8 + "\n$CATEGORY: Curso Ubuntu/Módulo 9 - Archivos y carpetas", "gift")
g = sub1(g, "$CATEGORY: Curso Ubuntu/Módulo 11 - Tus aplicaciones del día a día", b10 + "\n$CATEGORY: Curso Ubuntu/Módulo 11 - Tus aplicaciones del día a día", "gift")
g = g.replace("(15 categorías", f"({TOTAL} categorías")
wr("preguntas_moodle.gift", g)
n_gift = len(re.findall(r"(?m)^::", g))

# 9. README ------------------------------------------------------------------------------------
r = rd("README.txt")
r = sub1(r, "ventanas y atajos, archivos y carpetas,", "ventanas y atajos (con práctica guiada y simulador), archivos y carpetas (con práctica guiada\nde copiar, pegar, mover, renombrar y borrar, y simulador),", "README")
r = sub1(r, "- imsmanifest.xml: paquete SCORM 1.2 empaquetado como un único SCO (seguimiento correcto en Moodle).",
         "- imsmanifest.xml: paquete SCORM 1.2 con un SCO por página (el índice de Moodle se marca al avanzar).", "README")
r = sub1(r, "- modulo1.html ... modulo15.html: 15 módulos", f"- modulo1.html ... modulo{TOTAL}.html: {TOTAL} módulos", "README")
r = sub1(r, "un simulador de terminal (módulo 13).", "un simulador de terminal (módulo 15), un simulador de escritorio (módulo 8) y un\n  simulador de la aplicación Archivos (módulo 10).", "README")
r = re.sub(r"examen final interactivo de \d+ preguntas", f"examen final interactivo de {len(qs)} preguntas", r)
r = re.sub(r"\d+ preguntas en formato GIFT \(\d+ categorías", f"{n_gift} preguntas en formato GIFT ({TOTAL} categorías", r)
tem = "\n".join(f"{n}. {titulos[n]}" for n in range(1, TOTAL + 1))
r = re.sub(r"Temario:\n(?:\d+\..*\n)+", "Temario:\n" + tem + "\n", r)
wr("README.txt", r)
print(f"Ampliado: {TOTAL} módulos, examen de {len(qs)} preguntas, GIFT de {n_gift}.")
