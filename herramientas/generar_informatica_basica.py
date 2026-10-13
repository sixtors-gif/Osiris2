#!/usr/bin/env python3
"""Genera el curso SCORM «Informática básica para jóvenes».

Uso (desde la raíz del repositorio):
  python3 herramientas/generar_informatica_basica.py cursos/Curso_Informatica_Basica_Jovenes_SCORM
  python3 herramientas/generar_informatica_basica_imagenes.py cursos/Curso_Informatica_Basica_Jovenes_SCORM
  python3 herramientas/scorm_seguimiento.py
"""
import html, json, os, shutil, sys

OUT = sys.argv[1]
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
os.makedirs(os.path.join(OUT, "img"), exist_ok=True)
TITULO = "Informática básica para jóvenes"
FOOTER = f"{TITULO} · Material educativo · Creado por: Sixto Rodríguez de Sepúlveda"

# Estilo común de los cursos para jóvenes + piezas propias de este curso
base = open(os.path.join(RAIZ, "cursos", "CiberSeguridad_Avanzada", "style.css"), encoding="utf-8").read()
extra = """
/* Informática básica */
.figure img{max-width:100%;height:auto;border-radius:10px}
.tabla-wrap{overflow-x:auto;margin:16px 0}
.tabla{border-collapse:collapse;width:100%;font-size:1em}
.tabla th{background:#1e3c72;color:#fff;padding:9px 10px;text-align:left}
.tabla td{border:1px solid #dfe5ef;padding:9px 10px;vertical-align:top}
.tabla tr:nth-child(even) td{background:#f4f7fb}
.clasifica{display:grid;grid-template-columns:1fr auto;gap:8px 14px;align-items:center;margin:12px 0}
.clasifica select{padding:8px;border-radius:8px;border:1px solid #bbb;font:inherit}
.checklist label{display:block;padding:7px 0}
.checklist input{width:auto;margin-right:8px}
.num{max-width:160px}
"""
open(os.path.join(OUT, "style.css"), "w", encoding="utf-8").write(base + extra)
shutil.copy(os.path.join(RAIZ, "cursos", "CiberSeguridad_Avanzada", "img", "logo-centro.png"), os.path.join(OUT, "img", "logo-centro.png"))

N = 12


def fig(img, alt, cap):
    return f'<div class="figure"><img src="img/{img}" alt="{html.escape(alt, quote=True)}"><div class="figure-caption">{cap}</div></div>'


def kp(items, ico):
    return '<ul class="key-points">' + "".join(f'<li>{ico} <span>{i}</span></li>' for i in items) + '</ul>'


def cards(items):
    return '<div class="card-grid">' + "".join(
        f'<div class="mini-card"><div class="ico">{i}</div><b>{t}</b><span class="small">{d}</span></div>' for i, t, d in items) + '</div>'


def flow(steps):
    out = []
    for i, s in enumerate(steps):
        if i: out.append('<span class="flow-arrow">➜</span>')
        out.append(f'<div class="flow-step">{s}</div>')
    return '<div class="flow">' + "".join(out) + '</div>'


def quiz(qid, q, opts, ok, why):
    btns = "".join(f'<button class="option" onclick="checkAnswer(this,{str(j == ok).lower()},\'{qid}\')">{chr(65+j)}. {o}</button>'
                   for j, o in enumerate(opts))
    return (f'<div class="quiz"><h4>🧩 {q}</h4><div class="options">{btns}</div>'
            f'<p class="feedback" id="fb-{qid}" data-ok="{html.escape(why, quote=True)}"></p></div>')


def activity(title, txt, ph):
    return (f'<div class="activity"><h3>✍️ {title}</h3><p>{txt}</p><textarea placeholder="{ph}"></textarea></div>')


def tabla(cab, filas):
    return ('<div class="tabla-wrap"><table class="tabla"><tr>' + "".join(f"<th>{c}</th>" for c in cab) + "</tr>"
            + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in f) + "</tr>" for f in filas) + "</table></div>")


SCRIPT = """<script>
function checkAnswer(btn,ok,id){var p=btn.parentElement;p.querySelectorAll('.option').forEach(function(b){b.classList.remove('correct','incorrect')});btn.classList.add(ok?'correct':'incorrect');var fb=document.getElementById('fb-'+id);fb.textContent=ok?'✅ ¡Correcto! '+fb.getAttribute('data-ok'):'❌ No es correcto. Vuelve a leer el apartado e inténtalo de nuevo.';}
function checkNum(id,exp,fb,msg){var s=String(document.getElementById(id).value).trim(),e=document.getElementById(fb);
// Acepta 37,5 / 37.5 / 3.072 / 3072: prueba el punto como decimal y como separador de miles.
var c=[parseFloat(s.replace(/\\./g,'').replace(',','.')),parseFloat(s.replace(',','.'))];if(c.some(function(v){return isFinite(v)&&Math.abs(v-exp)<0.01})){e.textContent='✅ '+msg;}else{e.textContent='❌ Todavía no. Repasa la tabla y prueba de nuevo.';}}
function checkClasifica(id){var ok=0,t=0;document.querySelectorAll('#'+id+' select').forEach(function(s){t++;var bien=s.value===s.getAttribute('data-ok');if(bien)ok++;s.style.borderColor=s.value?(bien?'#4caf50':'#f44336'):'#bbb';});document.getElementById(id+'-fb').textContent=(ok===t?'✅ ¡Perfecto! ':'Llevas ')+ok+' de '+t+' bien.'+(ok===t?'':' Las que están en rojo merecen otra vuelta.');}
</script>"""


def page(n, icon, title, sub, body):
    prev = "index.html" if n == 1 else f"modulo{n-1}.html"
    nxt = "examen_final.html" if n == N else f"modulo{n+1}.html"
    lbl = "Ir al examen final 🏁" if n == N else "Siguiente módulo ➡️"
    return f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Módulo {n}: {title}</title>
<link rel="stylesheet" href="style.css">
</head>
<body>
<div class="container">
  <div class="header">
    <h1><span class="shield-icon">{icon}</span>Módulo {n}: {title}</h1>
    <img src="img/logo-centro.png" class="logo-centro" alt="Logotipo del centro">
    <p>{sub}</p>
  </div>
  <div class="progress-container">
    <div class="progress-bar"><div class="progress-fill" style="width:{round(n*100/(N+1))}%"></div></div>
    <div class="progress-text">Informática básica · Módulo {n} de {N}</div>
  </div>
  <div class="content-area">
    <section class="module">
{body}
      <div class="navigation">
        <button class="nav-btn" onclick="scormGo('{prev}')">⬅️ Anterior</button>
        <button class="nav-btn" onclick="scormGo('{nxt}')">{lbl}</button>
      </div>
    </section>
  </div>
