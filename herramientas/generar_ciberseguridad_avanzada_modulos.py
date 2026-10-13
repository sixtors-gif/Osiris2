#!/usr/bin/env python3
"""Genera el curso SCORM 'Curso 2: Ciberseguridad Avanzada y Defensa Digital'."""
import sys, os, html

OUT = sys.argv[1]
COURSE = "Curso 2: Ciberseguridad Avanzada y Defensa Digital"
FOOTER = "Curso 2: Ciberseguridad Avanzada y Defensa Digital · Material educativo · Creado por: Sixto Rodríguez de Sepúlveda"
N = 10

HELP = ('<div class="help-box"><b>¿Necesitas ayuda?</b><span class="phone">017</span>'
        'Línea de Ayuda en Ciberseguridad de INCIBE: gratuita y confidencial (teléfono, WhatsApp 900 116 117 y '
        '<a href="https://www.incibe.es/linea-de-ayuda-en-ciberseguridad" target="_blank" rel="noopener">incibe.es</a>).</div>')

def kp(items, ico):
    return '<ul class="key-points">' + "".join(f'<li>{ico} <span>{i}</span></li>' for i in items) + '</ul>'

def flow(steps):
    parts = []
    for i, s in enumerate(steps):
        if i: parts.append('<span class="flow-arrow">➜</span>')
        parts.append(f'<div class="flow-step">{s}</div>')
    return '<div class="flow">' + "".join(parts) + '</div>'

def cards(items):
    return '<div class="card-grid">' + "".join(
        f'<div class="mini-card"><div class="ico">{i}</div><b>{t}</b><span class="small">{d}</span></div>' for i, t, d in items) + '</div>'

def quiz(qid, q, opts, ok, why):
    btns = "".join(
        f'<button class="option" onclick="checkAnswer(this,{str(j == ok).lower()},\'{qid}\')">{chr(65+j)}. {o}</button>'
        for j, o in enumerate(opts))
    return (f'<div class="quiz"><h4>🧩 {q}</h4><div class="options">{btns}</div>'
            f'<p class="feedback" id="fb-{qid}" data-ok="{html.escape(why, quote=True)}"></p></div>')

def activity(title, text, ph):
    return (f'<div class="activity"><h3>✍️ {title}</h3><p>{text}</p>'
            f'<textarea placeholder="{ph}"></textarea>'
            '<p class="small">No escribas contraseñas ni datos personales reales en este cuadro.</p></div>')

SCRIPT = """<script>
function checkAnswer(btn,correct,id){var p=btn.parentElement;p.querySelectorAll('.option').forEach(function(b){b.classList.remove('correct','incorrect')});btn.classList.add(correct?'correct':'incorrect');var fb=document.getElementById('fb-'+id);fb.textContent=correct?'✅ ¡Correcto! '+fb.getAttribute('data-ok'):'❌ No es la mejor opción. Vuelve a leer el apartado e inténtalo de nuevo.';}
</script>"""

def page(n, icon, title, subtitle, body):
    prev = "index.html" if n == 1 else f"modulo{n-1}.html"
    nxt = "examen_final.html" if n == N else f"modulo{n+1}.html"
    nxt_lbl = "Ir al examen final 🏁" if n == N else "Siguiente módulo ➡️"
    pct = round(n * 100 / (N + 1))
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
    <p>{subtitle}</p>
  </div>
  <div class="progress-container">
    <div class="progress-bar"><div class="progress-fill" style="width:{pct}%"></div></div>
    <div class="progress-text">Ciberseguridad Avanzada · Módulo {n} de {N}</div>
  </div>
  <div class="content-area">
    <section class="module">
{body}
      <div class="navigation">
        <button class="nav-btn" onclick="scormGo('{prev}')">⬅️ Anterior</button>
        <button class="nav-btn" onclick="scormGo('{nxt}')">{nxt_lbl}</button>
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

