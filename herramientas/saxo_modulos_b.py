"""Módulos 8 a 14 del curso de saxofón alto: registro agudo, transposición, escalas, ritmo, sonido y afinación,
repertorio y jazz/blues."""
from saxo_helpers import actividad, caja, como, errores, fig, kp, lista, palabras, partitura, pasos, practica, quiz, tabla

MODULOS = []

CLAVES_OPC = "".join(f'<option value="{pc}">{n}</option>' for pc, n in enumerate(["Do", "Re♭", "Re", "Mi♭", "Mi", "Fa", "Fa♯", "Sol", "La♭", "La", "Si♭", "Si"]))

# 8 --------------------------------------------------------------------------------------------------
MODULOS.append(("⬆️", "El registro agudo y la llave de octava", "La misma digitación, una octava más aguda: cómo y cuándo usar la llave de octava.",
    palabras("La <b>llave de octava</b> (la pulsa el pulgar izquierdo) abre un orificio que hace que la misma digitación suene <b>una octava más aguda</b>. Tocas Re agudo con los mismos seis dedos que el Re grave, pero con el pulgar levantado hacia la llave.")
    + """
      <h2>Más arriba</h2>
      <h3>1. Qué hace la llave de octava</h3>
      <p>En el saxo, <b>todas las notas a partir del Re5 repiten la digitación de la octava inferior</b>, añadiendo la llave de octava. Eso reduce mucho lo que hay que memorizar: si sabes tocar Re, Mi, Fa, Sol, La y Si en el registro grave, ya sabes sus equivalentes agudas.</p>
      <p>Hay una única excepción en la parte baja del registro agudo: el <b>Do</b> (Do5) y el <b>Do♯</b> (Do♯5) pertenecen todavía al registro grave. Su versión aguda (Do6 y Do♯6) es la misma digitación con la llave de octava.</p>
      <h3>2. Cómo se usa</h3>"""
    + pasos([
        ("El pulgar izquierdo hace de «bisagra».", "descansa sobre la placa del pulgar y, para pulsar la llave de octava, rueda ligeramente hacia arriba sin levantarse del todo."),
        ("Pulsa con suavidad.", "no necesitas presionar con fuerza; basta un movimiento breve y preciso."),
        ("Mantén la boca igual.", "la embocadura no cambia: la llave de octava hace el trabajo. Lo que sí hay que hacer es dar un poco <b>más de velocidad al aire</b>."),
        ("Piensa la nota antes de tocarla.", "canta mentalmente la nota aguda antes de emitirla: ayuda a la garganta a colocarse."),
    ])
    + """<h3>3. Las notas agudas</h3>"""
    + fig("dig_agudo1.svg", "Digitaciones de Re5, Mi5, Fa♯5, Sol5, La5 y Si5", "Las mismas digitaciones del registro grave con la llave de octava (8.ª) pulsada.")
    + fig("dig_agudo2.svg", "Digitaciones de Do6, Do♯6, Mi♭5, Sol♯5, Si♭5 y Fa5", "Do6 se toca como Do5 más la llave de octava; Do♯6, con todos los dedos levantados y la llave de octava.")
    + tabla(["Nota aguda", "Digitación", "Equivale a…"], [
        ["Re5", "Seis dedos + octava", "Re4 + octava"],
        ["Mi5", "Izq 1-2-3, der 1-2 + octava", "Mi4 + octava"],
        ["Fa5 / Fa♯5", "Como Fa4 / Fa♯4 + octava", "Con la derecha 1 o 2"],
        ["Sol5", "Izq 1-2-3 + octava", "Sol4 + octava"],
        ["La5", "Izq 1-2 + octava", "La4 + octava"],
        ["Si5", "Izq 1 + octava", "Si4 + octava"],
        ["Do6", "Izq 2 + octava", "Do5 + octava"],
        ["Do♯6", "Todo levantado + octava", "Do♯5 + octava"]])
    + caja("Más arriba:", "las notas más agudas (Re6, Mi♭6, Mi6 y Fa6) se tocan con las <b>llaves de la palma</b> de la mano izquierda. Se aprenden más adelante, con el saxo y un profesor/a; este curso llega hasta el Do♯6.")
    + """<h3>4. Practicar el cambio de registro</h3>"""
    + partitura("p8_octavas") + partitura("p8_sol")
    + practica("Ejercicio de octavas (5 minutos)", [
        "<b>Una nota, dos registros:</b> toca Sol largo y luego Sol agudo, sin cambiar la boca; solo la llave y un poco más de aire.",
        "<b>Octavas ligadas:</b> Sol–sol–Sol–sol con una sola lengua, a ♩ = 60.",
        "<b>Escala de Sol mayor</b> de la partitura, despacio, comprobando el paso del Do al Re.",
        "<b>Después del Re,</b> sigue subiendo: Mi, Fa♯, Sol… y para en la que ya no suena limpia.",
    ])
    + """<h3>5. Melodías con el registro agudo</h3>"""
    + partitura("p8_twinkle") + partitura("p8_ode")
    + errores([
        ["La nota aguda no suena y salta al grave", "Falta aire o la llave no está pulsada", "Pulsa la llave a tiempo y da más velocidad al aire"],
        ["Las notas agudas suenan altas y chillonas", "Muerdo para que salgan", "Relaja la mordida: la llave de octava hace el cambio"],
        ["Me cuesta el paso Do–Re", "Cambio de registro", "Practica ese paso lento, con la nota larga antes y después"],
        ["La nota sube o baja de afinación", "Cambio la presión de los labios", "Mantén la misma embocadura en todo el registro"]])
    + quiz("s8a", "¿Qué hace la llave de octava?", ["Hace que la misma digitación suene una octava más aguda", "Cambia la tonalidad del saxo", "Sube el volumen"], 0, "Abre un orificio que fuerza el armónico octavado.")
    + quiz("s8b", "¿Qué dedos se usan para el Sol agudo (Sol5)?", ["Izq 1-2-3 + llave de octava", "Solo la llave de octava", "Los seis dedos"], 0, "Es la digitación del Sol4 con la llave de octava.")
    + quiz("s8c", "¿Qué hay que hacer con la boca al subir de registro con la llave?", ["Mantenerla igual y dar más velocidad al aire", "Morder más", "Cerrar los labios"], 0, "La llave hace el cambio; el aire va más rápido.")
    + '<div class="summary-box"><b>Resumen:</b> desde Re5 hasta Do♯6, la digitación del registro grave más la llave de octava. Boca igual y aire más rápido, sin morder.</div>'))

