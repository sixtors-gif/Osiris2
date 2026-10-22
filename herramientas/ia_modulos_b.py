"""Módulos 7 a 12 del curso de IA para jóvenes: prompts, IA en hostelería (3), ética y privacidad, futuro."""
from ia_helpers import (actividad, caja, cuidado, errores, fig, hosteleria, kp, lista, palabras, pasos, practica, prompt,
                        quiz, respuesta, tabla)

MODULOS = []

# 7 --------------------------------------------------------------------------------------------------
MODULOS.append(("✍️", "Hablar con Claude: el arte de pedir bien (prompts)", "Cómo escribir instrucciones claras para obtener respuestas útiles.",
    palabras("Un <b>prompt</b> es lo que le escribes a la IA. La calidad de la respuesta depende mucho de la calidad de lo que pides: <b>un buen prompt es como un buen encargo a un compañero nuevo</b>: claro, con contexto y con el resultado que esperas.")
    + """
      <h2>Escribir buenos prompts</h2>
      <h3>1. Los seis ingredientes de un buen prompt</h3>"""
    + tabla(["Ingrediente", "Qué es", "Ejemplo en hostelería"], [
        ["<b>Rol</b>", "Quién quieres que sea", "«Actúa como jefe de sala de un restaurante»"],
        ["<b>Contexto</b>", "La situación y los datos", "«Somos un bar de tapas de 40 plazas en Sevilla…»"],
        ["<b>Tarea</b>", "Lo que necesitas", "«Redacta una respuesta a esta reseña»"],
        ["<b>Formato</b>", "Cómo quieres la respuesta", "«Una tabla», «5 líneas», «lista numerada»"],
        ["<b>Tono</b>", "Cómo debe sonar", "«Cercano y profesional»"],
        ["<b>Límites</b>", "Lo que debe respetar", "«Sin prometer descuentos; máximo 80 palabras»"]])
    + """<h3>2. Del prompt flojo al prompt bueno</h3>"""
    + prompt("Hazme un menú.", "Prompt flojo")
    + prompt("Actúa como jefe de cocina de un restaurante de menú del día en una ciudad de interior. Es octubre. Tenemos 12 mesas y un presupuesto de 3,50 € de materia prima por plato. Propón un menú del día con 2 primeros, 2 segundos y 2 postres, usando productos de temporada. Preséntalo en una tabla con el plato y sus ingredientes principales. Marca con un asterisco los platos que podrían contener alérgenos para que yo los verifique.", "Prompt bueno")
    + caja("Fíjate:", "el segundo prompt es más largo, pero le ahorra a Claude (y a ti) adivinar. <b>Más contexto = menos respuestas genéricas.</b> Y no hace falta que sea perfecto: puedes mejorar el prompt después.")
    + """<h3>3. Construye tu propio prompt</h3>
      <p>Rellena los campos o pulsa un ejemplo. Abajo se monta el prompt listo para copiar y pegar en Claude.</p>
      <div class="activity pb">
        <p><button class="btn" onclick="pbEjemplo(0)">Reseña de hotel</button> <button class="btn" onclick="pbEjemplo(1)">Ideas de cocina</button> <button class="btn" onclick="pbEjemplo(2)">Cafetería en redes</button></p>
        <label>Rol <input type="text" id="pb-rol" oninput="pbMontar()" placeholder="Actúa como…"></label>
        <label>Contexto <textarea id="pb-contexto" oninput="pbMontar()" placeholder="Situación, datos, público…"></textarea></label>
        <label>Tarea <textarea id="pb-tarea" oninput="pbMontar()" placeholder="Qué necesitas exactamente"></textarea></label>
        <label>Formato <input type="text" id="pb-formato" oninput="pbMontar()" placeholder="Tabla, lista, 5 líneas…"></label>
        <label>Tono <input type="text" id="pb-tono" oninput="pbMontar()" placeholder="Cercano, formal, divertido…"></label>
        <label>Límites <input type="text" id="pb-limites" oninput="pbMontar()" placeholder="Lo que debe respetar o evitar"></label>
        <div class="prompt"><div class="prompt-t">💬 Tu prompt</div><pre id="pb-salida"></pre><button type="button" onclick="copiar(this)">📋 Copiar</button></div>
        <p id="pb-nota" class="small"></p>
      </div>
      <h3>4. Técnicas que funcionan</h3>"""
    + lista(["<b>Da ejemplos:</b> «Escríbelo con un estilo parecido a este texto: …».", "<b>Pide paso a paso:</b> «Explícame el razonamiento antes de la conclusión».", "<b>Pide preguntas:</b> «Antes de responder, hazme las preguntas que necesites».", "<b>Itera:</b> «Más corto», «menos formal», «añade una opción vegetariana».", "<b>Pide que se revise:</b> «Repasa tu respuesta y dime qué podría estar mal o qué debo comprobar»."], "🛠️")
    + pasos(["Escribe la primera versión de tu prompt, sin agobiarte.", "Lee la respuesta con ojo crítico: ¿qué falta o sobra?", "Contesta con una corrección concreta («hazlo más corto y sin tecnicismos»).", "Cuando salga bien, guarda ese prompt: es tu plantilla para la próxima vez."])
    + hosteleria("guarda una carpeta con tus plantillas de prompts (respuesta a reseñas, descripción de platos, mensaje de confirmación de reserva…). Con los datos del local ya puestos, cada tarea se hace en un minuto. Eso sí: <b>nunca incluyas en ellas datos personales de clientes</b>.")
    + errores([
        ["Pedir en una frase sin contexto", "Es rápido", "La respuesta será genérica; añade para quién, para qué y cómo"],
        ["Aceptar la primera respuesta", "Parece suficiente", "Conversa: pide cambios hasta que sirva"],
        ["Pensar que hay un «prompt mágico»", "Se ven trucos en redes", "Lo que funciona es ser claro, dar contexto e iterar"]])
    + quiz("i7a", "¿Qué hace mejor un prompt?", ["Dar contexto, tarea y formato", "Ser lo más corto posible", "Usar palabras raras"], 0, "Contexto, tarea y formato claros dan respuestas más útiles.")
    + quiz("i7b", "Si la primera respuesta no te sirve, ¿qué haces?", ["Pedir cambios concretos en la misma conversación", "Rendirte", "Escribir lo mismo otra vez sin cambios"], 0, "Iterar es parte normal del trabajo con IA.")
    + quiz("i7c", "¿Qué NO debe contener una plantilla de prompt guardada?", ["Datos personales de clientes", "El nombre de tu local", "El tono deseado"], 0, "Los datos personales no se reutilizan ni se pegan en la IA sin necesidad.")
    + actividad("Tu primer prompt", "Piensa en una tarea real de un bar, restaurante u hotel. Escribe el prompt con los seis ingredientes.", "Rol: … Contexto: … Tarea: … Formato: … Tono: … Límites: …")
    + '<div class="summary-box"><b>Resumen:</b> un buen prompt tiene rol, contexto, tarea, formato, tono y límites; se mejora conversando; y se guarda como plantilla sin datos personales.</div>'))

