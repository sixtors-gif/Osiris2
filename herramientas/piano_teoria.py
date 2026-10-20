"""Teoría musical a fondo para el curso de piano: notas faro, intervalos, círculo de quintas y tonalidad.

TEORIA[n] = (marcador, html): el generador inserta el html del módulo n justo antes de la primera
aparición de «marcador» en la página. Además de los marcadores de piano_explicaciones.py
([[partitura:clave]] y [[fig:archivo|alt|pie]]) se usa:
  [[quiz:id|pregunta|opción A;opción B;opción C|índice correcto|explicación]]
"""
from piano_explicaciones import caja, errores, lista, pasos, tabla

TEORIA = {}

# Módulo 2 · Notas faro e intervalos ----------------------------------------------------------------
TEORIA[2] = ('<h3>2. Entrenador de lectura</h3>', (
    "<h3>Las notas faro, a fondo</h3>"
    "<p>Piensa en un barco de noche: el capitán no conoce cada roca de la costa, pero sí sabe dónde están los <b>faros</b>, y desde ellos calcula su posición. En el pentagrama pasa lo mismo: si te sabes de memoria unas pocas notas bien repartidas, <b>ninguna nota estará a más de dos pasos de un faro</b> y podrás leerla en un instante, sin contar líneas desde abajo.</p>"
    "[[partitura:faros_sol]]"
    "[[partitura:faros_fa]]"
    + caja("El Do central es el puente entre las dos claves:", "Do4 se escribe en la 1.ª línea adicional <b>por debajo</b> de la clave de Sol y en la 1.ª línea adicional <b>por encima</b> de la clave de Fa. En el piano es la misma tecla, la que tienes delante del ombligo, a la izquierda del grupo de dos teclas negras.")
    + "<h3>Trucos para recordar los faros</h3>"
    + tabla(["Truco", "Clave de Sol", "Clave de Fa"], [
        ["La clave «señala» su nota", "La espiral se enrosca en la <b>2.ª línea</b>: ahí está <b>Sol4</b>", "Los dos puntos rodean la <b>4.ª línea</b>: ahí está <b>Fa3</b>"],
        ["Las cinco líneas, de abajo arriba", "Mi – Sol – Si – Re – Fa", "Sol – Si – Re – Fa – La"],
        ["Los cuatro espacios, de abajo arriba", "Fa – La – Do – Mi", "La – Do – Mi – Sol"],
        ["La «escalera» de los Do", "Do4 (1.ª adicional abajo), Do5 (3.er espacio), Do6 (2.ª adicional arriba)", "Do2 (2.ª adicional abajo), Do3 (2.º espacio), Do4 (1.ª adicional arriba)"]])
    + "<p>Fíjate en la escalera de los Do: de un Do al siguiente hay una octava, y en el pentagrama una octava siempre va de <b>línea a espacio</b> (o de espacio a línea), saltando tres líneas. Si reconoces un Do, reconoces todos.</p>"
    + "<h3>Cómo calcular cualquier nota desde un faro</h3>"
    + pasos([
        ("Busca el faro más cercano.",
         "mira si la nota está en una línea o en un espacio y cuántas líneas la separan del faro más próximo. Elige el que esté a uno o dos pasos, no el que te sepas mejor."),
        ("Cuenta los pasos desde el faro.",
         "cada salto de una línea al espacio de al lado (o de un espacio a la línea de al lado) es <b>un paso = una nota</b>. Hacia arriba recita Do, Re, Mi, Fa, Sol, La, Si; hacia abajo, al revés."),
        ("Usa los atajos de intervalo.",
         "de una línea a la línea siguiente (o de un espacio al siguiente) hay siempre <b>dos pasos: una 3.ª</b>. Así no cuentas nota a nota: «4.ª línea en clave de Sol = una 3.ª por debajo de Fa5 = Re5»."),
        ("Mira la armadura antes de tocar.",
         "si el nombre de la nota está en la armadura (por ejemplo, Fa en Sol mayor), la nota es Fa♯ aunque no lleve el sostenido delante. Las alteraciones accidentales duran hasta la barra de compás."),
    ])
    + tabla(["Ves una nota en…", "Faro más cercano", "Cálculo", "Es"], [
        ["Clave de Sol, 4.ª línea", "Fa5 (5.ª línea)", "Una línea más abajo = una 3.ª abajo", "<b>Re5</b>"],
        ["Clave de Sol, 1.er espacio", "Mi4 (1.ª línea)", "Un paso arriba", "<b>Fa4</b>"],
        ["Clave de Sol, 3.ª línea", "Sol4 (2.ª línea)", "Una línea más arriba = una 3.ª arriba", "<b>Si4</b>"],
        ["Clave de Sol, 4.º espacio", "Fa5 (5.ª línea)", "Un paso abajo", "<b>Mi5</b>"],
        ["Clave de Fa, 3.ª línea", "Fa3 (4.ª línea)", "Una línea más abajo = una 3.ª abajo", "<b>Re3</b>"],
        ["Clave de Fa, 1.er espacio", "Sol2 (1.ª línea)", "Un paso arriba", "<b>La2</b>"],
        ["Clave de Fa, 4.º espacio", "La3 (5.ª línea)", "Un paso abajo", "<b>Sol3</b>"],
        ["Clave de Fa, 1.ª línea adicional abajo", "Sol2 (1.ª línea)", "Una línea más abajo = una 3.ª abajo", "<b>Mi2</b>"]])
    + "[[quiz:t2a|En clave de Sol, una nota está en la 4.ª línea. Usando el faro Fa5 (5.ª línea), ¿qué nota es?|Mi5;Re5;Si4|1|De la 5.ª línea a la 4.ª hay una 3.ª: Fa, Mi, Re → Re5.]]"
    "[[quiz:t2b|En clave de Fa, una nota está en el 2.º espacio. ¿Cuál es?|Do3;Si2;Mi3|0|Es uno de los faros de la clave de Fa: Do3, en el 2.º espacio.]]"

    "<h3>Los intervalos, a fondo</h3>"
    "<p>Un <b>intervalo</b> es la distancia entre dos notas. Tiene dos «apellidos»: un <b>número</b> (2.ª, 3.ª, 4.ª…) que dice cuántas notas abarca, y una <b>calidad</b> (mayor, menor, justa…) que dice cuántos semitonos exactos tiene.</p>"
    + "<h4>1. El número: cuenta los nombres de nota, incluidos los dos extremos</h4>"
    "<p>De Do a Mi: Do (1), Re (2), Mi (3) → <b>3.ª</b>. De Re a La: Re, Mi, Fa, Sol, La → <b>5.ª</b>. El error típico es no contar la primera nota: recuerda que una nota consigo misma es un «unísono» (1.ª), no un 0.</p>"
    + tabla(["Intervalo", "Dibujo en el pentagrama", "Ejemplo desde Do4"], [
        ["2.ª", "De una línea al espacio de al lado", "Do – Re"],
        ["3.ª", "De una línea a la línea siguiente", "Do – Mi"],
        ["4.ª", "De línea a espacio, saltando una línea", "Do – Fa"],
        ["5.ª", "De línea a línea, saltando una línea", "Do – Sol"],
        ["6.ª", "De línea a espacio, saltando dos líneas", "Do – La"],
        ["7.ª", "De línea a línea, saltando dos líneas", "Do – Si"],
        ["8.ª (octava)", "De línea a espacio, saltando tres líneas", "Do – Do"]])
    + caja("La regla de los impares:", "3.ª, 5.ª y 7.ª unen siempre <b>línea con línea</b> o <b>espacio con espacio</b>; 2.ª, 4.ª, 6.ª y 8.ª unen línea con espacio. Con solo ver si las dos notas son «del mismo tipo» ya sabes si el intervalo es par o impar.")
    + "[[partitura:intervalos]]"
    + "<h4>2. El «apellido»: justa, mayor, menor, aumentada y disminuida</h4>"
    "<p>El número no basta. Mira estas dos 3.as: <b>Do–Mi</b> y <b>Re–Fa</b>. Las dos abarcan tres nombres de nota y en el pentagrama tienen el mismo dibujo (de línea a línea), pero en el teclado <b>no miden lo mismo</b>: de Do a Mi hay 4 semitonos y de Re a Fa solo 3. ¿Por qué? Porque las teclas blancas no están a la misma distancia: entre Mi–Fa y Si–Do no hay tecla negra, son semitonos. Según qué tramo del teclado «pise» un intervalo, sale más grande o más pequeño.</p>"
    "<p>Por eso cada intervalo lleva, además del número, un <b>apellido</b> que dice su tamaño exacto en semitonos. Es como decir «una calle» (el número) y «el portal exacto» (el apellido).</p>"
    + tabla(["Apellido", "Qué quiere decir", "Cómo suena"], [
        ["<b>Justa</b>", "El tamaño «normal» de la 4.ª, la 5.ª y la 8.ª (y del unísono). Estos intervalos solo tienen un tamaño normal, ni grande ni pequeño", "Estable, «hueco», abierto: las campanas, las trompas, las quintas de una guitarra"],
        ["<b>Mayor</b>", "El tamaño grande de la 2.ª, la 3.ª, la 6.ª y la 7.ª", "Luminoso, abierto (la 3.ª mayor es la del acorde mayor)"],
        ["<b>Menor</b>", "El tamaño pequeño de la 2.ª, la 3.ª, la 6.ª y la 7.ª: <b>un semitono menos que la mayor</b>", "Más oscuro, más íntimo o melancólico"],
        ["<b>Aumentada</b>", "Un semitono <b>más</b> que la justa o que la mayor: el intervalo «se ha estirado»", "Tenso, inestable: pide abrirse todavía más"],
        ["<b>Disminuida</b>", "Un semitono <b>menos</b> que la justa o que la menor: el intervalo «se ha encogido»", "Tenso, inestable: pide cerrarse"]])
    + caja("¿Por qué «justa»?", "Porque la 4.ª, la 5.ª y la 8.ª suenan tan «limpias» y estables que desde la Edad Media se consideraron las consonancias perfectas (en inglés se llaman <i>perfect</i>). Además, son las mismas en las escalas mayores y en las menores: Do–Sol es una 5.ª justa tanto en Do mayor como en Do menor. Como no hay una versión «mayor» y otra «menor», se les da un nombre propio: justas. Por eso <b>nunca existe una «5.ª mayor» ni una «3.ª justa»</b>.")
    + "<p>Todo se resume en dos familias, como dos escaleras en las que cada peldaño es <b>un semitono</b>:</p>"
    + "[[fig:calidades_intervalos.svg|Las dos familias de intervalos: justos (disminuida, justa, aumentada) y mayores/menores (disminuida, menor, mayor, aumentada)|Cada peldaño es un semitono. Los justos tienen un solo tamaño normal; los mayores y menores, dos.]]"
    + tabla(["Intervalo", "Familia", "Disminuida", "Menor", "Mayor", "Justa", "Aumentada"], [
        ["2.ª", "Mayor / menor", "0 (Mi–Fa♭, rarísima)", "1 (Mi–Fa)", "2 (Do–Re)", "—", "3 (Do–Re♯)"],
        ["3.ª", "Mayor / menor", "2 (Do♯–Mi♭)", "3 (Re–Fa)", "4 (Do–Mi)", "—", "5 (Do–Mi♯)"],
        ["4.ª", "Justa", "4 (Do♯–Fa)", "—", "—", "5 (Do–Fa)", "6 (Fa–Si)"],
        ["5.ª", "Justa", "6 (Si–Fa)", "—", "—", "7 (Do–Sol)", "8 (Do–Sol♯)"],
        ["6.ª", "Mayor / menor", "7 (Do♯–La♭)", "8 (Mi–Do)", "9 (Do–La)", "—", "10 (Do–La♯)"],
        ["7.ª", "Mayor / menor", "9 (Do♯–Si♭)", "10 (Re–Do)", "11 (Do–Si)", "—", "12 (Do–Si♯)"],
        ["8.ª", "Justa", "11 (Do♯–Do)", "—", "—", "12 (Do–Do)", "13 (Do–Do♯)"]])
    + "<p class=\"small\">Los números son semitonos. Las casillas con «—» no existen: una 4.ª nunca es mayor y una 3.ª nunca es justa. La 2.ª disminuida casi no se usa: suena igual que una nota repetida.</p>"
    + "<p>Escúchalo: cada compás toca el intervalo nota a nota y después las dos notas a la vez. Compara la 3.ª mayor con la menor y la 5.ª justa con sus versiones estirada y encogida.</p>"
    "[[partitura:calidades]]"
    + "<h4>Mismo sonido, distinto nombre</h4>"
    "<p>Do–Fa♯ y Do–Sol♭ son <b>la misma tecla</b> y miden lo mismo (6 semitonos), pero no se llaman igual. Do–Fa♯ es una <b>4.ª aumentada</b> (Do, Re, Mi, Fa: cuatro nombres) y Do–Sol♭ una <b>5.ª disminuida</b> (Do, Re, Mi, Fa, Sol: cinco nombres). El nombre depende de <b>cómo está escrita</b> la nota, no solo de cómo suena. Por eso el orden para nombrar un intervalo es siempre: primero el número (los nombres de nota), después el apellido (los semitonos).</p>"
    + caja("El tritono:", "la 4.ª aumentada y la 5.ª disminuida miden 6 semitonos, tres tonos: por eso se llaman <b>tritono</b>. Es justo la mitad de la octava y el intervalo más inestable de todos; en la Edad Media lo apodaban <i>diabolus in musica</i>. Entre teclas blancas solo aparece en <b>Fa–Si</b> (4.ª aumentada) y <b>Si–Fa</b> (5.ª disminuida), y es lo que da tensión al acorde de dominante Sol7 (Si y Fa).")
    + "<h4>Cómo ponerle nombre a cualquier intervalo</h4>"
    + pasos([
        ("Pon el número: cuenta los nombres de nota, sin mirar las alteraciones.",
         "ignora de momento los ♯ y ♭: Re–Fa♯ es «Re, Mi, Fa» = 3.ª. Mi–Si♭ es «Mi, Fa, Sol, La, Si» = 5.ª."),
        ("Mira a qué familia pertenece.",
         "4.ª, 5.ª y 8.ª (y el unísono) son de la familia de las <b>justas</b>; 2.ª, 3.ª, 6.ª y 7.ª, de la familia de las <b>mayores y menores</b>."),
        ("Cuenta los semitonos en el teclado.",
         "pon un dedo en la nota de abajo y avanza tecla a tecla (blancas y negras) hasta la de arriba, contando cada paso. Re → Re♯ → Mi → Fa → Fa♯ = 4 semitonos."),
        ("Compara con la tabla y elige el apellido.",
         "busca en la fila de su número la casilla con esos semitonos. 3.ª con 4 semitonos = <b>3.ª mayor</b>. 5.ª con 6 semitonos = un semitono menos que la justa (7) = <b>5.ª disminuida</b>."),
    ])
    + tabla(["Intervalo", "Número", "Semitonos", "Nombre completo"], [
        ["Re – Fa♯", "Re, Mi, Fa → 3.ª", "4", "<b>3.ª mayor</b>"],
        ["La – Do", "La, Si, Do → 3.ª", "3", "<b>3.ª menor</b>"],
        ["Mi – La", "Mi, Fa, Sol, La → 4.ª", "5", "<b>4.ª justa</b>"],
        ["Fa – Si", "Fa, Sol, La, Si → 4.ª", "6", "<b>4.ª aumentada</b> (tritono)"],
        ["Mi – Si♭", "Mi, Fa, Sol, La, Si → 5.ª", "6", "<b>5.ª disminuida</b> (tritono)"],
        ["Do – Sol♯", "Do, Re, Mi, Fa, Sol → 5.ª", "8", "<b>5.ª aumentada</b>"],
        ["La – Fa", "La, Si, Do, Re, Mi, Fa → 6.ª", "8", "<b>6.ª menor</b>"],
        ["Sol – Fa", "Sol, La, Si, Do, Re, Mi, Fa → 7.ª", "10", "<b>7.ª menor</b>"]])
    + caja("Atajo para las teclas blancas:", "entre teclas blancas, <b>todas las 4.as y 5.as son justas</b> excepto Fa–Si (4.ª aumentada) y Si–Fa (5.ª disminuida). Las 3.as mayores son Do–Mi, Fa–La y Sol–Si; todas las demás (Re–Fa, Mi–Sol, La–Do, Si–Re) son menores. Apréndetelo y nombrarás la mayoría de los intervalos de un vistazo.")
    + "<h4>Para qué sirve: los acordes están hechos de intervalos</h4>"
    + tabla(["Acorde", "3.ª desde la fundamental", "5.ª desde la fundamental", "En Do"], [
        ["Mayor", "3.ª mayor (4)", "5.ª justa (7)", "Do–Mi–Sol"],
        ["Menor", "3.ª menor (3)", "5.ª justa (7)", "Do–Mi♭–Sol"],
        ["Disminuido", "3.ª menor (3)", "5.ª disminuida (6)", "Do–Mi♭–Sol♭"],
        ["Aumentado", "3.ª mayor (4)", "5.ª aumentada (8)", "Do–Mi–Sol♯"]])
    + "<p>Así se entienden los nombres de los acordes del módulo 4: un acorde «disminuido» se llama así porque su 5.ª está disminuida, y uno «aumentado», porque su 5.ª está aumentada.</p>"
    + caja("Invertir un intervalo (truco para los grandes):", "si subes la nota de abajo una octava, el intervalo «se da la vuelta»: los números suman siempre <b>9</b> (una 3.ª se convierte en 6.ª, una 2.ª en 7.ª, una 4.ª en 5.ª) y el apellido cambia al contrario: <b>mayor ↔ menor, aumentada ↔ disminuida; la justa sigue justa</b>. Ejemplo: Do–Mi es 3.ª mayor, así que Mi–Do es 6.ª menor. Así calculas una 6.ª o una 7.ª pensando en una 3.ª o una 2.ª, que son más fáciles.")
    + "[[quiz:t2e|¿Qué intervalos NO pueden ser ni mayores ni menores?|2.ª, 3.ª, 6.ª y 7.ª;4.ª, 5.ª y 8.ª;Solo la 8.ª|1|La 4.ª, la 5.ª y la 8.ª son de la familia de las justas: pueden ser justas, aumentadas o disminuidas.]]"
    "[[quiz:t2f|Do–Fa♯ mide 6 semitonos. ¿Cómo se llama?|5.ª disminuida;4.ª aumentada;4.ª justa|1|Do, Re, Mi, Fa son cuatro nombres (4.ª); la 4.ª justa tiene 5 semitonos y esta tiene uno más: aumentada.]]"
    "[[quiz:t2g|¿Qué intervalo es Mi–Si♭?|5.ª justa;4.ª aumentada;5.ª disminuida|2|Mi a Si son cinco nombres (5.ª) y hay 6 semitonos, uno menos que la justa (7).]]"
    "[[quiz:t2h|Si Do–Mi es una 3.ª mayor, ¿qué es Mi–Do (Do arriba)?|6.ª menor;6.ª mayor;3.ª menor|0|Al invertir, 3 + 6 = 9 y mayor pasa a menor.]]"
    + "<h4>3. Todos los intervalos, con sus semitonos y una canción</h4>"
    + tabla(["Intervalo", "Semitonos", "Ejemplo", "Canción para reconocerlo de oído"], [
        ["2.ª menor", "1", "Mi – Fa", "El tema de la película <i>Tiburón</i>"],
        ["2.ª mayor", "2", "Do – Re", "«Cumpleaños feliz» (de «-ple-» a «-a-»)"],
        ["3.ª menor", "3", "La – Do", "<i>Greensleeves</i> (las dos primeras notas)"],
        ["3.ª mayor", "4", "Do – Mi", "<i>Oh When the Saints</i>"],
        ["4.ª justa", "5", "Do – Fa", "La marcha nupcial de Wagner («Here comes the bride»)"],
        ["4.ª aumentada / 5.ª disminuida (tritono)", "6", "Fa – Si", "«María», de <i>West Side Story</i>"],
        ["5.ª justa", "7", "Do – Sol", "«Estrellita, ¿dónde estás?» (de «-tre-» a «-lli-»)"],
        ["6.ª menor", "8", "Mi – Do", "Un semitono más que la 5.ª: suena dulce y triste"],
        ["6.ª mayor", "9", "Do – La", "<i>My Bonnie</i> (las dos primeras notas)"],
        ["7.ª menor", "10", "Sol – Fa", "La 7.ª del acorde de dominante (Sol7)"],
        ["7.ª mayor", "11", "Do – Si", "Un semitono menos que la octava: muy tensa"],
        ["8.ª justa", "12", "Do – Do", "<i>Somewhere Over the Rainbow</i> («some-where»)"]])
    + caja("Truco de la escala mayor:", "imagina la escala mayor que empieza en la nota de abajo. Si la nota de arriba pertenece a esa escala, el intervalo es <b>mayor</b> (2.ª, 3.ª, 6.ª, 7.ª) o <b>justo</b> (4.ª, 5.ª, 8.ª). Si está un semitono <b>por debajo</b>, es menor (o disminuido si era justo); un semitono <b>por encima</b>, aumentado. Ejemplo: Re–Fa. En Re mayor la 3.ª es Fa♯; Fa está un semitono por debajo → <b>3.ª menor</b>.")
    + "<h4>4. Los intervalos en la mano</h4>"
    + tabla(["Intervalo", "Dedos (posición de cinco dedos)", "Sensación"], [
        ["2.ª", "Dedos vecinos (1-2, 2-3…)", "Mano cerrada"],
        ["3.ª", "Saltando un dedo (1-3, 2-4, 3-5)", "Una tecla blanca libre en medio"],
        ["4.ª", "1-4", "Mano algo abierta"],
        ["5.ª", "1-5", "La posición de cinco dedos completa"],
        ["6.ª", "1-5 abriendo un poco", "Una tecla más que la posición"],
        ["8.ª", "1-5 (o 1-4 en teclas negras)", "La mano abierta del todo"]])
    + "<p>Con la práctica, los dedos «miden» los intervalos solos: lees «una 3.ª hacia arriba» y la mano coloca el dedo siguiente-pero-uno sin mirar el teclado.</p>"
    + "<h4>5. Leer por intervalos mientras tocas</h4>"
    + pasos([
        ("Lee la primera nota con un faro.",
         "es la única nota que necesitas «nombrar». Colócate en ella sin prisa antes de empezar."),
        ("Para las siguientes, mira solo la dirección y la distancia.",
         "pregúntate: ¿sube, baja o se repite? ¿es un paso (2.ª), un salto pequeño (3.ª) o grande? No digas el nombre de las notas: piensa «sube una 3.ª, baja una 2.ª»."),
        ("Traduce la distancia a los dedos sin mirar.",
         "2.ª = el dedo de al lado; 3.ª = saltando un dedo; 5.ª = de pulgar a meñique. Los ojos se quedan en la partitura."),
        ("Comprueba con un faro solo de vez en cuando.",
         "en las notas largas, después de un salto grande o al cambiar de línea de pentagrama, confirma que estás donde crees con el faro más cercano."),
    ])
    + "[[quiz:t2c|¿Qué intervalo hay entre Re y Fa?|3.ª mayor;3.ª menor;4.ª justa|1|Re–Mi–Fa son tres nombres (3.ª) y hay 3 semitonos: 3.ª menor.]]"
    "[[quiz:t2d|Dos notas están en la 2.ª y la 4.ª línea del pentagrama. ¿Qué intervalo forman?|Una 3.ª;Una 4.ª;Una 5.ª|2|De línea a línea saltando una línea es una 5.ª (por ejemplo, Sol4–Re5 en clave de Sol).]]"
    + errores([
        ["Cuento las líneas desde abajo cada vez", "No tengo faros memorizados", "Aprende los faros de la partitura de arriba; usa el entrenador de lectura 5 minutos al día"],
        ["Me sale un intervalo «de menos»", "No cuento la nota de partida", "Cuenta las dos notas extremas: de Do a Mi son Do, Re, Mi = 3.ª"],
        ["Confundo 3.ª mayor y menor", "Solo cuento nombres de nota", "Cuenta también los semitonos en el teclado: 4 = mayor, 3 = menor"],
        ["En clave de Fa leo como si fuera de Sol", "Costumbre de la mano derecha", "Repite «la 4.ª línea es Fa» y lee en clave de Fa también la mano derecha en ejercicios fáciles"]])
))

