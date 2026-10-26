"""Módulos 6 a 10 del curso de lengua de signos española (LSE)."""
from ia_helpers import actividad, caja, cuidado, errores, fig, hosteleria, kp, lista, palabras, pasos, practica, quiz, tabla

MODULOS = []

# 6 --------------------------------------------------------------------------------------------------
MODULOS.append(("👋", "Primeras conversaciones", "Saludar, presentarte, preguntar y responder: la estructura de un diálogo en LSE.",
    palabras("Una primera conversación en LSE es breve, visual y muy expresiva: <b>mirar a los ojos, sonreír, saludar, decir quién eres y preguntar algo sencillo</b>. Aquí aprendes cómo se organiza; los signos concretos los verás en vídeo oficial.")
    + """
      <h2>Empezar a conversar</h2>
      <h3>1. La estructura de un encuentro</h3>"""
    + pasos(["<b>Llamar la atención</b> y esperar el contacto visual.", "<b>Saludar</b> (con el signo de saludo y la cara).", "<b>Presentarse</b>: señalarse a uno mismo (el «yo» se hace señalando el pecho) y deletrear o signar el nombre.", "<b>Preguntar</b> algo sencillo: ¿cómo estás?, ¿de dónde eres?, ¿a qué te dedicas?", "<b>Despedirse</b> con claridad y cordialidad."])
    + """<h3>2. Los pronombres: señalar</h3>
      <p>En LSE los pronombres son sencillos: se <b>señala</b>. Se señala el propio pecho para «yo»; se señala a la persona para «tú»; se señala a un lado para «él/ella» (y se mantiene ese lugar como «su sitio» durante la conversación). Señalar a una persona presente es normal y educado en LSE; no es una falta de respeto.</p>
      <h3>3. El nombre en LSE: seña-nombre</h3>
      <p>Cada persona sorda suele tener una <b>seña-nombre</b>: un signo propio que se pone por su aspecto, su personalidad o la inicial de su nombre. <b>No te la inventes</b>: te la asigna la comunidad sorda. Mientras tanto, deletrea tu nombre.</p>
      <h3>4. Las preguntas</h3>
      <p>Hay dos grandes tipos, y se distinguen sobre todo por la <b>expresión de la cara</b>:</p>"""
    + tabla(["Tipo de pregunta", "Ejemplo", "Cara"], [
        ["<b>Sí / no</b>", "¿Quieres agua?", "Cejas levantadas, mirada fija, cabeza ligeramente adelantada"],
        ["<b>Con qué, quién, dónde, cuándo</b>", "¿Dónde vives?", "Cejas fruncidas, cabeza algo inclinada; la palabra interrogativa suele ir <b>al final</b>"]])
    + """<h3>5. Cortesía en la conversación</h3>"""
    + lista(["<b>No interrumpas</b> a quien está signando; espera a que termine.", "<b>Mantén el contacto visual</b> aunque haya algo distractor.", "Pide que repita si no entiendes: <b>«otra vez, por favor»</b> es una frase valiosa.", "Si vas a hacer una pausa, <b>avisa</b> (la comunicación visual no se puede «mantener» mirando el móvil).", "Si tienes algo que decirle a una tercera persona, <b>hazlo a la vista</b>: susurrar o signar a escondidas es muy mal visto."], "🙂")
    + """<h3>6. Un signo que casi todos conocen</h3>
      <p><b>GRACIAS:</b> se hace con la mano plana, con los dedos juntos, que parte de la barbilla o la boca y avanza hacia delante, acompañada de una sonrisa o un gesto de cabeza. (Búscalo en vídeo para ver el movimiento exacto.)</p>"""
    + cuidado("el resto de signos de este módulo (HOLA, BUENOS DÍAS, POR FAVOR, ADIÓS, NOMBRE…) deben aprenderse <b>en vídeo de un diccionario oficial</b>, porque varían un poco por región. Una descripción escrita nunca sustituye a ver el signo.")
    + hosteleria("saluda siempre con contacto visual y una sonrisa; señala la mesa, la carta y tu propio pecho para indicar «yo te atiendo»; y cuando el cliente se despida, recuérdalo con un gesto amable. Con eso ya has hecho una conversación.")
    + errores([
        ["Hablar y signar a la vez por defecto", "Parece ayudar", "Si lo haces a la vez, solemos perder la gramática de la LSE y el signo sale mal; practica signar en silencio, sin voz"],
        ["Mirar el móvil mientras alguien signa", "Costumbre", "Se pierde el mensaje y se considera descortés"],
        ["Señalar «con la mano entera» a las personas", "Ser amable", "En LSE se señala con el dedo índice, con naturalidad"]])
    + quiz("l6a", "¿Cómo se indica «yo» en LSE?", ["Señalando el propio pecho", "Con un gesto de adiós", "Tocando la oreja"], 0, "Los pronombres se hacen señalando.")
    + quiz("l6b", "¿Cómo se distingue una pregunta de sí/no de una pregunta con «qué» o «dónde»?", ["Por la expresión de la cara", "Por el volumen de la voz", "Por el color de la ropa"], 0, "Las cejas y la cabeza marcan el tipo de pregunta.")
    + quiz("l6c", "¿Qué es una seña-nombre?", ["Un signo propio asignado a cada persona por la comunidad sorda", "Un apellido", "Un diploma"], 0, "No te la inventes: te la asigna la comunidad.")
    + practica("Tu primer diálogo", [
        "Escribe en español un diálogo de 6 líneas: saludo, tu nombre, una pregunta, respuesta, otra pregunta y despedida.",
        "Búscalo en vídeo con un recurso oficial y apunta cada signo que reconozcas.",
        "Graba un vídeo corto presentándote (solo para ti) y revisa tu cara, tu mirada y tu ritmo."])
    + '<div class="summary-box"><b>Resumen:</b> el diálogo se estructura en saludo, presentación, pregunta y despedida; los pronombres se señalan; las preguntas se marcan con la cara; la cortesía visual es clave; los signos concretos se aprenden en vídeo.</div>'))

