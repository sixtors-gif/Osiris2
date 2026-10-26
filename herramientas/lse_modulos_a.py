"""Módulos 1 a 5 del curso de lengua de signos española (LSE)."""
from ia_helpers import actividad, caja, cuidado, errores, fig, hosteleria, kp, lista, palabras, pasos, practica, quiz, tabla

MODULOS = []

# 1 --------------------------------------------------------------------------------------------------
MODULOS.append(("🤟", "Personas sordas y comunidad sorda", "Quiénes son, cómo hablar de ellas con respeto y qué mitos conviene dejar atrás.",
    palabras("Una persona sorda es alguien que <b>no oye o oye poco</b>. No es una persona «enferma» ni «menos inteligente»: es una persona que <b>se comunica de otra manera</b>. Muchas personas sordas forman una <b>comunidad con su propia lengua y su propia cultura</b>.")
    + """
      <h2>Conocer a la comunidad sorda</h2>
      <h3>1. Sordera y pérdida auditiva: no todas son iguales</h3>
      <p>La audición se puede perder en distinto grado y a distintas edades. Eso cambia mucho cómo se comunica cada persona.</p>"""
    + tabla(["Situación", "Qué significa", "Cómo suele comunicarse"], [
        ["<b>Sordera de nacimiento o infancia temprana</b>", "No se oyó nunca o casi nunca", "A menudo con lengua de signos; algunas personas también con lengua oral"],
        ["<b>Sordera sobrevenida</b>", "Se pierde la audición de mayor", "Suelen mantener la lengua oral; algunas aprenden signos"],
        ["<b>Hipoacusia</b>", "Se oye, pero menos (leve, media, severa)", "Lengua oral con audífonos, subtítulos…"],
        ["<b>Sordoceguera</b>", "Pérdida de vista y oído", "Lengua de signos apoyada, escritura en la mano, sistema Braille… según la persona"],
        ["<b>Con implante coclear o audífonos</b>", "Ayudas técnicas para oír mejor", "Cada persona decide cómo y cuándo las usa"]])
    + """<h3>2. Palabras que sí y palabras que no</h3>"""
    + tabla(["Mejor decir", "Mejor evitar", "Por qué"], [
        ["Persona sorda", "Sordomudo / «mudito»", "Las personas sordas no son mudas: tienen aparato fonador. Muchas no hablan oralmente por elección o por falta de acceso al sonido, no por incapacidad"],
        ["Persona con discapacidad auditiva", "«Minusválido», «tarado»", "Son términos ofensivos"],
        ["Persona usuaria de la lengua de signos", "«Habla por gestos»", "La lengua de signos es una lengua, no «gestos»"],
        ["Persona oyente", "«Normal»", "Ser sorda o ser oyente no es ser «normal» o «anormal»"]])
    + caja("Un detalle importante:", "en la comunidad, <b>sordo</b> suele usarse con total normalidad. Quien prefiere «persona con discapacidad auditiva» o «sordo/a» lo decide cada persona: <b>si dudas, pregunta con respeto</b> cómo prefiere que se hable de ella.")
    + """<h3>3. Cultura sorda</h3>
      <p>Muchas personas sordas que usan lengua de signos forman una <b>comunidad lingüística y cultural</b>: comparten una lengua, una historia, asociaciones, humor, teatro, poesía en signos y formas propias de relacionarse (por ejemplo, <b>mirarse a los ojos</b> mientras se conversa o dar golpecitos en el hombro para llamar la atención). A esa identidad se la llama <b>cultura sorda</b>, y con frecuencia se escribe <b>Sorda</b> con mayúscula al referirse a la comunidad.</p>
      <h3>4. Mitos que debes olvidar</h3>"""
    + errores([
        ["«Las personas sordas leen perfectamente los labios»", "Parece lógico", "La lectura labial es muy incompleta: muchos sonidos se ven igual (p, b, m) y solo se percibe una parte de lo que se dice"],
        ["«Basta con hablar más alto»", "Es lo instintivo", "Gritar deforma los labios y no ayuda; hay que hablar de frente, con claridad y a ritmo normal, o usar otro medio"],
        ["«La lengua de signos es internacional»", "Se parece a un gesto universal", "Cada país y región tiene su lengua de signos: LSE en España, LSC en Cataluña, ASL en EE. UU., BSL en Reino Unido…"],
        ["«Aprender signos impide que hablen»", "Se creyó durante mucho tiempo", "La investigación actual indica que la lengua de signos ayuda al desarrollo del lenguaje y no impide aprender la oral"],
        ["«Es una forma de mímica»", "Se ven expresiones y gestos", "Es una lengua con gramática propia (módulos 3 y 7)"]])
    + hosteleria("si un cliente sordo llega a tu local, <b>no le grites ni te pongas nervioso/a</b>. Mírale a la cara, sonríe, haz gestos naturales, ofrécele la carta y usa papel y bolígrafo o el móvil si hace falta. En el módulo 9 verás un protocolo completo.")
    + quiz("l1a", "¿Cuál es la forma más adecuada de referirse a alguien que no oye?", ["Persona sorda", "Sordomudo", "Mudito"], 0, "«Sordomudo» es un término desfasado: las personas sordas no son mudas.")
    + quiz("l1b", "¿Es universal la lengua de signos?", ["No: cada país o región tiene la suya", "Sí, es igual en todo el mundo", "Solo en Europa"], 0, "Hay muchas lenguas de signos distintas, como hay muchas lenguas orales.")
    + quiz("l1c", "¿Qué conviene hacer al hablar con una persona sorda que lee los labios?", ["Hablar de frente, con claridad y a ritmo normal", "Gritar", "Hablar de espaldas"], 0, "Gritar deforma los labios; hay que dar la cara y vocalizar con naturalidad.")
    + actividad("Tu punto de partida", "Escribe qué ideas tenías antes sobre las personas sordas y cuáles has cambiado después de este módulo.", "Antes pensaba… Ahora sé que…")
    + '<div class="summary-box"><b>Resumen:</b> hay muchos tipos de sordera; se dice «persona sorda», no «sordomudo»; existe una cultura sorda con su propia lengua; la lectura labial es limitada y gritar no ayuda; la lengua de signos no es universal.</div>'))