# ---------------- Módulo 1
M.append(("🤖", "Ciberamenazas emergentes e inteligencia artificial",
  "La IA también la usan los delincuentes: aprende a reconocer sus trucos.", f"""
      <h2>¿Qué ha cambiado?</h2>
      <p>La inteligencia artificial generativa permite crear textos, voces, imágenes y vídeos casi perfectos en segundos. Eso es útil para estudiar o crear, pero también facilita estafas más creíbles y personalizadas.</p>
      <h3>1. Deepfakes y suplantación multimedia</h3>
      {kp(["<b>Clonación de voz (vishing con IA):</b> con unos segundos de audio de un vídeo o nota de voz pueden imitar a un familiar y pedir dinero «urgente».",
           "<b>Vídeo-suplantación:</b> vídeos falsos de famosos o conocidos que promocionan inversiones, sorteos o noticias falsas.",
           "<b>Imágenes manipuladas:</b> montajes íntimos o humillantes creados con IA para chantajear o acosar (es delito y debe denunciarse)."], "🎭")}
      <h3>2. Phishing generado por IA</h3>
      <p>Los modelos de lenguaje redactan correos y mensajes sin faltas de ortografía, en tu idioma y con datos tuyos sacados de redes sociales. <b>Ya no basta con buscar errores</b>: hay que fijarse en el contexto, la urgencia y el canal.</p>
      <div class="alert-box"><b>Señales de alerta:</b> urgencia («ahora o nunca»), petición de dinero, códigos o contraseñas, cambio de canal («escríbeme por otra app») y mensajes que apelan al miedo o a la emoción.</div>
      <h3>3. Protocolo de verificación de identidad</h3>
      {flow(["⏸️ Para y respira", "📵 Cuelga o no respondas", "📞 Contacta por otro canal", "🔑 Usa la palabra clave familiar", "✅ Decide"])}
      <div class="box tip"><b>Truco útil:</b> acuerda con tu familia una <b>palabra clave</b> que solo conozcáis vosotros para emergencias. Un deepfake no la sabrá.</div>
      {quiz("m1a", "Recibes un audio de tu hermano pidiendo 200 € por Bizum porque «ha perdido la cartera». ¿Qué haces?",
            ["Envío el dinero: es su voz.", "Le llamo a su número de siempre o le pregunto la palabra clave antes de hacer nada.", "Le pido que me mande otro audio."], 1,
            "Verificar por un canal distinto es la defensa más eficaz contra la clonación de voz.")}
      {quiz("m1b", "¿Por qué ya no es fiable buscar faltas de ortografía para detectar phishing?",
            ["Porque la IA redacta mensajes correctos y personalizados.", "Porque los bancos también cometen faltas.", "Porque el phishing ha desaparecido."], 0,
            "Hay que analizar el contexto, la urgencia y el remitente, no solo la forma.")}
      {activity("Actividad: diseña tu protocolo", "Escribe en tres pasos qué harías si un supuesto familiar te pide dinero por mensaje.", "1. ... 2. ... 3. ...")}
      <div class="summary-box"><b>Resumen:</b> la IA hace las estafas más creíbles, pero el antídoto es sencillo: pausa, verifica por otro canal y nunca actúes bajo presión.</div>
"""))

# ---------------- Módulo 2
M.append(("🕵️", "Doxxing, ingeniería social avanzada y privacidad",
  "Tu información pública puede usarse para encontrarte. Reduce tu huella.", f"""
      <h2>¿Qué es el doxxing?</h2>
      <p>El <b>doxxing</b> consiste en recopilar y publicar sin permiso información privada de una persona (dirección, centro educativo, teléfono, familiares) para intimidarla, acosarla o humillarla.</p>
      <h3>1. Cómo se recopila la información (OSINT)</h3>
      <p>Los atacantes usan <b>fuentes abiertas</b> (OSINT): redes sociales, fotos, comentarios, listas de clase, perfiles de juegos… Cada dato parece inofensivo, pero juntos forman un puzle.</p>
      {cards([("📸","Fotos","Uniformes, fachadas, matrículas, metadatos GPS."),("🎮","Alias","El mismo nombre en juegos y redes une identidades."),("🏫","Etiquetas","Ubicaciones, clubes y amigos etiquetados."),("🗓️","Rutinas","Publicar en directo dónde estás y a qué hora.")])}
      <h3>2. Ingeniería social avanzada</h3>
      {kp(["<b>Pretexting:</b> el atacante se inventa un papel creíble (técnico, profesor, soporte del juego) para pedirte datos.",
           "<b>Baiting:</b> te ofrece algo atractivo (skins gratis, apuntes, entradas) a cambio de iniciar sesión o descargar algo.",
           "<b>Pharming social:</b> perfiles falsos que ganan tu confianza durante semanas antes de pedir algo."], "🎣")}
      <h3>3. Limpieza de huella digital</h3>
      {kp(["Elimina los <b>metadatos EXIF</b> (ubicación GPS) de tus fotos antes de publicarlas o desactiva la ubicación de la cámara.",
           "Usa <b>alias distintos</b> en juegos, foros y redes personales.",
           "Busca tu nombre completo en buscadores y revisa qué aparece.",
           "Pon tus perfiles en privado y revisa quién te sigue."], "🧹")}
      <h3>4. Plan de acción si te ocurre</h3>
      {flow(["📷 Captura pruebas", "🔒 Cambia contraseñas y activa 2FA", "🚩 Denuncia en la plataforma", "👨‍👩‍👧 Avisa a un adulto", "👮 Denuncia policial"])}
      {quiz("m2a", "¿Qué medida reduce más el riesgo de que localicen tu casa a partir de una foto?",
            ["Ponerle un filtro de color.", "Eliminar los metadatos de ubicación y no mostrar fachadas o portales.", "Subirla en mayor resolución."], 1,
            "Los metadatos GPS y los detalles del entorno pueden revelar dónde vives.")}
      {quiz("m2b", "Alguien que dice ser «soporte del juego» te pide tu código de verificación para «proteger tu cuenta». Es un ejemplo de…",
            ["Pretexting (ingeniería social).", "Una actualización normal.", "Cifrado de extremo a extremo."], 0,
            "Ningún soporte legítimo te pide códigos de verificación.")}
      {activity("Actividad: auditoría OSINT de ti mismo", "Busca tu nombre o alias en un buscador. ¿Qué información encontrarías que preferirías que no fuera pública?", "Anota qué has encontrado y qué vas a cambiar.")}
      <div class="summary-box"><b>Resumen:</b> cuanta menos información conectable publiques, más difícil será encontrarte. Ante un doxxing: pruebas, contención, denuncia y apoyo.</div>
"""))