</div>
<footer class="footer-autor">{FOOTER}</footer>
<script src="scorm.js"></script>
{SCRIPT}
</body>
</html>
"""


M = []
# 1 -----------------------------------------------------------------------------
M.append(("💻", "¿Qué es un ordenador?", "Una máquina que recibe datos, los procesa y te devuelve un resultado.", f"""
      <h2>Una máquina que sigue instrucciones</h2>
      <p>Un <b>ordenador</b> es una máquina electrónica que recibe <b>datos</b>, los <b>procesa</b> siguiendo instrucciones (programas) y devuelve un <b>resultado</b>. No piensa por sí mismo: hace exactamente lo que le dicen los programas, pero a una velocidad enorme.</p>
      {fig("entrada_proceso_salida.svg", "Esquema: entrada, proceso, salida y almacenamiento", "El ciclo de cualquier ordenador: entrada → proceso → salida, guardando lo necesario en el almacenamiento.")}
      <h3>El ciclo, con un ejemplo</h3>
      {flow(["⌨️ Escribes un mensaje (entrada)", "🧠 El procesador lo prepara (proceso)", "📱 Aparece en la pantalla (salida)", "💾 Se guarda en el chat (almacenamiento)"])}
      <h3>Hay ordenadores por todas partes</h3>
      {cards([("🖥️","Sobremesa","Potente y ampliable; no se mueve de la mesa."),("💻","Portátil","Todo en uno con batería; para llevar."),("📱","Móvil y tablet","Ordenadores de bolsillo con pantalla táctil."),("🎮","Consola","Ordenador especializado en juegos."),("⌚","Reloj inteligente","Pequeño, con sensores."),("🚗","Integrados","En coches, lavadoras o semáforos.")])}
      <div class="box tip"><b>Dos palabras clave:</b> el <b>hardware</b> es todo lo que puedes tocar (piezas y aparatos) y el <b>software</b> son los programas y datos que lo hacen funcionar. Los verás a fondo en los próximos módulos.</div>
      {quiz("m1a", "Haces una foto con el móvil. ¿Qué parte del ciclo es pulsar el botón de la cámara?", ["Salida", "Entrada", "Almacenamiento"], 1, "La cámara y el botón introducen datos en el dispositivo.")}
      {quiz("m1b", "¿Cuál de estos aparatos también es un ordenador?", ["Una consola de videojuegos", "Una bicicleta", "Una lámpara de mesa normal"], 0, "Tiene procesador, memoria, almacenamiento y ejecuta programas.")}
      {activity("Actividad: ordenadores a tu alrededor", "Haz una lista de 5 aparatos de tu casa que lleven un ordenador dentro. Para cada uno, indica cuál es su entrada y su salida.", "Ejemplo: microondas → entrada: botones; salida: pantalla y pitido")}
      <div class="summary-box"><b>Resumen:</b> un ordenador recibe datos (entrada), los procesa, muestra resultados (salida) y guarda información (almacenamiento).</div>
"""))
# 2 -----------------------------------------------------------------------------
M.append(("🔩", "Hardware: el ordenador por dentro", "Conoce las piezas principales y para qué sirve cada una.", f"""
      <h2>¿Qué hay dentro de la caja?</h2>
      <p>Si abrimos un ordenador de sobremesa encontramos varias piezas conectadas a una gran tarjeta llamada <b>placa base</b>. En un portátil o un móvil están las mismas piezas, pero mucho más pequeñas y juntas.</p>
      {fig("ordenador_por_dentro.svg", "Torre abierta con procesador, memoria RAM, placa base, tarjeta gráfica, disco SSD, disco duro, fuente de alimentación y ventilador", "Las piezas principales de un ordenador de sobremesa.")}
      {tabla(["Pieza", "Qué hace", "Compáralo con…"], [
        ["<b>Placa base</b>", "Conecta todas las piezas entre sí.", "Las calles de una ciudad."],
        ["<b>Procesador (CPU)</b>", "Ejecuta las instrucciones de los programas.", "El cerebro."],
        ["<b>Memoria RAM</b>", "Guarda lo que estás usando <i>ahora</i>. Se borra al apagar.", "La mesa de estudio: cuanto más grande, más cosas abiertas a la vez."],
        ["<b>Almacenamiento (SSD/HDD)</b>", "Guarda archivos y programas aunque se apague.", "La estantería o el armario."],
        ["<b>Tarjeta gráfica (GPU)</b>", "Calcula las imágenes que ves (juegos, vídeo, 3D).", "Un artista especializado en dibujar."],
        ["<b>Fuente de alimentación</b>", "Transforma la corriente del enchufe para las piezas.", "El corazón que reparte energía."],
        ["<b>Ventiladores y disipador</b>", "Evitan que las piezas se calienten demasiado.", "El aire acondicionado."]])}
      <div class="alert-box"><b>RAM no es lo mismo que almacenamiento.</b> Un móvil «de 8 GB de RAM y 256 GB» tiene 8 GB para trabajar con lo que tienes abierto y 256 GB para guardar fotos, apps y archivos.</div>
      <h3>¿Qué hace que un ordenador vaya rápido?</h3>
      {kp(["Un <b>procesador</b> moderno con varios <b>núcleos</b> (trabajadores en paralelo).", "Suficiente <b>RAM</b> para lo que usas (hoy, 8 GB como mínimo; 16 GB va holgado).", "Un <b>SSD</b> en lugar de un disco duro mecánico: arranca y abre programas mucho antes."], "⚡")}
      {quiz("m2a", "Tienes muchas pestañas y programas abiertos y todo va lento. ¿Qué pieza se está quedando corta probablemente?", ["La memoria RAM", "La fuente de alimentación", "El ventilador"], 0, "La RAM guarda lo que tienes abierto; si se llena, el equipo se ralentiza.")}
      {quiz("m2b", "¿Qué pieza conserva tus fotos aunque apagues el ordenador?", ["La RAM", "El almacenamiento (SSD o disco duro)", "El procesador"], 1, "La RAM se borra al apagar; el almacenamiento, no.")}
      <div class="summary-box"><b>Resumen:</b> placa base (conecta), CPU (piensa), RAM (trabajo del momento), almacenamiento (guarda), GPU (imágenes), fuente (energía) y refrigeración (temperatura).</div>
"""))
# 3 -----------------------------------------------------------------------------
sel = lambda ok: f'<select data-ok="{ok}"><option value="">— elige —</option><option value="e">Entrada</option><option value="s">Salida</option><option value="m">Mixto</option></select>'
M.append(("🖱️", "Periféricos: entrada, salida y mixtos", "Los aparatos que conectas al ordenador para comunicarte con él.", f"""
      <h2>¿Qué es un periférico?</h2>
      <p>Un <b>periférico</b> es cualquier aparato que se conecta al ordenador para meter información, sacarla o las dos cosas. Se clasifican según hacia dónde viajan los datos.</p>
      {fig("perifericos.svg", "Periféricos de entrada, de salida y mixtos", "Entrada: los datos entran al ordenador. Salida: salen hacia ti. Mixtos: en los dos sentidos.")}
      {cards([("⬅️","Entrada","Teclado, ratón, micrófono, cámara web, escáner, lector de huellas, mando de juego."),("➡️","Salida","Monitor, altavoces, impresora, proyector."),("↔️","Mixtos (entrada/salida)","Pantalla táctil, cascos con micrófono, memoria USB, impresora multifunción.")])}
      <h3>¿Cómo se conectan?</h3>
      {tabla(["Conexión", "Para qué se usa"], [["<b>USB</b> (tipo A y tipo C)", "Ratón, teclado, memorias, móvil, carga… El USB-C es reversible."], ["<b>HDMI</b> / <b>DisplayPort</b>", "Monitores, televisores y proyectores."], ["<b>Jack de 3,5 mm</b>", "Auriculares y altavoces con cable."], ["<b>Bluetooth</b>", "Sin cables: auriculares, ratones, teclados, altavoces."]])}
      <div class="activity" id="clasif">
        <h3>🧩 Ejercicio: clasifica los periféricos</h3>
        <div class="clasifica">
          <span>⌨️ Teclado</span>{sel("e")}
          <span>🖨️ Impresora (solo imprime)</span>{sel("s")}
          <span>📱 Pantalla táctil</span>{sel("m")}
          <span>🎤 Micrófono</span>{sel("e")}
          <span>🔊 Altavoces</span>{sel("s")}
          <span>🎧 Cascos con micrófono</span>{sel("m")}
          <span>📷 Cámara web</span>{sel("e")}
          <span>📽️ Proyector</span>{sel("s")}
        </div>
        <button class="btn" onclick="checkClasifica('clasif')">Comprobar</button>
        <p class="feedback" id="clasif-fb"></p>
      </div>
      {quiz("m3a", "Una memoria USB, ¿qué tipo de periférico es?", ["Solo de entrada", "Solo de salida", "Mixto: se leen y se escriben datos"], 2, "El ordenador lee y escribe en ella.")}
      <div class="summary-box"><b>Resumen:</b> entrada (los datos entran), salida (salen hacia ti) y mixtos (en ambos sentidos).</div>
