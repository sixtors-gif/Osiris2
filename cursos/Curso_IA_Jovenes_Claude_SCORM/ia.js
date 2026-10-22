// ia.js · herramientas interactivas del curso (todo funciona en el navegador, sin conexión y sin enviar datos)
function copiar(btn){var t=btn.parentElement.querySelector('pre').textContent;
  var ok=function(){var o=btn.textContent;btn.textContent='✅ Copiado';setTimeout(function(){btn.textContent=o;},1600);};
  if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(t).then(ok,function(){fallback(t,ok);});}else fallback(t,ok);}
function fallback(t,ok){var a=document.createElement('textarea');a.value=t;document.body.appendChild(a);a.select();try{document.execCommand('copy');ok();}catch(e){}document.body.removeChild(a);}
function comoTodos(a){document.querySelectorAll('details.como').forEach(function(d){d.open=a;});}
function checkAnswer(btn,ok,id){var p=btn.parentElement;p.querySelectorAll('.option').forEach(function(b){b.classList.remove('correct','incorrect')});
  btn.classList.add(ok?'correct':'incorrect');var fb=document.getElementById('fb-'+id);fb.textContent=ok?'✅ ¡Correcto! '+fb.getAttribute('data-ok'):'❌ No es correcto. Repasa el apartado e inténtalo de nuevo.';}

// ---- Constructor de prompts ----
function pbMontar(){
  var v=function(id){return (document.getElementById(id).value||'').trim();};
  var partes=[];
  if(v('pb-rol'))partes.push('Actúa como '+v('pb-rol')+'.');
  if(v('pb-contexto'))partes.push('Contexto: '+v('pb-contexto'));
  if(v('pb-tarea'))partes.push('Tarea: '+v('pb-tarea'));
  if(v('pb-formato'))partes.push('Formato de la respuesta: '+v('pb-formato')+'.');
  if(v('pb-tono'))partes.push('Tono: '+v('pb-tono')+'.');
  if(v('pb-limites'))partes.push('Ten en cuenta: '+v('pb-limites'));
  var t=partes.join('\n\n');var out=document.getElementById('pb-salida');
  out.textContent=t||'Rellena al menos la tarea y aquí aparecerá tu prompt.';
  var n=[v('pb-rol'),v('pb-contexto'),v('pb-tarea'),v('pb-formato'),v('pb-tono'),v('pb-limites')].filter(Boolean).length;
  document.getElementById('pb-nota').textContent=n+' de 6 ingredientes. '+(n<3?'Añade contexto y formato para respuestas más útiles.':(n<5?'¡Bien! Con el tono y los límites quedará aún mejor.':'¡Un prompt completo!'));
}
function pbEjemplo(i){
  var E=[
   {rol:'responsable de atención al cliente de un hotel de 4 estrellas en la costa',contexto:'Un cliente ha dejado una reseña de 2 estrellas: dice que el desayuno estaba frío y que esperó 20 minutos en recepción, pero que la habitación era muy bonita.',tarea:'Redacta una respuesta pública a la reseña.',formato:'un párrafo de 5 o 6 líneas, sin listas',tono:'cercano, amable y profesional',limites:'no prometas compensaciones ni des excusas; no inventes datos; invita a contactar por correo.'},
   {rol:'jefe de cocina de un restaurante de cocina mediterránea',contexto:'Tengo en la cámara tomates maduros, calabacín, queso feta y pan del día anterior. Es verano.',tarea:'Propón 3 ideas de entrante para el menú del día.',formato:'una tabla con nombre del plato, ingredientes principales y dificultad',tono:'práctico',limites:'para un menú económico; indica qué alérgenos podría contener cada plato, para que yo lo verifique.'},
   {rol:'community manager de una cafetería de barrio',contexto:'Estrenamos terraza el viernes y tendremos música en directo por la tarde.',tarea:'Escribe 3 textos para Instagram anunciándolo.',formato:'cada texto de máximo 40 palabras con 3 hashtags',tono:'divertido y joven',limites:'sin emojis excesivos; el horario es de 17:00 a 21:00.'}];
  var e=E[i];['rol','contexto','tarea','formato','tono','limites'].forEach(function(k){document.getElementById('pb-'+k).value=e[k];});pbMontar();
}

// ---- Predictor de la siguiente palabra ----
var PRED=[
 {frase:'El camarero llevó la bandeja a la…',op:[['mesa',62],['cocina',20],['barra',13],['luna',1],['playa',4]]},
 {frase:'Para hacer una tortilla de patatas necesitas huevos, patatas y…',op:[['aceite',46],['cebolla',30],['sal',17],['pegamento',1],['leche',6]]},
 {frase:'Buenas noches, tenemos una reserva a nombre de…',op:[['García',34],['Martínez',22],['mi',14],['López',25],['jirafa',1],['Pérez',4]]},
 {frase:'El hotel está a cinco minutos de la…',op:[['playa',58],['estación',22],['catedral',12],['nevera',1],['plaza',7]]}
];
var pred={i:0};
function predPintar(){var p=PRED[pred.i];document.getElementById('pred-frase').textContent=p.frase;
  var c=document.getElementById('pred-ops');c.innerHTML='';
  p.op.forEach(function(o){var b=document.createElement('button');b.textContent=o[0];b.onclick=function(){predElegir(o,b);};c.appendChild(b);});
  document.getElementById('pred-res').innerHTML='';}