# 8 --------------------------------------------------------------------------------------------------
MODULOS.append(("🛎️", "IA en hostelería (I): atención al cliente y comunicación", "Reseñas, correos, reservas, idiomas y redes sociales.",
    palabras("En hostelería se escribe mucho: reseñas, correos, cartas, mensajes, redes. La IA es especialmente buena <b>redactando, resumiendo y traduciendo</b>. Tú pones la información y el criterio; ella, el borrador.")
    + """
      <h2>La IA en el trato con el cliente</h2>
      <h3>1. Responder reseñas</h3>
      <p>Una reseña negativa bien contestada puede ganar clientes. Claude te da un borrador; <b>tú compruebas que es verdad lo que dice y que suena a tu local</b>.</p>"""
    + prompt("Actúa como responsable de atención al cliente de un hotel de 3 estrellas en la costa. Un cliente ha puesto 2 estrellas: dice que el desayuno estaba frío y que esperó 15 minutos en recepción, pero que la habitación era muy bonita. Redacta una respuesta pública: agradece, reconoce los problemas sin excusas, no prometas compensaciones concretas y ofrece que nos contacte por correo. Cinco o seis líneas, tono cercano y profesional.")
    + respuesta("<p>«Gracias por tomarte el tiempo de contarnos tu experiencia. Nos alegra que la habitación te resultara bonita, pero lamentamos que el desayuno no estuviera a la temperatura adecuada y que tuvieras que esperar en recepción: no es el servicio que queremos ofrecer. Hemos trasladado tus comentarios al equipo para mejorarlo. Si te apetece, escríbenos a nuestro correo de atención al cliente y lo revisamos contigo. Esperamos poder recibirte de nuevo y que la próxima vez todo esté a la altura. ¡Gracias!»</p><p class='small'>Texto de ejemplo escrito para este curso; la respuesta real de Claude será distinta cada vez.</p>")
    + """<h3>2. Otras tareas de comunicación</h3>"""
    + tabla(["Tarea", "Qué le pides a Claude", "Qué compruebas tú"], [
        ["Correos a clientes", "Confirmación de reserva, grupos, cambios", "Fechas, precios y condiciones"],
        ["Idiomas", "Traducir la carta, un aviso o un mensaje al inglés, alemán, francés…", "Que los platos y alérgenos estén bien traducidos (pide ayuda a alguien que hable el idioma si es importante)"],
        ["Redes sociales", "Ideas de publicaciones, textos, calendario de la semana", "Que no prometa lo que no ofreces"],
        ["Descripciones", "Describir platos o habitaciones de forma apetecible", "Que sea verdad: ingredientes, tamaños, servicios"],
        ["Resúmenes", "Resumir 30 reseñas en puntos fuertes y débiles", "Que no se haya inventado ninguna"]])
    + hosteleria("un camarero con idiomas vale oro. Con Claude puedes preparar frases útiles para turistas («¿tiene alguna alergia?», «la cuenta, por favor») y su pronunciación, pero <b>en seguridad alimentaria nunca dependas solo de la traducción</b>: confirma con el cliente y con la carta oficial de alérgenos.")
    + """<h3>3. Un chatbot de atención en la web</h3>
      <p>Muchos negocios ponen asistentes de IA que contestan dudas frecuentes (horario, ubicación, carta). Funcionan bien si se les da <b>información fiable y limitada</b> y se indica que son un asistente automático. Para temas delicados (alergias, quejas graves, pagos) debe pasar a una persona.</p>"""
    + cuidado("la IA no debe prometer reembolsos, confirmar reservas ni asegurar que un plato «no tiene gluten» por su cuenta. Eso lo decide y lo comprueba una persona del negocio.")
    + errores([
        ["Copiar y pegar la respuesta sin leerla", "Ahorra tiempo", "Puede decir algo falso o sonar impersonal"],
        ["Todas las respuestas idénticas", "Funciona la plantilla", "Los clientes lo notan; añade un detalle personal"],
        ["Pegar el nombre y datos del cliente", "Parece dar contexto", "Basta con resumir el problema sin identificarle"]])
    + quiz("i8a", "Para responder una reseña con Claude, lo más acertado es...", ["Pedir un borrador y revisarlo antes de publicarlo", "Publicar lo que salga sin leerlo", "No usar la IA nunca"], 0, "El borrador ahorra tiempo; la revisión humana lo hace fiable.")
    + quiz("i8b", "¿Quién debe confirmar que un plato no tiene un alérgeno?", ["Una persona con la información oficial de ingredientes", "La IA a partir de su conocimiento general", "El cliente, sin preguntarle"], 0, "Los alérgenos se verifican con fuentes oficiales de cada establecimiento.")
    + quiz("i8c", "Al pedir un resumen de reseñas, ¿qué conviene hacer?", ["Comprobar que los puntos citados aparecen de verdad", "Fiarse sin mirar", "Pedirle que añada reseñas nuevas"], 0, "Los resúmenes pueden mezclar o inventar detalles.")
    + practica("Practica con tu local favorito", [
        "Elige un bar, restaurante u hotel que conozcas (o inventa uno).",
        "Escribe una reseña ficticia de 3 estrellas con un problema concreto.",
        "Redacta el prompt para responderla con los seis ingredientes.",
        "Si tienes acceso a Claude con un adulto responsable, pruébalo y apunta qué cambiarías."])
    + '<div class="summary-box"><b>Resumen:</b> en atención al cliente la IA redacta, resume y traduce; tú revisas la verdad, el tono y los temas delicados.</div>'))