"""))
# 4 -----------------------------------------------------------------------------
M.append(("🔢", "Bits y bytes: medir la información", "Aprende las unidades que verás en móviles, archivos y tarifas de datos.", f"""
      <h2>Todo son ceros y unos</h2>
      <p>Dentro del ordenador toda la información (textos, fotos, música, vídeos) se guarda como combinaciones de <b>0 y 1</b>. Cada 0 o 1 es un <b>bit</b>, la unidad más pequeña. Ocho bits forman un <b>byte</b>, que es más o menos lo que ocupa una letra.</p>
      {fig("unidades_informacion.svg", "Escalera de unidades: bit, byte, KB, MB, GB y TB", "Cada escalón es unas mil veces más grande que el anterior.")}
      {tabla(["Unidad", "Equivale a", "Ejemplo"], [["1 byte (B)", "8 bits", "una letra"], ["1 kilobyte (KB)", "1024 bytes", "un texto corto"], ["1 megabyte (MB)", "1024 KB", "una foto o una canción (3–5 MB)"], ["1 gigabyte (GB)", "1024 MB", "una película (1–4 GB)"], ["1 terabyte (TB)", "1024 GB", "cientos de miles de fotos"]])}
      <div class="box tip"><b>¿1000 o 1024?</b> Los ordenadores cuentan en potencias de 2 (1024), pero los fabricantes de discos usan 1000. Por eso un disco «de 1 TB» aparece en Windows como unos <b>931 GB</b>: no falta espacio, solo se cuenta distinto.</div>
      <div class="alert-box"><b>Ojo con la «b»:</b> las velocidades de Internet se miden en <b>bits</b> por segundo (Mb/s, con «b» minúscula). Una fibra de 600 Mb/s descarga como mucho unos 75 MB por segundo (600 ÷ 8).</div>
      <div class="activity"><h3>🧮 Calcula</h3>
        <p>1) ¿Cuántos MB son 3 GB? (usa 1 GB = 1024 MB)</p>
        <input id="c1" class="num" placeholder="MB"> <button class="btn" onclick="checkNum('c1',3072,'f1','Correcto: 3 × 1024 = 3072 MB.')">Comprobar</button><p class="feedback" id="f1"></p>
        <p>2) Tu móvil tiene 64 GB libres y cada vídeo ocupa 2 GB. ¿Cuántos vídeos caben?</p>
        <input id="c2" class="num" placeholder="vídeos"> <button class="btn" onclick="checkNum('c2',32,'f2','Correcto: 64 ÷ 2 = 32 vídeos.')">Comprobar</button><p class="feedback" id="f2"></p>
        <p>3) Una fibra de 300 Mb/s, ¿cuántos MB descarga como máximo por segundo?</p>
        <input id="c3" class="num" placeholder="MB/s"> <button class="btn" onclick="checkNum('c3',37.5,'f3','Correcto: 300 ÷ 8 = 37,5 MB por segundo.')">Comprobar</button><p class="feedback" id="f3"></p>
      </div>
      {quiz("m4a", "¿Qué es más grande?", ["500 MB", "1 GB", "900 KB"], 1, "1 GB son 1024 MB.")}
      <div class="summary-box"><b>Resumen:</b> bit → byte (×8) → KB → MB → GB → TB (cada uno ×1024). Internet se mide en bits por segundo.</div>
"""))
# 5 -----------------------------------------------------------------------------
M.append(("💾", "Almacenamiento: dónde se guardan tus archivos", "Discos duros, SSD, memorias USB, tarjetas y la nube.", f"""
      <h2>Guardar para no perder</h2>
      <p>El <b>almacenamiento</b> conserva tus archivos y programas aunque apagues el aparato. Hay varios tipos, cada uno con sus ventajas.</p>
      {fig("tipos_almacenamiento.svg", "Disco duro, SSD, memoria USB, tarjeta SD y nube", "Tipos de almacenamiento más comunes.")}
      {tabla(["Tipo", "Ventajas", "Inconvenientes"], [
        ["<b>Disco duro (HDD)</b>", "Mucha capacidad por poco dinero.", "Lento y delicado: tiene piezas que giran."],
        ["<b>SSD</b>", "Muy rápido, silencioso y resistente a golpes.", "Algo más caro por GB."],
        ["<b>Memoria USB / tarjeta SD</b>", "Pequeñas y fáciles de llevar.", "Se pierden con facilidad; no son buenas como única copia."],
        ["<b>Nube</b> (Google Drive, OneDrive, iCloud…)", "Accesible desde cualquier dispositivo; copia fuera de casa.", "Necesita Internet y una cuenta bien protegida; espacio gratis limitado."]])}
      <h3>La regla de oro: copias de seguridad</h3>
      <p>Los aparatos se rompen, se pierden y los roban. Si algo te importa, debe estar <b>al menos en dos sitios</b>; por ejemplo, en tu ordenador y en la nube o en un disco externo.</p>
      {kp(["Activa la copia automática de fotos del móvil.", "Guarda los trabajos de clase en una carpeta sincronizada con la nube.", "Comprueba de vez en cuando que puedes abrir la copia."], "🛟")}
      {quiz("m5a", "¿Qué tipo de almacenamiento hace que un ordenador arranque más rápido?", ["Disco duro mecánico (HDD)", "SSD", "Una memoria USB"], 1, "El SSD no tiene piezas móviles y es muchísimo más rápido.")}
      {quiz("m5b", "Tu trabajo final solo está en una memoria USB. ¿Qué deberías hacer?", ["Nada, es suficiente", "Guardar otra copia en el ordenador o en la nube", "Borrarlo del USB para que no ocupe"], 1, "Una sola copia es un riesgo: si se pierde el USB, pierdes el trabajo.")}
      <div class="summary-box"><b>Resumen:</b> HDD (barato y lento), SSD (rápido), USB/SD (portátiles), nube (en Internet). Y siempre, al menos dos copias.</div>
