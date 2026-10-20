#!/usr/bin/env python3
"""Amplía el curso de Escandallo con un módulo de estilos y formato condicional (migración de una vez).

Nuevo módulo 13: «Estilos y formato condicional: alarma de antigüedad de los precios».
La celda B2 («Fecha:») de cada ficha se marca:
  · en rojo  («Precio caducado») si su valor es <= AHORA()-60
  · en naranja («Precio antiguo») si su valor es <= AHORA()-30
con la condición de 60 días PRIMERO (Calc aplica la primera que se cumple).
El antiguo módulo 13 (reto final) pasa a ser el 14.

Uso: python3 herramientas/ampliar_escandallo_formato_condicional.py cursos/Curso_Escandallo_Catering_SCORM
Después: python3 herramientas/scorm_seguimiento.py && sh herramientas/empaquetar.sh
"""
import json, os, re, sys

D = sys.argv[1]
if os.path.exists(os.path.join(D, "modulo14.html")):
    sys.exit("El curso ya está ampliado (existe modulo14.html). No se hace nada.")
TOTAL = 14
rd = lambda f: open(os.path.join(D, f), encoding="utf-8").read()


def wr(f, s):
    open(os.path.join(D, f), "w", encoding="utf-8").write(s)


def sub1(s, a, b, f):
    assert s.count(a) == 1, (f, a[:70], s.count(a))
    return s.replace(a, b)


# 1. El reto final pasa a ser el módulo 14; progreso y «de 13» → «de 14» en todos ---------------
os.rename(os.path.join(D, "modulo13.html"), os.path.join(D, "modulo14.html"))
for n in list(range(1, 13)) + [14]:
    f = f"modulo{n}.html"
    s = rd(f)
    s = re.sub(r"Módulo \d+ de 13", f"Módulo {n} de {TOTAL}", s)
    s = re.sub(r'(class="progress-fill" style="width:)\d+%', lambda m: f"{m.group(1)}{round(n*100/TOTAL)}%", s)
    if n == 12:
        s = s.replace("scormGo('modulo13.html')", "scormGo('modulo13.html')")  # ya apunta al nuevo 13
    if n == 14:
        s = sub1(s, "scormGo('modulo12.html')", "scormGo('modulo13.html')", f)
    wr(f, s)

# 2. Página del nuevo módulo 13 (misma estructura que el resto) ---------------------------------
plantilla = rd("modulo12.html")
cab = plantilla[:plantilla.index('<div class="content-area">')]
pie = plantilla[plantilla.index("<footer"):]
K = lambda *t: " + ".join(f"<kbd>{x}</kbd>" for x in t)
TIT = "Estilos y formato condicional: alarma de antigüedad de los precios"
SUB = "Haz que la fecha de cada ficha se ponga naranja o roja cuando los precios del proveedor se queden viejos."
cab = re.sub(r"<title>.*?</title>", f"<title>{TIT}</title>", cab)
cab = re.sub(r'(<h1><span class="badge-icon">)[^<]*(</span>)[^<]*(</h1>)', lambda m: f"{m.group(1)}🚦{m.group(2)}{TIT}{m.group(3)}", cab)
cab = re.sub(r'(<div class="header">.*?<p>)[^<]*(</p>)', lambda m: m.group(1) + SUB + m.group(2), cab, flags=re.S)
cab = re.sub(r"Módulo \d+ de \d+", f"Módulo 13 de {TOTAL}", cab)
cab = re.sub(r'(class="progress-fill" style="width:)\d+%', lambda m: f"{m.group(1)}{round(13*100/TOTAL)}%", cab)


def ej(uid, titulo, preg, opciones, ok, exp):
    ops = "".join(f'<div class="option" onclick="pickc(this,\'{uid}\',{1 if i == ok else 0})">{o}</div>' for i, o in enumerate(opciones))
    return (f'<div class="exercise"><h3>🧩 {titulo}</h3><p>{preg}</p><div class="options" id="opt_{uid}">{ops}</div>'
            f'<div id="fb_{uid}" class="feedback-box" data-exp="{exp}"></div></div>')


def fila_dlg(n, op, form, estilo):
    return (f'<div class="cf-cond"><div class="cf-num">Condición {n}</div>'
            f'<div class="cf-row"><span class="cf-sel">El valor de la celda es</span><span class="cf-sel">{op}</span><span class="cf-in">{form}</span></div>'
            f'<div class="cf-row"><span class="cf-lab">Aplicar estilo</span><span class="cf-sel">{estilo}</span>'
            f'<span class="cf-prev {"cad" if "caducado" in estilo else "ant"}">10/01/2025</span></div></div>')