# ---------------- Módulo 3
M.append(("📱", "Vulnerabilidades y amenazas en dispositivos móviles",
  "Tu móvil guarda toda tu vida: conoce cómo lo atacan.", f"""
      <h2>El móvil, objetivo principal</h2>
      <p>En un smartphone están tus fotos, chats, contraseñas, banca y códigos de verificación. Por eso es el objetivo favorito del malware actual.</p>
      <h3>1. Vectores de ataque más frecuentes</h3>
      {kp(["<b>Sideloading:</b> instalar APK desde webs, Telegram o enlaces fuera de las tiendas oficiales. Es la vía principal de troyanos bancarios y apps «modificadas».",
           "<b>Abuso de los servicios de accesibilidad (Android):</b> una app maliciosa que obtiene este permiso puede leer la pantalla, capturar contraseñas y pulsar botones por ti.",
           "<b>Exploits zero-click:</b> fallos que permiten infectar un móvil sin que el usuario toque nada (por eso es vital actualizar).",
           "<b>Smishing:</b> SMS falsos de paquetería o bancos con enlaces a webs o descargas maliciosas.",
           "<b>Redes y cargadores públicos:</b> Wi‑Fi abiertas falsas y puertos USB manipulados (<i>juice jacking</i>)."], "⚠️")}
      <h3>2. Root y jailbreak</h3>
      <p>Modificar el sistema para obtener permisos de administrador <b>rompe el aislamiento (sandbox)</b> entre aplicaciones. Una app maliciosa podría entonces controlar todo el dispositivo. Además, muchas apps bancarias dejan de funcionar y se pierden actualizaciones de seguridad.</p>
      <h3>3. Indicadores de compromiso (IoC) en el móvil</h3>
      {cards([("🔋","Batería","Se gasta mucho más rápido sin motivo."),("📶","Datos","Consumo de datos alto en segundo plano."),("🆕","Apps","Aparecen apps o iconos que no instalaste."),("💬","SMS","Llegan códigos de verificación que no pediste."),("♿","Accesibilidad","Apps desconocidas con este permiso activado.")])}
      <div class="alert-box"><b>Si sospechas:</b> activa el modo avión, revisa las apps con permisos de accesibilidad y administrador del dispositivo, desinstala lo desconocido, cambia contraseñas desde otro dispositivo y pide ayuda (017).</div>
      {quiz("m3a", "Una app de «linterna» descargada desde un enlace de Telegram pide activar los servicios de accesibilidad. ¿Qué significa?",
            ["Es normal: las linternas lo necesitan.", "Es una señal muy sospechosa: podría leer tu pantalla y robar credenciales.", "Mejora la batería."], 1,
            "Una linterna no necesita ese permiso; es una técnica típica de troyanos bancarios.")}
      {quiz("m3b", "¿Qué es el sideloading?",
            ["Cargar el móvil por el lateral.", "Instalar apps desde fuera de las tiendas oficiales.", "Usar dos SIM a la vez."], 1,
            "Instalar APK de origen desconocido es la principal vía de infección en Android.")}
      {activity("Actividad: revisión de permisos especiales", "En Ajustes &gt; Accesibilidad (Android) o Ajustes &gt; Privacidad (iPhone), revisa qué apps tienen permisos especiales. ¿Alguna te sorprende?", "Apps revisadas y decisión tomada...")}
      <div class="summary-box"><b>Resumen:</b> instala solo desde tiendas oficiales, actualiza siempre, no hagas root/jailbreak y vigila los permisos especiales.</div>
"""))