"""))
# 6 -----------------------------------------------------------------------------
M.append(("🧩", "Software: los programas", "Sin software, el hardware no sabe qué hacer.", f"""
      <h2>¿Qué es el software?</h2>
      <p>El <b>software</b> es el conjunto de <b>programas</b>: instrucciones que le dicen al hardware qué hacer. Se organiza en capas: tú usas las aplicaciones, las aplicaciones se apoyan en el sistema operativo y el sistema operativo controla el hardware.</p>
      {fig("capas_software.svg", "Capas: usuario, aplicaciones, sistema operativo y hardware", "Cada capa se apoya en la de abajo.")}
      <h3>Tipos de software</h3>
      {cards([("⚙️","Sistema operativo","Gestiona el equipo: Windows, macOS, Linux, Android, iOS."),("📝","Aplicaciones","Programas para tareas: navegador, procesador de textos, editor de fotos, juegos."),("🔌","Controladores (drivers)","Permiten al sistema usar una pieza concreta: impresora, tarjeta gráfica…")])}
      <h3>Licencias: ¿qué puedo hacer con un programa?</h3>
      {tabla(["Tipo", "Qué significa", "Ejemplo"], [
        ["<b>Software libre</b>", "Puedes usarlo, estudiarlo, modificarlo y compartirlo. Suele ser gratuito.", "LibreOffice, Firefox, VLC, GIMP, Linux"],
        ["<b>Propietario (de pago)</b>", "Pagas una licencia para usarlo con las condiciones del fabricante.", "Algunas versiones de Microsoft Office, Photoshop"],
        ["<b>Freeware</b>", "Gratuito, pero no puedes ver ni modificar su código.", "Muchas apps gratuitas"],
        ["<b>Freemium</b>", "Gratis lo básico; pagas por funciones extra.", "Muchos juegos y apps del móvil"]])}
      <div class="alert-box"><b>Cuidado con el software «pirata» o crackeado:</b> además de ser ilegal, es una de las vías más habituales para meter virus en tu equipo. Si no puedes pagar un programa, busca una alternativa libre o gratuita.</div>
      {quiz("m6a", "¿Cuál de estos es un sistema operativo?", ["Android", "Un navegador web", "Un juego de fútbol"], 0, "Android gestiona el móvil; las apps funcionan encima de él.")}
      {quiz("m6b", "Puedes usar, modificar y compartir legalmente un programa. ¿Qué tipo de licencia tiene?", ["Propietario", "Software libre", "Pirata"], 1, "Esas son precisamente las libertades del software libre.")}
      {activity("Actividad: tus programas", "Elige 5 programas o apps que uses a menudo y busca qué tipo de licencia tienen. ¿Existe una alternativa libre para alguno?", "Programa → tipo de licencia → alternativa libre")}
      <div class="summary-box"><b>Resumen:</b> sistema operativo + aplicaciones + controladores. Fíjate en la licencia y evita el software pirata.</div>
"""))
# 7 -----------------------------------------------------------------------------
M.append(("🪟", "El sistema operativo", "El programa principal: arranca el equipo y organiza todo lo demás.", f"""
      <h2>El director de orquesta</h2>
      <p>El <b>sistema operativo (SO)</b> es el primer programa que se carga al encender el equipo. Se encarga de:</p>
      {kp(["Gestionar el hardware: memoria, procesador, discos, periféricos.", "Ofrecer una <b>interfaz</b> (ventanas, iconos, menús) para que puedas usar el equipo.", "Organizar los <b>archivos y carpetas</b>.", "Gestionar <b>usuarios</b> y permisos, y proteger el sistema con <b>actualizaciones</b>."], "🎼")}
      {tabla(["Sistema", "Dónde lo encuentras", "Licencia"], [["Windows", "La mayoría de ordenadores personales", "Propietario"], ["macOS", "Ordenadores Mac", "Propietario"], ["Linux (Ubuntu, Linux Mint…)", "Ordenadores, servidores, muchos centros educativos", "Libre"], ["ChromeOS", "Chromebooks", "Propietario (basado en Linux)"], ["Android", "La mayoría de móviles y tablets", "Base libre + servicios propietarios"], ["iOS / iPadOS", "iPhone y iPad", "Propietario"]])}
      <h3>Elementos que verás en casi todos</h3>
      {cards([("🖥️","Escritorio","La pantalla de fondo con iconos."),("📂","Explorador de archivos","Para ver y organizar carpetas."),("🔍","Buscador","Encuentra programas y archivos escribiendo su nombre."),("⚙️","Configuración","Wifi, pantalla, cuentas, actualizaciones."),("🔔","Notificaciones","Avisos del sistema y de las apps.")])}
      <div class="box tip"><b>Actualiza siempre.</b> Las actualizaciones del sistema corrigen fallos de seguridad. Un sistema que ya no recibe actualizaciones es un riesgo.</div>
      {quiz("m7a", "¿Qué hace el sistema operativo?", ["Solo sirve para navegar por Internet", "Gestiona el hardware, los archivos y los programas", "Es una pieza física del ordenador"], 1, "Es el software principal que coordina todo el equipo.")}
      {quiz("m7b", "¿Cuál de estos sistemas operativos es software libre?", ["Linux", "iOS", "macOS"], 0, "Linux y sus distribuciones (Ubuntu, Mint…) son libres.")}
      <div class="summary-box"><b>Resumen:</b> el SO arranca el equipo, gestiona el hardware, los archivos y los usuarios. Mantenlo actualizado.</div>
"""))
# 8 -----------------------------------------------------------------------------
M.append(("📂", "Archivos y carpetas", "Organizar bien tus archivos te ahorra mucho tiempo (y disgustos).", f"""
      <h2>Archivos, carpetas y rutas</h2>
      <p>Un <b>archivo</b> (o fichero) es un documento, foto, canción o programa guardado. Las <b>carpetas</b> sirven para agruparlos, y pueden contener otras carpetas. El camino hasta un archivo se llama <b>ruta</b>.</p>
      {fig("arbol_carpetas.svg", "Árbol de carpetas: Documentos, Instituto, Matemáticas, Inglés y Fotos con sus archivos", "Una estructura ordenada y la ruta para llegar a un archivo.")}
      <h3>La extensión: el «apellido» del archivo</h3>
      <p>Las letras después del punto indican el <b>tipo de archivo</b> y con qué programa se abre.</p>
      {tabla(["Extensión", "Tipo", "Se abre con…"], [[".odt / .docx", "Documento de texto", "LibreOffice Writer, Word"], [".ods / .xlsx", "Hoja de cálculo", "LibreOffice Calc, Excel"], [".pdf", "Documento para leer o imprimir", "Navegador, lector de PDF"], [".jpg / .png", "Imagen", "Visor de fotos"], [".mp3", "Audio", "Reproductor de música"], [".mp4", "Vídeo", "Reproductor de vídeo"], [".zip", "Archivo comprimido", "El propio sistema operativo"], [".exe", "Programa de Windows", "⚠️ Solo si viene de una fuente de confianza"]])}
      <h3>Buenas costumbres</h3>
      {kp(["Usa <b>nombres claros</b>: <code>tarea_fracciones_v2.odt</code> mejor que <code>documento1.odt</code>.", "Evita espacios raros, tildes y símbolos en los nombres si vas a compartir archivos: usa guiones bajos.", "Crea una carpeta por asignatura o proyecto.", "Vacía de vez en cuando la carpeta de <b>Descargas</b>.", "Lo que va a la <b>Papelera</b> aún se puede recuperar; al vaciarla, ya no."], "🗂️")}
      <div class="alert-box"><b>Doble extensión = alarma.</b> Un archivo llamado <code>notas.pdf.exe</code> parece un PDF, pero es un programa. No lo abras.</div>
      {quiz("m8a", "¿Qué tipo de archivo es <code>viaje.mp4</code>?", ["Una hoja de cálculo", "Un vídeo", "Un programa"], 1, ".mp4 es una extensión de vídeo.")}
      {quiz("m8b", "Te llega un archivo llamado <code>examen.pdf.exe</code>. ¿Qué es en realidad?", ["Un PDF normal", "Un programa que podría ser malicioso", "Una imagen"], 1, "La extensión real es la última: .exe (programa).")}
      {activity("Actividad: organiza tu estructura", "Diseña la estructura de carpetas que usarías este curso (asignaturas, proyectos, fotos…).", "Documentos › Instituto › ...")}
      <div class="summary-box"><b>Resumen:</b> carpetas bien organizadas, nombres claros, fíjate en la extensión y desconfía de las dobles extensiones.</div>
