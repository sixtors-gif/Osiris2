"""JavaScript del curso de LSE (lse.js): autoevaluaciones, desplegables y entrenadores de dactilología."""

LSE_JS = r"""// lse.js · herramientas interactivas del curso (todo funciona en el navegador, sin conexión)
function comoTodos(a){document.querySelectorAll('details.como').forEach(function(d){d.open=a;});}
function checkAnswer(btn,ok,id){var p=btn.parentElement;p.querySelectorAll('.option').forEach(function(b){b.classList.remove('correct','incorrect')});
  btn.classList.add(ok?'correct':'incorrect');var fb=document.getElementById('fb-'+id);fb.textContent=ok?'✅ ¡Correcto! '+fb.getAttribute('data-ok'):'❌ No es correcto. Repasa el apartado e inténtalo de nuevo.';}

// ---- Alfabeto manual: descripciones orientativas de cada letra ----
var LETRAS={
 A:'Puño cerrado con el pulgar apoyado al lado del índice, visto de frente.',
 B:'Mano abierta con los dedos juntos y estirados hacia arriba; el pulgar doblado sobre la palma.',
 C:'Mano en forma de «C»: dedos y pulgar curvados.',
 D:'Índice estirado hacia arriba; el resto de los dedos y el pulgar forman un círculo.',
 E:'Dedos doblados con las yemas hacia la palma; el pulgar queda debajo.',
 F:'Pulgar e índice forman un círculo; los otros tres dedos, estirados.',
 G:'Puño con el índice y el pulgar extendidos hacia el lado, paralelos.',
 H:'Índice y corazón juntos y extendidos hacia el lado.',
 I:'Puño con solo el meñique estirado.',
 J:'Meñique estirado que dibuja una J en el aire.',
 K:'Índice y corazón en «V»; el pulgar toca el corazón.',
 L:'Índice hacia arriba y pulgar hacia un lado, formando una «L».',
 M:'Índice, corazón y anular doblados sobre el pulgar.',
 N:'Índice y corazón doblados sobre el pulgar.',
 'Ñ':'Como la N, con un pequeño movimiento ondulante lateral.',
 O:'Todos los dedos y el pulgar forman un círculo.',
 P:'Como la K, pero apuntando hacia abajo.',
 Q:'Como la G, pero apuntando hacia abajo.',
 R:'Índice y corazón cruzados.',
 S:'Puño con el pulgar cruzado por delante de los dedos.',
 T:'Puño con el pulgar asomando entre el índice y el corazón.',
 U:'Índice y corazón juntos y estirados hacia arriba.',
 V:'Índice y corazón separados, en «V».',
 W:'Índice, corazón y anular separados y estirados hacia arriba.',
 X:'Índice doblado en forma de gancho.',
 Y:'Pulgar y meñique estirados; los demás dedos cerrados.',
 Z:'Índice que dibuja una Z en el aire.'
};
function limpiaPalabra(t){return t.toUpperCase().normalize('NFD').replace(/Ñ/g,'Ñ').replace(/[̀-ͯ]/g,'').replace(/[^A-ZÑ]/g,'');}
var dl={tm:null};
function dlGenerar(){
  var p=limpiaPalabra(document.getElementById('dl-texto').value||'');
  var c=document.getElementById('dl-tarjetas');c.innerHTML='';
  if(!p){c.innerHTML='<p class="small">Escribe una palabra o tu nombre (sin números ni signos).</p>';return;}
  p.split('').forEach(function(l){var d=document.createElement('div');d.className='letra-card';d.innerHTML='<b>'+l+'</b><span>'+LETRAS[l]+'</span>';c.appendChild(d);});
}
function dlReproducir(){
  clearTimeout(dl.tm);
  var p=limpiaPalabra(document.getElementById('dl-texto').value||''),v=parseInt(document.getElementById('dl-vel').value,10),g=document.getElementById('dl-grande');
  if(!p){g.innerHTML='';return;}
  var i=0;(function paso(){if(i>=p.length){g.innerHTML='<b>✔</b><span>Fin. ¿Has deletreado «'+p+'» siguiendo las descripciones?</span>';return;}
    var l=p[i++];g.innerHTML='<b>'+l+'</b><span>'+LETRAS[l]+'</span>';dl.tm=setTimeout(paso,v);})();
}
function dlVelTxt(){document.getElementById('dl-vel-t').textContent=(document.getElementById('dl-vel').value/1000).toFixed(1)+' s por letra';}
// ---- Juego: ¿qué letra es? ----
var jl={ok:0,n:0,cur:null};
function jlNueva(){
  var ks=Object.keys(LETRAS);var l=ks[Math.floor(Math.random()*ks.length)];jl.cur=l;
  var ops=[l];while(ops.length<4){var x=ks[Math.floor(Math.random()*ks.length)];if(ops.indexOf(x)<0)ops.push(x);}
  ops.sort(function(){return Math.random()-.5;});
  document.getElementById('jl-desc').textContent=LETRAS[l];
  var b=document.getElementById('jl-ops');b.innerHTML='';
  ops.forEach(function(o){var e=document.createElement('button');e.textContent=o;e.onclick=function(){jlResp(o,e);};b.appendChild(e);});
  document.getElementById('jl-msg').textContent='';
}
function jlResp(o,e){jl.n++;var ok=(o===jl.cur);if(ok){jl.ok++;e.className='ok';}else{e.className='ko';}
  document.getElementById('jl-msg').textContent=ok?'✅ ¡Correcto!':'❌ Era la '+jl.cur+'.';
  document.getElementById('jl-pt').textContent=jl.ok+' de '+jl.n;
  var bs=document.querySelectorAll('#jl-ops button');bs.forEach(function(x){x.disabled=true;});setTimeout(jlNueva,1300);}
window.addEventListener('load',function(){if(document.getElementById('dl-vel')){dlVelTxt();dlGenerar();}if(document.getElementById('jl-ops'))jlNueva();});
"""