# 9 --------------------------------------------------------------------------------------------------
MODULOS.append(("🔄", "Lectura y transposición: el saxo en Mi♭", "Por qué lo que lees no es lo que suena y cómo pasar de un tono a otro.",
    palabras("El saxo alto es un <b>instrumento transpositor</b>: lo que lees <b>no es lo que suena</b>. El saxo alto suena una <b>sexta mayor más grave</b> que lo escrito. La regla de oro: del piano al saxo alto, <b>añade tres sostenidos</b> a la armadura.")
    + """
      <h2>El saxo es un instrumento en Mi♭</h2>
      <h3>1. Por qué los saxos transponen</h3>
      <p>Todos los saxofones se tocan con la <b>misma digitación para la misma nota escrita</b>, aunque sean de tamaños muy distintos. Así, quien aprende el alto puede pasar al tenor o al soprano sin volver a aprender los dedos. A cambio, la música se escribe <b>transpuesta</b> para cada tipo de saxo, de modo que la misma nota escrita suena en alturas diferentes.</p>
      <p>Cuando decimos que el alto está «en Mi♭» queremos decir que, cuando lees un <b>Do</b>, suena un <b>Mi♭</b> (una sexta mayor, 9 semitonos, más grave). El piano, la flauta y la guitarra suenan lo que está escrito: se dice que están «en Do» o en <b>tono de concierto</b>.</p>
      <h3>2. Escrito y real: la tabla básica</h3>"""
    + tabla(["Lo que lees (escrito)", "Lo que suena (concierto)", "Intervalo"], [
        ["Do", "Mi♭", "Una sexta mayor más grave"],
        ["Re", "Fa", "Una sexta mayor más grave"],
        ["Mi", "Sol", "Una sexta mayor más grave"],
        ["Fa", "La♭", "Una sexta mayor más grave"],
        ["Sol", "Si♭", "Una sexta mayor más grave"],
        ["La", "Do", "Una sexta mayor más grave"],
        ["Si", "Re", "Una sexta mayor más grave"]])
    + caja("Las dos reglas:", "• Del <b>saxo al piano</b>: lo que suena es una sexta mayor <b>más grave</b> que lo escrito.<br>• Del <b>piano al saxo</b>: se escribe una sexta mayor <b>más aguda</b> (o una tercera menor más grave).")
    + """<h3>3. Las tonalidades</h3>
      <p>Si un piano toca una canción en cierta tonalidad (la «de concierto»), el saxo alto debe leerla en otra tonalidad, tres sostenidos por encima. Esto es lo que se hace con las partituras de saxo:</p>"""
    + tabla(["Piano (concierto)", "Saxo alto (escrita)", "Alteraciones de la escrita"], [
        ["Do mayor", "La mayor", "3 sostenidos"],
        ["Sol mayor", "Mi mayor", "4 sostenidos"],
        ["Re mayor", "Si mayor", "5 sostenidos"],
        ["Fa mayor", "Re mayor", "2 sostenidos"],
        ["Si♭ mayor", "Sol mayor", "1 sostenido"],
        ["Mi♭ mayor", "Do mayor", "Sin alteraciones"],
        ["La♭ mayor", "Fa mayor", "1 bemol"],
        ["Re♭ mayor", "Si♭ mayor", "2 bemoles"]])
    + como("Para pasar de la armadura del piano a la del saxo alto, <b>suma tres sostenidos</b> (o quita tres bemoles). Si el piano tiene 3 bemoles (Mi♭ mayor), quitas 3 y queda sin alteraciones (Do mayor). Si el piano no tiene ninguna (Do mayor), sumas 3 sostenidos (La mayor).")
    + """<h3>4. Convertidor de tonalidades</h3>
      <div class="activity"><label>Tonalidad del piano (concierto): <select id="conv-sel" onchange="convertir()">__CLAVES__</select></label>
        <p id="conv-res"></p><div id="conv-pent" style="max-width:300px"></div></div>
      <h3>5. Entrenador de transposición</h3>
      <div class="activity"><p id="trans-q">Pulsa «Empezar».</p><div class="lect-btns" id="trans-opts"></div><p class="feedback" id="trans-fb"></p>
        <p><button class="btn" onclick="transNueva()">Empezar / otra pregunta</button></p></div>
      <h3>6. La misma melodía en tres tonalidades</h3>"""
    + partitura("p9_ode_tres")
    + """<h3>7. Tu registro real</h3>
      <p>El saxo alto abarca, <b>escrito</b>, del Si♭ grave (Si♭3) al Fa♯ agudo (Fa♯6), pero lo que suena va del Re♭3 al La5. Un piano que quiera doblarte debe tocar las notas una sexta mayor más abajo.</p>
      <h3>8. Tocar con otros músicos</h3>"""
    + lista(["<b>En una banda o combo:</b> pide siempre la parte de <i>«saxo alto en Mi♭»</i>; los demás instrumentos tienen partes distintas.",
             "<b>Con una pista de acompañamiento (<i>play-along</i>):</b> suenan en tono de concierto; busca la edición «Eb instruments» o transpórtalas.",
             "<b>Con un pianista:</b> dile en qué tonalidad estás leyendo: «yo estoy en Do (escrito), tú estás en Mi♭ (concierto)».",
             "<b>Los acordes</b> de las partituras de saxo ya están transportados: no hace falta que los conviertas."], "🎙️")
    + errores([
        ["Toco lo que lee el piano y suena mal", "No he transpuesto", "Pide la parte de saxo alto o suma tres sostenidos a la armadura"],
        ["Me pierdo con tantas alteraciones", "Las armaduras transportadas tienen muchas", "Practica las escalas escritas y haz el convertidor a diario"],
        ["Confundo escrita y concierto", "Uso la misma palabra para las dos", "Di siempre «escrito» o «concierto» cuando hables de una nota"]])
    + quiz("s9a", "Lees un Do en la partitura del saxo alto. ¿Qué nota suena?", ["Mi♭", "Do", "La"], 0, "El saxo alto suena una sexta mayor más grave que lo escrito: Do suena Mi♭.")
    + quiz("s9b", "El piano toca en Sol mayor. ¿En qué tonalidad escrita lees con el saxo alto?", ["Mi mayor", "Re mayor", "Si♭ mayor"], 0, "Se suman tres sostenidos: Sol (1♯) pasa a Mi (4♯).")
    + quiz("s9c", "¿Qué regla vale para pasar la armadura del piano a la del saxo alto?", ["Sumar tres sostenidos (o quitar tres bemoles)", "Restar tres sostenidos", "Ninguna: son iguales"], 0, "El saxo alto escribe una sexta mayor por encima de lo que suena.")
    + quiz("s9d", "¿Cuántos semitonos más grave suena el saxo alto respecto a lo escrito?", ["9", "3", "12"], 0, "Una sexta mayor son 9 semitonos.")
    + '<div class="summary-box"><b>Resumen:</b> el saxo alto está en Mi♭: suena una sexta mayor más grave de lo escrito. Del piano al saxo, suma tres sostenidos. Pide siempre tu parte de «saxo alto».</div>'))