function predElegir(o,b){var p=PRED[pred.i],max=Math.max.apply(null,p.op.map(function(x){return x[1];}));
  var h='<p>'+(o[1]===max?'🎯 ¡Has elegido la palabra más probable!':'Has elegido «'+o[0]+'» ('+o[1]+' %). La más probable era otra.')+' Así «reparte» las probabilidades un modelo:</p>';
  p.op.slice().sort(function(a,b){return b[1]-a[1];}).forEach(function(x){h+='<div class="pred-fila"><span>'+x[0]+'</span><div class="pred-barra"><div style="width:'+x[1]+'%"></div></div><b>'+x[1]+' %</b></div>';});
  document.getElementById('pred-res').innerHTML=h;}
function predSiguiente(){pred.i=(pred.i+1)%PRED.length;predPintar();}
function predGenerar(){var p=PRED[pred.i],T=parseFloat(document.getElementById('pred-temp').value);
  document.getElementById('pred-t').textContent=T.toFixed(1);
  var w=p.op.map(function(o){return Math.pow(o[1]/100,1/Math.max(T,0.05));}),s=w.reduce(function(a,b){return a+b;},0),r=Math.random()*s,k=0;
  for(k=0;k<w.length;k++){r-=w[k];if(r<=0)break;}k=Math.min(k,w.length-1);
  var l=document.getElementById('pred-gen');var e=document.createElement('span');e.className='pred-chip';e.textContent=p.op[k][0];l.appendChild(e);}
function predLimpiar(){document.getElementById('pred-gen').innerHTML='';}

// ---- Revisor de privacidad ----
var PRIV=[
 {n:'Correo electrónico',re:/[\w.+-]+@[\w-]+\.[\w.-]+/g,r:'[CORREO]'},
 {n:'IBAN',re:/\b[A-Z]{2}\d{2}(?:[ ]?\d{4}){4,6}\b/g,r:'[IBAN]'},
 {n:'Tarjeta bancaria',re:/\b(?:\d[ -]?){13,19}\b/g,r:'[TARJETA]'},
 {n:'DNI o NIE',re:/\b(?:\d{8}|[XYZxyz]\d{7})[- ]?[A-Za-z]\b/g,r:'[DNI]'},
 {n:'Teléfono',re:/(?:\+34[ ]?)?\b[6789](?:[ .-]?\d){8}\b/g,r:'[TELÉFONO]'},
 {n:'Número de habitación o reserva',re:/\b(?:habitaci[oó]n|hab\.|reserva|localizador)\b[^.\d]{0,14}\d+\w*/gi,r:'[HABITACIÓN/RESERVA]'}
];
var PRIV_ALERTA=['alerg','intoleran','celiac','celíac','enfermedad','embaraz','religi','discapacidad','contraseña','clave de','pin '];
function privRevisar(){
  var t=document.getElementById('priv-texto').value,hallazgos=[],limpio=t;
  PRIV.forEach(function(p){var m=t.match(p.re);if(m){hallazgos.push(p.n+': '+m.length);}limpio=limpio.replace(p.re,p.r);});
  var alertas=PRIV_ALERTA.filter(function(w){return t.toLowerCase().indexOf(w)>=0;});
  var h='';
  if(!t.trim()){h='<p>Pega un texto de prueba (inventado) para revisarlo.</p>';}
  else if(!hallazgos.length&&!alertas.length){h='<p class="pv-ok">✅ No se detectan datos personales evidentes. Aun así, repasa tú el texto: los nombres propios y los detalles que identifican a una persona no siempre se detectan.</p>';}
  else{h='<p class="pv-ko">⚠️ Se han detectado posibles datos personales:</p><ul>'+hallazgos.map(function(x){return '<li>'+x+'</li>';}).join('')+(alertas.length?'<li>Datos sensibles (salud, creencias, claves…): '+alertas.join(', ')+'</li>':'')+'</ul>';}
  document.getElementById('priv-res').innerHTML=h;document.getElementById('priv-limpio').textContent=limpio;
}
function privEjemplo(){document.getElementById('priv-texto').value='Hola, soy Marta Ruiz (DNI 12345678Z). Mi reserva es la 48213 y mi habitación la 305. Mi correo es marta.ruiz@correo.es y mi teléfono el 612 345 678. Soy celíaca y mi tarjeta es 4111 1111 1111 1111. ¿Puedes escribirme un correo de queja?';privRevisar();}

// ---- Simulador de ventana de contexto ----
function ctxActualizar(){var n=parseInt(document.getElementById('ctx-n').value,10);document.getElementById('ctx-v').textContent=n;
  var paginas=Math.round(n*0.75/400*10)/10,libros=Math.round(n*0.75/90000*100)/100;
  document.getElementById('ctx-res').textContent='≈ '+n.toLocaleString('es-ES')+' tokens ≈ '+Math.round(n*0.75).toLocaleString('es-ES')+' palabras ≈ '+paginas.toLocaleString('es-ES')+' páginas ≈ '+libros.toLocaleString('es-ES')+' libros de 300 páginas';}
window.addEventListener('load',function(){if(document.getElementById('pred-frase'))predPintar();if(document.getElementById('pb-salida'))pbMontar();if(document.getElementById('ctx-n'))ctxActualizar();});
