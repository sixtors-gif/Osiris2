#!/usr/bin/env python3
"""Genera index, examen final, banco GIFT, manifiesto y README del Curso 2."""
import sys, os, html, json

OUT = sys.argv[1]
FOOTER = "Curso 2: Ciberseguridad Avanzada y Defensa Digital · Material educativo · Creado por: Sixto Rodríguez de Sepúlveda"

MODS = [
    ("🤖", "Ciberamenazas emergentes e inteligencia artificial", "Modulo01_IA_y_Amenazas"),
    ("🕵️", "Doxxing, ingeniería social avanzada y privacidad", "Modulo02_Doxxing_y_Privacidad"),
    ("📱", "Vulnerabilidades y amenazas en dispositivos móviles", "Modulo03_Seguridad_Movil"),
    ("🛡️", "Bastionado de smartphones y dispositivos IoT", "Modulo04_Bastionado_e_IoT"),
    ("🦠", "Malware avanzado y ransomware", "Modulo05_Malware_Avanzado"),
    ("🎩", "Hacking ético y auditoría de seguridad", "Modulo06_Hacking_Etico"),
    ("🔑", "Cifrado, redes privadas y navegación segura", "Modulo07_Cifrado_y_VPN"),
    ("🚨", "Respuesta ante incidentes y forense digital básica", "Modulo08_Respuesta_Incidentes"),
    ("⚖️", "Aspectos legales, ciberdelito y ética digital", "Modulo09_Legal_y_Etica"),
    ("🏆", "Proyecto final: auditoría de seguridad personal y móvil", "Modulo10_Proyecto_Final"),
]