# Módulo 3 · El círculo de quintas a fondo ----------------------------------------------------------
TEORIA[3] = ('<div class="practica">', (
    "<h3>El círculo de quintas, a fondo</h3>"
    "<p>El círculo de quintas es un <b>mapa de las 24 tonalidades</b> (12 mayores y sus 12 menores relativas) ordenadas de forma que las vecinas se parecen mucho entre sí. Con él puedes saber la armadura de cualquier tonalidad, encontrar sus acordes, transportar y entender por qué ciertos acordes «quieren» ir a otros.</p>"
    + "<h4>1. Cómo se construye</h4>"
    + pasos([
        ("Empieza en Do, arriba del todo (las doce de un reloj).",
         "Do mayor no tiene alteraciones: es el punto de partida y en el círculo está junto a su relativa, La menor."),
        ("Gira a la derecha subiendo una 5.ª justa en cada paso: Do → Sol → Re → La → Mi → Si → Fa♯ → Do♯.",
         "una 5.ª justa son <b>7 semitonos</b>, o en la mano, del pulgar al meñique en la posición de cinco dedos. Atajo: desde cualquier tecla blanca la 5.ª justa es otra tecla blanca, excepto desde Si (Si–Fa♯)."),
        ("Gira a la izquierda bajando una 5.ª en cada paso: Do → Fa → Si♭ → Mi♭ → La♭ → Re♭ → Sol♭ → Do♭.",
         "bajar una 5.ª lleva a la misma nota que subir una 4.ª justa (5 semitonos): desde Do, la 4.ª es Fa; desde Fa, Si♭; y así sucesivamente."),
        ("Abajo, las dos mitades se encuentran.",
         "Fa♯ mayor (6♯) y Sol♭ mayor (6♭) son la misma tonalidad escrita de dos formas: suenan igual en el piano. Esto se llama <b>enarmonía</b>. Pasa lo mismo con Si = Do♭ y Do♯ = Re♭."),
    ])
    + "<h4>2. ¿Por qué cada paso añade una alteración?</h4>"
    "<p>Compara Do mayor con su vecina de la derecha, Sol mayor:</p>"
    + tabla(["Grado", "1", "2", "3", "4", "5", "6", "7", "8"], [
        ["Do mayor", "Do", "Re", "Mi", "Fa", "Sol", "La", "Si", "Do"],
        ["Sol mayor", "Sol", "La", "Si", "Do", "Re", "Mi", "<b>Fa♯</b>", "Sol"]])
    + "<p>Solo cambia <b>una nota</b>: Fa se convierte en Fa♯, que es el 7.º grado (la sensible) de Sol. Siempre ocurre así: <b>el sostenido nuevo es el 7.º grado de la tonalidad nueva</b>. Hacia la izquierda pasa lo contrario: Fa mayor es Do mayor con Si♭, y Si♭ es su 4.º grado. <b>El bemol nuevo es el 4.º grado de la tonalidad nueva.</b> Por eso las tonalidades vecinas comparten seis de sus siete notas y suenan «emparentadas».</p>"
    "[[partitura:armaduras_sost]]"
    "[[partitura:armaduras_bem]]"
    + "<h4>3. El orden de las alteraciones</h4>"
    + tabla(["Alteraciones", "Orden (siempre el mismo)", "Truco"], [
        ["Sostenidos", "<b>Fa – Do – Sol – Re – La – Mi – Si</b>", "Van ellos mismos por quintas: ¡es el círculo otra vez, empezando en Fa!"],
        ["Bemoles", "<b>Si – Mi – La – Re – Sol – Do – Fa</b>", "El orden de los sostenidos leído al revés"]])
    + "<p>Una armadura con tres sostenidos lleva siempre los tres primeros: Fa♯, Do♯ y Sol♯. Nunca encontrarás una armadura con «Do♯ y Re♯» sin Fa♯.</p>"
    + "<h4>4. Leer la tonalidad a partir de la armadura</h4>"
    + pasos([
        ("Si hay sostenidos: el último sostenido, más un semitono, es la tónica mayor.",
         "mira el sostenido más a la derecha de la armadura y sube un semitono en el teclado. Fa♯ – Do♯ – Sol♯: el último es Sol♯ → un semitono más arriba es La → <b>La mayor</b>."),
        ("Si hay bemoles: el penúltimo bemol es la tónica mayor.",
         "Si♭ – Mi♭ – La♭ – Re♭: el penúltimo es La♭ → <b>La♭ mayor</b>. La única excepción es la armadura de un solo bemol (no tiene penúltimo): es <b>Fa mayor</b>, apréndela de memoria."),
        ("Encuentra la relativa menor: baja 3 semitonos desde la tónica mayor.",
         "o, lo que es lo mismo, busca el 6.º grado de la escala mayor. La mayor → bajando 3 semitonos (La, Sol♯, Sol, Fa♯) → <b>Fa♯ menor</b>. En el círculo, la relativa está justo debajo, en el anillo interior."),
        ("Decide entre la mayor y su relativa menor mirando la música.",
         "la armadura sola no basta: mira el último acorde y si aparece la sensible de la menor como alteración accidental. Lo verás paso a paso en el módulo 5."),
    ])
    + tabla(["Armadura", "Regla", "Tonalidad mayor", "Relativa menor"], [
        ["Sin alteraciones", "—", "Do mayor", "La menor"],
        ["2♯ (Fa, Do)", "Do♯ + semitono", "Re mayor", "Si menor"],
        ["4♯ (Fa, Do, Sol, Re)", "Re♯ + semitono", "Mi mayor", "Do♯ menor"],
        ["1♭ (Si)", "Excepción", "Fa mayor", "Re menor"],
        ["2♭ (Si, Mi)", "Penúltimo: Si♭", "Si♭ mayor", "Sol menor"],
        ["5♭ (Si, Mi, La, Re, Sol)", "Penúltimo: Re♭", "Re♭ mayor", "Si♭ menor"]])
    + "<h4>5. Al revés: escribir la armadura de una tonalidad</h4>"
    + pasos([
        ("Cuenta cuántos pasos hay desde Do en el círculo.",
         "Mi mayor: Do → Sol (1) → Re (2) → La (3) → Mi (4). Cuatro pasos a la derecha = <b>4 sostenidos</b>. Mi♭ mayor: Do → Fa (1) → Si♭ (2) → Mi♭ (3). Tres pasos a la izquierda = <b>3 bemoles</b>."),
        ("Escribe las primeras alteraciones del orden.",
         "4 sostenidos = Fa♯, Do♯, Sol♯, Re♯. 3 bemoles = Si♭, Mi♭, La♭."),
        ("Para una tonalidad menor, busca primero su relativa mayor.",
         "sube 3 semitonos desde la tónica menor: Sol menor → Si♭ mayor → 2 bemoles (Si♭, Mi♭). Mi menor → Sol mayor → 1 sostenido (Fa♯)."),
    ])
    + "<h4>6. Relativas y homónimas</h4>"
    + tabla(["", "Qué comparten", "Ejemplo", "En el círculo"], [
        ["<b>Relativas</b>", "La misma armadura (las mismas notas), distinta tónica", "Do mayor y La menor", "Una encima de otra"],
        ["<b>Homónimas</b>", "La misma tónica, distinta armadura", "Do mayor (sin alteraciones) y Do menor (3♭)", "La menor homónima está 3 pasos a la izquierda de la mayor"]])
    + caja("Truco de las homónimas:", "para pasar de una tonalidad mayor a su homónima menor, <b>añade 3 bemoles o quita 3 sostenidos</b>. La mayor (3♯) → La menor (0). Re mayor (2♯) → Re menor (1♭). Sol mayor (1♯) → Sol menor (2♭).")
    + "<h4>7. ¿Por qué hay tonalidades «raras»?</h4>"
    "<p>Do♯ mayor (7♯) y Re♭ mayor (5♭) suenan igual. Los compositores suelen elegir la escritura con <b>menos alteraciones</b>: por eso verás muchas obras en Re♭ mayor y muy pocas en Do♯ mayor. Al leer, si una armadura te parece imposible, piensa en su enarmónica.</p>"
    + "[[quiz:t3a|La armadura tiene Fa♯, Do♯ y Sol♯. ¿Cuál es la tonalidad mayor?|Sol mayor;La mayor;Mi mayor|1|El último sostenido es Sol♯; un semitono más arriba está La.]]"
    "[[quiz:t3b|La armadura tiene Si♭, Mi♭ y La♭. ¿Cuál es la tonalidad mayor?|La♭ mayor;Mi♭ mayor;Si♭ mayor|1|El penúltimo bemol es Mi♭.]]"
    "[[quiz:t3c|¿Cuántos sostenidos tiene Mi mayor?|3;4;5|1|Do → Sol → Re → La → Mi: cuatro pasos a la derecha. Son Fa♯, Do♯, Sol♯ y Re♯.]]"
    "[[quiz:t3d|¿Cuál es la relativa menor de Fa mayor?|Re menor;La menor;Fa menor|0|Tres semitonos por debajo de Fa está Re. Las dos tienen un bemol (Si♭).]]"
))

