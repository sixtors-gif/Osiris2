// piano.js · partituras (abcjs), reproducción, metrónomo y entrenador de lectura
var VISUAL = {}, sonando = null;
function dibujarPartituras(){
  if(!window.ABCJS||!window.PARTITURAS)return;
  Object.keys(PARTITURAS).forEach(function(id){
    var el=document.getElementById('p-'+id); if(!el)return;
    var op={responsive:'resize',add_classes:true,staffwidth:900,wrap:{minSpacing:1.6,maxSpacing:2.6,preferredMeasuresPerLine:4},paddingleft:0,paddingright:0};
    if(/^% sin-ajuste/m.test(PARTITURAS[id])){delete op.wrap;op.paddingright=30;} // respeta los saltos de línea (cambios de armadura)
    VISUAL[id]=ABCJS.renderAbc(el,PARTITURAS[id],op)[0];
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
// Entrenador de intervalos: dos notas, el alumno elige número y calidad
var INT={bien:0,total:0,n:null,c:null,sel:{n:null,c:null}},SEMI=[0,2,4,5,7,9,11],REF=[0,2,4,5,7,9,11,12],LETRAS=['C','D','E','F','G','A','B'];
var CAL=['justa','mayor','menor','aumentada','disminuida'];
function intAbc(d,a){var o=Math.floor(d/7),l=LETRAS[d%7],ac=a>0?'^':(a<0?'_':'');if(o===0)return ac+l;if(o===1)return ac+l.toLowerCase();return ac+l.toLowerCase()+"'";}
function intNueva(){
  clearTimeout(INT.t);
  for(var k=0;k<200;k++){
    var d1=Math.floor(Math.random()*8),n=2+Math.floor(Math.random()*7),d2=d1+n-1,a1=[0,0,0,1,-1][Math.floor(Math.random()*5)],a2=[0,0,0,1,-1][Math.floor(Math.random()*5)];
    var s1=12*Math.floor(d1/7)+SEMI[d1%7]+a1,s2=12*Math.floor(d2/7)+SEMI[d2%7]+a2,sem=s2-s1,dif=sem-REF[n-1],c=null;
    if(n===4||n===5||n===8){c=dif===0?'justa':(dif===1?'aumentada':(dif===-1?'disminuida':null));}
    else{c=dif===0?'mayor':(dif===-1?'menor':(dif===1?'aumentada':(dif===-2?'disminuida':null)));}
    if(!c||sem<1)continue;
    INT.n=n;INT.c=c;INT.sel={n:null,c:null};INT.sem=sem;
    ABCJS.renderAbc('int-pent','X:1\nL:1/1\nK:C clef=treble\n['+intAbc(d1,a1)+intAbc(d2,a2)+']|',{scale:1.6,staffwidth:150,paddingleft:10});
    document.querySelectorAll('#int-num button,#int-cal button').forEach(function(b){b.className='';});
    document.getElementById('int-fb').textContent='¿Qué intervalo forman estas dos notas?';return;
  }
}
function intElige(tipo,v,btn){if(!INT.n)return;INT.sel[tipo]=v;document.querySelectorAll(tipo==='n'?'#int-num button':'#int-cal button').forEach(function(b){b.className='';});btn.className='sel';}
function intComprobar(){
  if(!INT.n)return;if(!INT.sel.n||!INT.sel.c){document.getElementById('int-fb').textContent='Elige el número y la calidad.';return;}
  INT.total++;var ok=INT.sel.n===INT.n&&INT.sel.c===INT.c;if(ok)INT.bien++;
  document.getElementById('int-fb').textContent=(ok?'✅ ¡Correcto! ':'❌ Era una '+INT.n+'.ª '+INT.c+' ('+INT.sem+' semitonos). ')+(ok?'('+INT.sem+' semitonos). ':'')+'Aciertos: '+INT.bien+'/'+INT.total;
  INT.n=null;INT.t=setTimeout(intNueva,ok?900:2400);
}
// Entrenador de armaduras: aparece una armadura y se pregunta la tonalidad mayor
var ARM_T=[['C',['Do']],['G',['Sol']],['D',['Re']],['A',['La']],['E',['Mi']],['B',['Si']],['F#',['Fa♯']],['C#',['Re♭','Do♯']],
           ['F',['Fa']],['Bb',['Si♭']],['Eb',['Mi♭']],['Ab',['La♭']],['Db',['Re♭','Do♯']],['Gb',['Fa♯','Sol♭']],['Cb',['Si','Do♭']]],
    arm={k:null,bien:0,total:0};
function armNueva(){clearTimeout(arm.t);var t=ARM_T[Math.floor(Math.random()*ARM_T.length)];arm.k=t;
  ABCJS.renderAbc('arm-pent','X:1\nL:1\nK:'+t[0]+' clef=treble\nz|',{scale:1.6,staffwidth:200,paddingleft:10});
  document.querySelectorAll('#arm-btns button').forEach(function(b){b.className='';});document.getElementById('arm-fb').textContent='¿Qué tonalidad mayor es?';}
function armResp(nombre,btn){if(!arm.k)return;arm.total++;var ok=arm.k[1].indexOf(nombre)>=0;
  if(ok){arm.bien++;btn.className='ok';}else{btn.className='ko';}
  document.getElementById('arm-fb').textContent=(ok?'✅ ¡Bien! ':'❌ Era '+arm.k[1].join(' / ')+' mayor. ')+'Aciertos: '+arm.bien+'/'+arm.total;
  arm.k=null;arm.t=setTimeout(armNueva,ok?700:2000);}
function lectResp(letra,btn){if(!lect.nota)return;lect.total++;var ok=letra===lect.nota;
  if(ok){lect.bien++;lect.racha++;btn.className='ok';}else{lect.racha=0;btn.className='ko';}
  document.getElementById('lect-fb').textContent=(ok?'✅ ¡Bien! ':'❌ Era '+NOMBRE[lect.nota]+'. ')+'Aciertos: '+lect.bien+'/'+lect.total+' · racha: '+lect.racha;
  lect.nota=null;setTimeout(lectNueva,ok?600:1400);}
// Autoevaluaciones
function checkAnswer(btn,ok,id){var p=btn.parentElement;p.querySelectorAll('.option').forEach(function(b){b.classList.remove('correct','incorrect')});
  btn.classList.add(ok?'correct':'incorrect');var fb=document.getElementById('fb-'+id);fb.textContent=ok?'✅ ¡Correcto! '+fb.getAttribute('data-ok'):'❌ No es correcto. Repasa el apartado e inténtalo de nuevo.';}
window.addEventListener('load',dibujarPartituras);