# ---------------- Módulo 4
M.append(("🛡️", "Bastionado de smartphones y dispositivos IoT",
  "Bastionar es reforzar: reduce la superficie de ataque de tus dispositivos.", f"""
      <h2>¿Qué es el bastionado?</h2>
      <p><b>Bastionar</b> (en inglés <i>hardening</i>) es configurar un dispositivo para que tenga solo lo necesario y lo tenga bien protegido. Menos funciones abiertas = menos puertas para un atacante.</p>
      <h3>1. Checklist de bastionado del móvil</h3>
      {kp(["<b>Actualizaciones automáticas</b> del sistema y de las apps.",
           "<b>Bloqueo de pantalla</b> con PIN de 6 cifras o más, o contraseña, más biometría.",
           "<b>Permisos mínimos:</b> cámara, micrófono y ubicación solo «mientras se usa la app».",
           "<b>Bloquea la instalación de orígenes desconocidos</b> y activa Google Play Protect.",
           "<b>Localizar y borrar a distancia</b> activado (Encontrar mi dispositivo / Buscar).",
           "<b>Copia de seguridad</b> automática y cifrada.",
           "<b>Bluetooth, NFC y Wi‑Fi</b> desactivados cuando no se usan; olvida redes abiertas guardadas."], "✅")}
      <h3>2. Autenticación robusta</h3>
      <p>Usa un <b>gestor de contraseñas</b> y activa la <b>verificación en dos pasos (2FA)</b> con una app autenticadora o, mejor aún, <b>llaves de acceso (passkeys)</b>. El 2FA por SMS es mejor que nada, pero vulnerable a la duplicación de SIM (<i>SIM swapping</i>).</p>
      <h3>3. El hogar conectado (IoT)</h3>
      <p>Cámaras IP, asistentes de voz, bombillas, consolas y televisores inteligentes suelen tener contraseñas débiles y pocas actualizaciones.</p>
      <div class="figure">
        <svg viewBox="0 0 600 170" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Router con dos redes separadas: red principal para móviles y ordenadores, y red de invitados para dispositivos IoT">
          <rect x="250" y="10" width="100" height="40" rx="10" fill="#1e3c72"/><text x="300" y="36" font-size="14" text-anchor="middle" fill="#fff" font-weight="700">Router</text>
          <line x1="300" y1="50" x2="150" y2="100" stroke="#4ecdc4" stroke-width="3"/><line x1="300" y1="50" x2="450" y2="100" stroke="#ff9800" stroke-width="3"/>
          <rect x="50" y="100" width="200" height="55" rx="10" fill="#e8f5e8" stroke="#4caf50" stroke-width="2"/><text x="150" y="124" font-size="13" text-anchor="middle" fill="#2e7d32" font-weight="700">Red principal</text><text x="150" y="143" font-size="12" text-anchor="middle" fill="#2e7d32">Móviles · Ordenadores</text>
          <rect x="350" y="100" width="200" height="55" rx="10" fill="#fff3e0" stroke="#ff9800" stroke-width="2"/><text x="450" y="124" font-size="13" text-anchor="middle" fill="#e65100" font-weight="700">Red de invitados / IoT</text><text x="450" y="143" font-size="12" text-anchor="middle" fill="#e65100">Cámaras · Bombillas · TV</text>
        </svg>
        <div class="figure-caption">Segmentar la red: si un dispositivo IoT es comprometido, no puede llegar a tus equipos principales.</div>
      </div>
      {kp(["Cambia <b>todas las contraseñas por defecto</b> (router incluido).",
           "Usa cifrado <b>WPA2 o WPA3</b> y desactiva WPS.",
           "Conecta los dispositivos IoT a una <b>red de invitados</b> separada.",
           "Actualiza el <b>firmware</b> y desactiva funciones que no uses (acceso remoto, UPnP)."], "🏠")}
      {quiz("m4a", "¿Cuál es la mejor forma de conectar una cámara IP barata en casa?",
            ["En la misma red que el portátil, con la contraseña de fábrica.", "En una red de invitados separada, con contraseña propia y firmware actualizado.", "Sin contraseña para que funcione mejor."], 1,
            "Aislar el IoT limita el daño si el dispositivo es vulnerable.")}
      {quiz("m4b", "¿Qué método de 2FA es más resistente al SIM swapping?",
            ["Código por SMS.", "App autenticadora o passkey.", "Pregunta de seguridad."], 1,
            "Las apps autenticadoras y las passkeys no dependen de tu número de teléfono.")}
      {activity("Actividad: bastiona tu móvil", "Aplica tres puntos del checklist a tu móvil y anota cuáles has cambiado.", "Puntos aplicados...")}
      <div class="summary-box"><b>Resumen:</b> actualiza, minimiza permisos, autentica con 2FA o passkeys y separa los dispositivos IoT en su propia red.</div>
"""))

