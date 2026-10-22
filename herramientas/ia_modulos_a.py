"""Módulos 1 a 6 del curso de IA para jóvenes: qué es la IA, su historia, cómo funciona un modelo de lenguaje y quién es Claude."""
from ia_helpers import actividad, caja, como, cuidado, errores, fig, hosteleria, kp, lista, palabras, pasos, practica, prompt, quiz, respuesta, tabla

MODULOS = []

# 1 --------------------------------------------------------------------------------------------------
MODULOS.append(("🤖", "¿Qué es la inteligencia artificial?", "Qué es (y qué no es) la IA, y dónde ya está en tu día a día.",
    palabras("La inteligencia artificial son <b>programas que aprenden de ejemplos</b> para hacer tareas que antes necesitaban una persona: entender un texto, reconocer una cara, recomendar una serie o <b>escribir una carta de reclamación</b>. No es magia ni una mente: es matemáticas y muchísimos datos.")
    + """
      <h2>Entender la IA desde cero</h2>
      <h3>1. Un programa normal frente a la IA</h3>
      <p>Un programa tradicional sigue <b>reglas que ha escrito una persona</b>: «si la reserva es para más de 8 personas, avisa al encargado». La IA de hoy funciona al revés: en lugar de darle las reglas, se le dan <b>miles o millones de ejemplos</b> y ella descubre sola los patrones. A eso se le llama <b>aprendizaje automático</b> (<i>machine learning</i>).</p>"""
    + tabla(["", "Programa tradicional", "Inteligencia artificial (aprendizaje automático)"], [
        ["Cómo se crea", "Una persona escribe las reglas", "Se entrena con muchos ejemplos"],
        ["Ejemplo", "Una calculadora o un TPV", "Un traductor o un asistente como Claude"],
        ["Si algo cambia", "Hay que reprogramarlo", "Se puede volver a entrenar o ajustar"],
        ["Fallos", "Siempre falla igual", "Puede equivocarse de formas imprevistas"]])
    + fig("tipos_ia.svg", "Rectángulos anidados: IA, aprendizaje automático, aprendizaje profundo e IA generativa", "La IA es el campo más grande. Dentro están el aprendizaje automático, el aprendizaje profundo (redes neuronales) y, dentro de este, la IA generativa, donde está Claude.")
    + """<h3>2. Tipos de IA</h3>"""
    + tabla(["Tipo", "Qué hace", "Ejemplo"], [
        ["<b>IA estrecha</b> (la que existe hoy)", "Muy buena en tareas concretas", "Reconocer voz, recomendar música, traducir"],
        ["<b>IA generativa</b>", "Crea contenido nuevo: texto, imágenes, audio, código", "Claude, generadores de imágenes"],
        ["<b>IA general</b> (todavía no existe)", "Entendería y aprendería cualquier cosa como una persona", "Es una idea de ciencia ficción y de investigación"]])
    + caja("Una idea clave:", "ninguna IA actual «piensa» ni «siente» como tú. Hace cálculos muy sofisticados sobre patrones aprendidos. Eso la hace muy útil, pero también explica por qué a veces <b>se equivoca con total seguridad</b>.")
    + """<h3>3. La IA que ya usas sin darte cuenta</h3>"""
    + kp(["<b>Móvil:</b> desbloqueo con la cara, corrector, predicción de texto, fotos que se ordenan solas.", "<b>Redes y vídeo:</b> lo que te recomiendan TikTok, YouTube o Netflix.", "<b>Mapas:</b> el tráfico previsto y la ruta más rápida.", "<b>Traductores y asistentes de voz.</b>", "<b>Asistentes de texto</b> como Claude, que conversan y escriben."], "📱")
    + hosteleria("las plataformas de reservas ordenan los hoteles según lo que cada cliente suele elegir; los precios de habitación cambian a diario con sistemas que predicen la demanda; los mapas y las reseñas deciden en parte quién entra en tu local. La IA ya forma parte del negocio, la uses tú o no.")
    + """<h3>4. Para qué sirve este curso</h3>
      <p>No vas a aprender a programar IA. Vas a aprender a <b>entenderla, usarla con criterio y sacarle partido</b>, sobre todo en el mundo de la hostelería: atención al cliente, cocina, gestión y comunicación. Y a saber cuándo <b>no</b> fiarte de ella.</p>"""
    + errores([
        ["«La IA lo sabe todo»", "Suena muy segura al contestar", "Es un modelo que predice texto: puede inventar datos. Siempre se verifica lo importante"],
        ["«La IA es una persona»", "Habla de forma natural", "Es un programa; no tiene experiencias, emociones ni intención"],
        ["«La IA me va a quitar el trabajo mañana»", "Titulares alarmistas", "Cambiará tareas y oficios; quien sepa usarla tendrá ventaja (módulo 12)"]])
    + quiz("i1a", "¿Cómo aprende la IA actual de aprendizaje automático?", ["A partir de muchos ejemplos", "Siguiendo reglas escritas una a una", "Copiando a otra persona"], 0, "Descubre patrones en miles o millones de ejemplos.")
    + quiz("i1b", "¿Qué tipo de IA es Claude?", ["IA generativa (estrecha)", "IA general", "Un programa tradicional"], 0, "Claude genera texto: es IA generativa. La IA general todavía no existe.")
    + quiz("i1c", "¿Cuál de estos es un ejemplo de IA en tu día a día?", ["Las recomendaciones de vídeos", "Una calculadora básica", "Un reloj de arena"], 0, "Las plataformas usan IA para recomendarte contenido.")
    + actividad("Tu mapa de IA", "Escribe tres lugares donde crees que ya usas IA (en el móvil, en redes, en un trabajo de hostelería que conozcas) y qué hace en cada uno.", "1) … 2) … 3) …")
    + '<div class="summary-box"><b>Resumen:</b> la IA aprende de ejemplos en vez de seguir reglas; la generativa crea contenido; no piensa como una persona y conviene verificarla.</div>'))