# Módulo 5 · La tonalidad a fondo y el círculo en la armonía ----------------------------------------
TEORIA[5] = ('<div class="practica">', (
    "<h3>La tonalidad, a fondo</h3>"
    "<p>Una <b>tonalidad</b> es una forma de organizar las notas alrededor de una nota principal, la <b>tónica</b>, que funciona como un imán: todas las demás tienen más o menos «tensión» respecto a ella y la música tiende a volver a ella para descansar. Una tonalidad se nombra con su tónica y su <b>modo</b> (mayor o menor): «Re mayor», «Sol menor».</p>"
    + tabla(["Concepto", "Qué es", "Ejemplo"], [
        ["Escala", "Las notas de la tonalidad, ordenadas de grave a agudo", "Sol – La – Si – Do – Re – Mi – Fa♯ – Sol"],
        ["Armadura", "La forma de escribir las alteraciones fijas al principio del pentagrama", "Un sostenido (Fa♯)"],
        ["Tonalidad", "La «gravedad»: qué nota es la casa y qué papel tiene cada acorde", "Sol mayor: Sol es la casa, Re la tensión"]])
    + "<p>Por eso una misma armadura sirve para dos tonalidades (las relativas): las notas son las mismas, pero la casa es distinta.</p>"
    + "<h4>1. Los nombres de los grados</h4>"
    + tabla(["Grado", "Nombre", "En Do mayor", "Por qué se llama así"], [
        ["I", "<b>Tónica</b>", "Do", "La nota principal, la que da nombre a la tonalidad"],
        ["II", "Supertónica", "Re", "Está justo encima de la tónica"],
        ["III", "Mediante", "Mi", "Está a medio camino entre la tónica y la dominante"],
        ["IV", "<b>Subdominante</b>", "Fa", "Está una 5.ª por debajo de la tónica: es la «dominante de abajo»"],
        ["V", "<b>Dominante</b>", "Sol", "Domina la tonalidad: es la nota más importante después de la tónica"],
        ["VI", "Superdominante (o submediante)", "La", "Está justo encima de la dominante"],
        ["VII", "<b>Sensible</b>", "Si", "Está a un semitono de la tónica y «siente» su atracción: quiere subir a ella"]])
    + "<p>En la escala menor natural el VII está a un tono de la tónica (Sol en La menor) y se llama <b>subtónica</b>: ya no tira con tanta fuerza hacia la tónica. Por eso la escala menor armónica lo sube un semitono.</p>"
    + "<h4>2. Mayor y menor: qué cambia</h4>"
    + tabla(["Grado", "1", "2", "3", "4", "5", "6", "7"], [
        ["Do mayor", "Do", "Re", "Mi", "Fa", "Sol", "La", "Si"],
        ["Do menor natural", "Do", "Re", "<b>Mi♭</b>", "Fa", "Sol", "<b>La♭</b>", "<b>Si♭</b>"],
        ["Do menor armónica", "Do", "Re", "<b>Mi♭</b>", "Fa", "Sol", "<b>La♭</b>", "Si"]])
    + "<p>Lo que define el modo es la <b>3.ª</b> (Mi o Mi♭). ¿Y por qué en menor se sube el 7.º grado? Sin él, el acorde del V grado sería menor (Sol–Si♭–Re) y la cadencia V–i sonaría débil. Con Si natural, el V es mayor (Sol–Si–Re) y la sensible empuja hacia la tónica. Por eso, en las obras en tonalidad menor, <b>el 7.º grado aparece como alteración accidental</b> una y otra vez: es la pista más fiable para reconocerlas.</p>"
    + "<h4>3. ¿En qué tonalidad está esta obra? Método en cinco pasos</h4>"
    + pasos([
        ("Mira la armadura: te da dos candidatas.",
         "aplica las reglas del módulo 3 (último sostenido + semitono, o penúltimo bemol) para la mayor, y baja 3 semitonos para su relativa menor. Sin alteraciones: Do mayor o La menor."),
        ("Mira el final.",
         "casi todas las obras terminan en la tónica: fíjate en la última nota del bajo y en el último acorde. Si acaban en Do, apunta a Do mayor; si acaban en La, a La menor."),
        ("Mira el principio.",
         "el primer compás suele presentar el acorde de tónica, o la dominante que lleva a ella. Busca las notas del acorde de cada candidata en la primera frase."),
        ("Busca la sensible de la menor como alteración accidental.",
         "es el 7.º grado de la menor subido un semitono: Sol♯ en La menor, Re♯ en Mi menor, Do♯ en Re menor, Fa♯ en Sol menor. Si aparece varias veces, la obra está en menor."),
        ("Confírmalo con el oído.",
         "toca el acorde de tónica de tu candidata justo después del final de la obra. Si suena a «estar en casa», has acertado; si suena a algo nuevo, prueba la otra."),
    ])
    + "<p>Escucha estas dos melodías. Las dos están escritas sin armadura, pero no están en la misma tonalidad. Aplica el método antes de leer la explicación de debajo:</p>"
    "[[partitura:tono_do]]"
    "[[partitura:tono_lam]]"
    + "[[quiz:t5a|La melodía B no tiene armadura, empieza y termina en La y aparece Sol♯. ¿En qué tonalidad está?|Do mayor;La menor;Sol mayor|1|Termina en La y lleva la sensible de La menor (Sol♯): es La menor, relativa de Do mayor.]]"
    + "<h4>4. La modulación: cambiar de casa</h4>"
    "<p>Una obra larga no se queda siempre en la misma tonalidad: a menudo <b>modula</b>, es decir, se traslada a otra durante un tiempo. Cómo se reconoce:</p>"
    + lista(["Aparece una <b>alteración nueva que se repite</b> (por ejemplo, Fa♯ una y otra vez en una obra en Do mayor).",
             "Hay una <b>cadencia V–I en la tonalidad nueva</b> (D7 → G en el ejemplo de abajo).",
             "A veces el compositor cambia la <b>armadura</b> tras una doble barra; si la cambia solo con alteraciones accidentales, la modulación es más breve.",
             "Los destinos más habituales son la <b>dominante</b> (en las obras mayores) y la <b>relativa mayor</b> (en las menores)."], "🔀")
    + "[[partitura:modulacion]]"
    + "<h4>5. Los tonos vecinos y el círculo como mapa de la armonía</h4>"
    + "[[fig:circulo_vecinos.svg|Círculo de quintas con los seis acordes de Do mayor resaltados|Los seis acordes de Do mayor forman una «porción» del círculo: Fa, Do y Sol (IV, I, V) fuera; Re m, La m y Mi m (ii, vi, iii) dentro.]]"
    + "<p>Fíjate en la figura: <b>los acordes de una tonalidad son una porción de tres casillas del círculo</b>. Por fuera, IV – I – V; por dentro, sus relativas ii – vi – iii. Esas cinco tonalidades que rodean a la tuya son sus <b>tonos vecinos</b>: se diferencian en una alteración como mucho, y por eso modular a ellas suena natural.</p>"
    + tabla(["Si quieres…", "En el círculo", "Ejemplo en Do mayor"], [
        ["Encontrar la dominante (V)", "Un paso a la derecha", "Sol"],
        ["Encontrar la subdominante (IV)", "Un paso a la izquierda", "Fa"],
        ["Resolver una tensión (V → I)", "Un paso hacia la izquierda", "Sol7 → Do"],
        ["Hacer un ii–V–I", "Tres pasos seguidos hacia la izquierda", "Re m7 → Sol7 → Do"],
        ["Encadenar dominantes", "Varios pasos seguidos hacia la izquierda, todos con 7.ª", "Mi7 → La7 → Re7 → Sol7 → Do (muy usado en el ragtime y el jazz)"],
        ["Preparar cualquier acorde (dominante secundaria)", "Toca antes el acorde que está un paso a su derecha, mayor y con 7.ª", "La7 → Re m · Mi7 → La m"]])
    + "[[quiz:t5b|En Sol mayor, ¿qué acorde es la subdominante (IV)?|Do mayor;Re mayor;La menor|0|Un paso a la izquierda de Sol en el círculo está Do.]]"
    "[[quiz:t5c|Una obra en Do mayor empieza a usar Fa♯ y hace una cadencia D7 → G. ¿Qué ha ocurrido?|Ha modulado a Fa mayor;Ha modulado a Sol mayor, su dominante;Es un error de la partitura|1|Fa♯ es la sensible de Sol y D7 → G es su cadencia V7–I.]]"
    + "<h4>6. Transportar: la misma música en otra tonalidad</h4>"
    + pasos([
        ("Escribe la progresión en grados.",
         "pon el número romano de cada acorde en la tonalidad original: Do – La m – Fa – Sol en Do mayor = <b>I – vi – IV – V</b>. Los grados son la «receta» y valen para cualquier tonalidad."),
        ("Busca los acordes de la tonalidad nueva en el círculo.",
         "localiza la tónica nueva y su porción: a la izquierda el IV, a la derecha el V y debajo las tres relativas (ii, vi, iii). En Re mayor: IV = Sol, I = Re, V = La; ii = Mi m, vi = Si m, iii = Fa♯ m."),
        ("Sustituye cada grado por su acorde nuevo.",
         "I – vi – IV – V en Re mayor = Re – Si m – Sol – La. Comprueba la tabla de abajo."),
        ("Toca y escucha.",
         "la progresión transportada debe dar exactamente la misma sensación que la original, solo más aguda o más grave. Si un acorde suena «raro», revisa si es mayor o menor."),
    ])
    + tabla(["Tonalidad", "I", "vi", "IV", "V"], [
        ["Do mayor", "Do", "La m", "Fa", "Sol"],
        ["Sol mayor", "Sol", "Mi m", "Do", "Re"],
        ["Re mayor", "Re", "Si m", "Sol", "La"],
        ["Fa mayor", "Fa", "Re m", "Si♭", "Do"]])
    + "[[quiz:t5d|¿Qué acorde prepara a Re menor como dominante secundaria?|La7;Sol7;Mi7|0|La está un paso a la derecha de Re en el círculo: La7 → Re m.]]"
    + errores([
        ["Digo la tonalidad solo mirando la armadura", "Olvido que hay dos candidatas", "Mira siempre el final y busca la sensible de la menor"],
        ["Confundo relativa y homónima", "Los nombres se parecen", "Relativa = mismas notas (misma armadura); homónima = misma tónica"],
        ["Al transportar me sale un acorde mayor que debía ser menor", "Copio solo la letra del acorde", "Transporta los grados con su tipo: en mayor, ii, iii y vi son siempre menores"],
        ["No noto cuándo modula", "Leo las notas y no las alteraciones", "Subraya con lápiz las alteraciones accidentales que se repiten y busca la cadencia que las confirma"]])
))