# 9 --------------------------------------------------------------------------------------------------
MODULOS.append(("🍳", "IA en hostelería (II): cocina y sala", "Menús, recetas, escandallos, alérgenos y formación del equipo.",
    palabras("En cocina y sala la IA no cocina ni sirve, pero puede <b>dar ideas, hacer cuentas, preparar fichas y explicar procedimientos</b>. Eso sí: en todo lo que afecta a la salud (alérgenos, temperaturas, caducidades) manda la normativa y el criterio del profesional.")
    + """
      <h2>Cocina y sala con ayuda de la IA</h2>
      <h3>1. Ideas para el menú</h3>
      <p>Dile qué tienes, para cuántos, qué presupuesto y qué estilo. Pide varias opciones y quédate con la que se pueda hacer de verdad en tu cocina.</p>"""
    + prompt("Actúa como jefe de cocina de un restaurante mediterráneo. En la cámara tengo calabacín, tomates maduros, queso feta y pan del día anterior. Propón 3 entrantes para el menú del día, con coste bajo y poco desperdicio. Preséntalo en una tabla con nombre, ingredientes y dificultad (baja, media o alta). Indica qué alérgenos podrían estar presentes, aclarando que debo verificarlos con las etiquetas reales.")
    + """<h3>2. Aprovechar sobras y reducir el desperdicio</h3>
      <p>Pregunta cómo transformar lo que sobra (pan, verduras, caldos) en nuevos platos. Es una de las aplicaciones más prácticas para un negocio, porque cada kilo que no se tira es dinero.</p>
      <h3>3. Escandallos y cantidades</h3>
      <p>Un <b>escandallo</b> calcula el coste de un plato a partir de sus ingredientes. Claude puede explicarte el método, ayudarte a montar la tabla o a pasar una receta de 4 a 40 raciones. <b>Comprueba siempre las cuentas</b>: a los modelos de lenguaje les cuesta la aritmética larga; si es posible, pídele la fórmula de la hoja de cálculo y que sea la hoja la que calcule.</p>"""
    + prompt("Tengo una receta de salsa para 4 raciones: 200 g de tomate triturado, 40 ml de aceite, 20 g de cebolla y 5 g de sal. Quiero hacerla para 40 raciones. Dame la tabla con las cantidades nuevas y explícame cómo lo calculas para que yo pueda comprobarlo.")
    + tabla(["Uso", "Ayuda de la IA", "Comprobación humana"], [
        ["Carta y menús", "Ideas, nombres de platos, descripciones", "Que se pueda hacer, costes reales"],
        ["Fichas técnicas", "Estructura de la ficha y redacción de pasos", "Pesos, tiempos, temperaturas"],
        ["Alérgenos", "Plantilla y recordatorio de los 14 alérgenos de declaración obligatoria", "Ingredientes y etiquetas reales; normativa vigente"],
        ["Formación", "Guion para el equipo, test de preguntas, simulación de clientes difíciles", "Que coincida con vuestros protocolos"],
        ["Sala", "Frases de sugerencia, vino y maridajes como ideas, vocabulario en idiomas", "El criterio del sumiller o jefe de sala"]])
    + hosteleria("pídele a Claude que haga de <b>cliente exigente</b> para ensayar. Ejemplo: «Haz de cliente que reclama que su plato está frío. Yo soy el camarero; contesta tras cada frase mía y al final dime qué hice bien y qué mejoraría». Es un entrenamiento sin riesgo antes del servicio real.")
    + cuidado("la IA no sustituye al plan APPCC ni a la normativa de seguridad alimentaria. No le preguntes «¿puedo servir esto?» como única fuente: consulta a tu responsable y a las fuentes oficiales (Agencia Española de Seguridad Alimentaria y Nutrición, tu comunidad autónoma).")
    + errores([
        ["Fiarme de las cuentas largas", "Los números salen redondos", "Pide la fórmula y comprueba con calculadora u hoja de cálculo"],
        ["Usar la lista de alérgenos de la IA", "Parece completa", "Debe salir de las etiquetas reales de tus productos"],
        ["Copiar la receta tal cual", "Parece profesional", "Pruébala y ajusta tiempos y sazón: la IA no ha cocinado"]])
    + quiz("i9a", "¿Qué conviene hacer con los cálculos de un escandallo hechos por una IA?", ["Comprobarlos con calculadora o una hoja de cálculo", "Darlos por buenos", "Ignorarlos siempre"], 0, "La IA puede fallar en cuentas largas: se verifican.")
    + quiz("i9b", "¿De dónde debe salir la lista de alérgenos de un plato?", ["De los ingredientes y etiquetas reales", "De lo que supone la IA", "De la memoria del cocinero"], 0, "Es información de seguridad: se basa en datos reales y verificados.")
    + quiz("i9c", "¿Para qué sirve hacer que Claude actúe como cliente difícil?", ["Para ensayar cómo responder antes del servicio real", "Para evitar atender a clientes", "Para ganar propinas"], 0, "El juego de rol permite practicar sin riesgo.")
    + '<div class="summary-box"><b>Resumen:</b> en cocina y sala la IA da ideas, estructura documentos y permite ensayar; los cálculos, los alérgenos y la seguridad alimentaria los comprueba una persona con fuentes oficiales.</div>'))