DIALOGO = ('<div class="figure"><div class="cf-dlg"><div class="cf-title">Formato condicional para B2</div>'
           + fila_dlg(1, "menor o igual que", "AHORA()-60", "Precio caducado")
           + fila_dlg(2, "menor o igual que", "AHORA()-30", "Precio antiguo")
           + '<div class="cf-foot"><span class="cf-btn">Añadir</span><span class="cf-btn">Subir</span><span class="cf-btn">Bajar</span><span class="cf-btn">Eliminar</span>'
           '<span class="cf-sp"></span><span class="cf-btn ok">Aceptar</span><span class="cf-btn">Cancelar</span></div></div>'
           '<div class="figure-caption">Esquema del cuadro <b>Formato → Formato condicional → Condición…</b> de LibreOffice Calc con las dos condiciones en el orden correcto.</div></div>')

SIMULADOR = """
<div class="activity" id="simcf">
  <h3>🧪 Simulador: ¿de qué color se pone B2?</h3>
  <p>Mueve la antigüedad de los precios y cambia el orden de las condiciones.</p>
  <label>Los precios se revisaron hace <b id="cf-dias">45</b> días<br><input type="range" min="0" max="120" value="45" id="cf-rango" style="width:100%;max-width:420px" oninput="cfPinta()"></label>
  <p style="margin-top:10px"><label><input type="radio" name="cf-orden" value="ok" checked onchange="cfPinta()" style="width:auto"> Orden correcto: primero «≤ AHORA()-60», después «≤ AHORA()-30»</label><br>
  <label><input type="radio" name="cf-orden" value="mal" onchange="cfPinta()" style="width:auto"> Orden al revés: primero «≤ AHORA()-30», después «≤ AHORA()-60»</label></p>
  <div class="xl-wrap"><table class="xl"><tr><th class="corner"></th><th>A</th><th style="min-width:110px">B</th></tr>
  <tr><th class="rn">1</th><td class="lbl">Nombre:</td><td>Porra Archidonesa</td></tr>
  <tr><th class="rn">2</th><td class="lbl">Fecha:</td><td id="cf-celda" class="r"></td></tr>
  <tr><th class="rn">3</th><td class="lbl">Raciones:</td><td class="r">10</td></tr></table></div>
  <p class="feedback-box" id="cf-explica" style="display:block"></p>
</div>
<script>
function cfPinta(){
  var d=+document.getElementById('cf-rango').value, ok=document.querySelector('input[name=cf-orden]:checked').value==='ok';
  document.getElementById('cf-dias').textContent=d;
  var f=new Date();f.setDate(f.getDate()-d);var txt=('0'+f.getDate()).slice(-2)+'/'+('0'+(f.getMonth()+1)).slice(-2)+'/'+f.getFullYear();
  var conds=ok?[[60,'Precio caducado','cad'],[30,'Precio antiguo','ant']]:[[30,'Precio antiguo','ant'],[60,'Precio caducado','cad']];
  var c=document.getElementById('cf-celda'),e=document.getElementById('cf-explica'),usada=null;
  for(var i=0;i<conds.length;i++){if(d>=conds[i][0]){usada=i;break;}}
  c.textContent=txt;c.className='r '+(usada===null?'':'cf-'+conds[usada][2]);
  if(usada===null){e.className='feedback-box good';e.textContent='Ninguna condición se cumple (menos de 30 días): B2 se queda con su formato normal.';}
  else{var m='Se cumple la condición '+(usada+1)+' (≤ AHORA()-'+conds[usada][0]+') → estilo «'+conds[usada][1]+'». Calc ya no mira las condiciones siguientes.';
    if(!ok&&d>=60){e.className='feedback-box bad';m+=' ⚠️ ¡Fallo! Los precios tienen más de 60 días y deberían salir en rojo, pero la condición de 30 días va primero y «gana» siempre.';}
    else e.className='feedback-box '+(conds[usada][2]==='cad'?'bad':'good');
    e.textContent=m;}
}
cfPinta();
</script>
"""