"""))
# 9 -----------------------------------------------------------------------------
M.append(("🌐", "Redes e Internet", "Cómo se conectan tus dispositivos entre sí y con el resto del mundo.", f"""
      <h2>De tu casa al mundo</h2>
      <p>Una <b>red</b> son varios dispositivos conectados para compartir información. <b>Internet</b> es la red de redes: une millones de redes de todo el mundo.</p>
      {fig("red_domestica.svg", "Red doméstica: Internet, router y dispositivos por cable y wifi", "En casa, el router reparte la conexión a Internet por cable y por wifi.")}
      {tabla(["Elemento", "Qué es"], [["<b>Router</b>", "El aparato que conecta tu red de casa con Internet y crea el wifi."], ["<b>Wifi</b>", "Conexión sin cables entre tus dispositivos y el router."], ["<b>Cable de red (Ethernet)</b>", "Conexión con cable: más estable y rápida que el wifi."], ["<b>Datos móviles (4G/5G)</b>", "Internet a través de la compañía de teléfono, fuera de casa."], ["<b>Dirección IP</b>", "El «número de teléfono» de cada dispositivo en la red."], ["<b>Navegador</b>", "El programa para ver páginas web: Firefox, Chrome, Edge, Safari…"]])}
      <h3>Internet no es solo la web</h3>
      {cards([("🌍","Web","Páginas que visitas con el navegador."),("✉️","Correo","Mensajes con archivos adjuntos."),("💬","Mensajería","Chats, llamadas y videollamadas."),("☁️","Nube","Guardar y compartir archivos en servidores."),("🎮","Juego online","Partidas con otras personas."),("📺","Streaming","Música y vídeo sin descargarlos.")])}
      <div class="box tip"><b>Seguridad básica:</b> busca el candado 🔒 y <code>https://</code> al escribir datos, no te conectes a wifis públicas para cosas importantes y cambia la contraseña del wifi que trae el router de fábrica.</div>
      {quiz("m9a", "¿Qué aparato conecta la red de tu casa con Internet?", ["El router", "La impresora", "El monitor"], 0, "El router es la puerta entre tu red e Internet.")}
      {quiz("m9b", "¿Qué conexión suele ser más estable para jugar online?", ["Wifi lejos del router", "Cable de red (Ethernet)", "Bluetooth"], 1, "El cable no sufre interferencias ni pérdidas por distancia.")}
      <div class="summary-box"><b>Resumen:</b> router + wifi/cable en casa, datos móviles fuera. Internet incluye web, correo, mensajería, nube, juegos y streaming.</div>
"""))
# 10 ----------------------------------------------------------------------------
M.append(("🧰", "Cuidado y mantenimiento del equipo", "Pequeños hábitos para que tu equipo dure más y funcione mejor.", f"""
      <h2>Mantener el equipo en forma</h2>
      {cards([("🔄","Actualiza","Sistema y apps: corrigen fallos y agujeros de seguridad."),("🧹","Limpia","Desinstala lo que no uses y vacía Descargas y Papelera."),("🛡️","Protege","Antivirus activo (en Windows, el que trae ya sirve) y solo descargas oficiales."),("💾","Copia","Copias de seguridad de lo importante."),("🔋","Batería","Evita calor extremo; no la dejes siempre al 0 %."),("🌬️","Ventila","No tapes las rejillas; quita el polvo con cuidado.")])}
      <h3>Si el equipo va lento…</h3>
      {flow(["🔁 Reinicia", "📋 Cierra programas que no uses", "🧮 Mira el Administrador de tareas", "🗑️ Libera espacio", "🔄 Actualiza"])}
      <p>En Windows, el <b>Administrador de tareas</b> (<kbd>Ctrl</kbd>+<kbd>Mayús</kbd>+<kbd>Esc</kbd>) muestra qué programas consumen más procesador y memoria. En el móvil, revisa en Ajustes qué apps gastan más batería y almacenamiento.</p>
      <h3>Cuídate tú también: ergonomía</h3>
      {fig("ergonomia.svg", "Postura correcta: pantalla a la altura de los ojos, a un brazo de distancia, espalda apoyada, codos a 90 grados y pies en el suelo", "Una buena postura evita dolores de espalda, cuello y vista.")}
      {kp(["Regla <b>20-20-20</b>: cada 20 minutos, mira algo a 20 pies (unos 6 metros) durante 20 segundos.", "Levántate y muévete al menos cada hora.", "Buena iluminación, sin reflejos en la pantalla.", "Evita pantallas justo antes de dormir."], "🧘")}
      {quiz("m10a", "El portátil va muy lento desde hace días. ¿Qué es lo primero y más sencillo?", ["Comprar otro", "Reiniciarlo y cerrar los programas que no uses", "Abrirlo y quitar piezas"], 1, "Muchos problemas se resuelven reiniciando y liberando memoria.")}
      {quiz("m10b", "¿A qué altura debe quedar la pantalla?", ["Con el borde superior a la altura de los ojos", "Muy por debajo de la mesa", "Lo más alta posible, para mirar hacia arriba"], 0, "Así el cuello queda recto y relajado.")}
      <div class="summary-box"><b>Resumen:</b> actualiza, limpia, protege, copia y ventila. Y cuida tu postura y tu vista.</div>
"""))
# 11 ----------------------------------------------------------------------------
M.append(("🛒", "Elegir un ordenador: leer una ficha técnica", "Entiende qué significan los números antes de comprar.", f"""
      <h2>¿Qué dicen todos esos números?</h2>
      <p>Al comprar un ordenador o un móvil verás una <b>ficha técnica</b>. Con lo aprendido ya puedes entenderla.</p>
      {fig("ficha_tecnica.svg", "Ficha técnica de un portátil de ejemplo", "Ficha de ejemplo (datos ficticios) con la explicación de cada línea.")}
      {tabla(["Uso", "RAM orientativa", "Almacenamiento", "Gráfica"], [["Clase, ofimática, navegar, vídeos", "8 GB", "SSD de 256–512 GB", "Integrada"], ["Edición de fotos, programación, multitarea", "16 GB", "SSD de 512 GB o más", "Integrada o dedicada básica"], ["Juegos exigentes, vídeo, 3D", "16–32 GB", "SSD de 1 TB", "Dedicada"]])}
      {kp(["Primero decide <b>para qué</b> lo vas a usar; después mira el presupuesto.", "Prioriza <b>SSD</b> y suficiente <b>RAM</b>: se notan más que unos pocos GHz.", "Comprueba si incluye <b>sistema operativo</b>.", "Mira el <b>peso</b> y la <b>batería</b> si lo vas a llevar a clase.", "Compara en tiendas fiables y desconfía de chollos imposibles."], "✅")}
      {quiz("m11a", "Lo usarás para clase, documentos y vídeos. ¿Qué configuración tiene más sentido?", ["8–16 GB de RAM y SSD de 256–512 GB", "64 GB de RAM y gráfica de gama alta", "4 GB de RAM y disco duro mecánico"], 0, "Es suficiente para ese uso, sin pagar de más.")}
      {quiz("m11b", "En una ficha pone «SSD 512 GB». ¿A qué se refiere?", ["A la memoria RAM", "Al almacenamiento", "A la pantalla"], 1, "Es el espacio para guardar archivos y programas.")}
      {activity("Actividad: compara dos equipos", "Busca dos portátiles de precio parecido y compara procesador, RAM, almacenamiento, pantalla, peso y batería. ¿Cuál elegirías y por qué?", "Equipo A: ... Equipo B: ... Elijo ... porque ...")}
      <div class="summary-box"><b>Resumen:</b> uso → presupuesto → RAM y SSD → resto. Lee la ficha con calma.</div>