# 10 -------------------------------------------------------------------------------------------------
MODULOS.append(("📊", "IA en hostelería (III): gestión, marketing y emprendimiento", "Turnos, inventario, hojas de cálculo, promociones y un plan de negocio.",
    palabras("Detrás de cada local hay organización: turnos, pedidos, números, promociones. La IA ayuda a <b>ordenar ideas, escribir fórmulas, redactar documentos y analizar datos que no sean personales</b>. Es como tener un ayudante administrativo muy rápido.")
    + """
      <h2>Gestión, marketing y emprendimiento</h2>
      <h3>1. Organización del equipo y del trabajo</h3>"""
    + lista(["Plantillas de <b>turnos semanales</b> y de limpieza por zonas.", "Listas de apertura y cierre del local.", "Guiones para reuniones de equipo y de protocolo de incidencias.", "Resúmenes de una normativa o de un convenio (siempre contrastando con el texto oficial)."], "📋")
    + """<h3>2. Hojas de cálculo con ayuda</h3>
      <p>Claude puede explicarte una fórmula, escribirla a partir de lo que quieres hacer o ayudarte a entender un error. Por ejemplo, para calcular el porcentaje de coste de materia prima de un plato o marcar en rojo los productos con poco stock.</p>"""
    + prompt("Tengo una hoja de cálculo con estas columnas: A producto, B stock actual, C stock mínimo. Quiero que la columna D muestre «PEDIR» si el stock actual es menor que el mínimo y «OK» en caso contrario, y que se pinten de rojo las filas con «PEDIR». Dame la fórmula y los pasos para el formato condicional en LibreOffice Calc y en Excel.")
    + hosteleria("pegar en la IA la plantilla de tus tablas con <b>datos inventados o sin nombres de personas</b> es una buena forma de trabajar: obtienes la fórmula sin exponer datos reales.")
    + """<h3>3. Marketing y promociones</h3>
      <p>Pídele ideas de promociones de temporada, eslóganes, un calendario de publicaciones o la descripción de un local para una guía. Después <b>filtra con tu criterio</b>: lo que sea tópico, impreciso o que prometa lo que no puedes cumplir, fuera. Y si usas imágenes generadas por IA para publicitar tu comida, avisa de que son ilustraciones: el cliente no debe esperar un plato distinto del real.</p>
      <h3>4. Si quieres emprender</h3>
      <p>Claude te puede acompañar a pensar un proyecto: público objetivo, propuesta de valor, costes aproximados, riesgos y preguntas que debes responder. No te dará el negocio hecho, pero sí te evitará bloqueos y te propondrá preguntas que no habías pensado.</p>"""
    + prompt("Quiero abrir una pequeña cafetería de especialidad en mi barrio. Hazme un guion de 10 preguntas que debo responder antes de empezar (público, ubicación, costes, permisos, competencia, horarios, equipo…). Después ayúdame a ordenar mis respuestas en un esquema de plan de negocio de una página. No inventes cifras: dime qué datos debo buscar y dónde.")
    + tabla(["Área", "Bien para la IA", "Cuidado"], [
        ["Equipo", "Cuadrantes, guiones, protocolos", "Normativa laboral: consulta fuentes oficiales"],
        ["Datos", "Fórmulas, formatos, explicar un error", "No subas datos personales ni de nóminas"],
        ["Marketing", "Ideas, textos, calendario", "No prometer lo que no hay; avisar si la imagen es generada"],
        ["Emprender", "Preguntas, esquema, riesgos", "Cifras, permisos y leyes: verificar siempre"]])
    + errores([
        ["Pedirle cifras de mercado exactas", "Las da con seguridad", "Pueden ser inventadas; busca datos oficiales (INE, informes del sector)"],
        ["Subir la hoja de nóminas o de clientes", "Es más cómodo", "Datos personales: no se comparten sin base legal"],
        ["Copiar un plan de negocio genérico", "Queda bien", "Tu local es único; adáptalo con datos reales"]])
    + quiz("i10a", "¿Qué es mejor compartir con la IA para pedir una fórmula de hoja de cálculo?", ["Una plantilla con datos inventados", "La hoja con nóminas reales", "La lista de clientes con teléfono"], 0, "Datos ficticios permiten trabajar sin exponer información personal.")
    + quiz("i10b", "Si Claude te da una cifra de mercado exacta, ¿qué haces?", ["Buscarla en una fuente oficial antes de usarla", "Usarla directamente", "Subirle la cifra un 10 %"], 0, "Las cifras exactas pueden ser inventadas.")
    + quiz("i10c", "¿Qué debes hacer si usas imágenes de comida generadas por IA en publicidad?", ["Indicar que son ilustraciones y no confundir al cliente", "Decir que son fotos reales", "Nada"], 0, "La publicidad no debe inducir a error.")
    + actividad("Tu mini plan de negocio", "Imagina un negocio de hostelería (cafetería, foodtruck, hotel rural…). Escribe cinco preguntas que le harías a Claude para empezar.", "1) … 2) … 3) … 4) … 5) …")
    + '<div class="summary-box"><b>Resumen:</b> la IA ordena, redacta y explica fórmulas; tú aportas los datos reales (sin información personal) y verificas cifras y normas.</div>'))