# 2 --------------------------------------------------------------------------------------------------
MODULOS.append(("📜", "Historia y derechos de la lengua de signos", "De los primeros maestros a la ley de 2007, y por qué los signos fueron prohibidos durante décadas.",
    palabras("La lengua de signos tiene una historia larga, con avances y <b>prohibiciones</b>. Conocerla ayuda a entender por qué la comunidad sorda defiende tanto <b>su derecho a signar</b>.")
    + """
      <h2>Una lengua con historia</h2>"""
    + fig("linea_historia.svg", "Línea de tiempo de la historia de la lengua de signos en España y Europa", "Hitos: de los primeros maestros del siglo XVI a la Ley 27/2007.")
    + """<h3>1. Los primeros maestros</h3>
      <p>Aunque las personas sordas se comunicaban por signos desde siempre, la educación organizada llegó más tarde. En España destaca <b>Pedro Ponce de León</b>, monje benedictino del siglo XVI, que enseñó a hablar y a leer a hijos sordos de familias nobles. En 1620, <b>Juan Pablo Bonet</b> publicó un tratado sobre la enseñanza de las personas sordas. En Francia, el abad <b>Charles-Michel de l'Épée</b> fundó hacia 1760 la primera escuela pública para sordos y usó los signos de la comunidad como lengua de enseñanza.</p>
      <h3>2. El Congreso de Milán (1880): una decisión muy dañina</h3>
      <p>En 1880, un congreso de educadores de sordos (con pocas personas sordas presentes) decidió que la enseñanza debía hacerse <b>solo por vía oral</b> y desaconsejó los signos. Durante muchas décadas, en muchos colegios se <b>prohibió signar</b>, a veces atando las manos a los niños. Esta política se llama <b>oralismo</b>. Muchas personas sordas no tuvieron acceso a una lengua completa en la infancia, y el nivel educativo de la comunidad sufrió durante generaciones.</p>
      <h3>3. La recuperación de la lengua</h3>
      <p>Desde mediados del siglo XX, la investigación lingüística demostró que las lenguas de signos son <b>lenguas naturales completas</b>, con gramática propia. Las asociaciones de personas sordas, como la <b>CNSE</b> (Confederación Estatal de Personas Sordas, fundada en 1936 y con ese nombre desde 2013), lucharon por su reconocimiento.</p>
      <h3>4. Derechos hoy</h3>"""
    + tabla(["Norma", "Qué dice, en resumen"], [
        ["<b>Convención de la ONU sobre los derechos de las personas con discapacidad (2006)</b>", "Reconoce las lenguas de signos como lenguas y el derecho a usarlas y a recibir educación en ellas"],
        ["<b>Ley 27/2007, de 23 de octubre</b> (España)", "Reconoce las lenguas de signos españolas (LSE y LSC) y regula los medios de apoyo a la comunicación oral de personas sordas, con discapacidad auditiva y sordociegas"],
        ["<b>Día Internacional de las Lenguas de Signos</b>", "El 23 de septiembre, declarado por la ONU"]])
    + caja("Para entender la lucha:", "reconocer una lengua no es un favor: es garantizar que niñas, niños y adultos sordos puedan <b>aprender, trabajar, informarse y participar</b> en su propia lengua.")
    + hosteleria("hoy es posible ofrecer en un negocio una atención accesible: carta visual, subtítulos en las televisiones, personal con unos signos básicos, comunicación por escrito o móvil. Es una cuestión de derechos y también de clientela: muchas personas sordas recomiendan los locales donde se sienten bien atendidas.")
    + errores([
        ["Pensar que los signos «son un invento reciente»", "Se ven en las redes y en la televisión", "Las comunidades sordas signan desde hace siglos; lo reciente es su reconocimiento"],
        ["Creer que el oralismo «ayudó a integrarse»", "Se presentó así", "Dejó a muchas personas sin una lengua completa en la infancia"]])
    + quiz("l2a", "¿Qué ley reconoce en España las lenguas de signos?", ["La Ley 27/2007", "La Constitución de 1812", "El Estatuto de los Trabajadores"], 0, "La Ley 27/2007 reconoce la LSE y la LSC.")
    + quiz("l2b", "¿Qué decidió el Congreso de Milán (1880)?", ["Priorizar la enseñanza oral y desaconsejar los signos", "Crear una lengua de signos universal", "Abrir escuelas de signos"], 0, "Fue una decisión que perjudicó a la comunidad sorda durante décadas.")
    + quiz("l2c", "¿Cuándo se celebra el Día Internacional de las Lenguas de Signos?", ["El 23 de septiembre", "El 1 de enero", "El 8 de marzo"], 0, "Lo declaró la ONU.")
    + '<div class="summary-box"><b>Resumen:</b> la educación de personas sordas empezó en el siglo XVI; en 1880 se impuso el oralismo; hoy las lenguas de signos están reconocidas por la ONU (2006) y en España por la Ley 27/2007.</div>'))