# 10 -------------------------------------------------------------------------------------------------
MODULOS.append(("📈", "Escalas y arpegios", "La gimnasia diaria del saxofonista: dedos, oído, tonalidades y sonido.",
    palabras("Las escalas son la <b>gimnasia diaria</b> del saxofonista: igualan los dedos, afinan el oído y enseñan las tonalidades. Una tonalidad nueva cada semana, despacio, con metrónomo y con un sonido igual de bonito en todas las notas.")
    + """
      <h2>Escalas y arpegios</h2>
      <h3>1. ¿Para qué sirven?</h3>"""
    + lista(["<b>Dedos:</b> automatizan los movimientos que luego aparecen en las melodías.",
             "<b>Oído y afinación:</b> te enseñan cómo suenan las notas de una tonalidad.",
             "<b>Sonido:</b> cada nota debe sonar igual de limpia y conectada.",
             "<b>Lectura:</b> las melodías están hechas de escalas y arpegios."], "🎯")
    + """<h3>2. Las escalas del curso (en tono escrito)</h3>"""
    + tabla(["Escala escrita", "Armadura escrita", "Suena (concierto)", "Armadura de concierto"], [
        ["Do mayor", "Sin alteraciones", "Mi♭ mayor", "3 bemoles"],
        ["Sol mayor", "1 sostenido", "Si♭ mayor", "2 bemoles"],
        ["Fa mayor", "1 bemol", "La♭ mayor", "4 bemoles"],
        ["Re mayor", "2 sostenidos", "Fa mayor", "1 bemol"],
        ["La menor", "Sin alteraciones", "Do menor", "3 bemoles"],
        ["Mi menor", "1 sostenido", "Sol menor", "2 bemoles"],
        ["Re menor", "1 bemol", "Fa menor", "4 bemoles"]])
    + partitura("p8_sol") + partitura("p10_do") + partitura("p10_fa") + partitura("p10_re")
    + """<h3>3. Escalas menores</h3>
      <p>Tocamos la escala <b>menor natural</b>, que tiene la misma armadura que su relativa mayor y empieza por el sexto grado: La menor (relativa de Do), Mi menor (relativa de Sol) y Re menor (relativa de Fa).</p>"""
    + partitura("p10_lam") + partitura("p10_mim") + partitura("p10_rem")
    + """<h3>4. Arpegios</h3>
      <p>Un <b>arpegio</b> toca por separado las notas de un acorde: la tónica, la tercera, la quinta y la octava. Es la base de las melodías y de la improvisación.</p>"""
    + partitura("p10_arpegios")
    + """<h3>5. La escala cromática</h3>
      <p>La <b>escala cromática</b> recorre todos los semitonos. Las digitaciones de todas estas notas las has visto en el módulo 6.</p>"""
    + partitura("p10_cromatica")
    + practica("Cómo estudiar una escala (10 minutos)", [
        "<b>Una octava, nota larga a nota larga (♩ = 60):</b> escucha cada una y comprueba que sonidos y afinación son iguales.",
        "<b>Una octava ligada, subiendo y bajando (♩ = 72).</b> Toca con un solo aire, sin cortes.",
        "<b>Picada:</b> cada nota con la lengua, ritmo regular.",
        "<b>Con ritmos:</b> largo-corto y corto-largo, para igualar los dedos.",
        "<b>Con matices:</b> crescendo subiendo, diminuendo bajando.",
    ])
    + caja("Orden recomendado de las escalas:", "Sol mayor → Fa mayor → Do mayor → Re mayor → La menor → Mi menor → Re menor → cromática. Una por semana o cada dos semanas, repasando las anteriores.")
    + errores([
        ["Las notas no suenan iguales", "Los dedos van a destiempo o falta aire", "Más lento, y escucha cada nota; el aire no se detiene"],
        ["Me equivoco con las alteraciones", "No he mirado la armadura", "Antes de tocar, di en voz alta cuáles son (Fa♯, Si♭…)"],
        ["Se me «escapa» el sonido en el cambio de registro", "Falta aire en el paso Do–Re", "Practica ese paso solo, despacio, con un aire muy constante"]])
    + quiz("s10a", "¿Cuántas alteraciones tiene la escala de Re mayor (escrita)?", ["Dos sostenidos: Fa♯ y Do♯", "Un bemol", "Ninguna"], 0, "Re mayor lleva Fa♯ y Do♯.")
    + quiz("s10b", "¿Qué escala menor es la relativa de Sol mayor?", ["Mi menor", "La menor", "Re menor"], 0, "Mi menor es la relativa de Sol mayor: mismas notas, otra tónica.")
    + quiz("s10c", "¿Qué notas forman un arpegio mayor?", ["Tónica, tercera, quinta y octava", "Todas las de la escala", "Tónica y segunda"], 0, "Es el acorde mayor desplegado.")
    + '<div class="summary-box"><b>Resumen:</b> una escala nueva por semana, despacio y con metrónomo, ligada, picada y con ritmos. Arpegios y cromática completan la rutina.</div>'))