cuerpo = f"""
  <div class="content-area">
    <section class="module">
      <h2>{TIT}</h2>
<div class="activity"><h3>🎯 El problema</h3>
<p>Los precios del bloque <b>Proveedor</b> cambian: si la ficha se hizo hace meses, el escandallo calcula con precios viejos y el precio de venta puede quedarse corto. La celda <b>B2 («Fecha:»)</b> de cada ficha guarda cuándo revisaste esos precios. Vamos a convertirla en una <b>alarma</b>:</p>
<ul class="key-points"><li>🟧 <span>Más de <b>30 días</b>: fondo <b>naranja</b> («conviene revisar los precios»).</span></li>
<li>🟥 <span>Más de <b>60 días</b>: fondo <b>rojo</b> («precios caducados: no presupuestes sin revisarlos»).</span></li>
<li>⬜ <span>Menos de 30 días: sin color.</span></li></ul>
<p>Usaremos dos herramientas de Calc que trabajan juntas: los <b>estilos de celda</b> y el <b>formato condicional</b>.</p></div>

<h3>1. Los estilos de celda</h3>
<p>Un <b>estilo</b> es un formato con nombre (fondo, letra, números, bordes…) que se aplica de una vez. Si cambias el estilo, cambian <b>todas</b> las celdas que lo usan. En Calc, el formato condicional <b>aplica estilos</b>: por eso los creamos primero.</p>
<ol class="steps">
<li>Abre el panel de estilos: {K("F11")} (o <b>Ver → Estilos</b>) y elige el icono <b>Estilos de celda</b>.</li>
<li>Clic derecho sobre <b>Predeterminado</b> → <b>Nuevo…</b></li>
<li>Pestaña <b>Organizador</b> → Nombre: <code>Precio antiguo</code>.</li>
<li>Pestaña <b>Fondo</b> → <b>Color</b> → un naranja claro.</li>
<li>Pestaña <b>Efectos tipográficos</b> → color de letra marrón oscuro; pestaña <b>Tipo de letra</b> → <b>Negrita</b>.</li>
<li>Pestaña <b>Números</b> → <b>Fecha</b> → formato <code>DD/MM/AAAA</code>, para que la fecha se siga viendo como fecha. → <b>Aceptar</b>.</li>
<li>Repite para <code>Precio caducado</code> con fondo <b>rojo claro</b> y letra roja oscura.</li>
</ol>
<div class="tip-box">💡 <b>Atajo:</b> da el formato a mano a una celda, selecciónala y en el panel de estilos pulsa el menú <b>☰ Opciones de estilo → Estilo nuevo a partir de la selección…</b> ({K("Mayús", "F11")}). Solo tendrás que ponerle nombre.</div>

<h3>2. ¿Qué compara la alarma?</h3>
<p>Para Calc una fecha es un <b>número</b>: los días transcurridos desde el 30/12/1899. Por eso se puede restar: <code>AHORA()-30</code> es «hace 30 días».</p>
<div class="formula"><span class="f-label">Condición</span><code>B2 &lt;= AHORA()-30</code><span class="f-exp">La fecha de B2 es igual o <b>anterior</b> a la de hace 30 días → los precios tienen 30 días o más.</span></div>
<div class="formula"><span class="f-label">Condición</span><code>B2 &lt;= AHORA()-60</code><span class="f-exp">Igual o anterior a la de hace 60 días → 60 días o más.</span></div>
<p class="small"><b>AHORA()</b> devuelve la fecha y la hora actuales y se actualiza sola al abrir el archivo o al recalcular ({K("F9")}). También sirve <b>HOY()</b>, que da solo la fecha; para esta alarma el resultado es prácticamente el mismo.</p>

<h3>3. El formato condicional paso a paso</h3>
<ol class="steps">
<li>Haz clic en <b>B2</b> de la hoja <b>Entrante</b>.</li>
<li><b>Formato → Formato condicional → Condición…</b></li>
<li><b>Condición 1:</b> «El valor de la celda es» · «<b>menor o igual que</b>» · escribe <code>AHORA()-60</code> · Aplicar estilo: <b>Precio caducado</b>.</li>
<li>Pulsa <b>Añadir</b>. <b>Condición 2:</b> «El valor de la celda es» · «menor o igual que» · <code>AHORA()-30</code> · Aplicar estilo: <b>Precio antiguo</b>.</li>
<li><b>Aceptar</b>. Como la fecha del modelo es de enero de 2025, B2 se pondrá roja.</li>
</ol>
{DIALOGO}

<h3>4. ¡El orden de las condiciones importa!</h3>
<p>Calc comprueba las condiciones <b>de arriba abajo</b> y aplica la <b>primera que se cumple</b>. Una fecha de hace 75 días también es «≤ AHORA()-30». Si pusieras primero la de 30 días, se cumpliría siempre antes y <b>nunca verías el rojo</b>.</p>
<div class="xl-wrap"><table class="tbl"><tr><th>Antigüedad</th><th>¿≤ AHORA()-60?</th><th>¿≤ AHORA()-30?</th><th>Orden correcto (60 → 30)</th><th>Orden al revés (30 → 60)</th></tr>
<tr><td>10 días</td><td>No</td><td>No</td><td>Sin color</td><td>Sin color</td></tr>
<tr><td>45 días</td><td>No</td><td>Sí</td><td><span class="cf-ant">Naranja</span></td><td><span class="cf-ant">Naranja</span></td></tr>
<tr><td>75 días</td><td><b>Sí</b></td><td>Sí</td><td><span class="cf-cad">Rojo</span> ✅</td><td><span class="cf-ant">Naranja</span> ❌</td></tr></table></div>
<div class="alert-box">⚠️ <b>Regla:</b> la condición <b>más estricta</b> (la de más días) va <b>primero</b>. Si te equivocas de orden, en el cuadro de diálogo selecciona la condición y usa <b>Subir</b> o <b>Bajar</b>.</div>
{SIMULADOR}

<h3>5. Resultado en Calc</h3>
<div class="figure"><img src="img/alarma_ficha_calc.png" alt="Ficha con la fecha de B2 en rojo porque los precios tienen más de 60 días" style="max-width:100%"><div class="figure-caption">Ficha con precios de enero de 2025: B2 en rojo.</div></div>
<div class="figure"><img src="img/alarma_pruebas_calc.png" alt="Tres fechas: hace 10 días sin color, hace 40 días en naranja y hace 75 días en rojo" style="max-width:100%"><div class="figure-caption">Resultado real en LibreOffice Calc con fechas de hace 10, 40 y 75 días (archivo de práctica, hoja «Pruebas»).</div></div>
<div class="dl-box">📥 <b>Archivo de práctica:</b> <a href="Alarma_fechas_practica.ods" download>Alarma_fechas_practica.ods</a> — trae los dos estilos y el formato condicional ya hechos. Ábrelo, mira <b>Formato → Formato condicional → Gestionar…</b> y compáralo con el tuyo.</div>

<h3>6. Llevarlo a las cuatro fichas</h3>
<ul class="key-points">
<li>🔓 <span>Si protegiste las hojas en el módulo 12, primero <b>Herramientas → Proteger hoja</b> (quítalo); en una hoja protegida no se puede cambiar el formato. Vuelve a protegerla al terminar.</span></li>
<li>🖌️ <span>Selecciona B2 de <b>Entrante</b>, pulsa <b>Clonar formato</b> (el pincel) y haz clic en B2 de <b>Carne</b>; repite en <b>Pescado</b> y <b>Postre</b>. El pincel copia también el formato condicional.</span></li>
<li>📋 <span>Alternativa: copia B2 ({K("Ctrl", "C")}) y en la otra hoja <b>Editar → Pegado especial → Solo formatos</b>.</span></li>
<li>🔎 <span>Para revisar o borrar reglas: <b>Formato → Formato condicional → Gestionar…</b></span></li>
<li>🔄 <span>Cuando revises los precios con el proveedor, pon la fecha de hoy en B2 con {K("Ctrl", ";")}: la alarma se apaga.</span></li>
</ul>
<div class="ms-box"><span class="mbadge">En Excel</span> Selecciona B2 → <b>Inicio → Formato condicional → Nueva regla → Aplicar formato únicamente a las celdas que contengan</b> → «Valor de la celda» · «menor o igual que» · <code>=HOY()-60</code> → <b>Formato…</b> (relleno rojo). Crea otra regla igual con <code>=HOY()-30</code> y relleno naranja. En <b>Formato condicional → Administrar reglas</b>, la de arriba tiene prioridad: deja la de 60 días encima (usa las flechas).</div>

{ej("e13a", "El orden", "Pones primero la condición «≤ AHORA()-30» (naranja) y después «≤ AHORA()-60» (rojo). Una ficha tiene precios de hace 90 días. ¿De qué color sale B2?", ["Rojo", "Naranja", "Sin color"], 1, "La primera condición que se cumple es la de 30 días y Calc ya no mira la siguiente: por eso la de 60 días debe ir primero.")}
{ej("e13b", "La fórmula", "¿Qué significa la condición «El valor de la celda es menor o igual que AHORA()-30»?", ["Que la fecha es de hace 30 días o más", "Que faltan 30 días para esa fecha", "Que la celda contiene el número 30"], 0, "AHORA()-30 es la fecha de hace 30 días; una fecha menor o igual es igual o anterior a ella.")}
{ej("e13c", "Ventaja de los estilos", "Quieres cambiar el rojo de la alarma por un rojo más intenso en las cuatro fichas. ¿Qué es lo más rápido?", ["Cambiar el color en cada celda B2", "Modificar el estilo «Precio caducado»: cambia en todas las celdas que lo usan", "Borrar el formato condicional y empezar de nuevo"], 1, "El formato condicional aplica el estilo: basta con modificarlo una vez.")}

<div class="summary-box">🎯 <b>Idea clave:</b> crea los estilos, añade las condiciones en B2 con la <b>más estricta primero</b> (≤ AHORA()-60 → rojo; ≤ AHORA()-30 → naranja), cópialo a las cuatro fichas con el pincel y actualiza la fecha cada vez que revises los precios.</div>

      <div class="navigation"><button class="nav-btn" onclick="scormGo('modulo12.html')">⬅️ Anterior</button><button class="nav-btn" onclick="scormGo('modulo14.html')">Siguiente ➡️</button></div>
    </section>
  </div>
</div>
"""
wr("modulo13.html", cab + cuerpo + pie)