# 3 --------------------------------------------------------------------------------------------------
MODULOS.append(("🧩", "La LSE: una lengua completa", "Qué es la lengua de signos española, en qué se parece y se diferencia de la lengua oral y cuáles son sus cinco parámetros.",
    palabras("La <b>lengua de signos española (LSE)</b> es una lengua natural, con gramática y vocabulario propios, que se produce con <b>las manos, el cuerpo y la cara</b> y se percibe con <b>los ojos</b>. No es el español «con las manos».")
    + """
      <h2>Cómo es la LSE</h2>
      <h3>1. Lengua visual, lengua gestual</h3>
      <p>Las lenguas orales usan el canal <b>oído-voz</b>; las de signos, el canal <b>vista-cuerpo</b>. Por eso se llaman <b>lenguas visogestuales</b>. Puedes decir muchas cosas a la vez (por ejemplo, la mano dice «coche» y la cara dice «¡qué rápido!»), algo que en la lengua oral se hace en secuencia.</p>"""
    + tabla(["", "Lengua oral (español)", "Lengua de signos española"], [
        ["Canal", "Voz y oído", "Manos, cuerpo y cara; vista"],
        ["Unidad básica", "Palabra", "Signo"],
        ["Orden", "Sucesivo (una palabra detrás de otra)", "Sucesivo y simultáneo (varias cosas a la vez)"],
        ["Gramática", "La del español", "Propia (no copia la del español)"],
        ["Escritura", "Español escrito", "No tiene escritura habitual (existen notaciones técnicas)"]])
    + """<h3>2. LSE, LSC y otras lenguas de signos</h3>
      <p>En España hay dos lenguas de signos reconocidas: la <b>LSE</b> (lengua de signos española, usada en gran parte del país) y la <b>LSC</b> (lengua de signos catalana). Dentro de la LSE hay <b>variantes regionales</b>, igual que hay acentos y palabras distintas en el español. Y en otros países hay otras lenguas distintas: <b>ASL</b> (EE. UU.), <b>BSL</b> (Reino Unido), <b>LSF</b> (Francia)… No son traducciones unas de otras.</p>
      <h3>3. Los cinco parámetros de un signo</h3>
      <p>Igual que una palabra se forma con sonidos, un signo se forma combinando <b>cinco parámetros</b>. Si cambias uno, puede cambiar el significado.</p>"""
    + fig("parametros.svg", "Los cinco parámetros de un signo: configuración, orientación, lugar, movimiento y componentes no manuales", "Los cinco parámetros que se combinan al signar.")
    + tabla(["Parámetro", "Qué es", "Ejemplo de cambio"], [
        ["<b>1. Configuración</b>", "La forma de la mano (puño, mano plana, índice…)", "Misma posición y movimiento con otra forma de mano = otro signo"],
        ["<b>2. Orientación</b>", "Hacia dónde mira la palma o los dedos", "Palma hacia arriba o hacia abajo puede cambiar el sentido"],
        ["<b>3. Lugar de articulación</b>", "Dónde se hace: cara, frente, pecho, espacio neutro…", "El mismo movimiento en otra zona puede significar otra cosa"],
        ["<b>4. Movimiento</b>", "Recto, circular, repetido, con rebote…", "Repetirlo puede indicar plural o continuidad"],
        ["<b>5. Componentes no manuales</b>", "Expresión de la cara, mirada, cabeza y hombros", "Una misma frase puede ser pregunta, afirmación o negación"]])
    + fig("configuraciones.svg", "Esquemas de diez configuraciones básicas de la mano", "Algunas configuraciones muy frecuentes. Son esquemas simplificados; la forma real tiene más matices.")
    + """<h3>4. El espacio de signado</h3>
      <p>Los signos se hacen en un espacio delante del cuerpo, desde la cabeza hasta la cintura y de codo a codo. Cada zona tiene sus usos: la cara para sentidos y emociones, el pecho para el «yo», el espacio neutro para describir y conversar.</p>"""
    + fig("espacio_signado.svg", "Esquema del cuerpo con la zona de signado", "Zona de signado: de la cabeza a la cintura y de codo a codo.")
    + caja("Cuenta sorprendente:", "en la lengua de signos la <b>cara</b> forma parte de la gramática. Las cejas arriba pueden marcar una pregunta de sí/no; las cejas hacia abajo, una pregunta con «qué», «dónde», «quién». Si tienes la cara seria, ¡tu pregunta puede no entenderse!")
    + hosteleria("un camarero que sonríe y mira a los ojos ya comunica mucho: <b>la expresión y la mirada son parte del idioma</b>. Y señalar el plato en la carta, con una cara amable, ya es una conversación completa.")
    + errores([
        ["Signar mirando a tus manos", "Es lo natural al aprender", "El interlocutor mira tu cara; tú también debes mirar a la suya"],
        ["Mover solo las manos con cara seria", "Concentración", "Sin expresión la frase pierde parte de su significado"],
        ["Pensar «una palabra = un signo»", "Parece una traducción simple", "La lengua de signos tiene su gramática; se aprende por ideas, no palabra a palabra"]])
    + quiz("l3a", "¿Cuántos parámetros forman un signo?", ["Cinco", "Dos", "Diez"], 0, "Configuración, orientación, lugar, movimiento y componentes no manuales.")
    + quiz("l3b", "¿La LSE es el español hecho con las manos?", ["No: es una lengua distinta, con gramática propia", "Sí, igual que el español", "Solo en la escuela"], 0, "Es una lengua natural diferente del español.")
    + quiz("l3c", "¿Qué papel tiene la cara al signar?", ["Forma parte de la gramática (preguntas, negación, emociones)", "Ninguno", "Solo decorativo"], 0, "Los componentes no manuales son esenciales.")
    + practica("Practica los parámetros", [
        "Elige cuatro objetos o acciones sencillas (por ejemplo beber, comer, mesa, casa).",
        "Imagina cómo los harías con las manos: ¿qué forma de mano, dónde, qué movimiento?",
        "Compáralos con los signos oficiales de un diccionario de LSE (módulo 10) y apunta qué parámetros coinciden."])
    + '<div class="summary-box"><b>Resumen:</b> la LSE es una lengua visogestual con gramática propia; un signo se forma con cinco parámetros; la cara y la mirada son parte de la gramática; la LSE y la LSC son distintas y hay variantes regionales.</div>'))