# ---------------- Módulo 5
M.append(("🦠", "Malware avanzado y ransomware",
  "Conoce al enemigo: cómo funciona el malware moderno y cómo frenarlo.", f"""
      <h2>El malware de hoy</h2>
      <p>El malware actual es un negocio: se vende «como servicio» y busca sobre todo <b>datos y dinero</b>. Conocer sus tipos te ayuda a protegerte.</p>
      <h3>1. Tipologías modernas</h3>
      {cards([("🔐","Ransomware de doble extorsión","Cifra tus archivos y amenaza con publicar los datos robados."),
              ("🍪","Infostealers","Roban contraseñas guardadas, cookies de sesión y carteras de criptomonedas."),
              ("👻","Fileless","Se ejecuta en memoria usando herramientas legítimas del sistema."),
              ("🏦","Troyanos bancarios","Superponen pantallas falsas sobre apps de banca."),
              ("🤖","Botnets","Convierten tu equipo en un «zombi» para atacar a otros.")])}
      <h3>2. Robo de sesión: por qué los infostealers son tan peligrosos</h3>
      <p>Si un infostealer roba tu <b>cookie de sesión</b>, el atacante puede entrar en tu cuenta <b>sin contraseña ni 2FA</b>, porque el servicio cree que ya estás identificado. Por eso, tras una infección hay que <b>cerrar todas las sesiones</b> y cambiar contraseñas desde un equipo limpio.</p>
      <div class="alert-box"><b>Vía de entrada típica:</b> «cracks» de juegos, trucos o cheats, programas pirata, extensiones de navegador dudosas y anuncios que imitan descargas oficiales.</div>
      <h3>3. Cadena de un ataque de ransomware</h3>
      {flow(["📧 Entrada (phishing, crack)", "⚙️ Ejecución", "🔎 Movimiento por la red", "📤 Robo de datos", "🔐 Cifrado y nota de rescate"])}
      <h3>4. Defensa</h3>
      {kp(["<b>Copias de seguridad 3-2-1:</b> 3 copias, en 2 soportes distintos, 1 fuera de casa o desconectada.",
           "Antivirus/EDR activo y sistema actualizado.",
           "No descargar software pirata ni cracks.",
           "Analizar archivos sospechosos en entornos aislados (<i>sandbox</i>) o con servicios como VirusTotal, sin abrirlos en tu equipo.",
           "No pagar rescates: no garantiza recuperar los datos y financia el delito."], "🧰")}
      {quiz("m5a", "¿Por qué un infostealer puede saltarse tu 2FA?",
            ["Porque adivina el código.", "Porque roba la cookie de sesión ya autenticada.", "Porque desactiva el móvil."], 1,
            "Con la cookie de sesión el atacante «hereda» tu inicio de sesión.")}
      {quiz("m5b", "¿Qué regla de copias de seguridad protege mejor frente al ransomware?",
            ["Una sola copia en el mismo disco.", "La regla 3-2-1, con una copia desconectada.", "Guardar las fotos solo en el móvil."], 1,
            "Una copia desconectada no puede ser cifrada por el ransomware.")}
      {activity("Actividad: tu plan de copias", "Describe dónde guardas hoy tus archivos importantes y cómo aplicarías la regla 3-2-1.", "Mis copias...")}
      <div class="summary-box"><b>Resumen:</b> evita cracks y descargas dudosas, mantén copias 3-2-1 y, tras una infección, cierra sesiones y cambia contraseñas desde un equipo limpio.</div>
"""))

# ---------------- Módulo 6
M.append(("🎩", "Hacking ético y auditoría de seguridad",
  "Atacar para defender, siempre con permiso y con ética.", f"""
      <h2>¿Qué es el hacking ético?</h2>
      <p>Un <b>hacker ético</b> busca fallos de seguridad <b>con autorización expresa</b> del propietario del sistema, para que se corrijan antes de que los aproveche un delincuente. La diferencia entre un profesional y un delincuente es el <b>permiso</b>.</p>
      <h3>1. Equipos de seguridad</h3>
      {cards([("🔴","Red Team","Simula ataques reales para encontrar debilidades."),("🔵","Blue Team","Vigila, detecta y responde a incidentes."),("🟣","Purple Team","Une ambos para mejorar la defensa.")])}
      <h3>2. Fases de una auditoría</h3>
      {flow(["📝 Autorización y alcance", "🔎 Reconocimiento", "🧪 Análisis de vulnerabilidades", "📊 Informe", "🔧 Corrección y verificación"])}
      <p>Todo empieza con un <b>documento de autorización</b> que define qué se puede probar, cuándo y cómo. Sin él, cualquier prueba es ilegal.</p>
      <h3>3. Divulgación responsable</h3>
      <p>Si encuentras un fallo por casualidad (por ejemplo, en la web de tu centro), <b>no lo explotes ni lo difundas</b>. Avisa de forma privada al responsable o a INCIBE-CERT y da tiempo para corregirlo. Muchas empresas tienen programas de <b>bug bounty</b> que recompensan estos avisos.</p>
      <h3>4. Cómo aprender de forma legal</h3>
      {kp(["Retos <b>CTF</b> (Capture The Flag) y competiciones escolares como las de INCIBE.",
           "Laboratorios propios en <b>máquinas virtuales</b> en tu ordenador.",
           "Plataformas de entrenamiento diseñadas para practicar legalmente.",
           "Formación Profesional y grados en ciberseguridad."], "🎓")}
      <div class="alert-box"><b>Recuerda:</b> probar contraseñas de otros, entrar en cuentas ajenas o escanear redes sin permiso es delito, aunque sea «por curiosidad» o «para demostrar algo».</div>
      {quiz("m6a", "Descubres que la web de un club deportivo muestra datos de socios si cambias un número en la URL. ¿Qué haces?",
            ["Descargo los datos para demostrarlo.", "Lo publico en redes para que lo arreglen.", "Aviso de forma privada al responsable (o a INCIBE-CERT) sin acceder a más datos."], 2,
            "Eso es divulgación responsable: notificar sin explotar ni difundir.")}
      {quiz("m6b", "¿Qué distingue legalmente a un auditor de seguridad de un delincuente?",
            ["Las herramientas que usa.", "La autorización previa del propietario del sistema.", "La hora a la que trabaja."], 1,
            "Las herramientas pueden ser las mismas; la autorización marca la diferencia.")}
      {activity("Actividad: carta de autorización", "Imagina que tu centro te pide revisar la seguridad de su Wi‑Fi. ¿Qué debería incluir la autorización por escrito?", "Alcance, fechas, responsable, qué está prohibido...")}
      <div class="summary-box"><b>Resumen:</b> el hacking ético requiere permiso, alcance definido, informe y divulgación responsable. Practica solo en entornos propios o autorizados.</div>
"""))