# 3. Estilos para el diálogo simulado y los colores de la alarma ---------------------------------
css = rd("style.css")
if ".cf-dlg" not in css:
    css += """
/* Módulo 13: formato condicional */
.cf-ant{background:#ffd8a8;color:#7a4100;font-weight:700;padding:1px 6px;border-radius:3px}
.cf-cad{background:#f4b6b6;color:#9c0006;font-weight:700;padding:1px 6px;border-radius:3px}
td.cf-ant,td.cf-cad{border-radius:0}
.cf-dlg{max-width:620px;margin:0 auto;border:1px solid #9aa4bd;border-radius:8px;background:#f3f4f7;box-shadow:0 6px 18px rgba(0,0,0,.18);text-align:left;font-family:'Segoe UI',Tahoma,sans-serif;font-size:14px;overflow:hidden}
.cf-title{background:#e4e7ee;padding:8px 12px;font-weight:700;border-bottom:1px solid #c7ccd8}
.cf-cond{background:#fff;margin:10px;border:1px solid #d3d8e3;border-radius:6px;padding:8px 10px}
.cf-num{font-weight:700;color:#1f3a63;margin-bottom:6px}
.cf-row{display:flex;flex-wrap:wrap;gap:8px;align-items:center;margin:4px 0}
.cf-sel,.cf-in{border:1px solid #9aa4bd;border-radius:4px;padding:3px 8px;background:#fff}
.cf-sel:after{content:" ▾";color:#666}
.cf-in{font-family:Consolas,monospace;min-width:110px}
.cf-lab{color:#333}
.cf-prev{padding:3px 10px;border:1px solid #ccc;font-weight:700}
.cf-prev.cad{background:#f4b6b6;color:#9c0006}.cf-prev.ant{background:#ffd8a8;color:#7a4100}
.cf-foot{display:flex;flex-wrap:wrap;gap:6px;padding:8px 10px;border-top:1px solid #c7ccd8;background:#eceef3}
.cf-btn{border:1px solid #9aa4bd;border-radius:4px;padding:3px 12px;background:#fff}.cf-btn.ok{border-color:#2b6cb0;font-weight:700}
.cf-sp{flex:1}
.ms-box{background:#eef4fb;border:1px dashed #2b6cb0;border-radius:10px;padding:12px 16px;margin:14px 0}
.ms-box .mbadge{display:inline-block;background:#2b6cb0;color:#fff;border-radius:12px;padding:1px 10px;font-size:.8em;font-weight:700;margin-right:6px}
.small{font-size:.92em;color:#555}
"""
    wr("style.css", css)