# 11 -------------------------------------------------------------------------------------------------
MODULOS.append(("🥁", "Ritmo, compases y fraseo", "Pulso, compás, figuras, silencios, síncopa y dónde respirar.",
    palabras("Primero es el <b>pulso</b>: el latido constante que marcas con el pie. El ritmo se coloca encima. Y la música se divide en <b>frases</b> como un texto: respira donde acaba una, no a mitad.")
    + """
      <h2>El ritmo</h2>
      <h3>1. Pulso, ritmo, compás y tempo</h3>"""
    + tabla(["Palabra", "Qué es", "Ejemplo"], [
        ["<b>Pulso</b>", "El «latido» constante de la música; el que marcas con el pie", "Tic, tic, tic, tic…"],
        ["<b>Ritmo</b>", "El dibujo de notas largas y cortas sobre el pulso", "Larga-corta-corta-larga"],
        ["<b>Compás</b>", "El grupo de pulsos que se repite, con el primero más fuerte", "UNO-dos-tres UNO-dos-tres"],
        ["<b>Tempo</b>", "La velocidad del pulso, en pulsos por minuto (bpm)", "♩ = 80"]])
    + """<h3>2. El compás</h3>
      <p>El número de arriba indica <b>cuántos pulsos</b> hay en cada compás. El de abajo indica <b>qué figura es un pulso</b>: 4 = negra, 8 = corchea.</p>"""
    + tabla(["Compás", "Cómo se cuenta", "Dónde lo oyes"], [
        ["2/4", "UNO-dos", "Marchas, sambas"],
        ["3/4", "UNO-dos-tres", "Valses"],
        ["4/4", "UNO-dos-tres-cuatro", "La mayoría de la música"],
        ["6/8", "UNO-dos-tres CUATRO-cinco-seis (dos pulsos de tres)", "Baladas y danzas"]])
    + """<h3>3. Las figuras y los silencios</h3>"""
    + tabla(["Figura", "Dura (en negras)", "Cómo se cuenta"], [
        ["Redonda", "4", "1-2-3-4"], ["Blanca", "2", "1-2"], ["Negra", "1", "1"],
        ["Corchea", "½", "«1-y»: dos por pulso"],
        ["Negra con puntillo", "1½", "1-2-3 (en corcheas) y la siguiente en la «y»"],
        ["Silencios", "Igual que la figura", "Se cuentan con el pulso, sin sonar"]])
    + partitura("p11_pulso") + partitura("p11_corcheas") + partitura("p11_puntillo") + partitura("p11_sincopa")
    + """<h3>4. 3/4 y 6/8</h3>"""
    + partitura("p11_vals") + partitura("p11_68")
    + """<h3>5. El metrónomo</h3>
      <p>El metrónomo marca el pulso. Úsalo siempre al estudiar: empieza despacio y sube el tempo poco a poco.</p>
      <div class="activity"><div class="metro">
        <label>Compás: <select id="met-comp" onchange="metroPintar()"><option value="2">2/4</option><option value="3">3/4</option><option value="4" selected>4/4</option><option value="6">6/8</option></select></label>
        <label>Tempo: <input type="range" id="met-bpm" min="40" max="160" value="72" oninput="metroBpm(this.value)"> <b id="met-val">72</b> bpm</label>
        <button class="btn" id="met-btn" onclick="metroToggle()">▶ Iniciar</button></div><div class="beats" id="met-beats"></div></div>
      <h3>6. Las frases y las respiraciones</h3>
      <p>Una melodía se divide en <b>frases</b>, como las oraciones de un texto. Una frase suele durar 2 o 4 compases. En un instrumento de viento hay que respirar, y conviene hacerlo <b>entre frases</b>, en un silencio o en una nota larga, y nunca a mitad de una frase.</p>"""
    + partitura("p11_frase")
    + pasos([
        ("Canta la melodía.", "donde necesitas respirar para cantarla, probablemente termina una frase."),
        ("Marca la respiración con una coma (’) en la partitura.", "al final de cada frase, normalmente tras una nota larga o un silencio."),
        ("Toca respirando donde pone la coma.", "toma aire rápido y sin ruido, sin romper el pulso: el tiempo de la respiración se quita al valor de la última nota."),
    ])
    + errores([
        ["Corro en los pasajes fáciles", "No uso metrónomo", "Estudia con metrónomo y sube de 4 en 4 bpm"],
        ["Acorto los silencios", "Parece que no hay nada que hacer", "Cuéntalos en voz alta y marca el pulso con el pie"],
        ["Respiro a mitad de frase", "No he planificado dónde respirar", "Marca las respiraciones en la partitura antes de tocar"]])
    + quiz("s11a", "¿Cuántos pulsos se sienten en un compás de 6/8?", ["Dos (de tres corcheas cada uno)", "Seis", "Tres"], 0, "6/8 se siente en dos pulsos de tres corcheas.")
    + quiz("s11b", "¿Cuánto dura una negra con puntillo?", ["1½ tiempos", "2 tiempos", "1 tiempo"], 0, "El puntillo añade la mitad: 1 + ½.")
    + quiz("s11c", "¿Dónde conviene respirar?", ["Entre frases, en un silencio o nota larga", "Siempre a mitad de compás", "Cuando se acaba el aire, aunque sea en medio de la frase"], 0, "La respiración debe respetar la frase.")
    + '<div class="summary-box"><b>Resumen:</b> primero el pulso (con el pie y el metrónomo), luego el ritmo; respira entre frases y cuenta los silencios.</div>'))