# 7 --------------------------------------------------------------------------------------------------
MODULOS.append(("🧠", "La gramática de la LSE", "Cómo se organiza una frase en LSE: espacio, tiempo, clasificadores y expresión.",
    palabras("La gramática de la LSE <b>no copia la del español</b>. Usa <b>el espacio, la dirección del movimiento y la expresión de la cara</b> para decir lo que el español dice con preposiciones, conjugaciones y orden de palabras.")
    + """
      <h2>Cómo se construyen las frases</h2>
      <h3>1. Orden de las ideas</h3>
      <p>Muchas frases en LSE empiezan por <b>el tema</b> (de qué hablamos) y luego dan la información: «CASA, YO VIVO» en vez de «yo vivo en una casa». Fíjate: no se trata de aprender un orden fijo de memoria, sino de <b>presentar primero lo importante</b> y después los detalles. (Estos ejemplos están en español para ilustrar la idea; no son glosas oficiales.)</p>
      <h3>2. El tiempo: la línea del tiempo</h3>
      <p>El verbo no se conjuga como en español. Se usa un <b>punto de referencia en el espacio</b>: lo que pasó se sitúa <b>detrás</b> del cuerpo (o se marca con un signo de pasado), lo que ocurre <b>ahora</b> delante, y lo futuro <b>más adelante</b>. Así se entiende «ayer», «hoy» y «mañana» sin cambiar el verbo.</p>
      <h3>3. El espacio como gramática</h3>
      <p>Al hablar de varias personas o cosas, las colocas en <b>lugares del espacio</b> («aquí está mi hermana, allí mi madre») y después las vuelves a señalar o diriges el signo hacia ellas. Algunos verbos cambian su <b>dirección</b> según quién hace la acción y a quién se le hace: no es lo mismo «yo te doy» que «tú me das».</p>
      <h3>4. Los clasificadores</h3>
      <p>Un <b>clasificador</b> es una forma de mano que «representa» a una clase de cosas (vehículos, personas, objetos planos…) y se mueve para mostrar cómo se mueve o dónde está. Con una mano que «es un coche» puedes mostrar que sube, baja, gira o se detiene. Es una de las partes más expresivas de la lengua.</p>
      <h3>5. Negación, plural e intensidad</h3>"""
    + tabla(["Idea", "Cómo se marca"], [
        ["<b>Negación</b>", "Con un signo de negación y con la cabeza, que gira de lado a lado; a veces solo con la cabeza y la cara"],
        ["<b>Plural</b>", "Repitiendo el signo o moviéndolo por el espacio"],
        ["<b>Intensidad</b>", "Con un movimiento más amplio o más rápido, y con la cara («muy», «un poco»)"],
        ["<b>Cantidad</b>", "Con numerales y con la forma del movimiento"],
        ["<b>Duda, sorpresa, enfado</b>", "Con la cara y el cuerpo, que son parte de la frase"]])
    + """<h3>6. El cambio de rol</h3>
      <p>Para contar lo que alguien dijo o hizo, la persona que signa <b>«se convierte» en ella</b>: gira el cuerpo, cambia la mirada y la expresión, y signa como si fuera esa persona. Es como el estilo directo del español, pero con el cuerpo.</p>
      <h3>7. Un ejemplo para pensar</h3>
      <p>Imagina que quieres decir «¿Dónde está el baño?». En español usamos una pregunta con entonación; en LSE, la persona signa BAÑO y luego el interrogativo DÓNDE, con las cejas fruncidas y la cabeza adelantada. El «está» no hace falta: el significado va en la cara y en el orden.</p>"""
    + caja("Idea clave:", "para entender la gramática de la LSE, piensa como un <b>director de cine</b>: sitúas los personajes en el plano (espacio), muestras sus movimientos (clasificadores), cambias de cámara (cambio de rol) y marcas las emociones con la cara.")
    + hosteleria("para señalar «mesa de ventana», «cocina» o «baños», puedes usar el espacio: el dedo y la mirada indican la dirección. Un camarero que señala con claridad y mira al cliente ya está usando gramática espacial sin saberlo.")
    + errores([
        ["Traducir palabra por palabra del español", "Es lo que se conoce", "La LSE no tiene artículos ni conjugaciones como el español; se piensa por ideas"],
        ["Olvidar la cara en las preguntas", "Se piensa en las manos", "Sin cara, una pregunta puede parecer una afirmación"],
        ["Signar siempre «en el centro»", "Comodidad", "Usa los lados para colocar personas y cosas distintas"]])
    + quiz("l7a", "¿Cómo se marca el tiempo en LSE?", ["Con la línea del tiempo en el espacio y signos de tiempo", "Conjugando los verbos como en español", "No se marca nunca"], 0, "Pasado detrás, presente delante, futuro más adelante, o con signos de tiempo.")
    + quiz("l7b", "¿Qué es un clasificador?", ["Una forma de mano que representa una clase de cosas y muestra su movimiento", "Un archivo", "Un tipo de pregunta"], 0, "Sirve para describir cómo se mueve o dónde está algo.")
    + quiz("l7c", "¿Qué es el cambio de rol?", ["Signar «como si fueras» otra persona para contar lo que dijo o hizo", "Cambiar de mano", "Cambiar de intérprete"], 0, "El cuerpo y la mirada cambian para representar a otro personaje.")
    + actividad("Piensa en visual", "Describe con tus palabras cómo explicarías con las manos y la cara el trayecto de tu casa al centro, usando el espacio y los clasificadores.", "Primero señalaría… luego…")
    + '<div class="summary-box"><b>Resumen:</b> la LSE usa el espacio, la dirección del movimiento y la cara como gramática; el tiempo se marca con una línea espacial; los clasificadores describen movimientos; el cambio de rol permite contar lo que otros dicen; no se traduce palabra por palabra.</div>'))