# 4 --------------------------------------------------------------------------------------------------
MODULOS.append(("🔤", "Dactilología: el alfabeto manual", "Aprende a deletrear con las manos tu nombre, lugares y palabras nuevas.",
    palabras("La <b>dactilología</b> es el «alfabeto de las manos»: cada letra tiene una forma. Sirve para deletrear <b>nombres propios, lugares y palabras que no tienen signo</b>. No es la lengua de signos completa, pero es lo primero que casi todo el mundo aprende.")
    + """
      <h2>El alfabeto manual en LSE</h2>
      <h3>1. Cuándo se usa</h3>"""
    + lista(["<b>Nombres de personas</b> (aunque cada persona sorda suele tener además su «seña-nombre»).", "<b>Lugares, marcas y palabras técnicas</b> sin signo conocido.", "Cuando <b>no sabes un signo</b> y necesitas aclararlo."], "✋")
    + """<h3>2. Cómo se hace</h3>"""
    + pasos(["Usa normalmente <b>una mano</b> (la dominante), delante del hombro, a la altura de la barbilla o del pecho.", "Muestra la letra <b>de forma clara y estable</b>, de modo que quien te mira la vea de frente.", "Deletrea <b>de forma continua</b>, sin parar entre letras, y con un pequeño ritmo; las letras repetidas se marcan con un pequeño rebote de la mano; «ch», «ll» y «rr» se suelen deletrear letra a letra.", "Cuando termines, <b>relaja la mano</b> y mira a tu interlocutor para ver si te entendió."])
    + cuidado("las descripciones de esta lección son <b>orientativas</b>. El alfabeto manual solo se aprende bien <b>viéndolo en vídeo o con una persona</b>, y puede haber pequeñas diferencias de estilo. Contrasta cada letra con un recurso oficial (módulo 10).")
    + """<h3>3. Descripción de las letras</h3>
      <div class="activity dl">
        <p>Escribe una palabra (por ejemplo, tu nombre) y aparecerán las letras con su descripción. Pulsa «Reproducir» para verlas una a una.</p>
        <input type="text" id="dl-texto" value="HOLA" oninput="dlGenerar()" maxlength="20" aria-label="Palabra a deletrear">
        <p><button class="btn" onclick="dlGenerar()">Mostrar letras</button> <button class="btn" onclick="dlReproducir()">▶ Reproducir</button>
        <label>Velocidad: <input type="range" id="dl-vel" min="500" max="3000" step="250" value="1500" oninput="dlVelTxt()"> <b id="dl-vel-t"></b></label></p>
        <div id="dl-grande" class="letra-grande"></div>
        <div id="dl-tarjetas" class="letra-grid"></div>
      </div>
      <h3>4. Juego: ¿qué letra es?</h3>
      <div class="activity"><p>Lee la descripción y elige la letra.</p><p id="jl-desc" class="jl-desc"></p><div class="lect-btns" id="jl-ops"></div><p id="jl-msg"></p><p>Aciertos: <b id="jl-pt">0 de 0</b></p></div>
      <h3>5. Consejos para memorizar</h3>"""
    + lista(["Aprende <b>5 letras al día</b> y repásalas con un amigo.", "Deletrea <b>cosas que ves</b>: carteles, etiquetas, nombres de calles.", "Deletrea tu nombre, el de tus amigos y el de tu local favorito.", "Mira tu mano en un espejo: lo que ves es lo que verá tu interlocutor.", "Ve despacio al principio; la velocidad llega sola con la práctica."], "🧠")
    + hosteleria("deletrear nombres es muy útil al tomar una reserva con un cliente sordo: pídele que lo escriba o deletréalo tú para confirmar «¿García, G-A-R-C-Í-A?». Y si un cliente deletrea el nombre de un plato, ¡ya sabes qué ha pedido!")
    + errores([
        ["Deletrear muy deprisa", "Parece más fluido", "Si no se entiende, no sirve; la claridad va primero"],
        ["Tapar la mano con el cuerpo", "Distracción", "La letra debe verse de frente"],
        ["Usar solo el alfabeto para todo", "Es lo único que se sabe", "Aprende pronto signos reales: el alfabeto es un complemento"]])
    + quiz("l4a", "¿Para qué sirve sobre todo la dactilología?", ["Para deletrear nombres y palabras sin signo", "Para sustituir toda la lengua de signos", "Para hablar rápido"], 0, "Se usa para nombres, lugares y palabras sin signo conocido.")
    + quiz("l4b", "¿Qué mano se usa normalmente para deletrear?", ["La dominante", "Las dos siempre", "Solo la izquierda"], 0, "En general se usa la mano dominante.")
    + quiz("l4c", "Al deletrear, ¿cómo debe verse la letra?", ["De frente, clara y estable", "Escondida", "Lo más rápida posible"], 0, "La claridad es lo más importante.")
    + actividad("Tu nombre en dactilología", "Escribe tu nombre y apellidos. Deletréalos varias veces y apunta las letras que te cuestan más.", "Mi nombre: … Letras difíciles: …")
    + '<div class="summary-box"><b>Resumen:</b> el alfabeto manual se usa para nombres y palabras sin signo; se hace con la mano dominante, de frente y de forma continua; las descripciones del curso son orientativas y deben contrastarse en vídeo oficial.</div>'))