# 12 -------------------------------------------------------------------------------------------------
MODULOS.append(("📏", "Sonido y afinación", "Cómo conseguir un sonido bonito y estable y cómo afinar tu saxo.",
    palabras("Un buen sonido es <b>redondo, estable y sin ruidos</b>: se trabaja con notas largas y con un aire constante. La afinación se ajusta moviendo la boquilla: <b>si estás alto, saca la boquilla; si estás bajo, métela</b>.")
    + """
      <h2>El sonido y la afinación</h2>
      <h3>1. Qué es un buen sonido</h3>"""
    + lista(["<b>Redondo y lleno:</b> con cuerpo, sin sonar «delgado» ni «áspero».",
             "<b>Estable:</b> la altura y el volumen no tiemblan durante la nota.",
             "<b>Limpio:</b> sin ruido de aire ni chirridos.",
             "<b>Parecido en todo el registro:</b> las notas graves y agudas suenan como del mismo saxo."], "🎷")
    + """<h3>2. Cómo se trabaja el sonido</h3>"""
    + partitura("p12_largas")
    + pasos([
        ("Haz notas largas cada día (5 minutos).", "elige una nota fácil (Sol, La, Si) y mantenla 8 tiempos. Escucha cómo suena al principio, en medio y al final."),
        ("Aire cálido y constante.", "sopla como si empañaras un cristal, no como si apagaras una vela; la garganta abierta, como al bostezar."),
        ("Grábate y escúchate.", "la grabación dice la verdad: ¿se oyen ruidos?, ¿tiembla el sonido?"),
        ("Imita.", "escucha a un saxofonista que te guste e intenta acercarte a su sonido."),
        ("Crescendos y diminuendos.", "crece sin morder y baja sin que se te caiga la afinación."),
    ])
    + como("La <b>garganta abierta</b> es clave: di «oh» o bosteza con la boca cerrada. Una garganta cerrada da un sonido pequeño y estrangulado.")
    + """<h3>3. El vibrato (de momento, solo como idea)</h3>
      <p>El <b>vibrato</b> es una pequeña oscilación regular de la altura de la nota, que se consigue con un suave movimiento de la mandíbula inferior. Es un recurso expresivo avanzado: no lo uses hasta que tu sonido sea estable. Lo trabajarás con un profesor/a.</p>
      <h3>4. La afinación</h3>
      <p>Afinar es hacer que tu instrumento suene a la misma altura que los demás. El estándar es <b>La = 440 Hz</b> (a veces 442). Como el saxo alto es un instrumento en Mi♭, lo que tú lees como <b>Fa♯ (Fa♯5)</b> suena <b>La</b> (440 Hz). También puedes afinar con tu Sol (escrito), que suena Si♭.</p>"""
    + partitura("p12_afinacion")
    + pasos([
        ("Calienta el instrumento.", "toca unos minutos antes de afinar: el aire caliente sube la afinación."),
        ("Toca el Fa♯ (La de concierto) largo y firme.", "no lo ajustes con la boca: toca con la misma embocadura de siempre."),
        ("Compara con la referencia.", "con el tono de referencia o con un afinador."),
        ("Ajusta la boquilla.", "si estás alto, saca la boquilla un poco; si estás bajo, métela un poco."),
        ("Comprueba otras notas.", "toca Sol, Mi y Si para ver si sigues afinado."),
    ])
    + """<h3>5. Herramientas</h3>
      <h4>Tono de referencia</h4>
      <div class="activity"><label>Referencia: <select id="af-ref"><option value="440" selected>La = 440 Hz</option><option value="442">La = 442 Hz</option></select></label>
        <div class="lect-btns"><button onclick="tonoRef('Fa♯5')">Fa♯ escrito (La concierto)</button><button onclick="tonoRef('Sol5')">Sol escrito (Si♭ concierto)</button><button onclick="tonoRef('Sol4')">Sol4</button><button onclick="tonoRef('Re4')">Re4</button><button onclick="tonoRef('Mi4')">Mi4</button><button onclick="tonoRef('Si4')">Si4</button><button onclick="tonoParar()">■ Parar</button></div>
        <p class="feedback" id="tono-msg"></p></div>
      <h4>Afinador con micrófono</h4>
      <p>Toca una nota larga: el afinador te dice qué nota escrita tocas y si estás alto o bajo. Funciona si el navegador te deja usar el micrófono (dentro de algunas plataformas puede estar bloqueado).</p>
      <div class="activity"><button class="btn" id="af-btn" onclick="afIniciar()">🎤 Activar el afinador</button>
        <div style="text-align:center;margin:14px 0"><div id="af-nota" style="font-size:3em;font-weight:700;color:#6b3f0e">—</div>
        <div id="af-conc" style="color:#555"></div>
        <div style="position:relative;height:18px;background:linear-gradient(90deg,#f4b6b6,#a5d6a7 45%,#a5d6a7 55%,#f4b6b6);border-radius:9px;margin:12px auto;max-width:360px"><div id="af-aguja" style="position:absolute;left:50%;top:-4px;width:4px;height:26px;background:#3b2410;border-radius:2px"></div></div>
        <div id="af-cents" style="font-weight:700"></div></div><p class="feedback" id="af-msg"></p></div>
      <h3>6. Tendencias de afinación</h3>"""
    + lista(["Las notas <b>agudas</b> tienden a subir si se muerde: relaja la embocadura.",
             "Las notas <b>graves</b> tienden a quedar bajas si se sopla flojo: apoya con aire.",
             "El instrumento frío está bajo y el caliente, alto.",
             "El Do♯ y el Fa♯ suelen necesitar un pequeño ajuste con el aire y la garganta."], "📌")
    + errores([
        ["Estoy alto en todas las notas", "La boquilla está demasiado metida o muerdo", "Saca un poco la boquilla y relaja la embocadura"],
        ["Estoy bajo en todas las notas", "La boquilla está demasiado sacada o soplo flojo", "Mete un poco la boquilla y apoya con aire"],
        ["El sonido tiembla", "Poca presión del aire o falta de apoyo", "Notas largas con aire constante"],
        ["El afinador no detecta nada", "Hay ruido de fondo o estás lejos", "Acércate al micrófono, toca más fuerte y repite en un lugar silencioso"]])
    + quiz("s12a", "Estás tocando más alto que el La de referencia. ¿Qué haces?", ["Sacar un poco la boquilla", "Meter la boquilla", "Morder más"], 0, "Al sacar la boquilla el tubo se alarga y la nota baja.")
    + quiz("s12b", "¿Qué nota escrita da el La (440 Hz) de concierto con el saxo alto?", ["Fa♯", "La", "Do"], 0, "Sube una sexta mayor: La → Fa♯.")
    + quiz("s12c", "¿Qué se trabaja con las notas largas?", ["El sonido: estabilidad, redondez y afinación", "La velocidad", "El vibrato"], 0, "Las notas largas son el ejercicio básico del sonido.")
    + '<div class="summary-box"><b>Resumen:</b> notas largas con aire cálido y garganta abierta; afina con el Fa♯ escrito (La 440); si estás alto, saca la boquilla; si estás bajo, métela.</div>'))