# (módulo, pregunta, [opciones], índice correcto, en_examen)
Q = [
 (1, "Recibes una llamada con la voz exacta de un familiar pidiendo una transferencia urgente. ¿Cuál es la respuesta más segura?",
  ["Hacer la transferencia para evitar problemas.", "Colgar y llamar a su número habitual o pedir la palabra clave acordada.", "Pedirle una foto de su DNI por WhatsApp.", "Pedirle que mande otro audio."], 1, True),
 (1, "Un deepfake es:",
  ["Un virus que bloquea la cámara web.", "Un contenido de audio, imagen o vídeo manipulado o generado con inteligencia artificial de forma hiperrealista.", "Una técnica para comprimir vídeos.", "Un ataque que daña el hardware del móvil."], 1, True),
 (1, "¿Por qué ya no basta con buscar faltas de ortografía para detectar phishing?",
  ["Porque la IA redacta mensajes correctos y personalizados.", "Porque el phishing ya no existe.", "Porque los bancos escriben con faltas.", "Porque los antivirus corrigen los mensajes."], 0, False),
 (2, "¿Qué medida ayuda a prevenir el doxxing al publicar fotografías?",
  ["Eliminar los metadatos de ubicación (EXIF/GPS) y no mostrar fachadas o portales.", "Usar el mismo alias en todas las plataformas.", "Añadir un filtro de color.", "Subir la foto en mayor resolución."], 0, True),
 (2, "El doxxing consiste en:",
  ["Enviar correo basura masivo.", "Recopilar y publicar sin consentimiento información personal de alguien para intimidarle o acosarle.", "Un fallo del router Wi‑Fi.", "Instalar apps de prueba en el móvil."], 1, True),
 (2, "Alguien que se hace pasar por «soporte técnico del juego» para pedirte tu código de verificación está usando:",
  ["Pretexting (ingeniería social).", "Cifrado de extremo a extremo.", "Una actualización legítima.", "Bastionado."], 0, False),
 (3, "¿Por qué el abuso de los servicios de accesibilidad en Android es un riesgo crítico?",
  ["Porque consume más datos.", "Porque permite a una app maliciosa leer la pantalla, capturar credenciales y actuar sin tu permiso.", "Porque desactiva el Wi‑Fi.", "Porque cambia el fondo de pantalla."], 1, True),
 (3, "El sideloading es:",
  ["Cargar el móvil por un lateral.", "Instalar aplicaciones (por ejemplo APK) desde fuera de las tiendas oficiales.", "Usar dos tarjetas SIM a la vez.", "Duplicar la pantalla en la televisión."], 1, True),
 (3, "¿Cuál de estos es un indicador de compromiso en un móvil?",
  ["Recibir códigos de verificación por SMS que no has solicitado.", "Que la pantalla se apague al no usarla.", "Que las apps se actualicen solas desde la tienda oficial.", "Que el móvil se caliente al cargar."], 0, False),
 (4, "¿Cuál es la mejor práctica para proteger los dispositivos IoT del hogar?",
  ["Conectarlos a una red de invitados separada, con contraseña propia y firmware actualizado.", "Apagar el router por la noche.", "Mantener la contraseña de fábrica.", "Darles permisos de administrador de red."], 0, True),
 (4, "¿Qué método de verificación en dos pasos es más resistente al SIM swapping?",
  ["Código por SMS.", "App autenticadora o llave de acceso (passkey).", "Pregunta de seguridad.", "Correo electrónico sin contraseña."], 1, True),
 (4, "Bastionar un dispositivo significa:",
  ["Configurarlo para reducir funciones innecesarias y reforzar su protección.", "Hacerle root para tener más control.", "Instalarle más aplicaciones.", "Desactivar las actualizaciones."], 0, False),
 (5, "¿Cuál es la función principal de un infostealer?",
  ["Bloquear la pantalla con una contraseña.", "Robar contraseñas guardadas, cookies de sesión y carteras de criptomonedas.", "Mostrar publicidad.", "Acelerar el ordenador."], 1, True),
 (5, "¿Qué regla de copias de seguridad protege mejor frente al ransomware?",
  ["Una única copia en el mismo disco.", "La regla 3-2-1, con al menos una copia desconectada o fuera de casa.", "Guardar todo solo en el móvil.", "No hacer copias para no ocupar espacio."], 1, True),
 (5, "El ransomware de doble extorsión:",
  ["Cifra los archivos y además amenaza con publicar los datos robados.", "Solo muestra anuncios.", "Borra el sistema operativo sin pedir nada.", "Únicamente ralentiza el equipo."], 0, False),
 (6, "¿Qué distingue legalmente a un hacker ético de un ciberdelincuente?",
  ["Las herramientas que usa.", "La autorización previa y por escrito del propietario del sistema.", "Que trabaja de noche.", "Que no cobra por su trabajo."], 1, True),
 (6, "Descubres por casualidad un fallo que expone datos en una web. ¿Qué es la divulgación responsable?",
  ["Publicarlo en redes para presionar.", "Descargar los datos como prueba.", "Avisar de forma privada al responsable (o a INCIBE-CERT) sin explotarlo ni difundirlo.", "Venderlo al mejor postor."], 2, True),
 (6, "¿Cuál es una forma legal de practicar hacking?",
  ["Probar contraseñas en cuentas de compañeros.", "Participar en retos CTF y usar laboratorios propios en máquinas virtuales.", "Escanear la red del centro sin permiso.", "Entrar en la Wi‑Fi del vecino."], 1, False),
 (7, "Una web muestra el candado HTTPS. ¿Qué garantiza?",
  ["Que la web es legítima.", "Que la conexión está cifrada, aunque la web podría ser fraudulenta.", "Que no tiene virus.", "Que tus datos no se guardan."], 1, True),
 (7, "¿Qué afirmación sobre una VPN es correcta?",
  ["Te hace totalmente anónimo.", "Cifra tu tráfico hasta el servidor VPN, pero no te protege del phishing ni del malware.", "Elimina virus.", "Impide que las webs usen cookies."], 1, True),
 (7, "El cifrado de extremo a extremo (E2EE) significa que:",
  ["Solo el emisor y el receptor pueden leer el mensaje.", "El servicio puede leer los mensajes para protegerte.", "Los mensajes se borran al leerlos.", "El mensaje viaja sin cifrar."], 0, False),
 (8, "Ante una infección por ransomware en un equipo conectado a la red, la primera acción debe ser:",
  ["Reiniciarlo varias veces.", "Desconectarlo de la red (Wi‑Fi o cable) para evitar la propagación.", "Formatear el disco sin guardar pruebas.", "Pagar el rescate."], 1, True),
 (8, "¿Cuál es el orden correcto del ciclo de respuesta ante incidentes?",
  ["Recuperar, detectar, contener, erradicar, aprender.", "Detectar, contener, erradicar, recuperar, aprender.", "Contener, aprender, detectar, recuperar, erradicar.", "Erradicar, detectar, recuperar, contener, aprender."], 1, True),
 (8, "Tras robarte una cuenta, ¿desde dónde conviene cambiar las contraseñas y cerrar sesiones?",
  ["Desde el mismo equipo infectado.", "Desde otro dispositivo limpio y de confianza.", "Desde un ordenador público.", "No hace falta cambiarlas."], 1, False),
 (9, "Reenviar a un grupo una imagen íntima de otra persona sin su consentimiento:",
  ["Es legal si no la has creado tú.", "Es delito, aunque tú no la hayas creado.", "Solo es delito si cobras por ello.", "Es legal si el grupo es privado."], 1, True),
 (9, "Pedir a una plataforma que borre tus datos personales es ejercer el derecho de:",
  ["Portabilidad.", "Supresión.", "Rectificación.", "Acceso."], 1, True),
 (9, "En España, ¿desde qué edad puede un menor responder penalmente por un ciberdelito?",
  ["Desde los 12 años.", "Desde los 14 años.", "Desde los 16 años.", "Solo a partir de los 18 años."], 1, False),
 (10, "¿Qué cuenta es prioritaria proteger en una auditoría personal?",
  ["La del juego que menos usas.", "El correo electrónico principal, porque permite recuperar las demás.", "Una cuenta de foro antigua.", "La de una app de linterna."], 1, True),
 (10, "Si tu correo aparece en una filtración conocida, debes:",
  ["Ignorarlo.", "Cambiar esa contraseña y cualquier otra donde la repitieras, y activar 2FA.", "Borrar el correo inmediatamente.", "Cambiar solo el nombre de usuario."], 1, True),
 (10, "¿Cada cuánto se recomienda repetir el checklist de seguridad personal?",
  ["Nunca, basta con hacerlo una vez.", "Periódicamente, por ejemplo cada tres meses.", "Solo cuando cambies de móvil.", "Solo si te roban una cuenta."], 1, False),
]
def _place(k, q):
    # Coloca la respuesta correcta en una posición rotatoria (A, B, C, D...) para equilibrar el examen.
    m, t, opts, ok, ex = q
    opts = list(opts); target = (k * 3 + 1) % len(opts)
    opts[ok], opts[target] = opts[target], opts[ok]
    return (m, t, opts, target, ex)