# 5 --------------------------------------------------------------------------------------------------
MODULOS.append(("🤝", "Comunicarse sin barreras", "Cómo llamar la atención, cómo hablar con una persona sorda y qué ayudas técnicas existen.",
    palabras("Aunque no sepas signar, puedes <b>comunicarte con una persona sorda</b> si sigues unas pautas sencillas. Lo importante no es hablar «perfecto»: es <b>querer entenderse</b>.")
    + """
      <h2>Buenas prácticas de comunicación</h2>
      <h3>1. Cómo llamar la atención</h3>"""
    + lista(["<b>Un toque suave</b> en el hombro o el brazo (no en la cara ni por detrás de golpe).", "<b>Agitar la mano</b> o hacer un gesto amplio en su campo de visión.", "<b>Dar golpecitos suaves</b> en la mesa (si se sienta delante).", "<b>Apagar y encender la luz</b> si estáis en una habitación (en entornos privados y con aviso).", "Pedir a otra persona que le avise."], "👋")
    + """<h3>2. Hablar con una persona sorda (si lee labios o usa audífonos)</h3>"""
    + pasos(["Colócate <b>de frente</b>, con buena luz sobre tu cara (no a contraluz).", "<b>Mírale a los ojos</b> y espera a que te mire.", "Habla con <b>claridad y ritmo normal</b>, sin gritar ni exagerar.", "Usa <b>frases cortas y sencillas</b>, con una idea cada vez.", "Si no te entiende, <b>reformula</b> con otras palabras; no repitas lo mismo cada vez más fuerte.", "Si hace falta, <b>escribe</b> o usa el móvil. No es una molestia, es una solución."])
    + """<h3>3. Con intérprete</h3>
      <p>Un <b>intérprete de lengua de signos</b> traduce entre una lengua oral y una de signos. Cuando hablas con una persona sorda mediante intérprete, <b>mírala a ella</b>, no al intérprete, y habla con naturalidad en primera persona («quiero…», no «dile que…»). El intérprete mantiene el <b>secreto profesional</b> y solo traduce.</p>
      <h3>4. Ayudas técnicas y servicios</h3>"""
    + tabla(["Recurso", "Para qué sirve"], [
        ["<b>Subtitulado</b>", "Texto en vídeos, televisión y eventos"],
        ["<b>Bucle de inducción magnética</b>", "Envía el sonido directo a audífonos e implantes sin ruido de fondo (mostradores, salones de actos…)"],
        ["<b>Servicio de videointerpretación</b> (como <b>SVisual</b>, de la Fundación CNSE)", "Un intérprete atiende por videollamada; muy útil en gestiones y atención al público"],
        ["<b>Mensajería y notas del móvil</b>", "Escribir y enseñar la pantalla"],
        ["<b>Alarmas luminosas y vibradores</b>", "Avisos de timbre, de alarma y de emergencias visuales"],
        ["<b>Subtitulado automático</b> en el móvil", "Útil para conversaciones breves, pero con errores: revisa lo importante"]])
    + hosteleria("<b>consejo de oro para servicio:</b> pon tu móvil o una libreta a mano; un cartel con «¿Necesitas ayuda? Escribe aquí» y una pantalla con pedidos; luces o vibradores para avisar de que el pedido está listo. Esa pequeña inversión tiene mucho valor para el cliente.")
    + errores([
        ["Hablar de espaldas o tapándote la boca", "Descuido", "La persona no puede leer tus labios ni tu cara"],
        ["Hablar con el acompañante en vez de con la persona sorda", "Parece más fácil", "Es una falta de respeto: dirígete siempre a ella"],
        ["Decir «Da igual, no es importante»", "Para no insistir", "Parece que no te importa; vuelve a intentarlo de otra manera"],
        ["Exagerar la boca", "Parece que ayuda", "Deforma las palabras y es más difícil de leer"]])
    + quiz("l5a", "¿Cómo se debe llamar la atención de una persona sorda?", ["Un toque suave en el hombro o un gesto amplio", "Un grito", "Un golpe fuerte"], 0, "Se usan métodos visuales o táctiles suaves.")
    + quiz("l5b", "Con un intérprete delante, ¿a quién se mira?", ["A la persona sorda", "Al intérprete", "A la pared"], 0, "La conversación es con la persona sorda.")
    + quiz("l5c", "¿Qué hacer si no te entiende?", ["Reformular con otras palabras o escribir", "Gritar más fuerte", "Marcharte"], 0, "Reformular o escribir suele ayudar.")
    + practica("Ensaya con un compañero", [
        "Uno hace de persona sorda (sin usar la voz) y otro de camarero.",
        "El camarero debe llamar la atención, saludar y entender un pedido solo con gestos, mirada, mímica y escritura.",
        "Cambiad los papeles y comentad qué ayudó y qué no."])
    + '<div class="summary-box"><b>Resumen:</b> llama la atención con toque suave o gesto; habla de frente, claro y sin gritar; con intérprete mira a la persona sorda; usa ayudas técnicas y escribe cuando haga falta.</div>'))