# 13 -------------------------------------------------------------------------------------------------
MODULOS.append(("🎼", "Repertorio y tocar con otros", "Cómo estudiar una pieza, melodías con acompañamiento y tocar en grupo.",
    palabras("Estudiar una pieza es <b>entenderla y dividirla</b>: escúchala, marca las frases, trabaja por trozos cortos y vuelve a unirlos. Tocar con otros es escuchar, respirar juntos y mantener el pulso.")
    + """
      <h2>Tocar música</h2>
      <h3>1. Cómo se estudia una pieza</h3>"""
    + pasos([
        ("Escúchala y cántala.", "escucha la grabación (o el audio de la partitura) y canta la melodía. Si no puedes cantarla, aún no la conoces."),
        ("Analiza la partitura.", "tonalidad (armadura), compás, tempo y figuras raras. Marca las alteraciones y los pasos difíciles con lápiz."),
        ("Marca las respiraciones.", "una coma (’) al final de cada frase, normalmente en una nota larga o un silencio."),
        ("Trabaja por trozos de 2 compases.", "con metrónomo a una velocidad en la que no falles. Sube 4 bpm cuando salga tres veces seguidas sin errores."),
        ("Une los trozos y toca de principio a fin.", "sin parar aunque falles, para sentir la pieza entera."),
        ("Grábate y evalúa.", "escucha con la partitura: ¿se oyen los matices?, ¿las frases?, ¿el pulso?"),
    ])
    + """<h3>2. Cuatro piezas del curso con acompañamiento</h3>
      <p>Cada partitura tiene un selector de sonido: <b>Saxo + acompañamiento</b> (escuchas cómo suena), <b>Solo saxo</b> y <b>Solo acompañamiento</b> (para tocar tú encima).</p>"""
    + partitura("r_frere") + partitura("r_marcha") + partitura("r_balada") + partitura("r_samba")
    + caja("Tocar con el acompañamiento:", "primero toca la melodía sin acompañamiento hasta que salga. Después, a la mitad de velocidad con el acompañamiento. Cuando salga, sube al 75 % y al 100 %.")
    + """<h3>3. Tocar en grupo</h3>"""
    + lista(["<b>Escucha:</b> intenta oír a los demás más que a ti mismo.",
             "<b>Afinad juntos</b> antes de empezar, con la misma referencia.",
             "<b>Respirad juntos</b> antes de entrar: el director o el primer músico da la entrada con la respiración.",
             "<b>Cuenta los compases de silencio:</b> si no, entrarás tarde o pronto.",
             "<b>Mira al director</b> o al líder del grupo, sobre todo en los finales y los cambios de tempo.",
             "<b>Equilibra:</b> cuando acompañas, toca más suave que quien lleva la melodía."], "👥")
    + """<h3>4. Dónde conseguir partituras</h3>"""
    + lista(["<b>Métodos</b> para saxofón (Essential Elements, Rubank, Hal Leonard…): piezas graduadas, con audio.",
             "<b>IMSLP</b> (imslp.org): partituras de dominio público; busca «saxophone» o «alto saxophone».",
             "<b>Música de tu profesor/a:</b> la mejor opción al empezar.",
             "<b>Canciones que te gusten</b>, en su versión para saxo alto en Mi♭ o transportadas por ti."], "📚")
    + """<h3>5. Los nervios</h3>
      <p>Tocar delante de otras personas pone nerviosos a casi todos. Se reduce con la costumbre: toca para un amigo, para la familia, graba un vídeo… Respira hondo antes de entrar, piensa en el pulso del primer compás y no pares aunque falles.</p>"""
    + errores([
        ["Me pierdo en la pieza", "Hay trozos que no domino", "Trabaja por trozos de 2 compases y marca dónde empiezan las frases"],
        ["El acompañamiento me despista", "Voy deprisa o despacio respecto al pulso", "Practica con metrónomo y luego baja el tempo del acompañamiento al 50 %"],
        ["Entro tarde", "No cuento los silencios", "Cuenta en voz alta y marca el pulso con el pie"]])
    + quiz("s13a", "¿Qué es lo primero que debes hacer con una pieza nueva?", ["Escucharla y analizarla", "Tocarla a tempo desde el primer día", "Memorizarla sin leer"], 0, "Conocer la pieza ahorra mucho tiempo de estudio.")
    + quiz("s13b", "¿Cuándo se sube el tempo del metrónomo?", ["Cuando sale tres veces seguidas sin errores", "Cada cinco minutos", "Nunca"], 0, "Se sube poco a poco cuando el tempo actual está dominado.")
    + quiz("s13c", "Tocas en un grupo y haces de acompañamiento. ¿Qué debes hacer?", ["Tocar más suave que quien lleva la melodía", "Tocar más fuerte", "Tocar más rápido"], 0, "El acompañamiento está al servicio de la melodía.")
    + '<div class="summary-box"><b>Resumen:</b> escucha, analiza, marca las frases, trabaja por trozos, une y grábate. En grupo: escucha, afina, respira juntos y cuenta los silencios.</div>'))