Q = [_place(k, q) for k, q in enumerate(Q)]
EXAM = [q for q in Q if q[4]]
assert len(EXAM) == 20 and len(Q) == 30

def gift_esc(s):
    for c in "~=#{}:":
        s = s.replace(c, "\\" + c)
    return s

# ---------- GIFT
g = ["// ===============================================",
     "// CURSO 2: CIBERSEGURIDAD AVANZADA Y DEFENSA DIGITAL",
     f"// BANCO DE PREGUNTAS EN FORMATO GIFT PARA MOODLE ({len(Q)} preguntas)",
     "// ==============================================="]
cur = None
cnt = {}
for m, q, opts, ok, _ in Q:
    if m != cur:
        cur = m
        g.append("")
        g.append(f"$CATEGORY: $course$/Ciberseguridad_Avanzada/{MODS[m-1][2]}")
    cnt[m] = cnt.get(m, 0) + 1
    g.append("")
    g.append(f"::M{m}_P{cnt[m]}::{gift_esc(q)} {{")
    for j, o in enumerate(opts):
        g.append(f"    {'=' if j == ok else '~'}{gift_esc(o)}")
    g.append("}")
open(os.path.join(OUT, "preguntas_moodle.gift"), "w", encoding="utf-8").write("\n".join(g) + "\n")

# ---------- Examen
qs = []
for i, (m, q, opts, ok, _) in enumerate(EXAM, 1):
    o = "".join(f'<label class="option"><input type="radio" name="q{i}" value="{j}" style="width:auto;margin-right:8px">{html.escape(t)}</label>'
                for j, t in enumerate(opts))
    qs.append(f'<div class="quiz" id="box{i}"><h4>{i}. {html.escape(q)} <span class="small">(Módulo {m})</span></h4><div class="options">{o}</div></div>')