# 2 --------------------------------------------------------------------------------------------------
MODULOS.append(("🕰️", "Historia de la IA (I): de Turing al primer invierno", "De la pregunta de Alan Turing a los primeros éxitos y las primeras decepciones.",
    palabras("La IA tiene <b>más de 70 años</b>. Empezó con una pregunta de Alan Turing (1950), recibió su nombre en 1956 y vivió años de mucho entusiasmo seguidos de «inviernos» en los que la gente dejó de creer en ella. Entender esos altibajos ayuda a no creerte ni el miedo ni el humo de hoy.")
    + """
      <h2>Los primeros pasos (1943-1980)</h2>"""
    + fig("linea_tiempo.svg", "Línea de tiempo de la IA de 1950 a 2023", "Algunos hitos de la historia de la IA. Los años no están a escala.")
    + """<h3>1. Antes de la IA: la idea</h3>
      <p>Desde la Antigüedad hay historias de máquinas y autómatas que parecen pensar. Pero la historia técnica empieza en el siglo XX, cuando aparecen los <b>ordenadores</b>. En 1943, Warren McCulloch y Walter Pitts propusieron un modelo matemático de una neurona, la semilla de las <b>redes neuronales</b>.</p>
      <h3>2. 1950: la pregunta de Turing</h3>
      <p>El matemático británico <b>Alan Turing</b> publicó en 1950 el artículo <i>Computing Machinery and Intelligence</i>, que empieza con una pregunta: «¿pueden pensar las máquinas?». Para no discutir qué es pensar, propuso un juego: si una persona conversa por escrito con una máquina y con otra persona y <b>no sabe distinguirlas</b>, la máquina pasa lo que hoy llamamos el <b>test de Turing</b>.</p>
      <h3>3. 1956: nace el nombre «inteligencia artificial»</h3>
      <p>En el verano de 1956 se celebró en el Dartmouth College (EE. UU.) un taller organizado por <b>John McCarthy</b>, <b>Marvin Minsky</b>, <b>Claude Shannon</b> y Nathaniel Rochester. McCarthy había acuñado el término «inteligencia artificial» en la propuesta del encuentro. Los participantes pensaban que en pocos años las máquinas aprenderían a usar el lenguaje y resolver problemas «de personas». Fueron demasiado optimistas.</p>
      <h3>4. Los años 50 y 60: primeros logros</h3>"""
    + tabla(["Año", "Hito", "Qué fue"], [
        ["1952-1959", "Primeros programas que juegan a las damas", "Arthur Samuel hizo que un programa mejorara jugando contra sí mismo: uno de los primeros ejemplos de «aprender»"],
        ["1958", "El perceptrón", "Frank Rosenblatt construyó una máquina que aprendía a clasificar imágenes sencillas: una neurona artificial"],
        ["1966", "<b>ELIZA</b>", "Joseph Weizenbaum (MIT) creó un programa que imitaba a un psicoterapeuta devolviendo preguntas. Muchos usuarios se sentían escuchados, aunque solo seguía reglas de texto"],
        ["1966-1972", "Shakey", "Un robot de la Universidad de Stanford (SRI) que planificaba movimientos por una habitación"]])
    + caja("ELIZA y el «efecto ELIZA»:", "el propio Weizenbaum se asustó al ver que la gente atribuía comprensión a un programa tan simple. Hoy, con asistentes que escriben tan bien, ese efecto es todavía más fuerte: <b>que suene humano no significa que entienda como un humano</b>.")
    + """<h3>5. El primer «invierno de la IA» (años 70)</h3>
      <p>Las promesas eran enormes y los resultados, modestos: los ordenadores eran lentos, había pocos datos y los problemas reales eran mucho más difíciles. En 1969 Minsky y Papert demostraron los límites de los perceptrones simples, y en 1973 el <b>informe Lighthill</b> en el Reino Unido criticó duramente los resultados de la IA. Los gobiernos recortaron fondos. Esa época de poco dinero y menos ilusión se conoce como el <b>primer invierno de la IA</b>.</p>"""
    + hosteleria("imagina un hotel que promete «habitaciones inteligentes» en 1970: la tecnología no existía. Con la IA pasó igual: la idea estaba, pero faltaban potencia de cálculo y datos. Cuando llegaron, cambió todo.")
    + """<h3>Lo que nos enseña esta etapa</h3>"""
    + lista(["Las ideas pueden llegar <b>décadas antes</b> que la tecnología necesaria.",
             "Las promesas exageradas llevan a decepciones: conviene ser <b>crítico</b> con los anuncios.",
             "La IA avanza por oleadas: entusiasmo, desencanto y nuevo impulso."], "💡")
    + quiz("i2a", "¿Qué propuso Alan Turing en 1950?", ["Un juego para decidir si una máquina puede hacerse pasar por una persona en una conversación", "El primer robot camarero", "Una calculadora mecánica"], 0, "Es el test de Turing, también llamado «juego de la imitación».")
    + quiz("i2b", "¿Dónde se acuñó el término «inteligencia artificial» (1956)?", ["En el taller del Dartmouth College", "En Hollywood", "En una feria de electrodomésticos"], 0, "John McCarthy lo propuso para el taller de Dartmouth.")
    + quiz("i2c", "¿Qué fue ELIZA?", ["Un programa de 1966 que imitaba a un psicoterapeuta", "Un robot de cocina", "Un ordenador que ganaba al ajedrez"], 0, "Weizenbaum creó ELIZA en el MIT; solo seguía reglas de texto.")
    + '<div class="summary-box"><b>Resumen:</b> Turing (1950), Dartmouth (1956), perceptrón (1958), ELIZA (1966) y el primer invierno de la IA (años 70).</div>'))

