/* dragdrop.js · actividades de arrastrar y soltar para los cursos SCORM (sin dependencias).
   Tipos: emparejar, clasificar, ordenar, rellenar y etiquetar (sobre una imagen).
   Funciona con ratón, con el dedo (pantallas táctiles) y con teclado/pulsación: se pulsa una ficha y después su destino. */
(function(){
'use strict';
var drag=null,sel=null,sinClic=false;
function el(t,c,txt){var e=document.createElement(t);if(c)e.className=c;if(txt!=null)e.textContent=txt;return e;}
function mezclar(a){a=a.slice();for(var i=a.length-1;i>0;i--){var j=Math.floor(Math.random()*(i+1)),t=a[i];a[i]=a[j];a[j]=t;}return a;}
function mezclarDistinto(a){var b=mezclar(a),k=0,igual=function(){return b.every(function(x,i){return x===a[i];});};while(a.length>1&&igual()&&k++<20)b=mezclar(a);return b;}

/* ---------- fichas ---------- */
function ficha(d,txt,id,cat){
  var c=el('button','dd-chip',txt);c.type='button';c.setAttribute('data-id',id);if(cat!=null)c.setAttribute('data-cat',cat);
  c.addEventListener('pointerdown',function(ev){iniciar(ev,d,c);});
  c.addEventListener('click',function(ev){ev.stopPropagation();if(sinClic){return;}seleccionar(c);});
  return c;
}
function seleccionar(c){
  if(sel===c){c.classList.remove('dd-sel');sel=null;return;}
  if(sel)sel.classList.remove('dd-sel');sel=c;c.classList.add('dd-sel');
}
function destinoDe(x,y,ghost){
  if(ghost)ghost.style.display='none';var e=document.elementFromPoint(x,y);if(ghost)ghost.style.display='';
  return e&&e.closest?e.closest('.dd-slot,.dd-cat,.dd-pool'):null;
}
function iniciar(ev,d,c){
  if(ev.button>0)return;
  drag={d:d,c:c,x:ev.clientX,y:ev.clientY,on:false,g:null};
  document.addEventListener('pointermove',mover);document.addEventListener('pointerup',soltar);document.addEventListener('pointercancel',cancelar);
}
function mover(ev){
  if(!drag)return;
  if(!drag.on){if(Math.hypot(ev.clientX-drag.x,ev.clientY-drag.y)<7)return;
    drag.on=true;var r=drag.c.getBoundingClientRect(),g=drag.c.cloneNode(true);g.className='dd-chip dd-ghost';g.style.width=r.width+'px';
    document.body.appendChild(g);drag.g=g;drag.dx=ev.clientX-r.left;drag.dy=ev.clientY-r.top;drag.c.classList.add('dd-arrastrando');}
  drag.g.style.left=(ev.clientX-drag.dx)+'px';drag.g.style.top=(ev.clientY-drag.dy)+'px';
  document.querySelectorAll('.dd-sobre').forEach(function(x){x.classList.remove('dd-sobre');});
  var t=destinoDe(ev.clientX,ev.clientY,drag.g);if(t)t.classList.add('dd-sobre');
  ev.preventDefault();
}
function fin(){
  document.removeEventListener('pointermove',mover);document.removeEventListener('pointerup',soltar);document.removeEventListener('pointercancel',cancelar);
  document.querySelectorAll('.dd-sobre').forEach(function(x){x.classList.remove('dd-sobre');});
  if(drag&&drag.g&&drag.g.parentNode)drag.g.parentNode.removeChild(drag.g);
  if(drag)drag.c.classList.remove('dd-arrastrando');
}
function soltar(ev){
  if(!drag)return;var on=drag.on,t=on?destinoDe(ev.clientX,ev.clientY,drag.g):null,d=drag.d,c=drag.c;
  fin();drag=null;
  if(on){sinClic=true;setTimeout(function(){sinClic=false;},60);if(t)colocar(d,c,t);}
}
function cancelar(){fin();drag=null;}

/* ---------- colocar una ficha en un destino ---------- */
function colocar(d,c,t){
  if(sel){sel.classList.remove('dd-sel');sel=null;}
  if(t.classList.contains('dd-slot')){
    var ocupante=t.querySelector('.dd-chip');if(ocupante&&ocupante!==c)d.pool.appendChild(ocupante);
    t.appendChild(c);
  }else if(t.classList.contains('dd-cat')){t.querySelector('.dd-cat-lista').appendChild(c);}
  else{d.pool.appendChild(c);}
  limpiar(d);
}
function limpiar(d){
  d.root.querySelectorAll('.dd-ok,.dd-ko').forEach(function(x){x.classList.remove('dd-ok','dd-ko');});
  d.msg.textContent='';d.msg.className='dd-msg';
}
function destinoClic(d,t){return function(ev){
  if(ev.target.closest&&ev.target.closest('.dd-chip'))return;
  if(sel&&sel.closest('.dd')===d.root)colocar(d,sel,t);
};}
function hacerSlot(d,cls){var s=el('div','dd-slot'+(cls?' '+cls:''));s.tabIndex=0;s.setAttribute('role','button');
  s.addEventListener('click',destinoClic(d,s));s.addEventListener('keydown',function(ev){if((ev.key==='Enter'||ev.key===' ')&&ev.target===s){ev.preventDefault();destinoClic(d,s)(ev);}});return s;}

/* ---------- barra de botones ---------- */
function barra(d,comprobar,solucion){
  var b=el('div','dd-barra');
  var c=el('button','dd-btn','Comprobar');c.type='button';c.onclick=comprobar;
  var s=el('button','dd-btn dd-sec','Ver solución');s.type='button';s.onclick=solucion;
  var r=el('button','dd-btn dd-sec','Reiniciar');r.type='button';r.onclick=function(){construir(d.root,d.cfg);};
  b.appendChild(c);b.appendChild(s);b.appendChild(r);d.msg=el('div','dd-msg');d.msg.setAttribute('aria-live','polite');
  d.root.appendChild(b);d.root.appendChild(d.msg);
}
function resultado(d,ok,total,cuentaTodo){
  if(ok===total){d.msg.textContent='✅ ¡Perfecto! '+ok+' de '+total+'.';d.msg.className='dd-msg dd-bien';}
  else{d.msg.textContent=ok+' de '+total+' bien. Revisa las que están en rojo y vuelve a intentarlo.'+(cuentaTodo||'');d.msg.className='dd-msg dd-mal';}
}

/* ---------- construcción ---------- */
function cabecera(d){
  var cfg=d.cfg;if(cfg.titulo)d.root.appendChild(el('h4','dd-titulo','🖱️ '+cfg.titulo));
  d.root.appendChild(el('p','dd-instr',cfg.instruccion||'Arrastra cada ficha a su sitio (o pulsa una ficha y después su destino).'));
}
function reserva(d,fichas){
  d.pool=el('div','dd-pool');d.pool.setAttribute('aria-label','Fichas por colocar');
  d.pool.addEventListener('click',destinoClic(d,d.pool));
  mezclar(fichas).forEach(function(f){d.pool.appendChild(f);});d.root.appendChild(d.pool);
}
var TIPOS={
 emparejar:function(d){
  var cfg=d.cfg,filas=el('div','dd-filas'),slots=[];
  cfg.pares.forEach(function(p,i){var f=el('div','dd-fila');f.appendChild(el('div','dd-pregunta',p[0]));var s=hacerSlot(d,'');s.setAttribute('data-i',i);f.appendChild(s);filas.appendChild(f);slots.push(s);});
  d.root.appendChild(filas);
  reserva(d,cfg.pares.map(function(p,i){return ficha(d,p[1],i);}).concat((cfg.extra||[]).map(function(t){return ficha(d,t,-1);})));
  barra(d,function(){var ok=0;slots.forEach(function(s,i){var c=s.querySelector('.dd-chip');s.classList.remove('dd-ok','dd-ko');if(c&&+c.getAttribute('data-id')===i){ok++;s.classList.add('dd-ok');}else s.classList.add('dd-ko');});resultado(d,ok,slots.length);},
   function(){cfg.pares.forEach(function(p,i){var c=d.root.querySelector('.dd-chip[data-id="'+i+'"]');colocar(d,c,slots[i]);});});
 },
 clasificar:function(d){
  var cfg=d.cfg,cats=el('div','dd-cats'),zonas=[];
  cfg.categorias.forEach(function(n,j){var c=el('div','dd-cat');c.setAttribute('data-j',j);c.appendChild(el('div','dd-cat-t',n));c.appendChild(el('div','dd-cat-lista'));
    c.addEventListener('click',destinoClic(d,c));cats.appendChild(c);zonas.push(c);});
  d.root.appendChild(cats);
  reserva(d,cfg.items.map(function(it,i){return ficha(d,it[0],i,it[1]);}));
  barra(d,function(){var ok=0,tot=cfg.items.length;d.root.querySelectorAll('.dd-chip').forEach(function(c){c.classList.remove('dd-ok','dd-ko');var z=c.closest('.dd-cat');
      if(z&&+z.getAttribute('data-j')===+c.getAttribute('data-cat')){ok++;c.classList.add('dd-ok');}else c.classList.add('dd-ko');});resultado(d,ok,tot);},
   function(){d.root.querySelectorAll('.dd-chip').forEach(function(c){colocar(d,c,zonas[+c.getAttribute('data-cat')]);});});
 },
 ordenar:function(d){
  var cfg=d.cfg,n=cfg.items.length,lista=el('ol','dd-orden');
  function numerar(){Array.prototype.forEach.call(lista.children,function(li,k){li.querySelector('.dd-num').textContent=(k+1)+'.';});}
  function mover(li,dir){var h=dir<0?li.previousElementSibling:li.nextElementSibling;if(!h)return;if(dir<0)lista.insertBefore(li,h);else lista.insertBefore(h,li);numerar();limpiar(d);}
  var orden=mezclarDistinto(cfg.items.map(function(t,i){return i;}));
  orden.forEach(function(i){
    var li=el('li','dd-item');li.setAttribute('data-i',i);
    li.appendChild(el('span','dd-asa','☰'));li.appendChild(el('span','dd-num',''));li.appendChild(el('span','dd-txt',cfg.items[i]));
    var up=el('button','dd-flecha','▲'),dn=el('button','dd-flecha','▼');up.type=dn.type='button';up.setAttribute('aria-label','Subir');dn.setAttribute('aria-label','Bajar');
    up.onclick=function(){mover(li,-1);};dn.onclick=function(){mover(li,1);};li.appendChild(up);li.appendChild(dn);
    li.addEventListener('pointerdown',function(ev){
      if(ev.button>0||ev.target.closest('.dd-flecha'))return;var y0=ev.clientY,on=false;
      function mv(e){if(!on&&Math.abs(e.clientY-y0)<6)return;on=true;li.classList.add('dd-arrastrando');
        var hs=Array.prototype.slice.call(lista.children);for(var k=0;k<hs.length;k++){var h=hs[k];if(h===li)continue;var r=h.getBoundingClientRect();
          if(e.clientY>r.top&&e.clientY<r.bottom){var antes=hs.indexOf(li)>k;if(antes)lista.insertBefore(li,h);else lista.insertBefore(li,h.nextSibling);break;}}
        numerar();e.preventDefault();}
      function up2(){document.removeEventListener('pointermove',mv);document.removeEventListener('pointerup',up2);li.classList.remove('dd-arrastrando');if(on)limpiar(d);}
      document.addEventListener('pointermove',mv,{passive:false});document.addEventListener('pointerup',up2);
    });
    lista.appendChild(li);
  });
  numerar();d.root.appendChild(lista);
  barra(d,function(){var ok=0;Array.prototype.forEach.call(lista.children,function(li,k){li.classList.remove('dd-ok','dd-ko');if(+li.getAttribute('data-i')===k){ok++;li.classList.add('dd-ok');}else li.classList.add('dd-ko');});resultado(d,ok,n);},
   function(){for(var i=0;i<n;i++){lista.appendChild(lista.querySelector('li[data-i="'+i+'"]'));}numerar();limpiar(d);});
 },
 rellenar:function(d){
  var cfg=d.cfg,p=el('p','dd-texto'),slots={};
  cfg.texto.split(/(\{\d+\})/).forEach(function(parte){var m=/^\{(\d+)\}$/.exec(parte);
    if(m){var s=hacerSlot(d,'dd-hueco');s.setAttribute('data-i',m[1]);slots[m[1]]=s;p.appendChild(s);}else p.appendChild(document.createTextNode(parte));});
  d.root.appendChild(p);
  reserva(d,cfg.huecos.map(function(w,i){return ficha(d,w,i);}).concat((cfg.extra||[]).map(function(t){return ficha(d,t,-1);})));
  barra(d,function(){var ok=0;Object.keys(slots).forEach(function(i){var s=slots[i],c=s.querySelector('.dd-chip');s.classList.remove('dd-ok','dd-ko');if(c&&+c.getAttribute('data-id')===+i){ok++;s.classList.add('dd-ok');}else s.classList.add('dd-ko');});resultado(d,ok,cfg.huecos.length);},
   function(){cfg.huecos.forEach(function(w,i){colocar(d,d.root.querySelector('.dd-chip[data-id="'+i+'"]'),slots[i]);});});
 },
 etiquetar:function(d){
  var cfg=d.cfg,caja=el('div','dd-img'),slots=[];
  if(cfg.ancho)caja.style.maxWidth=cfg.ancho+'px';
  var img=el('img');img.src=cfg.imagen;img.alt=cfg.alt||'';img.draggable=false;caja.appendChild(img);
  var NS='http://www.w3.org/2000/svg',svg=document.createElementNS(NS,'svg');svg.setAttribute('class','dd-lineas');svg.setAttribute('viewBox','0 0 100 100');svg.setAttribute('preserveAspectRatio','none');caja.appendChild(svg);
  cfg.zonas.forEach(function(z,i){
    if(z.punto){var l=document.createElementNS(NS,'line');l.setAttribute('x1',z.x);l.setAttribute('y1',z.y);l.setAttribute('x2',z.punto[0]);l.setAttribute('y2',z.punto[1]);l.setAttribute('vector-effect','non-scaling-stroke');svg.appendChild(l);
      var pt=el('span','dd-punto');pt.style.left=z.punto[0]+'%';pt.style.top=z.punto[1]+'%';caja.appendChild(pt);}
    var s=hacerSlot(d,'dd-zona');s.style.left=z.x+'%';s.style.top=z.y+'%';if(z.ancho)s.style.width=z.ancho+'px';s.setAttribute('data-i',i);s.setAttribute('aria-label','Zona '+(i+1));caja.appendChild(s);slots.push(s);});
  d.root.appendChild(caja);
  reserva(d,cfg.zonas.map(function(z,i){return ficha(d,z.respuesta,i);}).concat((cfg.extra||[]).map(function(t){return ficha(d,t,-1);})));
  barra(d,function(){var ok=0;slots.forEach(function(s,i){var c=s.querySelector('.dd-chip');s.classList.remove('dd-ok','dd-ko');if(c&&+c.getAttribute('data-id')===i){ok++;s.classList.add('dd-ok');}else s.classList.add('dd-ko');});resultado(d,ok,slots.length);},
   function(){cfg.zonas.forEach(function(z,i){colocar(d,d.root.querySelector('.dd-chip[data-id="'+i+'"]'),slots[i]);});});
 }
};
function construir(root,cfg){
  root.innerHTML='';sel=null;
  var d={root:root,cfg:cfg};cabecera(d);TIPOS[cfg.tipo](d);
}
function iniciarTodo(){
  document.querySelectorAll('.dd[data-config]').forEach(function(root){
    if(root.getAttribute('data-listo'))return;
    try{var cfg=JSON.parse(root.getAttribute('data-config'));root.setAttribute('data-listo','1');construir(root,cfg);}
    catch(e){root.textContent='No se ha podido cargar esta actividad.';}
  });
}
window.DD={iniciar:iniciarTodo};
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',iniciarTodo);else iniciarTodo();
})();