answers = json.dumps([q[3] for q in EXAM])
exam = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Examen final: Ciberseguridad Avanzada</title>
<link rel="stylesheet" href="style.css">
</head>
<body>
<div class="container">
  <div class="header">
    <h1><span class="shield-icon">🏁</span>Examen final</h1>
    <img src="img/logo-centro.png" class="logo-centro" alt="Logotipo del centro">
    <p>Curso 2: Ciberseguridad Avanzada y Defensa Digital</p>
  </div>
  <div class="progress-container">
    <div class="progress-bar"><div class="progress-fill" style="width:100%"></div></div>
    <div class="progress-text">Ciberseguridad Avanzada · Examen final</div>
  </div>
  <div class="content-area">
    <section class="module">
      <h2>Evaluación final</h2>
      <p>Responde a las {len(EXAM)} preguntas. Necesitas al menos un <b>70 %</b> para aprobar. Al corregir verás qué respuestas son correctas y podrás repetir el examen.</p>
      {''.join(qs)}
      <div style="text-align:center"><button class="btn" onclick="corregir()">Corregir examen</button> <button class="btn" onclick="location.reload()">Reintentar</button></div>
      <div id="resultado" style="margin-top:20px"></div>
      <div class="navigation">
        <button class="nav-btn" onclick="window.location='modulo10.html'">⬅️ Módulo 10</button>
        <button class="nav-btn" onclick="window.location='index.html'">Inicio 🏠</button>
      </div>
    </section>
  </div>