# 8 --------------------------------------------------------------------------------------------------
MODULOS.append(("📚", "Vocabulario básico y cómo aprenderlo", "Los temas de vocabulario esenciales, números, tiempo y un método para memorizar signos.",
    palabras("El vocabulario se aprende <b>viendo y practicando signos en vídeo</b>, con ayuda de personas sordas o profesores de LSE. Aquí tienes los <b>temas esenciales</b>, una lista de palabras clave y un método para memorizarlas.")
    + """
      <h2>Construir tu vocabulario</h2>
      <h3>1. Temas esenciales</h3>"""
    + tabla(["Tema", "Palabras para empezar (en español)"], [
        ["<b>Saludos y cortesía</b>", "hola, adiós, buenos días, buenas noches, por favor, gracias, perdón, de nada"],
        ["<b>Personas y familia</b>", "yo, tú, él, madre, padre, hermano, amigo, bebé, niño, mujer, hombre"],
        ["<b>Números</b>", "uno, dos, tres, cuatro, cinco… diez, veinte, cien, edad, dinero, euro"],
        ["<b>Tiempo</b>", "hoy, ayer, mañana, ahora, después, lunes…domingo, hora, semana, mes"],
        ["<b>Lugares</b>", "casa, escuela, trabajo, baño, calle, hospital, restaurante, hotel"],
        ["<b>Comida y bebida</b>", "agua, pan, café, leche, carne, pescado, fruta, vino, cerveza, postre"],
        ["<b>Colores</b>", "rojo, azul, verde, amarillo, blanco, negro"],
        ["<b>Acciones</b>", "comer, beber, ir, venir, trabajar, estudiar, querer, necesitar, ayudar, esperar"],
        ["<b>Sentimientos</b>", "contento, triste, enfadado, cansado, enfermo, sorprendido"],
        ["<b>Preguntas</b>", "qué, quién, dónde, cuándo, cuánto, por qué, cómo"]])
    + """<h3>2. Los números</h3>
      <p>Los números del 1 al 5 se hacen mostrando los dedos correspondientes, pero <b>la forma exacta (cuál es el pulgar, cómo se muestra el 3, y los números del 6 al 10) varía según la lengua de signos y la región</b>. Comprueba la forma oficial en el diccionario de LSE y practica con los números de tu móvil, las matrículas o los precios de la carta.</p>
      <h3>3. Tipos de signos según su origen</h3>"""
    + tabla(["Tipo", "Idea", "Ejemplo de idea"], [
        ["<b>Icónico</b>", "El signo se parece a lo que representa", "Beber (mano como un vaso que se acerca a la boca)"],
        ["<b>Arbitrario</b>", "No se parece; es convención", "Muchos signos abstractos"],
        ["<b>Deíctico</b>", "Se señala", "Yo, tú, aquí, allí"],
        ["<b>Dactilológico</b>", "Se forma con letras", "Siglas y nombres"]])
    + """<h3>4. Método para memorizar signos</h3>"""
    + pasos(["<b>Mira</b> el signo en vídeo varias veces y fíjate en los cinco parámetros.", "<b>Imítalo</b> despacio delante de un espejo.", "<b>Practícalo en frases</b> sencillas, no aislado.", "<b>Repásalo</b> al día siguiente, a los tres días y a la semana (repetición espaciada).", "<b>Úsalo</b> en una conversación real o con un compañero."])
    + kp(["Aprende <b>5 signos al día</b>, no 50 de golpe.", "Agrúpalos por <b>temas</b> (comida, familia, trabajo).", "Anota en una libreta <b>qué parámetros</b> tiene cada signo.", "Graba un vídeo corto y compáralo con el original.", "Sigue canales y cursos de <b>personas sordas</b>: su ritmo y su estilo son el modelo."], "🧠")
    + hosteleria("para un local, los 30 primeros signos que debes aprender: <b>hola, adiós, gracias, por favor, mesa, carta, agua, café, cerveza, vino, pan, carne, pescado, postre, cuenta, pagar, tarjeta, efectivo, baño, esperar, un momento, ayuda, alergia, picante, caliente, frío, aquí, allí, cuánto, ¿necesitas algo?</b>")
    + errores([
        ["Memorizar listas escritas sin ver vídeo", "Es cómodo", "Un signo es movimiento y cara; solo se aprende viéndolo"],
        ["Aprender signos aislados sin frases", "Parece más fácil", "Los signos cambian de forma al combinarse; practica en frases"],
        ["Copiar signos de vídeos sin comprobar quién los hace", "Hay mucho contenido", "Prefiere personas sordas y fuentes oficiales"]])
    + quiz("l8a", "¿Qué es un signo icónico?", ["Uno que se parece a lo que representa", "Uno que se deletrea", "Uno que se señala"], 0, "Por ejemplo, el signo de beber imita el gesto.")
    + quiz("l8b", "¿Cada cuánto conviene repasar un signo nuevo?", ["Al día siguiente, a los tres días y a la semana", "Una sola vez", "Nunca"], 0, "La repetición espaciada ayuda a fijar el vocabulario.")
    + quiz("l8c", "¿Cuántos signos es razonable aprender cada día?", ["Unos cinco, con práctica", "Cincuenta de golpe", "Ninguno"], 0, "Mejor poco y bien repasado.")
    + actividad("Tu lista de 20 signos", "Escribe 20 palabras del vocabulario del módulo que vayas a aprender primero y apunta para cuáles has encontrado ya vídeo oficial.", "1) … 2) … 3) …")
    + '<div class="summary-box"><b>Resumen:</b> el vocabulario se aprende en vídeo y por temas; los números pueden variar según región; hay signos icónicos, arbitrarios, deícticos y dactilológicos; la repetición espaciada y la práctica en frases son la clave.</div>'))