# 11 -------------------------------------------------------------------------------------------------
MODULOS.append(("🔒", "Usar la IA con cabeza: privacidad, ética y límites", "Datos personales, sesgos, derechos de autor, trampas y honestidad.",
    palabras("Usar IA no es solo «copiar y pegar». Hay que pensar <b>qué datos compartes, si lo que sale es cierto y justo, y si es honesto usarlo</b>. En hostelería manejas datos de clientes y alérgenos: aquí hay que ser especialmente cuidadoso.")
    + """
      <h2>Responsabilidad con la IA</h2>
      <h3>1. Privacidad y datos personales</h3>
      <p>Un <b>dato personal</b> es cualquier información que identifica a una persona: nombre, DNI, correo, teléfono, número de reserva o habitación unido a un nombre, y también <b>datos sensibles</b> como la salud o las alergias vinculadas a alguien. En Europa los protege el <b>RGPD</b>. Regla práctica: <b>si no lo contarías en voz alta en un tren, no lo pegues en una IA</b>.</p>
      <h3>Prueba el revisor de privacidad</h3>
      <p>Escribe o pega un texto inventado y comprueba qué datos personales hay. Todo ocurre en tu navegador: no se envía nada.</p>
      <div class="activity pv">
        <textarea id="priv-texto" rows="5" placeholder="Pega aquí un texto de prueba (inventado)…" oninput="privRevisar()"></textarea>
        <p><button class="btn" onclick="privEjemplo()">Ver un ejemplo</button> <button class="btn" onclick="privRevisar()">Revisar</button></p>
        <div id="priv-res"></div>
        <p><b>Versión anonimizada (solo detecta patrones evidentes; revisa tú el resto):</b></p><pre id="priv-limpio" class="pv-limpio"></pre>
      </div>
      <h3>2. Cómo anonimizar</h3>"""
    + pasos(["Quita nombres, DNI, correos, teléfonos y números de reserva o habitación.", "Sustituye por marcas genéricas: «el cliente», «la mesa 5», «un grupo de 8 personas».", "Quita detalles que identifiquen a alguien por sí solos (profesión rara, fechas exactas, matrícula).", "Pregúntate: ¿necesita la IA ese dato para ayudarme? Si no, fuera."])
    + hosteleria("un camarero apunta que un cliente es celíaco para no cometer un error. Ese dato <b>sí</b> es útil en el local, pero si lo mezclas con su nombre y lo pegas en una IA, ya estás tratando datos de salud de una persona. Sin base legal, y con una herramienta que quizá no es la que autoriza el negocio, <b>no se hace</b>. Consulta con tu responsable qué herramientas están permitidas.")
    + """<h3>3. Sesgos e injusticias</h3>
      <p>Como la IA aprende de textos humanos, puede repetir <b>prejuicios</b>: asociar profesiones con un género, tratar peor ciertos nombres o acentos, olvidar a grupos pequeños. Por eso no debe decidir sola sobre personas (contratar, despedir, dar un trato distinto a un cliente). Si algo te parece injusto, dilo y corrígelo.</p>
      <h3>4. Derechos de autor y honestidad</h3>"""
    + lista(["Usar la IA para <b>ayudarte a aprender</b> es buena idea; usarla para hacer trampas en un examen o presentar como tuyo lo que no lo es, no.", "Si en un trabajo te piden que indiques las herramientas usadas, <b>hazlo</b>.", "Los textos e imágenes generados pueden parecerse a obras existentes: revisa que no copien un logotipo o una marca.", "Las <b>falsificaciones</b> (deepfakes, voces clonadas, reseñas falsas) engañan y pueden ser ilegales."], "⚖️")
    + """<h3>5. Cómo detectar errores y bulos</h3>"""
    + pasos(["Desconfía de datos exactos, citas y enlaces: compruébalos.", "Busca la misma información en dos fuentes fiables.", "Pregúntale a Claude «¿qué debería comprobar de esto?».", "En salud, seguridad y dinero, consulta siempre a una persona experta."])
    + caja("En Europa hay normas específicas:", "el <b>Reglamento Europeo de IA</b> (2024) regula usos de riesgo y exige transparencia, por ejemplo avisar cuando se habla con una IA o se publican contenidos generados. Los detalles se van aplicando por etapas: consulta las fuentes oficiales para saber qué te afecta.")
    + errores([
        ["Pegar el listado de reservas para «ordenarlo»", "Es rápido", "Contiene datos personales; usa herramientas autorizadas o datos anonimizados"],
        ["Creer que borrar el chat borra todo", "Se ve vacío", "Lee la política de privacidad y las opciones de la herramienta"],
        ["Usar la IA para hacer los deberes sin entenderlos", "Sale perfecto", "No aprendes y puede ser considerado trampa; úsala para estudiar y practicar"]])
    + quiz("i11a", "¿Cuál de estos datos NO debes pegar en una IA?", ["Nombre y alergia de un cliente", "Una receta de salsa", "La definición de escandallo"], 0, "Nombre más datos de salud son datos personales sensibles.")
    + quiz("i11b", "¿Qué es un sesgo de la IA?", ["Un prejuicio aprendido de los datos con los que se entrenó", "Un fallo de corriente", "Una pregunta mal escrita"], 0, "Los sesgos vienen de los datos humanos usados al entrenar.")
    + quiz("i11c", "Si no estás seguro de una respuesta de la IA, ¿qué haces?", ["Comprobarla en fuentes fiables o con una persona experta", "Darla por buena", "Enviársela a un cliente"], 0, "Contrastar es parte del uso responsable.")
    + actividad("Tu código personal", "Escribe tres reglas que seguirás al usar IA (qué datos no compartirás, qué comprobarás, cuándo avisarás de que la has usado).", "1) … 2) … 3) …")
    + '<div class="summary-box"><b>Resumen:</b> no compartas datos personales, anonimiza, desconfía de lo que no puedas comprobar, no la uses para hacer trampas y recuerda que decisiones sobre personas las toman personas.</div>'))