# ---------------- Módulo 7
M.append(("🔑", "Cifrado, redes privadas y navegación segura",
  "Protege lo que envías y lo que guardas.", f"""
      <h2>¿Qué es el cifrado?</h2>
      <p>Cifrar es transformar la información para que solo pueda leerla quien tiene la <b>clave</b>. Lo usamos a diario sin darnos cuenta: en webs HTTPS, en WhatsApp o al desbloquear el móvil.</p>
      <h3>1. Tipos de cifrado</h3>
      {kp(["<b>En tránsito (HTTPS/TLS):</b> protege los datos mientras viajan entre tu navegador y la web. El candado indica conexión cifrada, <b>no</b> que la web sea legítima.",
           "<b>De extremo a extremo (E2EE):</b> solo emisor y receptor pueden leer el mensaje; ni siquiera el servicio puede.",
           "<b>En reposo:</b> cifra los datos guardados (móvil, portátil con BitLocker/FileVault, copias de seguridad)."], "🔐")}
      <h3>2. VPN: qué hace y qué no hace</h3>
      <div class="card-grid">
        <div class="mini-card"><div class="ico">✅</div><b>Sí hace</b><span class="small">Cifra el tráfico entre tu dispositivo y el servidor VPN; útil en Wi‑Fi públicas.</span></div>
        <div class="mini-card"><div class="ico">❌</div><b>No hace</b><span class="small">No te hace anónimo, no bloquea el phishing ni el malware y el proveedor VPN puede ver tu tráfico.</span></div>
        <div class="mini-card"><div class="ico">⚠️</div><b>Cuidado</b><span class="small">Las VPN «gratis» desconocidas pueden vender tus datos o contener malware.</span></div>
      </div>
      <h3>3. Privacidad al navegar</h3>
      {kp(["<b>DNS cifrado (DoH/DoT):</b> evita que terceros vean qué dominios visitas.",
           "<b>Modo incógnito:</b> no guarda historial en tu equipo, pero <b>no te oculta</b> de la web, tu centro o tu proveedor.",
           "<b>Bloqueadores de rastreadores</b> y revisión de cookies.",
           "Comprueba siempre el <b>dominio</b> antes de iniciar sesión, aunque haya candado."], "🌐")}
      {quiz("m7a", "Una web tiene el candado HTTPS. ¿Qué te garantiza?",
            ["Que es una web legítima y segura.", "Que la conexión está cifrada, pero podría ser una web de phishing.", "Que no tiene virus."], 1,
            "Muchas webs de phishing usan HTTPS: revisa siempre el dominio.")}
      {quiz("m7b", "¿Qué afirmación sobre las VPN es correcta?",
            ["Te hacen completamente anónimo.", "Protegen tu tráfico en redes Wi‑Fi públicas, pero no evitan el phishing.", "Eliminan los virus del móvil."], 1,
            "Una VPN cifra el canal, pero no te protege de engaños ni de malware.")}
      {activity("Actividad: revisa tu cifrado", "Comprueba si tu móvil y tu ordenador tienen el cifrado del dispositivo activado y si tus copias de seguridad están cifradas.", "Resultado de la revisión...")}
      <div class="summary-box"><b>Resumen:</b> HTTPS cifra el canal, E2EE protege la conversación y el cifrado en reposo protege tus dispositivos. Una VPN ayuda, pero no es magia.</div>
"""))