# 9 --------------------------------------------------------------------------------------------------
MODULOS.append(("🍽️", "Atención accesible en hostelería", "Cómo atender bien a clientes sordos en bares, restaurantes y hoteles.",
    palabras("En un local de hostelería, la atención a clientes sordos no exige saber signar perfectamente: exige <b>organización, paciencia y recursos visuales</b>. Con unos pocos cambios, tu local será un sitio donde la comunidad sorda se siente bienvenida.")
    + """
      <h2>Un local accesible</h2>
      <h3>1. Protocolo paso a paso: recibir a un cliente sordo</h3>"""
    + pasos(["<b>Contacto visual y sonrisa</b>: colócate a su vista y acércate de frente.", "<b>Saluda</b> con gesto de mano o un signo si lo sabes; indica con la mano «mesa» y acompáñale.", "<b>Muestra la carta</b>, preferiblemente con fotos, y señala los platos; ofrece papel o móvil para escribir.", "<b>Confirma el pedido</b> escribiéndolo o señalándolo; en alergias, <b>por escrito y con doble comprobación</b>.", "<b>Avisa visualmente</b> (desde la mesa, cuando el plato esté listo, con un gesto) y no grites a lo lejos.", "<b>Cobra</b> mostrando la cuenta en pantalla o en papel; confirma el importe con los dedos o escribiéndolo.", "<b>Despídete</b> con contacto visual y una sonrisa."])
    + """<h3>2. Qué puede tener tu local</h3>"""
    + tabla(["Recurso", "Detalle", "Ventaja"], [
        ["<b>Carta con fotos o pictogramas</b>", "Platos con foto, alérgenos con iconos", "Más claro para todos, también para turistas"],
        ["<b>Libreta o pantalla para escribir</b>", "En la barra y en la recepción", "Resuelve dudas al instante"],
        ["<b>Avisadores luminosos o vibrantes</b>", "Para aviso de «pedido listo»", "No depende del sonido"],
        ["<b>Subtítulos en televisiones</b>", "Activados por defecto", "Accesible para todos en un bar"],
        ["<b>Cartel de bienvenida</b>", "«Aquí te atendemos con gusto. Escribe o señala»", "Da confianza"],
        ["<b>Formación al equipo</b>", "Unos signos básicos y trato respetuoso", "El cliente nota la diferencia"]])
    + """<h3>3. Seguridad y emergencias</h3>
      <p>Una persona sorda puede <b>no oír</b> una alarma de incendio. Los establecimientos deben contar con <b>señales luminosas</b>, un protocolo de evacuación visual y personal que sepa avisar a las personas con discapacidad auditiva de manera directa. En un hotel, comprueba que la habitación tenga <b>aviso visual o vibrador</b> para el despertador, el timbre y la alarma.</p>
      <h3>4. Frases útiles en papel (para tener listas)</h3>"""
    + lista(["«Hola, ¿qué desea tomar?»", "«Un momento, por favor. Enseguida le atiendo.»", "«¿Tiene alguna alergia o intolerancia?»", "«La cuenta es de … euros.»", "«¿Quiere pagar con tarjeta o en efectivo?»", "«Gracias por su visita. ¡Hasta pronto!»"], "✏️")
    + cuidado("en <b>alergias</b>, nunca des por entendido: confirma <b>por escrito</b> y con una pregunta clara («¿Es alérgico a…?») y revisa con la cocina antes de servir. Es un tema de seguridad, no de cortesía.")
    + hosteleria("pide opinión a clientes sordos o a una asociación de personas sordas de tu zona sobre cómo mejorar la accesibilidad. Será una ayuda valiosa y una buena forma de crear comunidad.")
    + errores([
        ["Hablar a lo lejos o por detrás", "Se hace sin pensar", "La persona sorda no se entera; acércate de frente"],
        ["Ocultar la carta con el cuerpo", "Descuido", "El cliente debe poder ver y señalar"],
        ["Dirigirse solo al acompañante oyente", "Parece más rápido", "Es una falta de respeto; atiende a quien consume"],
        ["Servir sin confirmar una alergia", "Prisa", "Puede ser peligroso; confirma siempre por escrito"]])
    + quiz("l9a", "¿Qué es lo más importante al confirmar una alergia con un cliente sordo?", ["Confirmarlo por escrito y revisar con la cocina", "Suponerlo", "Preguntar solo al acompañante"], 0, "Es un tema de seguridad: hay que verificarlo.")
    + quiz("l9b", "¿Qué ayuda al avisar de que un pedido está listo?", ["Un aviso luminoso o vibrante, o un gesto desde la mesa", "Un grito desde la cocina", "Ninguna"], 0, "Los avisos visuales o táctiles son accesibles.")
    + quiz("l9c", "¿A quién debes dirigirte al atender a una mesa con una persona sorda?", ["A la persona sorda", "Solo al acompañante oyente", "A nadie"], 0, "Hay que dirigirse siempre a la persona que consume.")
    + practica("Auditoría de accesibilidad", [
        "Elige un bar, restaurante u hotel que conozcas (o inventa uno).",
        "Revisa la lista de recursos de la tabla: ¿cuáles tiene y cuáles faltan?",
        "Escribe cinco mejoras sencillas que costarían poco y explica por qué ayudarían."])
    + '<div class="summary-box"><b>Resumen:</b> un local accesible usa carta visual, papel o móvil, avisos luminosos, subtítulos y trato respetuoso; las alergias se confirman por escrito; se atiende siempre a la persona sorda, no solo a su acompañante.</div>'))