"""))
# 12 ----------------------------------------------------------------------------
M.append(("🏆", "Proyecto final: la ficha de tu equipo", "Investiga tu propio ordenador o móvil con lo que has aprendido.", f"""
      <h2>Conviértete en detective de tu equipo</h2>
      <p>Vas a hacer la <b>ficha técnica de tu ordenador o móvil</b> (o de uno del centro, con permiso). Así es como se averiguan los datos:</p>
      {tabla(["Dispositivo", "Dónde mirarlo"], [["Windows", "<b>Configuración › Sistema › Información</b>. Para más detalle, escribe <code>msinfo32</code> en el buscador."], ["macOS", "Menú  › <b>Acerca de este Mac</b>"], ["Linux (Ubuntu)", "<b>Configuración › Acerca de</b> (o «Sistema › Acerca de»)"], ["Android", "<b>Ajustes › Acerca del teléfono</b>"], ["iPhone / iPad", "<b>Ajustes › General › Información</b>"]])}
      <div class="activity checklist">
        <h3>✔️ Rellena tu ficha</h3>
        <p>Marca cada dato a medida que lo encuentres:</p>
        <label><input type="checkbox" class="chk"> Tipo de dispositivo y modelo</label>
        <label><input type="checkbox" class="chk"> Procesador</label>
        <label><input type="checkbox" class="chk"> Memoria RAM</label>
        <label><input type="checkbox" class="chk"> Almacenamiento total y libre</label>
        <label><input type="checkbox" class="chk"> Sistema operativo y versión</label>
        <label><input type="checkbox" class="chk"> ¿Está actualizado?</label>
        <label><input type="checkbox" class="chk"> Periféricos que usas (entrada, salida, mixtos)</label>
        <label><input type="checkbox" class="chk"> ¿Cómo se conecta a Internet? (wifi, cable, datos)</label>
        <label><input type="checkbox" class="chk"> ¿Dónde están tus copias de seguridad?</label>
        <button class="btn" onclick="progreso()">Ver mi progreso</button>
        <p class="feedback" id="prog"></p>
      </div>
      {activity("Entrega: tu ficha y tu valoración", "Copia aquí los datos y responde: ¿es suficiente tu equipo para lo que haces? ¿Qué mejorarías primero (RAM, SSD, copias, actualizaciones…)?", "Modelo: ... Procesador: ... RAM: ... Valoración: ...")}
      <div class="box tip"><b>No compartas</b> números de serie, IMEI ni contraseñas en tu entrega: no hacen falta para el proyecto.</div>
      <div class="summary-box"><b>¡Enhorabuena!</b> Has completado los 12 módulos. Ahora puedes hacer el examen final.</div>
      <script>function progreso(){{var c=document.querySelectorAll('.chk:checked').length,t=document.querySelectorAll('.chk').length;document.getElementById('prog').textContent=c===t?'🏆 ¡Ficha completa! '+c+'/'+t:'Llevas '+c+' de '+t+' datos. ¡Sigue!';}}</script>