# 4. Portada: itinerario --------------------------------------------------------------------------
s = rd("index.html")
s = sub1(s, '<li><span><b>13.</b></span><span><a href="modulo13.html">Reto final: tu propio escandallo',
         f'<li><span><b>13.</b></span><span><a href="modulo13.html">{TIT}</a></span></li><li><span><b>14.</b></span><span><a href="modulo14.html">Reto final: tu propio escandallo', "index.html")
s = s.replace("13 módulos", "14 módulos")
wr("index.html", s)

# 5. Examen: dos preguntas nuevas ---------------------------------------------------------------
s = rd("examen_final.html")
qs = json.loads(re.search(r"const qs=(\[.*?\]);", s, re.S).group(1))
nuevas = [["En el formato condicional de B2, ¿qué condición debe ir primero?", "«≤ AHORA()-60» (la más estricta), y después «≤ AHORA()-30»", "«≤ AHORA()-30», y después «≤ AHORA()-60»", "Da igual el orden", "Solo hace falta una condición"],
          ["¿Qué ventaja tiene usar estilos de celda en el formato condicional?", "Si cambias el estilo, cambia en todas las celdas que lo usan", "Las fórmulas se calculan más rápido", "Protege la hoja automáticamente", "Ocupa menos espacio en el archivo"]]