# 10 -------------------------------------------------------------------------------------------------
MODULOS.append(("🎓", "Seguir aprendiendo y plan de práctica", "Recursos oficiales, cómo practicar con la comunidad sorda y cómo llegar a un nivel real de conversación.",
    palabras("Ningún curso por escrito sustituye a la práctica con <b>personas sordas</b>. Este módulo te dice <b>dónde aprender</b>, <b>cómo practicar</b> y <b>cómo avanzar</b> hasta mantener conversaciones reales.")
    + """
      <h2>Tu camino con la LSE</h2>
      <h3>1. Dónde aprender</h3>"""
    + tabla(["Recurso", "Para qué sirve"], [
        ["<b>Asociaciones de personas sordas</b> de tu ciudad y la <b>CNSE</b> (Confederación Estatal de Personas Sordas) y sus federaciones", "Cursos, actividades, información y contacto con la comunidad"],
        ["<b>Fundación CNSE</b> y su diccionario normativo de la LSE (DILSE)", "Vídeos de signos y variantes; recurso de referencia"],
        ["<b>Escuelas de idiomas, universidades y centros de formación</b> con cursos de LSE", "Formación reglada por niveles"],
        ["<b>Cursos y canales de personas sordas</b>", "Aprender el ritmo, el estilo y el vocabulario actual"],
        ["<b>Intérpretes y profesionales de LSE</b>", "Orientación sobre formación y profesión"]])
    + caja("Para buscar:", "escribe en tu buscador el nombre de la entidad («CNSE», «Fundación CNSE DILSE», «federación de personas sordas de mi comunidad») y comprueba que la página es la oficial antes de usarla.")
    + """<h3>2. Niveles de aprendizaje</h3>
      <p>La LSE suele enseñarse por niveles similares a los de cualquier idioma, desde <b>inicial</b> (saludos, vocabulario básico, deletreo) hasta <b>avanzado</b> (conversación fluida, narración, textos complejos). Alcanzar un nivel conversacional exige <b>cientos de horas de práctica con personas sordas</b>, no solo clases.</p>
      <h3>3. Un plan de práctica de 12 semanas</h3>"""
    + tabla(["Semanas", "Objetivo", "Práctica diaria (20 min)"], [
        ["1–2", "Alfabeto manual y números", "Deletrear nombres y números de tu entorno"],
        ["3–4", "Saludos, presentación y cortesía", "Repasar el módulo 6 con un compañero"],
        ["5–6", "Vocabulario de familia, comida y lugares", "5 signos nuevos al día, repasados"],
        ["7–8", "Preguntas y respuestas", "Practicar preguntas sí/no y con qué, con la cara"],
        ["9–10", "Frases con espacio y tiempo", "Contar tu día usando línea del tiempo"],
        ["11–12", "Conversación guiada", "Acudir a una actividad de la comunidad sorda"]])
    + """<h3>4. Ética y respeto al aprender</h3>"""
    + lista(["<b>Pide permiso</b> antes de grabar o fotografiar a una persona sorda signando.", "No uses la lengua de signos como «curiosidad» o espectáculo: es la lengua de una comunidad.", "No te presentes como «intérprete» sin la formación y titulación necesarias.", "<b>Escucha</b> (mira) a las personas sordas: son ellas quienes mejor enseñan su lengua.", "Si cometes un error, <b>acéptalo con humildad</b> y corrige."], "🌱")
    + """<h3>5. Profesiones relacionadas</h3>
      <p>Hay muchos caminos: <b>intérprete de LSE</b>, <b>guía-intérprete</b> para personas sordociegas, <b>profesor/a de LSE</b> (con frecuencia, personas sordas), educadores, logopedas, trabajadores sociales y profesionales de atención al público con formación en accesibilidad.</p>"""
    + hosteleria("si trabajas de cara al público, una formación breve en LSE y atención accesible puede darte una <b>ventaja profesional</b> y hacer tu local más acogedor. Algunas asociaciones ofrecen charlas y cursos para empresas.")
    + errores([
        ["Aprender solo con vídeos", "Es cómodo", "Falta la conversación con personas sordas, la parte esencial"],
        ["Presumir de «hablar signos»", "Orgullo", "La humildad es clave: la lengua pertenece a la comunidad"],
        ["Abandonar a las pocas semanas", "Es difícil al principio", "Mejor poca práctica diaria y constante"]])
    + quiz("l10a", "¿Qué es lo más importante para aprender LSE de verdad?", ["Practicar con personas sordas", "Memorizar listas escritas", "Ver solo televisión"], 0, "Una lengua se aprende en conversación.")
    + quiz("l10b", "Antes de grabar a una persona sorda signando...", ["Debes pedirle permiso", "No hace falta", "Basta con avisar al profesor"], 0, "El respeto y el consentimiento van primero.")
    + quiz("l10c", "¿Cuántos minutos diarios plantea el plan de 12 semanas?", ["Unos 20", "Ninguno", "Más de 5 horas"], 0, "Lo importante es la constancia.")
    + '<div class="summary-box"><b>Resumen:</b> aprende con la comunidad sorda y fuentes oficiales; sigue un plan constante; pide permiso y muestra respeto; la lengua pertenece a la comunidad.</div>'))