# 12 -------------------------------------------------------------------------------------------------
MODULOS.append(("🚀", "El futuro de la IA y tu futuro profesional", "Tendencias, empleo en hostelería, agentes, robots y tu plan personal.",
    palabras("Nadie sabe con certeza cómo será la IA dentro de diez años, y quien diga lo contrario exagera. Lo que sí sabemos: <b>va a cambiar la forma de trabajar</b>, y quien la entienda y la use bien tendrá ventaja.")
    + """
      <h2>Mirando hacia delante</h2>
      <h3>1. Hacia dónde va la tecnología</h3>"""
    + lista(["<b>Modelos más capaces y baratos:</b> hacen más tareas, con más texto, imágenes, audio y vídeo.", "<b>Agentes:</b> sistemas que no solo contestan, sino que realizan tareas con herramientas (buscar, rellenar un formulario, organizar una agenda) con supervisión humana.", "<b>IA multimodal:</b> entender y generar a la vez texto, voz e imágenes.", "<b>IA en el dispositivo:</b> modelos pequeños que funcionan en el móvil sin conexión.", "<b>Más normas y más debate</b> sobre seguridad, transparencia y uso responsable."], "🔭")
    + cuidado("las predicciones concretas (fechas, cifras de empleos) fallan a menudo. Mira las tendencias, no las apuestas.")
    + """<h3>2. Hostelería del futuro: qué es probable</h3>"""
    + tabla(["Ámbito", "Posible cambio", "Lo que seguirá siendo humano"], [
        ["Reservas y atención", "Asistentes que contestan 24 h y gestionan reservas sencillas", "Trato en persona, resolver imprevistos, empatía"],
        ["Cocina", "Previsión de compras y de demanda para reducir el desperdicio; equipos automáticos", "Creatividad, sabor, criterio y seguridad alimentaria"],
        ["Sala y hotel", "Robots de reparto o limpieza en tareas concretas; check-in digital", "Hospitalidad, ambiente, atención personalizada"],
        ["Gestión", "Informes automáticos, precios dinámicos, análisis de reseñas", "Decisiones, estrategia, responsabilidad"],
        ["Formación", "Simulaciones y tutores de idiomas personalizados", "Mentores y compañeros que enseñan el oficio"]])
    + hosteleria("la hostelería vive de las personas. Muchos clientes aprecian las máquinas para lo rápido (pedir, pagar), pero <b>vuelven por el trato</b>. Quien combine oficio + trato + manejo de herramientas de IA será muy valioso.")
    + """<h3>3. ¿Me quitará el trabajo?</h3>
      <p>Lo más probable no es que «la IA sustituya a todos», sino que <b>cambien las tareas dentro de cada puesto</b>: menos tiempo en papeleo y más en el cliente; algunos puestos se reducirán y aparecerán otros. Lo que ayuda es aprender continuamente, tener buenas habilidades humanas (comunicación, trabajo en equipo, resolución de problemas) y saber usar las herramientas.</p>
      <h3>4. Habilidades que no caducan</h3>"""
    + kp(["Pensar con <b>criterio</b> y comprobar la información.", "<b>Comunicar</b> bien, por escrito y en persona.", "<b>Trabajar en equipo</b> y atender a las personas.", "<b>Aprender a aprender</b>: las herramientas cambian rápido.", "<b>Ética</b>: saber qué se debe y qué no se debe hacer con la tecnología."], "🌱")
    + """<h3>5. Tu plan personal de uso de IA</h3>"""
    + pasos(["Elige dos tareas de tu estudio o trabajo donde la IA te pueda ayudar.", "Escribe los prompts y guárdalos como plantillas.", "Decide qué comprobarás siempre y qué datos nunca compartirás.", "Revisa cada mes qué te ha servido y qué no."])
    + errores([
        ["Pensar que no hace falta aprender nada", "La IA lo hace todo", "Sin criterio no sabrás si lo que hace está bien"],
        ["Creer que todo cambiará de golpe", "Titulares espectaculares", "Los cambios llegan por etapas; hay tiempo de adaptarse"],
        ["Rechazar la IA por miedo", "Suena peligroso", "Conocerla te da más control y más opciones"]])
    + quiz("i12a", "¿Qué es un agente de IA?", ["Un sistema que realiza tareas con herramientas, con supervisión", "Un empleado de una agencia", "Un virus"], 0, "Los agentes actúan con herramientas, no solo conversan.")
    + quiz("i12b", "¿Qué probablemente seguirá siendo valioso en hostelería?", ["El trato humano y el criterio profesional", "Saber de memoria la carta", "Nada: todo será automático"], 0, "La hospitalidad y el criterio son difíciles de sustituir.")
    + quiz("i12c", "¿Cómo conviene tomar las predicciones sobre el futuro de la IA?", ["Con cautela: las tendencias importan más que las cifras exactas", "Como certezas", "Ignorándolas completamente"], 0, "Nadie sabe con certeza lo que pasará.")
    + actividad("Mi carta a mí dentro de cinco años", "Escribe en pocas líneas cómo te gustaría trabajar con IA dentro de cinco años y qué tendrás que aprender para lograrlo.", "Dentro de cinco años me gustaría…")
    + '<div class="summary-box"><b>Resumen:</b> la IA seguirá avanzando; cambiarán tareas más que oficios enteros; el trato humano, el criterio y el aprendizaje continuo seguirán siendo la ventaja.</div>'))