# ---------------- Módulo 8
M.append(("🚨", "Respuesta ante incidentes y forense digital básica",
  "Cuando algo sale mal: actúa con orden y conserva las pruebas.", f"""
      <h2>Un incidente no es el fin del mundo</h2>
      <p>Una cuenta robada, un móvil infectado o un chantaje pueden ocurrirle a cualquiera. Lo importante es <b>actuar rápido y con método</b>.</p>
      <h3>1. Ciclo de respuesta ante incidentes</h3>
      {flow(["🔍 Detectar", "🧯 Contener", "🧹 Erradicar", "♻️ Recuperar", "📚 Aprender"])}
      <h3>2. Contención inmediata</h3>
      {kp(["<b>Aísla</b> el equipo afectado: desconecta Wi‑Fi y cable de red para evitar que se propague.",
           "<b>No lo apagues de golpe</b> si se va a hacer un análisis forense (la memoria RAM contiene pruebas).",
           "Desde <b>otro dispositivo limpio</b>: cambia contraseñas, cierra todas las sesiones abiertas y revoca accesos de apps.",
           "Avisa a tu banco si hay datos bancarios implicados."], "🧯")}
      <h3>3. Preservar evidencias</h3>
      <p>La <b>forense digital</b> analiza los dispositivos para saber qué ocurrió. Tú puedes ayudar conservando pruebas:</p>
      {kp(["Capturas de pantalla con <b>fecha, hora y URL</b> o número del remitente.",
           "No borres mensajes, correos ni perfiles del agresor.",
           "Guarda los archivos sospechosos sin abrirlos.",
           "Anota una <b>cronología</b>: qué pasó, cuándo y qué hiciste.",
           "Para procesos judiciales se puede pedir una <b>certificación</b> de las pruebas (por ejemplo, ante notario o con servicios de evidencia digital)."], "🗂️")}
      <div class="alert-box"><b>Nunca</b> pagues un chantaje ni negocies con el atacante, y no intentes «hackear de vuelta».</div>
      <h3>4. ¿A quién acudir?</h3>
      {HELP}
      <p class="small">También puedes denunciar en la Policía Nacional, Guardia Civil o la policía autonómica, y en España solicitar la retirada de contenido sexual o violento difundido sin consentimiento mediante el <a href="https://www.aepd.es/canalprioritario" target="_blank" rel="noopener">Canal Prioritario de la AEPD</a>.</p>
      {quiz("m8a", "Tu portátil muestra una nota de rescate y está conectado al Wi‑Fi de casa. ¿Primera acción?",
            ["Reiniciarlo varias veces.", "Desconectarlo de la red para que no se propague.", "Formatearlo inmediatamente."], 1,
            "Aislar el equipo es la prioridad de la contención.")}
      {quiz("m8b", "¿Cuál es la mejor forma de conservar pruebas de acoso en una red social?",
            ["Borrar los mensajes para no verlos.", "Capturas con fecha, hora y perfil, sin borrar nada, y denunciar.", "Responder al agresor."], 1,
            "Las pruebas completas permiten a la plataforma y a la policía actuar.")}
      {activity("Actividad: tu cronología", "Imagina que te roban la cuenta de Instagram. Escribe los 5 pasos que darías, en orden.", "1. ... 2. ... 3. ... 4. ... 5. ...")}
      <div class="summary-box"><b>Resumen:</b> detecta, contén, erradica, recupera y aprende. Conserva pruebas y pide ayuda: no estás solo/a.</div>
"""))

# ---------------- Módulo 9
M.append(("⚖️", "Aspectos legales, ciberdelito y ética digital",
  "Lo que es delito en la calle también lo es en Internet.", f"""
      <h2>Internet no es un lugar sin leyes</h2>
      <p>En España, el <b>Código Penal</b> castiga los delitos cometidos a través de medios digitales. Desde los <b>14 años</b> se puede responder penalmente según la Ley Orgánica de Responsabilidad Penal del Menor.</p>
      <h3>1. Ciberdelitos frecuentes</h3>
      {cards([("🚪","Acceso ilícito","Entrar sin permiso en cuentas o sistemas ajenos."),
              ("👂","Interceptación","Espiar comunicaciones o instalar apps espía."),
              ("📤","Revelación de secretos","Difundir datos o imágenes íntimas sin consentimiento, aunque se obtuvieran con permiso."),
              ("🎭","Suplantación","Crear perfiles falsos usando la identidad de otra persona."),
              ("💸","Estafa","Engañar para obtener dinero o datos."),
              ("😡","Acoso y amenazas","Hostigar de forma insistente o amenazar.")])}
      <div class="alert-box"><b>Reenviar también cuenta:</b> compartir una imagen íntima de otra persona sin su permiso es delito, aunque tú no la hayas creado.</div>
      <h3>2. Protección de datos (RGPD y LOPDGDD)</h3>
      <p>Tus datos personales te pertenecen. En España, desde los <b>14 años</b> puedes dar tu propio consentimiento para el tratamiento de tus datos en servicios digitales. Tus derechos:</p>
      {kp(["<b>Acceso:</b> saber qué datos tienen sobre ti.",
           "<b>Rectificación:</b> corregir datos erróneos.",
           "<b>Supresión</b> («derecho al olvido»): pedir que se borren.",
           "<b>Oposición y limitación</b> del tratamiento.",
           "<b>Portabilidad:</b> llevarte tus datos a otro servicio.",
           "Si no te atienden, puedes reclamar ante la <b>AEPD</b>."], "📜")}
      <h3>3. Ética digital</h3>
      {kp(["Que algo sea técnicamente posible no significa que sea correcto.",
           "Respeta la privacidad de los demás igual que quieres que respeten la tuya.",
           "Usa tus conocimientos para proteger, no para dañar.",
           "Si ves un delito o acoso, no participes: apoya a la víctima y comunícalo."], "🤝")}
      {quiz("m9a", "Un compañero te reenvía una foto íntima de otra persona. ¿Qué es lo correcto?",
            ["Reenviarla a un grupo: no la hice yo.", "No reenviarla, borrarla, apoyar a la víctima y comunicarlo a un adulto.", "Guardarla por si acaso."], 1,
            "Difundirla es delito y causa un daño grave a la víctima.")}
      {quiz("m9b", "¿Qué derecho ejerces si pides a una red social que borre tus datos?",
            ["Derecho de supresión.", "Derecho de portabilidad.", "Derecho de rectificación."], 0,
            "El derecho de supresión permite solicitar el borrado de tus datos personales.")}
      {activity("Actividad: dilema ético", "Conoces la contraseña de la cuenta de un amigo porque te la dijo hace tiempo. Ahora estáis enfadados. ¿Qué harías y por qué?", "Mi respuesta razonada...")}
      <div class="summary-box"><b>Resumen:</b> acceder, espiar, suplantar o difundir sin permiso es delito. Conoce tus derechos sobre tus datos y actúa con ética.</div>
"""))