# 14 -------------------------------------------------------------------------------------------------
MODULOS.append(("🎷", "Jazz, blues e improvisación", "Swing, escala de blues, primeras improvisaciones y los siguientes pasos.",
    palabras("Improvisar es <b>conversar con notas</b>: frases cortas, silencios, preguntas y respuestas. Con la <b>escala de blues</b> y un ritmo claro ya puedes hacer música, aunque solo uses tres notas.")
    + """
      <h2>Jazz y blues</h2>
      <h3>1. El swing</h3>
      <p>En el jazz, las corcheas no suenan iguales sino <b>desiguales</b>: la primera es más larga y la segunda más corta, como en un tresillo en el que las dos primeras notas van unidas. Se escriben iguales, pero se tocan «largo-corto». Escucha la grabación y fíjate en el balanceo.</p>"""
    + partitura("p14_swing")
    + lista(["<b>Acentos en el 2 y el 4:</b> el «chasquido» del jazz cae en los tiempos débiles.",
             "<b>Articulación suave:</b> las corcheas se ligan ligeramente (con «du» más que con «tu») y la última se acentúa.",
             "<b>Escucha mucho:</b> el swing no se aprende por escrito."], "🎵")
    + """<h3>2. El blues de 12 compases</h3>
      <p>El blues es una forma de <b>doce compases</b> sobre tres acordes. En la partitura de saxo alto, los acordes están transportados: «A7» suena Do7, «D7» suena Fa7 y «E7» suena Sol7.</p>"""
    + tabla(["Compases", "Acordes (escritos)", "Suenan (concierto)"], [
        ["1-4", "A7 · A7 · A7 · A7", "C7"],
        ["5-6", "D7 · D7", "F7"],
        ["7-8", "A7 · A7", "C7"],
        ["9", "E7", "G7"],
        ["10", "D7", "F7"],
        ["11-12", "A7 · E7", "C7 · G7"]])
    + partitura("p14_blues")
    + """<h3>3. La escala de blues</h3>
      <p>La <b>escala de blues</b> es la base de la improvisación. Se forma con una pentatónica menor más una nota de paso, la <b>«nota azul»</b>. Escrita en La, suena en Do de concierto: <b>La – Do – Re – Mi♭ – Mi – Sol</b> (el Mi♭ es la nota azul).</p>"""
    + partitura("p14_escala")
    + caja("La nota azul:", "el Mi♭ (Mi♭5 en la partitura) se toca con los seis dedos más la llave de Mi♭ del meñique derecho y la llave de octava. Es la nota que «no encaja» del todo, y por eso da el color del blues. Se suele deslizar hacia el Mi.")
    + """<h3>4. Cómo improvisar: cinco pasos</h3>"""
    + pasos([
        ("Aprende la escala de blues.", "tócala despacio, subiendo y bajando, hasta que salga sin pensar."),
        ("Empieza con tres notas.", "elige La, Do y Re y toca frases de dos compases con distintos ritmos. Las limitaciones liberan."),
        ("Pregunta y respuesta.", "una frase de dos compases que «pregunta» y otra que «responde», como en una conversación."),
        ("Deja silencios.", "los espacios dan sentido a las frases. Si tocas sin parar, nadie entiende la conversación."),
        ("Repite y varía.", "toca una idea dos veces y cambia el final: suena intencionado."),
    ])
    + partitura("p14_pregunta")
    + como("Toca con el acompañamiento de «Solo acompañamiento» y empieza con una sola nota larga. Después añade un ritmo repetido y, por último, la pregunta y la respuesta. Grábate para elegir tu mejor frase.")
    + """<h3>5. Aprender de oído</h3>
      <p>Los saxofonistas de jazz aprenden <b>imitando</b>. Elige una frase corta de un solista que te guste, escúchala una y otra vez, cántala y búscala en el saxo. Así se aprenden los giros del lenguaje.</p>
      <h3>6. Siguientes pasos</h3>"""
    + lista(["<b>Un/a profesor/a:</b> corrige la técnica y te propone repertorio.",
             "<b>Una banda o agrupación:</b> tocar con otros es lo que más enseña.",
             "<b>Vibrato y matices:</b> cuando tengas un sonido estable.",
             "<b>Notas agudas (altísimo) y llaves de la palma:</b> con un profesor/a.",
             "<b>Otros saxos:</b> con lo que sabes, pasar al soprano o al tenor es cuestión de adaptarse.",
             "<b>Teoría y armonía:</b> acordes, escalas y modos para improvisar con más libertad."], "🚀")
    + errores([
        ["Toco notas sin dirección", "No hay un plan para la frase", "Piensa en frases cortas, con principio, desarrollo y final"],
        ["Mi swing suena a corcheas iguales", "No he escuchado suficiente jazz", "Escucha, canta el balanceo y toca despacio al principio"],
        ["Me bloqueo al improvisar", "Demasiadas opciones", "Limítate a tres notas y juega solo con el ritmo"]])
    + quiz("s14a", "¿Qué es la nota azul de la escala de blues?", ["La nota de paso que da color: el Mi♭ en la escala de La (escrita)", "La nota más aguda", "La tónica"], 0, "El Mi♭ es la nota que no encaja del todo y da el sabor del blues.")
    + quiz("s14b", "¿Cuántos compases tiene la forma básica del blues?", ["12", "8", "16"], 0, "El blues clásico es de 12 compases.")
    + quiz("s14c", "Escrito A7, ¿qué acorde suena de concierto?", ["C7", "A7", "E♭7"], 0, "El saxo alto suena una sexta mayor más grave: La → Do.")
    + actividad("Tu primer solo", "Graba un coro de blues (12 compases) con las tres notas La, Do y Re sobre el acompañamiento del blues y escribe qué frase te ha gustado más.", "Me ha gustado…")
    + '<div class="summary-box"><b>¡Enhorabuena!</b> Has completado los 14 módulos. Revisa la página de ejercicios y el planning de 6 meses, y haz el examen final.</div>'))