GLOSARIO_TEORIA = [
    ("Nota faro", "Nota de referencia del pentagrama que se sabe de memoria; las demás se calculan desde ella."),
    ("Tonalidad", "Organización de las notas y acordes alrededor de una tónica; se nombra con la tónica y el modo (Do mayor)."),
    ("Modo", "Mayor o menor: depende de la 3.ª de la tónica."),
    ("Relativa", "Tonalidad con la misma armadura y distinta tónica (Do mayor y La menor)."),
    ("Homónima", "Tonalidad con la misma tónica y distinta armadura (Do mayor y Do menor)."),
    ("Tonos vecinos", "Las tonalidades que se diferencian en una alteración como mucho; en el círculo, las de alrededor."),
    ("Modulación", "Cambio de tonalidad dentro de una obra."),
    ("Transportar", "Tocar o escribir la misma música en otra tonalidad."),
    ("Enarmonía", "Mismo sonido escrito con nombres distintos (Fa♯ y Sol♭)."),
    ("Tritono", "Intervalo de tres tonos (6 semitonos), como Fa–Si; es la tensión del acorde de dominante."),
    ("Intervalo justo", "Tamaño normal de la 4.ª (5 semitonos), la 5.ª (7) y la 8.ª (12); estos intervalos no pueden ser mayores ni menores."),
    ("Intervalo mayor / menor", "Los dos tamaños normales de la 2.ª, 3.ª, 6.ª y 7.ª; el menor tiene un semitono menos que el mayor."),
    ("Intervalo aumentado / disminuido", "Un semitono más que el justo o el mayor (aumentado), o uno menos que el justo o el menor (disminuido)."),
    ("Grado", "Posición de una nota o un acorde dentro de la escala (I, II, III…)."),
    ("Círculo de quintas", "Mapa de las tonalidades ordenadas por quintas: cada paso añade o quita una alteración."),
]