# 3 --------------------------------------------------------------------------------------------------
MODULOS.append(("♟️", "Historia de la IA (II): expertos, ajedrez y deep learning", "Sistemas expertos, la victoria sobre Kasparov y la revolución del aprendizaje profundo.",
    palabras("En los 80 la IA volvió con <b>sistemas expertos</b>, ganó al campeón mundial de ajedrez en 1997 y, desde 2012, el <b>aprendizaje profundo</b> con redes neuronales muy grandes y muchos datos hizo que la IA empezara a funcionar de verdad.")
    + """
      <h2>Del ajedrez a las redes neuronales (1980-2016)</h2>
      <h3>1. Los años 80: sistemas expertos</h3>
      <p>Tras el primer invierno, la IA volvió con otra idea: en lugar de intentar crear una inteligencia general, construir programas <b>expertos en un tema</b>, con las reglas de especialistas humanos. Un sistema experto llamado <b>XCON</b> ayudaba a configurar ordenadores en la empresa DEC y ahorraba millones. Otro, <b>MYCIN</b>, proponía diagnósticos de infecciones.</p>
      <p>Funcionaban, pero eran caros de mantener: cada regla había que escribirla a mano y los sistemas fallaban si les preguntabas algo fuera de su tema. A finales de los 80 y principios de los 90 llegó el <b>segundo invierno de la IA</b>.</p>
      <h3>2. Aprender de los datos: las redes neuronales vuelven</h3>
      <p>En 1986, David Rumelhart, Geoffrey Hinton y Ronald Williams popularizaron la <b>retropropagación</b> (<i>backpropagation</i>), una forma de entrenar redes neuronales con varias capas. Una red neuronal es un conjunto de «neuronas» artificiales organizadas en capas que ajustan sus conexiones al ver ejemplos.</p>"""
    + fig("red_neuronal.svg", "Esquema de una red neuronal", "Cada círculo es una «neurona»; cada línea, una conexión con un peso que se ajusta al entrenar. Muchas capas dan lugar al aprendizaje profundo.")
    + """<h3>3. 1997: Deep Blue gana a Kasparov</h3>
      <p>En mayo de 1997, el superordenador <b>Deep Blue</b> de IBM derrotó al campeón mundial de ajedrez, <b>Garri Kaspárov</b>, en un match a seis partidas. Fue un hito simbólico, pero Deep Blue no «aprendía»: calculaba millones de jugadas por segundo con reglas escritas por expertos.</p>
      <h3>4. 2011: Watson y los asistentes de voz</h3>
      <p>En 2011, <b>Watson</b> de IBM ganó el concurso de televisión <i>Jeopardy!</i> contra campeones humanos. Ese mismo año, Apple presentó <b>Siri</b>, y poco después llegaron Google Now, Alexa y Cortana: la IA empezaba a entrar en los móviles y en las casas.</p>
      <h3>5. 2012: la explosión del aprendizaje profundo</h3>
      <p>Tres cosas coincidieron: <b>muchísimos datos</b> (internet), <b>mucha potencia de cálculo</b> (las tarjetas gráficas o GPU) y <b>mejores técnicas</b>. En 2012, una red llamada <b>AlexNet</b> (Krizhevsky, Sutskever y Hinton) ganó con ventaja el concurso de reconocimiento de imágenes ImageNet. A partir de ahí, el <b>aprendizaje profundo</b> (<i>deep learning</i>) dominó el campo: reconocimiento de voz, de imágenes y traducción dieron un salto enorme.</p>
      <h3>6. 2016: AlphaGo</h3>
      <p>El juego de mesa <b>Go</b> es mucho más complejo que el ajedrez. En marzo de 2016, <b>AlphaGo</b>, de DeepMind (Google), venció 4-1 al campeón <b>Lee Sedol</b>. Lo sorprendente fue que aprendió jugando millones de partidas contra sí mismo y encontró jugadas que ningún humano había pensado.</p>"""
    + tabla(["Año", "Hito", "Por qué importa"], [
        ["1980s", "Sistemas expertos", "La IA llega a las empresas, pero es cara y frágil"],
        ["1986", "Retropropagación", "Se pueden entrenar redes con varias capas"],
        ["1997", "Deep Blue vence a Kasparov", "Una máquina gana al campeón de ajedrez (con cálculo, no con aprendizaje)"],
        ["2011", "Watson y Siri", "La IA llega al gran público"],
        ["2012", "AlexNet", "El aprendizaje profundo funciona de verdad"],
        ["2016", "AlphaGo", "Una IA aprende sola a un nivel superior al humano"]])
    + hosteleria("el reconocimiento de imágenes de 2012 es la base de que hoy tu móvil pueda decirte qué plato es en una foto, o de que un sistema de cocina detecte si una tabla de cortar está limpia. Y la voz de 2011 es la que hoy toma notas de una comanda en algunos locales.")
    + errores([
        ["Pensar que Deep Blue «aprendía»", "Se le suele comparar con la IA de hoy", "Deep Blue calculaba muchas jugadas con reglas de expertos; AlphaGo sí aprendió por sí misma"],
        ["Creer que el deep learning es nuevo", "Parece surgido en 2012", "Sus ideas son de los años 40 a 80; lo nuevo es tener datos y potencia para entrenarlas"]])
    + quiz("i3a", "¿Qué hizo posible el salto del aprendizaje profundo desde 2012?", ["Muchos datos, mucha potencia de cálculo y mejores técnicas", "Que los ordenadores empezaron a pensar", "Una ley nueva"], 0, "Los tres factores coincidieron: datos, GPU y técnicas.")
    + quiz("i3b", "¿Quién ganó a Garri Kaspárov en 1997?", ["Deep Blue", "AlphaGo", "Watson"], 0, "Deep Blue, de IBM.")
    + quiz("i3c", "¿Qué logró AlphaGo en 2016?", ["Ganar al campeón de Go Lee Sedol", "Ganar a Kasparov", "Escribir un libro"], 0, "Ganó 4-1 a Lee Sedol tras aprender jugando contra sí misma.")
    + '<div class="summary-box"><b>Resumen:</b> sistemas expertos (80), Deep Blue (1997), Watson y Siri (2011), AlexNet (2012) y AlphaGo (2016): el aprendizaje profundo cambió el rumbo de la IA.</div>'))