# ---------------- Módulo 10
M.append(("🏆", "Proyecto final: auditoría de seguridad personal y móvil",
  "Pon en práctica todo lo aprendido sobre tu propio entorno digital.", f"""
      <h2>Tu proyecto</h2>
      <p>Vas a realizar una <b>auditoría de seguridad de tu propio entorno</b> (móvil, cuentas y redes sociales). Solo trabajarás sobre <b>tus dispositivos y cuentas</b>. No incluyas contraseñas ni datos sensibles en la entrega.</p>
      <h3>Fase 1 · Inventario</h3>
      {kp(["Lista tus dispositivos (móvil, ordenador, consola, tablet, IoT).",
           "Lista tus cuentas importantes (correo, redes, juegos, banca).",
           "Identifica cuál es tu <b>cuenta de correo principal</b>: es la llave de todas las demás."], "📋")}
      <h3>Fase 2 · Revisión técnica</h3>
      <div class="activity">
        <h3>✔️ Checklist interactivo</h3>
        <div id="checklist">
          <label><input type="checkbox" class="chk" style="width:auto"> Sistema y apps actualizados</label><br>
          <label><input type="checkbox" class="chk" style="width:auto"> Bloqueo de pantalla robusto</label><br>
          <label><input type="checkbox" class="chk" style="width:auto"> Permisos de apps revisados (accesibilidad, ubicación, micrófono, cámara)</label><br>
          <label><input type="checkbox" class="chk" style="width:auto"> Apps de origen desconocido eliminadas</label><br>
          <label><input type="checkbox" class="chk" style="width:auto"> 2FA con app autenticadora o passkey en el correo principal</label><br>
          <label><input type="checkbox" class="chk" style="width:auto"> Gestor de contraseñas y contraseñas únicas</label><br>
          <label><input type="checkbox" class="chk" style="width:auto"> Sesiones abiertas revisadas y cerradas</label><br>
          <label><input type="checkbox" class="chk" style="width:auto"> Perfiles sociales en privado y metadatos de fotos desactivados</label><br>
          <label><input type="checkbox" class="chk" style="width:auto"> Copia de seguridad 3-2-1 configurada</label><br>
          <label><input type="checkbox" class="chk" style="width:auto"> Router con contraseña propia y red de invitados para IoT</label>
        </div>
        <button class="btn" onclick="puntuar()">Calcular mi nivel</button>
        <p class="feedback" id="nivel"></p>
      </div>
      <h3>Fase 3 · Comprobación de filtraciones</h3>
      <p>Comprueba si tu correo aparece en filtraciones conocidas con servicios como <a href="https://haveibeenpwned.com" target="_blank" rel="noopener">Have I Been Pwned</a>. Si aparece, cambia la contraseña de esa cuenta y de cualquier otra donde la repitieras.</p>
      <h3>Fase 4 · Informe</h3>
      {flow(["🔎 Hallazgos", "⚠️ Riesgo (alto/medio/bajo)", "🔧 Medida aplicada", "📅 Próxima revisión"])}
      {activity("Entrega: informe de auditoría", "Redacta un breve informe con al menos 5 hallazgos, su nivel de riesgo y la medida que has aplicado.", "Hallazgo 1: ... Riesgo: ... Medida: ...")}
      <div class="box tip"><b>Consejo final:</b> la seguridad es un hábito. Programa una revisión de este checklist cada 3 meses.</div>
      <div class="summary-box"><b>¡Enhorabuena!</b> Has completado los 10 módulos. Ahora puedes hacer el examen final.</div>
      <script>
      function puntuar(){{var c=document.querySelectorAll('.chk:checked').length;var t=document.querySelectorAll('.chk').length;var m=c>=9?'🟢 Nivel experto: '+c+'/'+t+'. ¡Tu entorno está muy bien protegido!':c>=6?'🟡 Nivel intermedio: '+c+'/'+t+'. Vas por buen camino; completa los puntos pendientes.':'🔴 Nivel inicial: '+c+'/'+t+'. Prioriza actualizaciones, 2FA y permisos.';document.getElementById('nivel').textContent=m;}}
      </script>
"""))

assert len(M) == N
for i, (icon, title, sub, body) in enumerate(M, 1):
    with open(os.path.join(OUT, f"modulo{i}.html"), "w", encoding="utf-8") as f:
        f.write(page(i, icon, title, sub, body))
print("módulos generados:", len(M))