i12 = max(i for i, q in enumerate(qs) if "proteger la hoja" in q[0].lower())
qs = qs[:i12 + 1] + nuevas + qs[i12 + 1:]
s = re.sub(r"const qs=\[.*?\];", lambda m: "const qs=" + json.dumps(qs, ensure_ascii=False) + ";", s, count=1, flags=re.S)
s = sub1(s, "scormGo('modulo13.html')", "scormGo('modulo14.html')", "examen")
s = re.sub(r"Módulo 13 de 13", "Examen final", s)
s = re.sub(r"\b26 preguntas\b", f"{len(qs)} preguntas", s)
wr("examen_final.html", s)

# 6. Banco GIFT ---------------------------------------------------------------------------------
g = rd("preguntas_moodle.gift")
g = sub1(g, "$CATEGORY: Curso Escandallo/Módulo 13 - Reto final: tu propio escandallo", "$CATEGORY: Curso Escandallo/Módulo 14 - Reto final: tu propio escandallo", "gift")
g = re.sub(r"::ESC13-(\d+)::", r"::ESC14-\1::", g)
esc = lambda t: re.sub(r"([~=#{}:])", r"\\\1", t)
bloque = ["$CATEGORY: Curso Escandallo/Módulo 13 - Estilos y formato condicional - alarma de antigüedad", ""]
preg = nuevas + [["Quieres que la alarma de B2 se apague tras revisar los precios. ¿Qué haces?", "Escribir en B2 la fecha de hoy (Ctrl + ;)", "Borrar el formato condicional", "Cambiar el color de la letra", "Proteger la hoja"]]
for k, (q, ok, *mal) in enumerate(preg, 1):
    bloque += [f"::ESC13-{k}::{esc(q)} {{", f"={esc(ok)}"] + [f"~{esc(x)}" for x in mal] + ["}", ""]
g = sub1(g, "$CATEGORY: Curso Escandallo/Módulo 14 - Reto final", "\n".join(bloque) + "\n$CATEGORY: Curso Escandallo/Módulo 14 - Reto final", "gift")
g = g.replace("(13 categorías", "(14 categorías")
wr("preguntas_moodle.gift", g)
n_gift = len(re.findall(r"(?m)^::", g))

# 7. README ---------------------------------------------------------------------------------------
r = rd("README.txt")
r = r.replace("- imsmanifest.xml: paquete SCORM 1.2 empaquetado como un único SCO (seguimiento correcto en Moodle).",
              "- imsmanifest.xml: paquete SCORM 1.2 con un SCO por página (el índice de Moodle se marca al avanzar).")
r = sub1(r, "- modulo1.html ... modulo13.html: 13 módulos", f"- modulo1.html ... modulo{TOTAL}.html: {TOTAL} módulos", "README")
r = re.sub(r"examen final interactivo de \d+ preguntas", f"examen final interactivo de {len(qs)} preguntas", r)
r = re.sub(r"\d+ preguntas en formato GIFT \(\d+ categorías", f"{n_gift} preguntas en formato GIFT ({TOTAL} categorías", r)
r = sub1(r, "- Escandallo_modelo.ods:", "- Alarma_fechas_practica.ods: práctica del módulo 13 (estilos «Precio antiguo» y «Precio caducado» y\n  formato condicional de la fecha, con una hoja de pruebas de 10, 40 y 75 días).\n- Escandallo_modelo.ods:", "README")
r = sub1(r, "13. Reto final: tu propio escandallo", f"13. {TIT}\n14. Reto final: tu propio escandallo", "README")
wr("README.txt", r)
print(f"Ampliado: {TOTAL} módulos, examen de {len(qs)} preguntas, GIFT de {n_gift}.")