# 4 --------------------------------------------------------------------------------------------------
MODULOS.append(("💬", "Historia de la IA (III): de los Transformers a Claude", "Cómo se llegó a las IA que conversan, y dónde aparece Anthropic.",
    palabras("En 2017 apareció una idea nueva, los <b>Transformers</b>, que permitió crear modelos que <b>entienden y generan lenguaje</b>. En 2022 ChatGPT lo llevó al gran público y en 2023 llegó el primer <b>Claude</b>, de la empresa Anthropic.")
    + """
      <h2>La era de los modelos de lenguaje (2017-hoy)</h2>
      <h3>1. 2017: «Attention is all you need»</h3>
      <p>Investigadores de Google publicaron en 2017 un artículo con ese título, que presentaba la arquitectura <b>Transformer</b>. Su gran idea es el mecanismo de <b>atención</b>: para entender una palabra, el modelo mira todas las demás palabras de la frase y decide <b>cuáles son importantes</b>. Por ejemplo, en «el camarero dejó la bandeja en la mesa y <i>la</i> limpió», «la» se refiere a la mesa o a la bandeja según el contexto.</p>
      <h3>2. Los modelos grandes de lenguaje (LLM)</h3>
      <p>Con los Transformers se pudieron entrenar modelos enormes con textos de internet, libros y otras fuentes: son los <b>modelos grandes de lenguaje</b> (<i>LLM</i>, <i>large language models</i>). Los hitos más conocidos:</p>"""
    + tabla(["Año", "Hito", "Qué aportó"], [
        ["2018", "GPT-1 (OpenAI) y BERT (Google)", "Primeros modelos de lenguaje basados en Transformers"],
        ["2020", "GPT-3 (OpenAI)", "Un modelo con 175.000 millones de parámetros que escribía textos sorprendentes"],
        ["2021", "Se funda <b>Anthropic</b>", "Un grupo de investigadores crea una empresa centrada en hacer IA segura"],
        ["nov. 2022", "<b>ChatGPT</b>", "Una conversación sencilla con un modelo llega a millones de personas en semanas"],
        ["mar. 2023", "<b>Claude</b>", "Primera versión del asistente de Anthropic"],
        ["2024 y después", "Claude 3 y nuevas versiones", "Familias de modelos de distintos tamaños y capacidades; salen versiones nuevas con frecuencia"]])
    + caja("Un ritmo muy rápido:", "las versiones y las funciones de estos asistentes cambian cada pocos meses. Por eso este curso se centra en lo que <b>no caduca</b>: cómo funcionan, cómo pedir bien las cosas y cómo usarlas con criterio.")
    + """<h3>3. Anthropic y Claude</h3>
      <p><b>Anthropic</b> es una empresa de investigación y desarrollo de IA fundada en 2021 por antiguos miembros de OpenAI, entre ellos los hermanos <b>Dario y Daniela Amodei</b>. Su lema es construir sistemas de IA <b>fiables, interpretables y controlables</b>. <b>Claude</b> es el nombre de su familia de asistentes. En los módulos siguientes verás cómo funciona y cómo usarlo.</p>
      <h3>4. Más allá de los chats</h3>
      <p>La IA generativa no solo escribe texto: hay modelos que crean <b>imágenes</b>, <b>música</b>, <b>vídeo</b> y <b>código</b>. Y la IA también se usa en ciencia: en 2024, los premios Nobel de Física y de Química reconocieron trabajos de IA (John Hopfield y Geoffrey Hinton, por sus ideas sobre redes neuronales; Demis Hassabis y John Jumper, junto con David Baker, por predecir estructuras de proteínas con AlphaFold).</p>"""
    + hosteleria("desde 2023, muchos negocios usan asistentes de este tipo para responder correos, preparar cartas, traducir menús o generar textos de redes sociales. Los verás en detalle en los módulos 8, 9 y 10.")
    + """<h3>Reto: ordena la historia</h3>
      <p>Cuando hayas leído los tres módulos de historia, pon a prueba tu memoria con las actividades de abajo.</p>"""
    + errores([
        ["Pensar que ChatGPT fue la primera IA", "Fue la que más ruido hizo", "La IA existe desde los 50; ChatGPT popularizó los modelos de lenguaje para el público general"],
        ["Pensar que Claude es lo mismo que ChatGPT", "Los dos son asistentes de texto", "Son productos distintos de empresas distintas (Anthropic y OpenAI), con enfoques y modelos diferentes"]])
    + quiz("i4a", "¿Qué idea clave aportó el Transformer en 2017?", ["El mecanismo de atención", "Un robot camarero", "El primer chatbot"], 0, "La atención permite al modelo decidir qué palabras del contexto importan.")
    + quiz("i4b", "¿Quién creó Claude?", ["Anthropic", "Google", "Apple"], 0, "Claude es la familia de asistentes de Anthropic, empresa fundada en 2021.")
    + quiz("i4c", "¿Qué significa LLM?", ["Modelo grande de lenguaje", "Lenguaje de lógica matemática", "Línea de lectura mecánica"], 0, "Large language model: modelo entrenado con enormes cantidades de texto.")
    + '<div class="summary-box"><b>Resumen:</b> Transformers (2017), GPT-3 (2020), Anthropic (2021), ChatGPT (2022) y Claude (2023): la era de los modelos grandes de lenguaje.</div>'))