</div>
<footer class="footer-autor">{FOOTER}</footer>
<script src="scorm.js"></script>
<script>
var RESP={answers};
function corregir(){{
  var ok=0,sin=0;
  for(var i=0;i<RESP.length;i++){{
    var n=i+1,sel=document.querySelector('input[name="q'+n+'"]:checked');
    var labels=document.querySelectorAll('#box'+n+' .option');
    labels.forEach(function(l){{l.classList.remove('correct','incorrect')}});
    labels[RESP[i]].classList.add('correct');
    if(!sel){{sin++;continue;}}
    if(+sel.value===RESP[i])ok++;else labels[+sel.value].classList.add('incorrect');
  }}
  var nota=Math.round(ok*100/RESP.length),r=document.getElementById('resultado');
  if(nota>=70){{
    r.innerHTML='<div class="certificate"><h2>🏆 ¡Enhorabuena!</h2><p>Has superado el <b>Curso 2: Ciberseguridad Avanzada y Defensa Digital</b>.</p><p style="font-size:1.6em;font-weight:700;color:#2e7d32">'+ok+'/'+RESP.length+' · '+nota+' %</p></div>';
  }}else{{
    r.innerHTML='<div class="alert-box"><b>Resultado: '+ok+'/'+RESP.length+' ('+nota+' %).</b> Necesitas un 70 % para aprobar'+(sin?' (has dejado '+sin+' sin responder)':'')+'. Repasa los módulos indicados en las preguntas falladas y vuelve a intentarlo.</div>';
  }}
  if(window.scorm)scorm.complete(nota);
  r.scrollIntoView({{behavior:'smooth'}});
}}
</script>
</body>
</html>
"""
open(os.path.join(OUT, "examen_final.html"), "w", encoding="utf-8").write(exam)

# ---------- Index
nums = ["1️⃣","2️⃣","3️⃣","4️⃣","5️⃣","6️⃣","7️⃣","8️⃣","9️⃣","🔟"]
itin = "".join(f'<li>{nums[i]} <span><a href="modulo{i+1}.html">{t}</a></span></li>' for i, (_, t, _) in enumerate(MODS))
index = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Curso 2: Ciberseguridad Avanzada y Defensa Digital</title>
<link rel="stylesheet" href="style.css">
</head>
<body>
<div class="container">
  <div class="header">
    <h1><span class="shield-icon">🛡️</span>Ciberseguridad Avanzada y Defensa Digital</h1>
    <img src="img/logo-centro.png" class="logo-centro" alt="Logotipo del centro">
    <p>Curso 2 · Da el salto: entiende cómo atacan y aprende a defenderte como un profesional.</p>
  </div>
  <div class="progress-container">
    <div class="progress-bar"><div class="progress-fill" style="width:0%"></div></div>
    <div class="progress-text">Ciberseguridad Avanzada · Módulo 0 de 10</div>
  </div>
  <div class="content-area">
    <section class="module">
      <h2>Bienvenido/a al Curso 2 👋</h2>
      <p>Este curso continúa el <b>Curso de Ciberseguridad para jóvenes</b>. Ya conoces los buenos hábitos básicos; ahora vas a profundizar en las amenazas actuales (inteligencia artificial, doxxing, malware móvil, ransomware), en cómo se defienden los profesionales y en lo que dice la ley.</p>
      <div class="box"><b>Objetivo:</b> al terminar sabrás reconocer amenazas avanzadas, bastionar tus dispositivos, responder ante un incidente conservando pruebas y realizar una auditoría de seguridad de tu propio entorno digital.</div>
      <div class="figure">
        <svg viewBox="0 0 640 130" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Recorrido del curso: amenazas, defensa, respuesta y ley, proyecto final y examen">
          <line x1="55" y1="45" x2="585" y2="45" stroke="#4ecdc4" stroke-width="4"/>
          <circle cx="55" cy="45" r="24" fill="#1e3c72"/><text x="55" y="51" font-size="13" text-anchor="middle" fill="#fff" font-weight="700">1‑3</text>
          <text x="55" y="90" font-size="12" text-anchor="middle" fill="#1e3c72" font-weight="700">Amenazas</text>
          <circle cx="188" cy="45" r="24" fill="#1e3c72"/><text x="188" y="51" font-size="13" text-anchor="middle" fill="#fff" font-weight="700">4‑7</text>
          <text x="188" y="90" font-size="12" text-anchor="middle" fill="#1e3c72" font-weight="700">Defensa</text>
          <circle cx="320" cy="45" r="24" fill="#1e3c72"/><text x="320" y="51" font-size="13" text-anchor="middle" fill="#fff" font-weight="700">8‑9</text>
          <text x="320" y="90" font-size="12" text-anchor="middle" fill="#1e3c72" font-weight="700">Respuesta</text>
          <text x="320" y="104" font-size="12" text-anchor="middle" fill="#1e3c72" font-weight="700">y ley</text>
          <circle cx="452" cy="45" r="24" fill="#4ecdc4"/><text x="452" y="52" font-size="18" text-anchor="middle">🏆</text>
          <text x="452" y="90" font-size="12" text-anchor="middle" fill="#1e3c72" font-weight="700">Proyecto</text>
          <text x="452" y="104" font-size="12" text-anchor="middle" fill="#1e3c72" font-weight="700">final</text>
          <circle cx="585" cy="45" r="24" fill="#4caf50"/><text x="585" y="52" font-size="18" text-anchor="middle">🏁</text>
          <text x="585" y="90" font-size="12" text-anchor="middle" fill="#2e7d32" font-weight="700">Examen</text>
          <text x="585" y="104" font-size="12" text-anchor="middle" fill="#2e7d32" font-weight="700">final</text>
        </svg>
      </div>
      <div class="alert-box"><b>Compromiso ético:</b> todo lo que aprendas aquí es para protegerte y proteger a los demás. Practica solo en tus propios dispositivos o en entornos autorizados. Acceder a sistemas o cuentas ajenas sin permiso es delito.</div>
      <h3>Itinerario</h3>
      <ul class="key-points">{itin}<li>🏁 <span><a href="examen_final.html">Examen final ({len(EXAM)} preguntas)</a></span></li></ul>
      <div class="activity">
        <h3>Reto inicial</h3>
        <p>¿Qué amenaza digital te preocupa más hoy y por qué? Vuelve a leer tu respuesta al terminar el curso.</p>
        <textarea placeholder="Ejemplo: que clonen la voz de alguien de mi familia..."></textarea>
        <button class="btn" onclick="document.getElementById('fb').textContent='¡Anotado! Al final del curso comprobarás cuánto has avanzado.'">Guardar reflexión</button>
        <p id="fb" class="feedback"></p>
      </div>
      <div class="navigation">
        <span></span>
        <button class="nav-btn" onclick="window.location='modulo1.html'">Comenzar ➡️</button>
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

# ---------- Manifiesto
common = '      <file href="style.css"/>\n      <file href="scorm.js"/>\n      <file href="img/logo-centro.png"/>\n'
items = [("ITEM_INTRO", "RES_INTRO", "Presentación del curso", "index.html")]
items += [(f"ITEM_MOD{i}", f"RES_MOD{i}", f"Módulo {i}: {t}", f"modulo{i}.html") for i, (_, t, _) in enumerate(MODS, 1)]
items += [("ITEM_EXAMEN", "RES_EXAMEN", "Examen final de Ciberseguridad Avanzada", "examen_final.html")]
it = "".join(f'      <item identifier="{a}" identifierref="{b}">\n        <title>{html.escape(t)}</title>\n      </item>\n' for a, b, t, _ in items)
rs = "".join(f'    <resource identifier="{b}" type="webcontent" adlcp:scormtype="sco" href="{h}">\n      <file href="{h}"/>\n{common}    </resource>\n' for _, b, _, h in items)
manifest = f"""<?xml version="1.0" encoding="UTF-8"?>
<manifest identifier="MANIFEST_CIBERSEGURIDAD_AVANZADA" version="2.0"
          xmlns="http://www.imsproject.org/xsd/imscp_rootv1p1p2"
          xmlns:adlcp="http://www.adlnet.org/xsd/adlcp_rootv1p1p2"
          xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
          xsi:schemaLocation="http://www.imsproject.org/xsd/imscp_rootv1p1p2 imscp_rootv1p1p2.xsd
                              http://www.adlnet.org/xsd/adlcp_rootv1p1p2 adlcp_rootv1p1p2.xsd">
  <metadata>
    <schema>ADL SCORM</schema>
    <schemaversion>1.2</schemaversion>
  </metadata>
  <organizations default="ORG_CIBER_AVANZADA">
    <organization identifier="ORG_CIBER_AVANZADA">
      <title>Curso 2: Ciberseguridad Avanzada y Defensa Digital</title>
{it}    </organization>
  </organizations>
  <resources>
{rs}  </resources>
</manifest>
"""
open(os.path.join(OUT, "imsmanifest.xml"), "w", encoding="utf-8").write(manifest)

# ---------- README
readme = f"""CURSO 2: CIBERSEGURIDAD AVANZADA Y DEFENSA DIGITAL — Paquete SCORM 1.2
Continuación del curso "Ciberseguridad para jóvenes".

