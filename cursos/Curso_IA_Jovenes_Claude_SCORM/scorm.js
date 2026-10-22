// scorm.js - Seguimiento SCORM 1.2 (generado por herramientas/scorm_seguimiento.py)
(function(){
var ORDEN=["index.html", "modulo1.html", "modulo2.html", "modulo3.html", "modulo4.html", "modulo5.html", "modulo6.html", "modulo7.html", "modulo8.html", "modulo9.html", "modulo10.html", "modulo11.html", "modulo12.html", "proyecto_final.html", "examen_final.html"];
var APROBADO=70;
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