# 5 --------------------------------------------------------------------------------------------------
MODULOS.append(("🧠", "Cómo funciona un modelo de lenguaje", "Datos, entrenamiento, tokens, probabilidades y por qué a veces «alucina».",
    palabras("Un modelo de lenguaje hace una sola cosa: <b>predice la siguiente palabra</b> (en realidad, el siguiente «token») según lo que ya hay escrito. Repitiendo eso muchas veces escribe respuestas enteras. Por eso es creativo, pero también puede <b>inventarse cosas</b> con mucha seguridad.")
    + """
      <h2>Por dentro de Claude (y de otros asistentes)</h2>
      <h3>1. Paso 1: el entrenamiento</h3>
      <p>El modelo se entrena con <b>enormes cantidades de texto</b>. Durante el entrenamiento, cada vez que se le muestra un fragmento, tiene que adivinar la siguiente palabra; si falla, sus conexiones internas (<b>parámetros</b>, miles de millones de números) se ajustan un poquito. Tras hacerlo con billones de palabras, el modelo ha aprendido gramática, datos del mundo, estilos de escritura y hasta cierto razonamiento. Después se le <b>afina</b> con ejemplos de buenas respuestas y con valoraciones de personas para que sea útil y seguro.</p>
      <h3>2. Paso 2: tu mensaje se convierte en tokens</h3>
      <p>El modelo no lee palabras como tú, sino <b>tokens</b>: trozos de texto que pueden ser una palabra corta, parte de una palabra larga o un signo. En español, una palabra suele ser de 1 a 3 tokens. El modelo trabaja con números, no con letras.</p>"""
    + fig("flujo_llm.svg", "Flujo de un modelo de lenguaje: mensaje, tokens, modelo, siguiente token", "El modelo calcula qué token es más probable, lo añade y repite el proceso hasta terminar la respuesta.")
    + """<h3>3. Paso 3: predecir la siguiente palabra</h3>
      <p>El modelo calcula una <b>probabilidad para cada token posible</b> y elige uno. No siempre elige el más probable: un ajuste llamado <b>temperatura</b> controla cuánto se arriesga. Con temperatura baja, respuestas más previsibles; con temperatura alta, más variadas y creativas. Por eso <b>la misma pregunta puede dar respuestas distintas</b>.</p>
      <h3>Juega con las probabilidades</h3>
      <p>Elige la palabra que crees más probable y mira cómo se reparten las probabilidades. Luego genera palabras con la temperatura.</p>
      <div class="activity"><p id="pred-frase" style="font-size:1.15em;font-weight:700"></p><div class="lect-btns" id="pred-ops"></div><div id="pred-res"></div>
        <p><button class="btn" onclick="predSiguiente()">Otra frase ➡️</button></p>
        <hr><p><b>Genera palabras al azar</b> con esta frase. <label>Temperatura: <input type="range" id="pred-temp" min="0.1" max="2" step="0.1" value="1"> <b id="pred-t">1.0</b></label></p>
        <p><button class="btn" onclick="predGenerar()">🎲 Generar una palabra</button> <button class="btn" onclick="predLimpiar()">Borrar</button></p><p id="pred-gen" class="pred-gen"></p>
        <p class="small">Con temperatura baja casi siempre sale la palabra más probable; con temperatura alta salen también las raras.</p></div>
      <h3>4. La ventana de contexto: la «memoria» de una conversación</h3>
      <p>El modelo solo «ve» una cantidad limitada de texto a la vez: lo que está en la conversación (tu mensaje, sus respuestas y los documentos que le des). Eso es la <b>ventana de contexto</b>, y se mide en tokens. Las versiones recientes de Claude admiten ventanas muy grandes (cientos de páginas), pero <b>no recuerdan por sí mismas conversaciones antiguas</b> si no se les vuelven a dar o si la aplicación no tiene una función de memoria activada.</p>
      <div class="activity"><label>Tokens: <input type="range" id="ctx-n" min="1000" max="200000" step="1000" value="100000" oninput="ctxActualizar()"> <b id="ctx-v">100000</b></label><p id="ctx-res"></p></div>
      <h3>5. ¿Por qué se equivoca? Las «alucinaciones»</h3>
      <p>Como el modelo genera lo que <b>suena probable</b>, a veces produce datos falsos con aspecto de verdaderos: una cita inexistente, un horario inventado, una receta con un ingrediente imposible. Se llama <b>alucinación</b>. Es más probable cuando:</p>"""
    + lista(["le preguntas algo <b>muy concreto o poco conocido</b> (un restaurante pequeño, una ley reciente);", "no le das el contexto o el documento con la información;", "le pides números, fechas o citas exactas;", "le haces una pregunta con una premisa falsa y la acepta."], "⚠️")
    + cuidado("en hostelería, un dato inventado (un alérgeno, una temperatura de conservación, un horario) puede causar un problema serio. <b>La IA ayuda a redactar y a pensar; la información crítica se verifica siempre con fuentes oficiales.</b>")
    + """<h3>6. Lo que sí hace bien… y lo que no</h3>"""
    + tabla(["Suele hacerlo bien", "Hay que vigilarlo"], [
        ["Redactar, resumir y reformular textos", "Datos exactos, cifras y citas"],
        ["Traducir y adaptar el tono", "Información muy reciente (depende de su fecha de conocimiento)"],
        ["Dar ideas y alternativas", "Temas legales, médicos o de seguridad alimentaria"],
        ["Explicar conceptos paso a paso", "Hechos sobre personas o negocios concretos"],
        ["Ayudar con fórmulas, código y tablas", "Cálculos largos (conviene comprobarlos)"]])
    + quiz("i5a", "¿Qué hace un modelo de lenguaje en cada paso?", ["Predecir el siguiente token", "Buscar en internet siempre", "Copiar una respuesta guardada"], 0, "Predice el siguiente token y repite el proceso.")
    + quiz("i5b", "¿Qué es una alucinación de la IA?", ["Una respuesta falsa que suena verdadera", "Un fallo del teclado", "Un sueño del modelo"], 0, "El modelo puede inventar datos con aspecto de ciertos.")
    + quiz("i5c", "¿Qué controla la temperatura?", ["Lo arriesgado y variado que es el modelo al elegir palabras", "La velocidad del ordenador", "El volumen de la voz"], 0, "Con temperatura baja es más previsible; con alta, más creativo.")
    + quiz("i5d", "¿Qué es la ventana de contexto?", ["La cantidad de texto que el modelo puede «ver» a la vez", "El hueco de la pantalla", "Un tipo de licencia"], 0, "Es la «memoria de trabajo» de una conversación, medida en tokens.")
    + '<div class="summary-box"><b>Resumen:</b> el modelo predice tokens según probabilidades; se entrena con muchos textos; tiene una ventana de contexto limitada; puede alucinar, así que se verifica lo importante.</div>'))