Contenido:
- imsmanifest.xml: paquete SCORM 1.2 (presentación + 10 módulos + examen, cada uno como SCO).
- index.html: presentación, itinerario, compromiso ético y reto inicial.
- modulo1.html ... modulo10.html: 10 módulos con teoría, esquemas, autoevaluaciones interactivas,
  actividades prácticas y resumen:
    1. Ciberamenazas emergentes e inteligencia artificial
    2. Doxxing, ingeniería social avanzada y privacidad
    3. Vulnerabilidades y amenazas en dispositivos móviles
    4. Bastionado de smartphones y dispositivos IoT
    5. Malware avanzado y ransomware
    6. Hacking ético y auditoría de seguridad
    7. Cifrado, redes privadas y navegación segura
    8. Respuesta ante incidentes y forense digital básica
    9. Aspectos legales, ciberdelito y ética digital
   10. Proyecto final: auditoría de seguridad personal y móvil (checklist interactivo)
- examen_final.html: examen de {len(EXAM)} preguntas (2 por módulo), aprobado con 70 %, envía la nota al LMS.
- preguntas_moodle.gift: {len(Q)} preguntas en formato GIFT (3 por módulo) organizadas por categorías.
- style.css + scorm.js + img/logo-centro.png.

Importación en Moodle:
1. Crea una actividad "SCORM".
2. Sube el ZIP del curso completo (sin descomprimir).
3. Para las preguntas: Banco de preguntas > Importar > Formato GIFT y sube preguntas_moodle.gift.

Recursos de ayuda citados: Línea de Ayuda en Ciberseguridad de INCIBE (017) y Canal Prioritario de la AEPD.
"""
open(os.path.join(OUT, "README.txt"), "w", encoding="utf-8").write(readme)
print("ok", len(EXAM), len(Q))