"""))
assert len(M) == N
for i, (ic, t, sub, body) in enumerate(M, 1):
    open(os.path.join(OUT, f"modulo{i}.html"), "w", encoding="utf-8").write(page(i, ic, t, sub, body))

# Banco de preguntas: (módulo, enunciado, opciones, índice correcto, va al examen)
Q = [
 (1, "¿Cuál es el ciclo básico de funcionamiento de un ordenador?", ["Entrada, proceso y salida", "Encender, jugar y apagar", "Cargar, enchufar y desenchufar", "Descargar, instalar y borrar"], 0, True),
 (1, "¿Qué diferencia hay entre hardware y software?", ["El hardware son las piezas físicas y el software, los programas", "Son lo mismo", "El hardware son los programas y el software, las piezas", "El software solo existe en los móviles"], 0, True),
 (1, "¿Cuál de estos aparatos lleva un ordenador dentro?", ["Una lavadora moderna con programas", "Una silla", "Un libro de papel", "Una mochila"], 0, False),
 (2, "¿Qué pieza ejecuta las instrucciones de los programas?", ["El procesador (CPU)", "La fuente de alimentación", "El ventilador", "La caja"], 0, True),
 (2, "¿Qué ocurre con el contenido de la memoria RAM al apagar el ordenador?", ["Se borra", "Se guarda para siempre", "Se envía a la nube", "Se imprime"], 0, True),
 (2, "¿Qué pieza conecta todos los componentes entre sí?", ["La placa base", "El monitor", "El teclado", "La memoria USB"], 0, False),
 (3, "¿Cuál de estos es un periférico de entrada?", ["El micrófono", "El altavoz", "El proyector", "La impresora"], 0, True),
 (3, "¿Por qué una pantalla táctil es un periférico mixto?", ["Porque muestra imágenes y también recibe tus toques", "Porque es muy grande", "Porque funciona sin electricidad", "Porque solo muestra imágenes"], 0, True),
 (3, "¿Qué conexión se usa normalmente para un monitor o un televisor?", ["HDMI", "Jack de 3,5 mm", "Cargador de batería", "Ninguna"], 0, False),
 (4, "¿Cuántos bits tiene un byte?", ["8", "2", "10", "1024"], 0, True),
 (4, "¿Cuántos MB son 2 GB, contando 1 GB = 1024 MB?", ["2048", "2000", "1024", "200"], 0, True),
 (4, "Una conexión de 600 Mb/s, ¿cuántos MB por segundo descarga como máximo?", ["75", "600", "4800", "60"], 0, False),
 (5, "¿Qué ventaja principal tiene un SSD frente a un disco duro mecánico?", ["Es mucho más rápido y no tiene piezas móviles", "Siempre es más barato", "Tiene más capacidad por el mismo precio", "No necesita electricidad"], 0, True),
 (5, "¿Qué significa tener una buena copia de seguridad?", ["Tener lo importante en al menos dos sitios distintos", "Tener el archivo abierto", "Guardar el archivo dos veces en la misma carpeta", "Imprimirlo"], 0, True),
 (5, "¿Qué necesita el almacenamiento en la nube para funcionar?", ["Conexión a Internet y una cuenta", "Un disco duro externo", "Una impresora", "Nada"], 0, False),
 (6, "¿Qué es el software libre?", ["Software que puedes usar, estudiar, modificar y compartir", "Cualquier programa pirata", "Programas que solo funcionan sin Internet", "Programas sin licencia de ningún tipo"], 0, True),
 (6, "¿Por qué es peligroso descargar programas «crackeados»?", ["Además de ser ilegal, suelen traer virus o malware", "Porque ocupan poco", "Porque son más rápidos", "No tiene ningún riesgo"], 0, True),
 (6, "¿Qué es un controlador (driver)?", ["Un programa que permite al sistema usar una pieza concreta", "Un tipo de virus", "Una pieza del teclado", "Un videojuego"], 0, False),
 (7, "¿Cuál de estos es un sistema operativo para móviles?", ["Android", "LibreOffice", "Firefox", "VLC"], 0, True),
 (7, "¿Por qué hay que instalar las actualizaciones del sistema operativo?", ["Porque corrigen fallos y problemas de seguridad", "Porque cambian el fondo de pantalla", "Porque borran tus archivos", "No sirven para nada"], 0, True),
 (7, "¿Qué es la interfaz de un sistema operativo?", ["Las ventanas, iconos y menús con los que lo manejas", "El cable de corriente", "La memoria RAM", "La caja del ordenador"], 0, False),
 (8, "¿Qué indica la extensión de un archivo, como .pdf o .jpg?", ["El tipo de archivo y con qué programa se abre", "Su tamaño", "La fecha en que se creó", "Quién lo creó"], 0, True),
 (8, "¿Qué es en realidad un archivo llamado «trabajo.pdf.exe»?", ["Un programa que podría ser malicioso", "Un PDF normal", "Una foto", "Una carpeta"], 0, True),
 (8, "¿Cómo se llama el camino hasta un archivo, por ejemplo Documentos › Instituto › tarea.odt?", ["Ruta", "Extensión", "Driver", "Píxel"], 0, False),
 (9, "¿Qué aparato conecta la red de tu casa con Internet?", ["El router", "El monitor", "La impresora", "El ratón"], 0, True),
 (9, "¿Qué conexión suele ser más estable y rápida?", ["Cable de red (Ethernet)", "Wifi a mucha distancia del router", "Bluetooth", "Infrarrojos"], 0, True),
 (9, "¿Qué programa usas para ver páginas web?", ["Un navegador", "Un procesador de textos", "Un antivirus", "Un controlador"], 0, False),
 (10, "El ordenador va lento. ¿Qué es lo primero y más sencillo que puedes probar?", ["Reiniciar y cerrar los programas que no uses", "Comprar otro ordenador", "Desmontar el procesador", "Borrar el sistema operativo"], 0, True),
 (10, "¿Qué dice la regla 20-20-20 para cuidar la vista?", ["Cada 20 minutos, mirar a unos 6 metros durante 20 segundos", "Usar el ordenador 20 horas seguidas", "Poner el brillo al 20 %", "Sentarse a 20 cm de la pantalla"], 0, True),
 (10, "¿Qué programa de Windows muestra qué aplicaciones consumen más memoria y procesador?", ["El Administrador de tareas", "El Bloc de notas", "La Papelera", "El Explorador de archivos"], 0, False),
 (11, "Para un ordenador de clase y ofimática, ¿qué es lo más importante priorizar?", ["Un SSD y suficiente RAM", "La gráfica más cara", "Las luces de colores", "El tamaño de la caja"], 0, True),
 (11, "En una ficha técnica pone «RAM 16 GB». ¿Qué te indica?", ["Cuánta memoria de trabajo tiene para tener cosas abiertas a la vez", "Cuántas fotos caben", "El tamaño de la pantalla", "La duración de la batería"], 0, True),
 (11, "¿Qué es lo primero que debes decidir antes de elegir un ordenador?", ["Para qué lo vas a usar", "El color", "La marca de tu amigo", "Nada, lo más caro siempre es mejor"], 0, False),
 (12, "¿Dónde puedes ver la memoria RAM y el procesador de un ordenador con Windows?", ["En Configuración › Sistema › Información", "En la Papelera", "En el navegador", "En la calculadora"], 0, True),
 (12, "Al compartir la ficha de tu equipo en un trabajo, ¿qué no deberías incluir?", ["Contraseñas y números de serie o IMEI", "La cantidad de RAM", "El sistema operativo", "El tipo de almacenamiento"], 0, True),
 (12, "¿En qué menú de un móvil Android encuentras la información del dispositivo?", ["Ajustes › Acerca del teléfono", "Galería", "Cámara", "Contactos"], 0, False),
]


def _place(k, q):
    m, t, opts, ok, ex = q
    opts = list(opts); target = (k * 3 + 1) % len(opts)
    opts[ok], opts[target] = opts[target], opts[ok]
    return (m, t, opts, target, ex)


Q = [_place(k, q) for k, q in enumerate(Q)]
EXAM = [q for q in Q if q[4]]
NOMBRES = [m[1] for m in M]


def gift_esc(s):
    for c in "~=#{}:":
        s = s.replace(c, "\\" + c)
    return s


g = ["// Informática básica para jóvenes — Banco de preguntas GIFT para Moodle",
     "// Autor: Sixto Rodríguez de Sepúlveda. Una única respuesta correcta por pregunta; una categoría por módulo."]
cur, cnt = None, {}
for m, q, opts, ok, _ in Q:
    if m != cur:
        cur = m
        g += ["", f"$CATEGORY: Informática básica para jóvenes/Módulo {m:02d} - {gift_esc(NOMBRES[m-1])}"]
    cnt[m] = cnt.get(m, 0) + 1
    g += ["", f"::INF{m:02d}-{cnt[m]}::{gift_esc(q)} {{"] + [f"{'=' if j == ok else '~'}{gift_esc(o)}" for j, o in enumerate(opts)] + ["}"]
open(os.path.join(OUT, "preguntas_moodle.gift"), "w", encoding="utf-8").write("\n".join(g) + "\n")

# Examen ------------------------------------------------------------------------
qs_html = "".join(
    f'<div class="quiz" id="box{i}"><h4>{i}. {html.escape(q)} <span class="small">(Módulo {m})</span></h4><div class="options">'
    + "".join(f'<label class="option"><input type="radio" name="q{i}" value="{j}" style="width:auto;margin-right:8px">{html.escape(o)}</label>' for j, o in enumerate(opts))
    + '</div></div>' for i, (m, q, opts, ok, _) in enumerate(EXAM, 1))
exam = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Examen final: Informática básica</title>
<link rel="stylesheet" href="style.css">
</head>
<body>
<div class="container">
  <div class="header">
    <h1><span class="shield-icon">🏁</span>Examen final</h1>
    <img src="img/logo-centro.png" class="logo-centro" alt="Logotipo del centro">
    <p>{TITULO}</p>
  </div>
  <div class="progress-container">
    <div class="progress-bar"><div class="progress-fill" style="width:100%"></div></div>
    <div class="progress-text">Informática básica · Examen final</div>
  </div>
  <div class="content-area">
    <section class="module">
      <h2>Evaluación final</h2>
      <p>Responde a las {len(EXAM)} preguntas. Necesitas al menos un <b>70 %</b> para aprobar. Al corregir verás las respuestas correctas y podrás repetirlo.</p>
      {qs_html}
      <div style="text-align:center"><button class="btn" onclick="corregir()">Corregir examen</button> <button class="btn" onclick="reiniciar()">Reintentar</button></div>
      <div id="resultado" style="margin-top:20px"></div>
      <div class="navigation">
        <button class="nav-btn" onclick="scormGo('modulo{N}.html')">⬅️ Módulo {N}</button>
        <button class="nav-btn" onclick="scormGo('index.html')">Inicio 🏠</button>
      </div>
    </section>
  </div>
</div>
<footer class="footer-autor">{FOOTER}</footer>
<script src="scorm.js"></script>
<script>
var RESP={json.dumps([q[3] for q in EXAM])};
function reiniciar(){{document.querySelectorAll('input[type=radio]').forEach(function(r){{r.checked=false}});document.querySelectorAll('.option').forEach(function(l){{l.classList.remove('correct','incorrect')}});document.getElementById('resultado').innerHTML='';window.scrollTo(0,0);}}
function corregir(){{
  var ok=0,sin=0;
  for(var i=0;i<RESP.length;i++){{
    var n=i+1,sel=document.querySelector('input[name="q'+n+'"]:checked'),labels=document.querySelectorAll('#box'+n+' .option');
    labels.forEach(function(l){{l.classList.remove('correct','incorrect')}});labels[RESP[i]].classList.add('correct');
    if(!sel){{sin++;continue;}}
    if(+sel.value===RESP[i])ok++;else labels[+sel.value].classList.add('incorrect');
  }}
  var nota=Math.round(ok*100/RESP.length),r=document.getElementById('resultado');
  r.innerHTML=nota>=70?'<div class="certificate"><h2>🏆 ¡Enhorabuena!</h2><p>Has superado el curso <b>{TITULO}</b>.</p><p style="font-size:1.6em;font-weight:700;color:#2e7d32">'+ok+'/'+RESP.length+' · '+nota+' %</p></div>'
    :'<div class="alert-box"><b>Resultado: '+ok+'/'+RESP.length+' ('+nota+' %).</b> Necesitas un 70 %'+(sin?' (has dejado '+sin+' sin responder)':'')+'. Repasa los módulos indicados y vuelve a intentarlo.</div>';
  if(window.scorm)scorm.complete(nota);
  r.scrollIntoView({{behavior:'smooth'}});
}}
</script>
</body>
</html>
"""
open(os.path.join(OUT, "examen_final.html"), "w", encoding="utf-8").write(exam)

