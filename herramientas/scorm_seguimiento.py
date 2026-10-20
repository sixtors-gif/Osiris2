#!/usr/bin/env python3
"""Prepara cada curso de cursos/ para que Moodle marque el índice según se avanza.

Para cada curso:
  1. Reescribe imsmanifest.xml con un elemento (SCO) por página, en orden:
     presentación, módulos/unidades, prácticas y examen final.
  2. Genera scorm.js con el orden de páginas y la nota de aprobado del curso:
       - al abrir una página de contenido la marca como «completada»;
       - el examen registra la nota y «aprobado»/«suspenso»;
       - «Siguiente»/«Anterior» piden a Moodle que abra el SCO vecino
         (nav.event = continue/previous), así Moodle actualiza el índice.
  3. Sustituye en las páginas window.location='x.html' por scormGo('x.html').

El examen conserva la mejor nota si se repite.

Uso:  python3 herramientas/scorm_seguimiento.py   (desde la raíz del repositorio)
Es idempotente: puede ejecutarse tantas veces como se quiera.
"""
import html, json, os, re, sys

RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "cursos")

SCORM_JS = r"""// scorm.js - Seguimiento SCORM 1.2 (generado por herramientas/scorm_seguimiento.py)
(function(){
var ORDEN=__ORDEN__;
var APROBADO=__APROBADO__;
var EXAMEN='examen_final.html';
function findAPI(w){var n=0;while(w&&n<10){try{if(w.API)return w.API;if(w.parent===w)break;w=w.parent}catch(e){break}n++}return null}
var api=findAPI(window);if(!api){try{api=findAPI(window.opener)}catch(e){}}
function call(fn,args){try{if(api&&api[fn])return api[fn].apply(api,args||[])}catch(e){}return ''}
function pagina(){var p=location.pathname.split('/').pop()||'index.html';return decodeURIComponent(p)}
var iniciado=false,terminado=false,esExamen=pagina()===EXAMEN;
function aviso(t){var d=document.getElementById('scorm-aviso');if(!d){d=document.createElement('div');d.id='scorm-aviso';d.setAttribute('role','status');d.style.cssText='position:fixed;left:50%;bottom:20px;transform:translateX(-50%);max-width:90%;background:#1e3c72;color:#fff;padding:12px 18px;border-radius:12px;box-shadow:0 6px 20px rgba(0,0,0,.3);z-index:9999;font:15px/1.4 sans-serif;text-align:center';document.body.appendChild(d)}d.textContent=t;d.style.display='block';clearTimeout(d._t);d._t=setTimeout(function(){d.style.display='none'},6000)}
window.scorm={
  enLMS:!!api,
  start:function(){
    if(iniciado||!api)return;iniciado=String(call('LMSInitialize',['']))==='true';
    var st=String(call('LMSGetValue',['cmi.core.lesson_status']));
    if(esExamen){if(st===''||st==='not attempted')call('LMSSetValue',['cmi.core.lesson_status','incomplete']);}
    else if(st!=='completed'&&st!=='passed'){call('LMSSetValue',['cmi.core.lesson_status','completed']);}
    call('LMSCommit',['']);
  },
  complete:function(nota){
    if(esExamen&&nota!=null){var prev=parseFloat(call('LMSGetValue',['cmi.core.score.raw']));if(!isNaN(prev)&&prev>nota)nota=prev;}
    if(nota!=null&&!isNaN(nota)){call('LMSSetValue',['cmi.core.score.min','0']);call('LMSSetValue',['cmi.core.score.max','100']);call('LMSSetValue',['cmi.core.score.raw',String(Math.round(nota))]);}
    call('LMSSetValue',['cmi.core.lesson_status',esExamen&&nota!=null?(nota>=APROBADO?'passed':'failed'):'completed']);
    call('LMSCommit',['']);
  },
  finish:function(){if(terminado||!api)return;terminado=true;call('LMSFinish',[''])}
};
window.scormGo=function(url){
  if(!api){location.href=url;return}
  var a=ORDEN.indexOf(pagina()),b=ORDEN.indexOf(url);
  if(a>=0&&b>=0&&Math.abs(b-a)===1){
    call('LMSSetValue',['nav.event',b>a?'continue':'previous']);
    window.scorm.finish();
    // Si el LMS no cambia de página por sí mismo, se navega igualmente.
    setTimeout(function(){location.href=url},2500);
    return;
  }
  aviso('Para ir a otro apartado usa el índice del curso de Moodle. Así queda registrado tu progreso.');
};
document.addEventListener('click',function(ev){
  var el=ev.target;while(el&&el.tagName!=='A')el=el.parentNode;
  if(!el||!api||el.target==='_blank'||el.hasAttribute('download'))return;
  var h=el.getAttribute('href')||'';
  if(/^[^:\/?#]+\.html$/i.test(h)){ev.preventDefault();window.scormGo(h)}
});
window.addEventListener('beforeunload',function(){window.scorm.finish()});
window.scorm.start();
})();
"""


def numero(nombre):
    m = re.search(r"(\d+)", nombre)
    return int(m.group(1)) if m else 0