# 6 --------------------------------------------------------------------------------------------------
MODULOS.append(("✨", "Conoce a Claude", "Qué es Claude, cómo se le ha enseñado a comportarse y cómo se accede a él.",
    palabras("Claude es el <b>asistente de IA de Anthropic</b>. Está pensado para ser útil, honesto e inofensivo: ayuda con textos, ideas, análisis y programación, y también dice «no lo sé» o «no puedo ayudar con eso» cuando corresponde. Hay <b>varios modelos de distinto tamaño</b>: los pequeños son más rápidos y baratos; los grandes, más capaces.")
    + """
      <h2>Quién es Claude</h2>
      <h3>1. Un asistente con carácter y valores</h3>
      <p>Claude es un <b>modelo de lenguaje</b> que conversa contigo. Anthropic lo ha entrenado para que sea:</p>"""
    + kp(["<b>Útil:</b> intenta resolver lo que realmente necesitas, no solo lo que dices.", "<b>Honesto:</b> procura no engañar, reconocer sus dudas y no inventar.", "<b>Inofensivo:</b> evita ayudar a hacer daño y trata con cuidado los temas delicados."], "✅")
    + """<p>Para enseñarle a comportarse así, Anthropic desarrolló un método llamado <b>IA constitucional</b> (<i>Constitutional AI</i>, 2022): en lugar de depender solo de personas que valoren cada respuesta, se le da al modelo un conjunto de <b>principios escritos</b> (una «constitución») y se entrena para que revise y mejore sus propias respuestas según esos principios.</p>
      <h3>2. La familia de modelos</h3>
      <p>Claude no es un único modelo, sino una <b>familia</b>. Cada versión tiene varios tamaños:</p>"""
    + tabla(["Tipo de modelo", "Características", "Cuándo conviene"], [
        ["Pequeño y rápido", "Responde enseguida y cuesta poco", "Tareas sencillas y repetitivas: clasificar reseñas, responder preguntas frecuentes"],
        ["Intermedio", "Equilibrio entre velocidad y capacidad", "Uso diario: textos, resúmenes, análisis"],
        ["Grande y potente", "El más capaz, más lento y caro", "Tareas complejas: análisis largos, razonamiento difícil, programación"]])
    + caja("Los nombres cambian:", "Anthropic lanza versiones nuevas con frecuencia y los nombres exactos de los modelos varían. No hace falta memorizarlos: en la aplicación verás qué modelos hay disponibles y para qué sirve cada uno.")
    + """<h3>3. Qué puede hacer</h3>"""
    + lista(["<b>Conversar y explicar</b> cualquier tema con el nivel que le pidas.", "<b>Escribir y corregir</b>: correos, cartas, descripciones, discursos.", "<b>Resumir y analizar documentos</b> que le das (PDF, hojas de cálculo, textos).", "<b>Entender imágenes</b> (por ejemplo, la foto de una carta o un plato).", "<b>Programar y trabajar con datos</b>: fórmulas de hojas de cálculo, pequeñas webs, scripts.", "<b>Traducir</b> entre muchos idiomas."], "🧰")
    + """<h3>4. Qué NO puede (o no debe) hacer</h3>"""
    + lista(["No «sabe» lo que pasó después de su fecha de entrenamiento, salvo que tenga una herramienta de búsqueda activa.", "No tiene acceso a tu negocio, tus archivos ni a internet si tú no se los das o no hay una herramienta conectada.", "No siempre acierta con cálculos, datos exactos y citas.", "Se niega a ayudar con cosas dañinas o ilegales."], "🚫")
    + """<h3>5. Cómo se accede a Claude</h3>"""
    + tabla(["Forma", "Para quién", "Qué es"], [
        ["Web y apps (claude.ai y aplicaciones móvil y de escritorio)", "Usuarios", "Chat con Claude; permite subir archivos y organizar proyectos. Hay versión gratuita y de pago"],
        ["API", "Desarrolladores y empresas", "Para integrar Claude en otras aplicaciones (por ejemplo, un asistente de reservas de un hotel)"],
        ["Aplicaciones de empresas", "Equipos de trabajo", "Algunos programas y plataformas incorporan Claude por dentro"]])
    + cuidado("las condiciones de uso de Claude.ai están pensadas para <b>personas mayores de 18 años</b>. Si eres menor de edad, <b>no crees una cuenta por tu cuenta</b>: úsalo solo con tu profesor/a o con tu familia en un entorno educativo autorizado. Este curso funciona sin cuenta: los ejercicios son interactivos y los prompts de ejemplo los puedes probar en clase con quien tenga acceso.")
    + """<h3>6. Tu privacidad al usar Claude</h3>
      <p>Lo que escribes en un asistente de IA se envía a los servidores de la empresa. Antes de usarlo, conviene saber cómo trata tus datos: Anthropic explica su política de privacidad y las opciones sobre el uso de conversaciones en su web. Regla de oro: <b>no pegues datos personales de otras personas ni datos confidenciales</b> (lo verás a fondo en el módulo 11).</p>"""
    + hosteleria("si usas Claude en un hotel o restaurante, piensa en él como un <b>ayudante nuevo muy rápido, que no conoce tu negocio</b>: hay que explicarle bien las cosas, revisarle lo que hace y no darle información privada de clientes ni de la empresa sin permiso.")
    + errores([
        ["Pensar que Claude me conoce", "Habla con naturalidad", "Cada conversación empieza desde cero salvo funciones concretas de memoria; cuéntale lo que necesite saber"],
        ["Fiarme de lo que dice sobre mi negocio", "Contesta con seguridad", "No conoce tu local: dale los datos o verifica lo que diga"],
        ["Pegar un listado de clientes para «analizarlo»", "Parece cómodo", "Son datos personales: se anonimizan o no se usan (RGPD)"]])
    + quiz("i6a", "¿Qué es la «IA constitucional» de Anthropic?", ["Entrenar al modelo para que revise sus respuestas con principios escritos", "Una ley de la Constitución", "Un tipo de ordenador"], 0, "El modelo se guía por principios escritos (una «constitución») para mejorar sus respuestas.")
    + quiz("i6b", "¿Qué debe hacer una persona menor de 18 años para usar Claude.ai?", ["Usarlo solo con profesores o familia en un entorno autorizado", "Crear una cuenta propia", "Pedir una a un amigo"], 0, "Las condiciones de uso son para mayores de 18 años.")
    + quiz("i6c", "¿Cómo es mejor tratar a un asistente de IA en el trabajo?", ["Como un ayudante nuevo, rápido pero al que hay que revisarle el trabajo", "Como un jefe que siempre acierta", "Como un amigo al que se cuenta todo"], 0, "Es muy útil pero no conoce tu negocio y puede equivocarse.")
    + '<div class="summary-box"><b>Resumen:</b> Claude es el asistente de Anthropic: útil, honesto e inofensivo; hay modelos de distintos tamaños; funciona como un ayudante rápido al que se revisa; la cuenta de Claude.ai es para mayores de 18.</div>'))