# Portada -----------------------------------------------------------------------
nums = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣", "🔟", "1️⃣1️⃣", "1️⃣2️⃣"]
itin = "".join(f'<li>{nums[i]} <span><a href="modulo{i+1}.html">{t}</a></span></li>' for i, t in enumerate(NOMBRES))
index = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{TITULO}</title>
<link rel="stylesheet" href="style.css">
</head>
<body>
<div class="container">
  <div class="header">
    <h1><span class="shield-icon">💻</span>{TITULO}</h1>
    <img src="img/logo-centro.png" class="logo-centro" alt="Logotipo del centro">
    <p>Entiende cómo funcionan los aparatos que usas cada día: hardware, software, archivos, redes y mucho más.</p>
  </div>
  <div class="progress-container">
    <div class="progress-bar"><div class="progress-fill" style="width:0%"></div></div>
    <div class="progress-text">Informática básica · Módulo 0 de {N}</div>
  </div>
  <div class="content-area">
    <section class="module">
      <h2>Bienvenido/a 👋</h2>
      {fig("portada.svg", "Portátil, móvil y torre de ordenador", "Ordenadores, portátiles y móviles: por dentro funcionan igual.")}
      <p>Usas ordenadores y móviles a diario, pero ¿sabes qué hay dentro, qué es un sistema operativo o por qué tu disco «de 1 TB» no muestra 1000 GB? En este curso lo descubrirás con explicaciones sencillas, ilustraciones y ejercicios.</p>
      <div class="box"><b>Objetivo:</b> al terminar sabrás distinguir hardware y software, reconocer las piezas y periféricos, medir la información, organizar tus archivos, entender tu red de casa, cuidar tu equipo y leer la ficha técnica de un ordenador.</div>
      <h3>Itinerario</h3>
      <ul class="key-points">{itin}<li>🏁 <span><a href="examen_final.html">Examen final ({len(EXAM)} preguntas)</a></span></li></ul>
      <div class="activity">
        <h3>Reto inicial</h3>
        <p>Sin buscar en Internet: ¿qué crees que tiene dentro tu móvil para poder funcionar? Escribe todas las piezas que se te ocurran y compáralas al terminar el módulo 2.</p>
        <textarea placeholder="Ejemplo: una batería, una pantalla..."></textarea>
      </div>
      <div class="navigation">
        <span></span>
        <button class="nav-btn" onclick="scormGo('modulo1.html')">Comenzar ➡️</button>
      </div>
    </section>
  </div>
</div>
<footer class="footer-autor">{FOOTER}</footer>
<script src="scorm.js"></script>
</body>
</html>
"""
open(os.path.join(OUT, "index.html"), "w", encoding="utf-8").write(index)

# Manifiesto mínimo: herramientas/scorm_seguimiento.py lo completa (un SCO por página).
if not os.path.exists(os.path.join(OUT, "imsmanifest.xml")):
    open(os.path.join(OUT, "imsmanifest.xml"), "w", encoding="utf-8").write(
        f'<?xml version="1.0" encoding="UTF-8"?>\n<manifest identifier="informatica-basica-jovenes" version="1.0" '
        f'xmlns="http://www.imsproject.org/xsd/imscp_rootv1p1p2"><organizations default="ORG_1"><organization identifier="ORG_1">'
        f'<title>{TITULO}</title></organization></organizations><resources/></manifest>\n')
if not os.path.exists(os.path.join(OUT, "scorm.js")):
    open(os.path.join(OUT, "scorm.js"), "w", encoding="utf-8").write("")

readme = f"""INFORMÁTICA BÁSICA PARA JÓVENES — Paquete SCORM 1.2
Autor: Sixto Rodríguez de Sepúlveda

Curso introductorio de informática para jóvenes: qué es un ordenador, hardware, periféricos,
unidades de información, almacenamiento, software y licencias, sistema operativo, archivos y
carpetas, redes e Internet, mantenimiento y ergonomía, cómo leer una ficha técnica y un proyecto
final para hacer la ficha del propio equipo.

Contenido:
- imsmanifest.xml: SCORM 1.2 con un SCO por página; el índice de Moodle marca cada módulo al abrirlo
  y el examen registra la nota y aprobado/suspenso (70 %).
- index.html: presentación, itinerario y reto inicial.
- modulo1.html ... modulo{N}.html: {N} módulos con ilustraciones, tablas, autoevaluaciones y actividades
  (clasificar periféricos, calcular unidades, checklist del proyecto final).
- examen_final.html: examen de {len(EXAM)} preguntas (2 por módulo).
- preguntas_moodle.gift: {len(Q)} preguntas en formato GIFT, una categoría por módulo.
- img/: 11 ilustraciones propias en SVG (sin marcas ni fotos de terceros) + logo-centro.png.
- style.css + scorm.js.

Importación en Moodle:
1. Crea una actividad "SCORM" y sube el ZIP completo (sin descomprimir).
2. Banco de preguntas > Importar > formato GIFT > preguntas_moodle.gift.
"""
open(os.path.join(OUT, "README.txt"), "w", encoding="utf-8").write(readme)
print("ok", N, "módulos,", len(EXAM), "preguntas de examen,", len(Q), "GIFT")