def orden_paginas(d):
    pags = [f for f in os.listdir(d) if f.endswith(".html")]
    contenido = sorted([f for f in pags if re.match(r"(modulo|unidad)\d+\.html$", f)], key=numero)
    orden = ["index.html"] + contenido
    # Prácticas: van justo después del módulo al que pertenecen.
    if "practica_instalacion.html" in pags:
        orden.insert(orden.index("modulo12.html") + 1, "practica_instalacion.html")
    # Planning (curso de Piano): justo después de la presentación; gimnasio de ejercicios: tras el último módulo.
    if "planificacion.html" in pags:
        orden.insert(1, "planificacion.html")
    if "ejercicios.html" in pags:
        orden.append("ejercicios.html")
    # Repaso previo al examen (curso de Matemática básica).
    if "repaso.html" in pags:
        orden.append("repaso.html")
    orden.append("examen_final.html")
    extra = set(pags) - set(orden)
    assert not extra, f"{d}: páginas sin ubicar en el orden: {extra}"
    return orden


def titulo_pagina(d, f):
    s = open(os.path.join(d, f), encoding="utf-8").read()
    t = html.unescape(re.search(r"<title>(.*?)</title>", s, re.S).group(1)).strip()
    if f == "index.html":
        return "Presentación del curso"
    if f == "examen_final.html":
        return "Examen final"
    if f == "repaso.html":
        return "Repaso previo al examen"
    if f == "planificacion.html":
        return "Planning de 6 meses (1 hora al día)"
    if f == "ejercicios.html":
        return "Gimnasio: ejercicios prácticos"
    t = re.sub(r"^[^—]+ — ", "", t)  # «Curso — Tema» → «Tema»
    m = re.match(r"(modulo|unidad)(\d+)\.html$", f)
    if m:
        pref = ("Módulo " if m.group(1) == "modulo" else "Unidad ") + m.group(2)
        t = re.sub(r"^(Módulo|Unidad)\s*\d+\s*[:.\-–]\s*", "", t)
        return f"{pref}: {t}"
    return t


def nota_aprobado(d):
    s = open(os.path.join(d, "examen_final.html"), encoding="utf-8").read()
    m = re.search(r">=\s*(\d{2})", s)
    return int(m.group(1)) if m else 70


def recursos_comunes(d):
    comunes = ["style.css", "scorm.js"]
    for raiz, _, fs in os.walk(d):
        for f in sorted(fs):
            rel = os.path.relpath(os.path.join(raiz, f), d).replace(os.sep, "/")
            # Todo lo que no es una página del curso (las de la raíz son los SCO) ni
            # documentación del paquete: imágenes, prácticas, plantillas, partituras…
            if not (rel.endswith(".html") and "/" not in rel) and rel not in ("style.css", "scorm.js", "imsmanifest.xml",
                                                         "README.txt", "preguntas_moodle.gift"):
                comunes.append(rel)
    return comunes


def manifiesto(d, orden):
    viejo = open(os.path.join(d, "imsmanifest.xml"), encoding="utf-8").read()
    ident = re.search(r'<manifest[^>]*identifier="([^"]+)"', viejo).group(1)
    org = re.search(r"<organization[^>]*>\s*<title>(.*?)</title>", viejo, re.S).group(1).strip()
    files = "".join(f'      <file href="{c}"/>\n' for c in recursos_comunes(d))
    items, res = [], []
    for i, f in enumerate(orden):
        rid = "RES_" + re.sub(r"\W", "_", f[:-5]).upper()
        items.append(f'      <item identifier="ITEM_{i:02d}" identifierref="{rid}">\n'
                     f'        <title>{html.escape(titulo_pagina(d, f), quote=False)}</title>\n      </item>\n')
        res.append(f'    <resource identifier="{rid}" type="webcontent" adlcp:scormtype="sco" href="{f}">\n'
                   f'      <file href="{f}"/>\n{files}    </resource>\n')
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<manifest identifier="{ident}" version="1.1"
          xmlns="http://www.imsproject.org/xsd/imscp_rootv1p1p2"
          xmlns:adlcp="http://www.adlnet.org/xsd/adlcp_rootv1p2"
          xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
          xsi:schemaLocation="http://www.imsproject.org/xsd/imscp_rootv1p1p2 imscp_rootv1p1p2.xsd
                              http://www.adlnet.org/xsd/adlcp_rootv1p2 adlcp_rootv1p2.xsd">
  <metadata>
    <schema>ADL SCORM</schema>
    <schemaversion>1.2</schemaversion>
  </metadata>
  <organizations default="ORG_1">
    <organization identifier="ORG_1">
      <title>{org}</title>
{''.join(items)}    </organization>
  </organizations>
  <resources>
{''.join(res)}  </resources>
</manifest>
"""


def procesar(d):
    orden = orden_paginas(d)
    js = SCORM_JS.replace("__ORDEN__", json.dumps(orden)).replace("__APROBADO__", str(nota_aprobado(d)))
    open(os.path.join(d, "scorm.js"), "w", encoding="utf-8").write(js)
    for f in orden:
        p = os.path.join(d, f)
        s = open(p, encoding="utf-8").read()
        s2 = re.sub(r"window\.location(?:\.href)?\s*=\s*'([^']+\.html)'", r"scormGo('\1')", s)
        if s2 != s:
            open(p, "w", encoding="utf-8").write(s2)
        assert "scorm.js" in s2, f"{p} no carga scorm.js"
    nuevo = manifiesto(d, orden)  # se calcula antes de abrir el archivo para escritura
    open(os.path.join(d, "imsmanifest.xml"), "w", encoding="utf-8").write(nuevo)
    print(f"{os.path.basename(d)}: {len(orden)} SCO, aprobado {nota_aprobado(d)} %")


if __name__ == "__main__":
    raiz = sys.argv[1] if len(sys.argv) > 1 else RAIZ
    for n in sorted(os.listdir(raiz)):
        d = os.path.join(raiz, n)
        if os.path.isfile(os.path.join(d, "imsmanifest.xml")):
            procesar(d)
