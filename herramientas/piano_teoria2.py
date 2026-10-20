"""Segunda ampliación de teoría del curso de piano.

TEORIA_EXTRA[n] = lista de (marcador, html): cada bloque se inserta justo antes de la primera aparición
de «marcador» en la página del módulo n. Marcadores de contenido: [[partitura:clave]], [[fig:…]],
[[quiz:id|pregunta|A;B;C|índice|explicación]] y [[entrenador:intervalos]] / [[entrenador:armaduras]].
"""
from piano_explicaciones import caja, errores, lista, pasos, tabla

QUIZ = '<div class="quiz">'
TEORIA_EXTRA = {}

# Módulo 2 · El ritmo a fondo -------------------------------------------------------------------------
TEORIA_EXTRA[2] = [('<h3>3. Ritmos que aparecen a partir de ahora</h3>', (
    "<h3>Entrenador de intervalos</h3>"
    "<p>Aparecen dos notas a la vez. Elige el <b>número</b> del intervalo y su <b>calidad</b> (justa, mayor, menor, aumentada o disminuida) y pulsa «Comprobar». Cuenta nombres de nota para el número y semitonos para la calidad.</p>"
    "[[entrenador:intervalos]]"
    "<h3>El ritmo a fondo</h3>"
    "<p>Hay cuatro palabras que se confunden mucho y conviene separarlas bien:</p>"
    + tabla(["Palabra", "Qué es", "Ejemplo"], [
        ["<b>Pulso</b>", "El «latido» constante de la música, el que marcas con el pie", "Tic, tic, tic, tic…"],
        ["<b>Ritmo</b>", "El dibujo de notas largas y cortas que se coloca sobre el pulso", "Larga-corta-corta-larga"],
        ["<b>Compás</b>", "El grupo de pulsos que se repite, con un pulso fuerte al principio", "UNO-dos-tres | UNO-dos-tres"],
        ["<b>Tempo</b>", "La velocidad del pulso, en pulsos por minuto (bpm)", "♩ = 80"]])
    + "<p>Una canción es siempre un ritmo (lo que cantas) que camina sobre un pulso (lo que marcas con el pie), agrupado en compases.</p>"
    + "<h4>1. El compás: qué dicen los dos números</h4>"
    + "<p>Un compás se escribe como una fracción. El número de <b>arriba</b> dice <b>cuántos pulsos</b> hay en cada compás. El de <b>abajo</b> dice <b>qué figura es un pulso</b>: 2 = blanca, 4 = negra, 8 = corchea.</p>"
    + tabla(["Compás", "Lectura", "Cómo se cuenta", "Tipo"], [
        ["2/4", "Dos negras por compás", "UNO-dos", "Simple, binario"],
        ["3/4", "Tres negras por compás", "UNO-dos-tres", "Simple, ternario (vals)"],
        ["4/4 (C)", "Cuatro negras por compás", "UNO-dos-tres-cuatro (el 3 es medio fuerte)", "Simple, cuaternario"],
        ["2/2 (¢)", "Dos blancas por compás", "UNO-dos, con pulso de blanca", "Simple, binario"],
        ["6/8", "Seis corcheas por compás", "<b>UNO</b>-dos-tres <b>CUATRO</b>-cinco-seis", "Compuesto, binario"],
        ["9/8", "Nueve corcheas por compás", "UNO-dos-tres CUATRO-cinco-seis SIETE-ocho-nueve", "Compuesto, ternario"],
        ["12/8", "Doce corcheas por compás", "Cuatro grupos de tres", "Compuesto, cuaternario"]])
    + caja("Simple o compuesto, ¿cómo lo sé?", "Mira en qué se divide el pulso. Si el pulso se parte en <b>dos</b> (negra = dos corcheas) el compás es <b>simple</b>. Si se parte en <b>tres</b> (negra con puntillo = tres corcheas) es <b>compuesto</b>. Los compuestos tienen el número de arriba <b>divisible por 3</b> (6, 9, 12) y el pulso es una figura con puntillo.")
    + "[[partitura:compases]]"
    + "<h4>2. Silencios y figuras: las parejas</h4>"
    + tabla(["Figura", "Silencio", "Dura (negras)", "Cómo se llama el silencio"], [
        ["Redonda", "Rectángulo colgado de la 4.ª línea", "4", "Silencio de redonda (también vale para un compás completo)"],
        ["Blanca", "Rectángulo sentado sobre la 3.ª línea", "2", "Silencio de blanca"],
        ["Negra", "Signo en zigzag", "1", "Silencio de negra"],
        ["Corchea", "Un trazo con un banderín", "½", "Silencio de corchea"],
        ["Semicorchea", "Un trazo con dos banderines", "¼", "Silencio de semicorchea"]])
    + "<p>Los silencios <b>también se tocan</b>: la música sigue contando aunque no suene nada. Cuenta en voz alta durante un silencio y no lo acortes.</p>"
    + "<h4>3. Puntillo y ligadura: dos formas de alargar</h4>"
    + lista(["<b>Puntillo (·):</b> añade <b>la mitad</b> del valor. Blanca con puntillo = 2 + 1 = 3 pulsos. Un segundo punto añade la mitad del primero.",
             "<b>Ligadura de unión:</b> arco entre <b>dos notas iguales</b>: se toca la primera y se mantiene el sonido durante la duración de las dos. Sirve para pasar de un compás a otro o para durar lo que ninguna figura sola da.",
             "<b>Ligadura de expresión (legato):</b> arco sobre <b>notas distintas</b>: se tocan unidas, sin cortes. No alarga nada, solo indica cómo tocar."], "🔗")
    + "<h4>4. Anacrusa: empezar antes del compás</h4>"
    + "<p>A veces la melodía empieza por uno o dos pulsos <b>antes</b> del primer compás. Se llama <b>anacrusa</b> o «ritmo de tipo anacrúsico»: «Cumpleaños feliz» empieza así. El primer compás queda incompleto y el último también; entre los dos suman un compás entero.</p>"
    + "[[partitura:anacrusa]]"
    + "<h4>5. Síncopa y contratiempo</h4>"
    + lista(["<b>Síncopa:</b> una nota que empieza en una parte débil del compás y se prolonga hasta la parte fuerte (por ejemplo, una corchea que empieza en la «y» del 2 y llega al 3). Desplaza el acento.",
             "<b>Contratiempo:</b> una nota que cae justo en la parte débil del pulso (la «y»), rodeada de silencios.",
             "<b>Cómo se toca:</b> cuenta siempre las subdivisiones en voz alta («1-y-2-y…»). Los acentos «raros» se encajan solos si el pulso no se mueve."], "🔀")
    + "<h4>6. El tempo y sus nombres italianos</h4>"
    + tabla(["Término", "Significa", "Pulsos por minuto (aprox.)"], [
        ["Largo", "Muy lento, amplio", "40-60"],
        ["Adagio", "Lento, cómodo", "66-76"],
        ["Andante", "Caminando", "76-108"],
        ["Moderato", "Moderado", "108-120"],
        ["Allegro", "Vivo, alegre", "120-156"],
        ["Presto", "Muy rápido", "168-200"],
        ["<i>ritardando</i> (rit.)", "Ir frenando poco a poco", "—"],
        ["<i>accelerando</i> (accel.)", "Ir acelerando poco a poco", "—"],
        ["<i>a tempo</i>", "Volver al tempo anterior", "—"],
        ["<i>fermata</i> (calderón)", "Alargar la nota o el silencio a voluntad", "—"]])
    + "[[quiz:r2a|En un compás de 9/8, ¿cuántos pulsos se sienten?|9;3;6|1|9/8 es compuesto: tres pulsos, cada uno de tres corcheas.]]"
    "[[quiz:r2b|¿Qué hace una ligadura entre dos notas iguales?|Las une: suena una sola nota con la duración de las dos;Las toca más fuertes;Indica que se toquen más rápido|0|Es la ligadura de unión: no se vuelve a tocar la segunda nota.]]"
    "[[quiz:r2c|Una blanca con puntillo dura…|2 negras;3 negras;4 negras|1|El puntillo añade la mitad: 2 + 1 = 3 negras.]]"
    "[[quiz:r2d|¿Qué es la anacrusa?|Un compás completo de silencio;La nota o notas que empiezan antes del primer compás;Un adorno de la mano izquierda|1|Empieza en tiempo débil; el último compás queda incompleto para compensarla.]]"
    + errores([
        ["Cuento el 6/8 en seis pulsos iguales", "Veo el 6 y no el compuesto", "Cuenta «UNO-dos-tres CUATRO-cinco-seis»: dos acentos"],
        ["Acorto los silencios", "Parece que «no hay nada que hacer»", "Cuenta los silencios en voz alta y marca el pulso con el pie"],
        ["Confundo ligadura de unión y de expresión", "Los dos son arcos", "Mira las notas: iguales = unión (alarga); distintas = expresión (legato)"]]))) ]

# Módulo 3 · Menores, pentatónica, cromática y modos ---------------------------------------------------
TEORIA_EXTRA[3] = [(QUIZ, (
    "<h3>Entrenador de armaduras</h3>"
    "<p>Aparece una armadura. Averigua la tonalidad <b>mayor</b> con las reglas del círculo de quintas (último sostenido + semitono; penúltimo bemol) y pulsa su nombre.</p>"
    "[[entrenador:armaduras]]"
    "<h3>Más escalas: menor, pentatónica, cromática y modos</h3>"
    "<h4>1. La escala menor, a fondo</h4>"
    "<p>La escala menor natural sigue otro patrón de tonos (T) y semitonos (S): <b>T–S–T–T–S–T–T</b>. Es el mismo patrón de la mayor, pero empezando por su 6.º grado: por eso La menor tiene las mismas notas que Do mayor.</p>"
    + tabla(["Tipo", "Patrón", "Rasgo", "Dónde se usa"], [
        ["Natural", "T–S–T–T–S–T–T", "Es la mayor «empezando por el 6.º»", "Melodías suaves, folk, base de las otras dos"],
        ["Armónica", "T–S–T–T–S–<b>T½</b>–S", "7.º grado subido: aparece una 2.ª aumentada (3 semitonos) entre el 6.º y el 7.º", "Acordes: da el V mayor y la sensible"],
        ["Melódica", "Subiendo: T–S–T–T–T–T–S; bajando, como la natural", "6.º y 7.º subidos al subir; al bajar vuelven a su sitio", "Melodías: evita el salto de la armónica"]])
    + pasos([
        ("Para construir una menor natural desde cualquier nota, empieza por su relativa mayor.",
         "sube 3 semitonos desde la tónica menor para encontrar la mayor. Do menor → Mi♭ mayor (3♭): la menor natural de Do tiene Mi♭, La♭ y Si♭."),
        ("Para la armónica, sube un semitono el 7.º grado.",
         "en Do menor armónica el Si♭ pasa a Si natural. Es la nota que se escribe como alteración accidental en las obras en menor."),
        ("Para la melódica ascendente, sube el 6.º y el 7.º; para la descendente, usa la natural.",
         "en Do menor melódica subiendo: Do–Re–Mi♭–Fa–Sol–La–Si–Do; bajando: Do–Si♭–La♭–Sol–Fa–Mi♭–Re–Do."),
    ])
    + "<h4>2. La escala pentatónica: cinco notas sin tensiones</h4>"
    "<p>«Penta» = cinco. Se obtiene quitando de la escala mayor el 4.º y el 7.º grados, es decir, las dos notas que forman semitonos. Queda: <b>Do–Re–Mi–Sol–La</b>. Es la escala de las melodías populares de todo el mundo, y como no tiene semitonos ni tritono, <b>es muy difícil que suene mal</b> sobre su acorde.</p>"
    + lista(["<b>Pentatónica mayor de Do:</b> Do–Re–Mi–Sol–La (teclas blancas).",
             "<b>Pentatónica menor de La:</b> La–Do–Re–Mi–Sol (las mismas notas, empezando por La). Es la relativa de la anterior.",
             "<b>Truco de las teclas negras:</b> la pentatónica de Fa♯ mayor son las cinco teclas negras: Fa♯–Sol♯–La♯–Do♯–Re♯."], "🎵")
    + "[[partitura:pentatonica]]"
    + "<h4>3. La escala cromática: todos los semitonos</h4>"
    "<p>Doce notas, una por cada tecla blanca y negra de la octava, cada una a un semitono de la anterior. No pertenece a ninguna tonalidad: es una escala «de paso». Se escribe con <b>sostenidos subiendo</b> y con <b>bemoles bajando</b>.</p>"
    + "[[partitura:cromatica]]"
    + "<h4>4. Los modos: la misma escala, otra nota de partida</h4>"
    "<p>Si tocas las notas de Do mayor pero <b>empiezas y terminas en otra nota</b>, sale otro «color», llamado <b>modo</b>. Se pueden obtener siete: uno por cada grado de la escala.</p>"
    + tabla(["Modo", "Empieza en… (teclas blancas)", "Qué lo distingue de la mayor (desde su tónica)", "Carácter"], [
        ["Jónico", "Do", "Es la escala mayor", "Alegre, estable"],
        ["Dórico", "Re", "3.ª y 7.ª menores", "Menor pero luminoso (jazz, folk)"],
        ["Frigio", "Mi", "2.ª, 3.ª, 6.ª y 7.ª menores", "Oscuro, flamenco"],
        ["Lidio", "Fa", "4.ª aumentada", "Soñador, ligero"],
        ["Mixolidio", "Sol", "7.ª menor", "Mayor «de blues» o rock"],
        ["Eólico", "La", "3.ª, 6.ª y 7.ª menores", "Es la menor natural"],
        ["Locrio", "Si", "2.ª, 3.ª, 5.ª, 6.ª y 7.ª menores", "Inestable, rara vez es tónica"]])
    + "[[partitura:modos_do]]"
    + caja("Para comparar los modos:", "tócalos siempre <b>desde la misma nota</b> (Do), como en la partitura. Así oyes solo lo que cambia: el dórico es «menor con 6.ª mayor»; el mixolidio, «mayor con 7.ª menor»; el lidio, «mayor con 4.ª aumentada».")
    + "[[quiz:r3a|¿Qué notas se quitan de la escala mayor para formar la pentatónica?|El 1.º y el 5.º;El 4.º y el 7.º;El 2.º y el 6.º|1|Se quitan los dos grados que forman semitono: el 4.º y el 7.º.]]"
    "[[quiz:r3b|¿Qué modo es «mayor con la 7.ª menor»?|Dórico;Mixolidio;Lidio|1|Mixolidio: Do–Re–Mi–Fa–Sol–La–Si♭.]]"
    "[[quiz:r3c|¿Qué escala menor tiene el 7.º grado subido?|Natural;Armónica;Pentatónica|1|La armónica sube el 7.º para tener sensible y un V mayor.]]"
    "[[quiz:r3d|¿Cuántas notas tiene la escala cromática de una octava (sin repetir la nota final)?|7;10;12|2|Una por cada tecla, blanca o negra, de la octava.]]"
    + errores([
        ["En la menor armónica toco el Sol natural", "Me olvido de la alteración accidental", "Subraya el 7.º grado en la partitura: en La menor es Sol♯"],
        ["Los modos me parecen una escala más que aprender", "Los aprendo aparte de la mayor", "Piensa en «la mayor empezando en otra nota» o en «qué nota cambia respecto a la mayor»"],
        ["La cromática se me traba", "Uso un dedo cualquiera", "Aprende la regla: 3.º en las negras, 1.º en las blancas, y 2.º en la segunda blanca de Mi–Fa y Si–Do"]]))) ]

# Módulo 4 · Armonizar la escala ----------------------------------------------------------------------
TEORIA_EXTRA[4] = [(QUIZ, (
    "<h3>Armonizar la escala: un acorde sobre cada nota</h3>"
    "<p>«Armonizar» es construir un acorde sobre cada grado de la escala, usando <b>solo las notas de la escala</b>. Se apilan terceras: se toma una nota, se salta una y se toma la siguiente, y así dos veces. El resultado depende de dónde caigan los semitonos:</p>"
    + "[[partitura:armonizar_do]]"
    + tabla(["Grado", "Notas", "Distancias", "Tipo", "Número romano"], [
        ["I", "Do–Mi–Sol", "3.ª mayor + 3.ª menor", "Mayor", "I"],
        ["II", "Re–Fa–La", "3.ª menor + 3.ª mayor", "Menor", "ii"],
        ["III", "Mi–Sol–Si", "3.ª menor + 3.ª mayor", "Menor", "iii"],
        ["IV", "Fa–La–Do", "3.ª mayor + 3.ª menor", "Mayor", "IV"],
        ["V", "Sol–Si–Re", "3.ª mayor + 3.ª menor", "Mayor", "V"],
        ["VI", "La–Do–Mi", "3.ª menor + 3.ª mayor", "Menor", "vi"],
        ["VII", "Si–Re–Fa", "3.ª menor + 3.ª menor", "Disminuido", "vii°"]])
    + caja("Regla para recordarlo:", "en cualquier tonalidad <b>mayor</b>, los acordes de los grados <b>I, IV y V son mayores</b>; los de los grados <b>ii, iii y vi, menores</b>; y el del <b>vii°, disminuido</b>. Es lo que indican las mayúsculas y las minúsculas de los números romanos.")
    + "<h4>Armonizar cualquier tonalidad en 3 pasos</h4>"
    + pasos([
        ("Escribe la escala de la tonalidad con sus alteraciones.",
         "por ejemplo, Sol mayor: Sol–La–Si–Do–Re–Mi–Fa♯–Sol."),
        ("Apila terceras sobre cada nota usando solo notas de la escala.",
         "sobre Sol: Sol–Si–Re. Sobre La: La–Do–Mi. Sobre Fa♯: Fa♯–La–Do (¡el Do natural!, porque en la escala de Sol mayor Do es natural)."),
        ("Pon a cada acorde su tipo según la regla (I, IV, V mayores; ii, iii, vi menores; vii° disminuido).",
         "en Sol mayor: Sol, La m, Si m, Do, Re, Mi m, Fa♯°. Si el resultado no coincide, revisa una alteración."),
    ])
    + "<h4>Acordes «suspendidos» (sus) y acordes con otro bajo</h4>"
    + tabla(["Cifrado", "Notas en Do", "Cómo se forma", "Cómo suena"], [
        ["Csus2", "Do–Re–Sol", "Se sustituye la 3.ª por la 2.ª", "Abierto, sin decidir mayor o menor"],
        ["Csus4", "Do–Fa–Sol", "Se sustituye la 3.ª por la 4.ª", "En suspenso: pide volver al acorde mayor"],
        ["C/E", "Mi en el bajo; Do–Mi–Sol", "El mismo acorde con otra nota en el bajo (1.ª inversión)", "Igual de claro pero con un bajo que camina"],
        ["C/G", "Sol en el bajo; Do–Mi–Sol", "2.ª inversión", "Estable pero inquieto"]])
    + "[[partitura:sus_slash]]"
    + "<p>La <b>barra</b> del cifrado (C/E) indica solo la nota del bajo: lo que va a la izquierda de la barra es el acorde, y lo que va a la derecha, la nota que toca la mano izquierda. Los bajos suaves por grados (Do, Do/Mi, Fa…) hacen que las progresiones suenen más «cantables».</p>"
    + "<h4>Posición cerrada y posición abierta</h4>"
    + lista(["<b>Cerrada:</b> las tres notas están juntas, dentro de una octava (Do–Mi–Sol). Es la que usas en la mano derecha.",
             "<b>Abierta:</b> las notas están más separadas (Do–Sol–Mi'), con una más de una octava. Suena más amplia, como en el acompañamiento romántico.",
             "<b>Plaqué o arpegiado:</b> las notas del acorde suenan a la vez (plaqué) o una tras otra (arpegio): son el mismo acorde, vestido de otra manera."], "🧱")
    + "[[quiz:r4a|En una tonalidad mayor, ¿qué tipo de acorde es el del 6.º grado (vi)?|Mayor;Menor;Disminuido|1|Los acordes del ii, iii y vi son menores.]]"
    "[[quiz:r4b|¿Qué notas forman Csus4?|Do–Mi–Sol;Do–Re–Sol;Do–Fa–Sol|2|Se sustituye la 3.ª (Mi) por la 4.ª (Fa).]]"
    "[[quiz:r4c|En el cifrado C/E, ¿qué indica la «E»?|El acorde es Mi;La nota que toca el bajo;La tonalidad|1|La barra indica solo la nota del bajo: Do con Mi en el bajo.]]"
    + errores([
        ["Me sale Fa mayor en lugar de Fa♯ disminuido", "Olvido que el vii° tiene un Fa♯ en Sol mayor", "Apila terceras siempre dentro de la armadura de la tonalidad"],
        ["Confundo sus2 con el acorde menor", "Los dos «ceden» algo de la 3.ª mayor", "En sus no hay 3.ª: es 2.ª o 4.ª y la 5.ª; el menor lleva 3.ª menor"],
        ["La barra del cifrado me confunde", "Pienso en una división matemática", "Piensa «acorde sobre bajo»: C/E = Do sobre Mi"]]))) ]

# Módulo 5 · Progresiones habituales ------------------------------------------------------------------
TEORIA_EXTRA[5] = [('<div class="practica">', (
    "<h3>Progresiones de acordes: las «recetas» que se repiten</h3>"
    "<p>La mayor parte de la música tonal se escribe con unas pocas «recetas» de acordes. Conocerlas permite acompañar cientos de canciones y <b>adivinar</b> el acorde siguiente.</p>"
    + tabla(["Progresión", "En Do mayor", "Dónde se oye", "Sensación"], [
        ["I – IV – V – I", "Do – Fa – Sol – Do", "Folk, himnos, rock and roll", "Clara, definitiva"],
        ["I – V – vi – IV", "Do – Sol – La m – Fa", "Música pop de los últimos 50 años", "Emotiva, «de viaje»"],
        ["I – vi – IV – V", "Do – La m – Fa – Sol", "Doo-wop, baladas de los años 50", "Nostálgica"],
        ["ii – V – I", "Re m – Sol – Do", "Jazz, bossa nova, clásica", "Resolución natural"],
        ["I – V – vi – iii – IV – I – IV – V", "Do – Sol – La m – Mi m – Fa – Do – Fa – Sol", "Canon de Pachelbel y mil canciones", "Fluida, descendente"],
        ["vi – IV – I – V", "La m – Fa – Do – Sol", "Pop e indie", "Melancólica que acaba esperanzada"]])
    + "[[partitura:progresiones]]"
    + "[[partitura:canon_prog]]"
    + caja("Por qué funcionan:", "casi todas parten de la misma historia: <b>tónica (casa) → subdominante (paseo) → dominante (tensión) → tónica</b>. Los acordes de «sustitución» (vi en lugar de I, ii en lugar de IV) cambian el color sin cambiar la función.")
    + "<h4>Armonía en tonalidad menor</h4>"
    + tabla(["Grado (La menor)", "Acorde", "Tipo", "Notas"], [
        ["i", "La m", "Menor", "La–Do–Mi"],
        ["ii°", "Si°", "Disminuido", "Si–Re–Fa"],
        ["III", "Do", "Mayor", "Do–Mi–Sol"],
        ["iv", "Re m", "Menor", "Re–Fa–La"],
        ["v / V", "Mi m / <b>Mi</b>", "Menor / <b>mayor</b>", "Mi–Sol–Si / Mi–Sol♯–Si"],
        ["VI", "Fa", "Mayor", "Fa–La–Do"],
        ["VII", "Sol", "Mayor", "Sol–Si–Re"]])
    + "<p>En menor, el acorde de dominante casi siempre se hace <b>mayor</b> (Mi, o Mi7) subiendo el 7.º grado de la escala (Sol♯). Es la «sensible» de la menor armónica. Observa la cadencia i–iv–V7–i:</p>"
    + "[[partitura:ej_cadencia_lam]]"
    + "<h4>Cómo averiguar los acordes de una melodía</h4>"
    + pasos([
        ("Averigua la tonalidad (armadura y última nota) y escribe sus siete acordes.",
         "usa la tabla del módulo 4. En Do mayor: Do, Re m, Mi m, Fa, Sol, La m, Si°."),
        ("Mira la nota más importante de cada compás (la que cae en el pulso fuerte).",
         "es la que debe pertenecer al acorde. Si la melodía tiene Mi en el primer tiempo, el acorde puede ser Do (Do–Mi–Sol), La m (La–Do–Mi) o Mi m."),
        ("Elige el acorde que contenga esa nota y que siga la «historia»: I, IV, V.",
         "si dudas entre dos, prefiere el más sencillo y compruébalo tocándolo con la melodía. Cuando suene mal, cambia a otro que tenga la misma nota."),
        ("Termina en la tónica.",
         "casi todas las melodías acaban sobre el acorde I, normalmente precedido de V."),
    ])
    + "[[quiz:r5a|¿Qué progresión es I–V–vi–IV en Do mayor?|Do–Fa–Sol–Do;Do–Sol–La m–Fa;Do–La m–Fa–Sol|1|I=Do, V=Sol, vi=La m, IV=Fa.]]"
    "[[quiz:r5b|En La menor, ¿qué acorde es la dominante habitual (V)?|Mi m;Mi mayor (con Sol♯);Sol mayor|1|Se sube el 7.º grado (Sol♯) para que el V sea mayor.]]"
    "[[quiz:r5c|Una melodía tiene Mi en el pulso fuerte. ¿Qué acorde de Do mayor NO puede acompañarla?|Do;La m;Re m|2|Re–Fa–La no contiene Mi.]]"
    + errores([
        ["Acompaño toda la canción solo con I, IV y V", "Es lo que mejor conozco", "Prueba a sustituir el I por el vi o el IV por el ii para cambiar de color"],
        ["Mi acorde de dominante no suena a «cierre»", "Falta el Sol♯ en la menor", "En menor, sube el 7.º grado y usa Mi o Mi7"],
        ["No sé qué acorde sigue", "Pienso nota a nota", "Piensa en funciones: casa, paseo y tensión"]]))) ]

# Módulo 6 · Texturas --------------------------------------------------------------------------------
TEORIA_EXTRA[6] = [(QUIZ, (
    "<h3>Texturas: cómo se combinan las voces</h3>"
    "<p>La <b>textura</b> es la manera en que se superponen las distintas líneas musicales. Reconocerla ayuda a decidir qué mano manda y cómo equilibrar el volumen.</p>"
    + tabla(["Textura", "Qué es", "Ejemplo en piano", "Qué mano manda"], [
        ["Monodía", "Una sola línea", "Una melodía a una mano o en octavas", "La que toca"],
        ["Melodía acompañada (homofonía)", "Una melodía clara y un fondo de acordes", "Bajo Alberti, vals, balada", "La melodía (normalmente la derecha)"],
        ["Homorritmia", "Todas las voces con el mismo ritmo (coral)", "Un himno o coral a cuatro voces", "Ninguna: todas por igual, con la voz aguda un poco por delante"],
        ["Polifonía", "Dos o más melodías independientes", "Una invención o una fuga de Bach", "Las dos manos a igualdad; escuchas cada voz"]])
    + "<h4>Del acompañamiento sencillo al elaborado</h4>"
    + pasos([
        ("Acordes en bloque.",
         "toca el acorde entero en el primer tiempo y manténlo. Es la forma más simple y la que debes dominar primero."),
        ("Bajo + acorde.",
         "bajo en el 1 y acorde en los demás tiempos (como el vals) o bajo en 1 y 3 y acordes en 2 y 4 (marcha, stride)."),
        ("Arpegio sencillo.",
         "las notas del acorde una a una, de abajo arriba (Do–Mi–Sol–Mi…). Mantén todas con el pedal."),
        ("Patrón característico.",
         "Alberti, ostinato, boogie: aprende uno y úsalo para acompañar varias canciones."),
    ])
    + "<h4>Cómo equilibrar el volumen entre manos</h4>"
    + lista(["La mano que lleva la melodía <b>toca con el brazo, un poco más pesada</b>; la otra, desde la yema del dedo.",
             "Escucha <b>una nota de la melodía y una del acompañamiento a la vez</b>: la primera debe oírse mejor.",
             "Si la melodía está en la mano izquierda (un bajo cantabile), invierte los papeles: la derecha acompaña ligera.",
             "El pedal difumina el balance: si se mezclan, cambia el pedal con más frecuencia."], "⚖️")
    + "[[quiz:r6a|¿Qué textura tiene una melodía clara con acordes de fondo?|Monodía;Melodía acompañada;Polifonía|1|Es homofonía o melodía acompañada.]]"
    "[[quiz:r6b|En una fuga a dos voces, ¿qué mano manda?|Solo la derecha;Solo la izquierda;Las dos a igualdad, cada una canta su voz|2|En polifonía las dos voces son independientes e igual de importantes.]]"
    + errores([
        ["Todo suena igual de fuerte", "Las dos manos tocan con el mismo peso", "Grábate y escucha: ¿distingues la melodía? Si no, baja el acompañamiento"],
        ["La mano izquierda se acelera", "Compite con la derecha", "Toca la izquierda sola con metrónomo hasta que sea automática"]]))) ]

# Módulo 7 · Pedal: por qué suena ---------------------------------------------------------------------
TEORIA_EXTRA[7] = [(QUIZ, (
    "<h3>La resonancia: por qué el pedal «embellece» el sonido</h3>"
    "<p>Cuando una cuerda suena no vibra de una sola manera: además de la vibración principal tiene vibraciones más rápidas, los <b>armónicos</b>. Con el pedal pisado, todas las cuerdas quedan libres y las que comparten armónicos con las notas tocadas vibran <b>por simpatía</b>. Eso da el efecto de «aire» y de nota larga.</p>"
    + tabla(["Marca en la partitura", "Qué significa"], [
        ["<i>Ped.</i>", "Pisar el pedal"],
        ["✱", "Levantar el pedal"],
        ["Línea bajo el pentagrama con ángulos (⌐ ¬)", "Los ángulos marcan el cambio de pedal: pisar, levantar y volver a pisar"],
        ["<i>Ped.</i> sin más indicaciones", "Pedal derecho, cambiándolo con cada armonía"],
        ["<i>una corda</i>", "Pedal izquierdo (suavizar)"],
        ["<i>tre corde</i>", "Soltar el pedal izquierdo"]])
    + "<h4>Medio pedal y pedal de colores</h4>"
    + lista(["<b>Medio pedal:</b> se pisa solo a medias: los apagadores quedan «rozando» las cuerdas, sin dejarlas libres del todo. Reduce la resonancia de los graves y mantiene un poco de aire.",
             "<b>Pedal de colores (impresionismo):</b> a veces se mezcla a propósito una armonía con la anterior para conseguir una atmósfera difusa.",
             "<b>Pedal de bajo (sostenuto):</b> mantiene solo las notas graves que estaban pulsadas, mientras que las demás se tocan sin pedal."], "🎨")
    + caja("Regla para decidir:", "pisa el pedal cuando quieras <b>unir</b> o dar color; no lo uses para tapar errores. Si no sabes si lo necesitas, prueba el pasaje <b>sin</b> pedal: lo que no suene limpio, tampoco lo hará con él.")
    + "[[quiz:r7a|¿Por qué suenan las cuerdas «por simpatía» con el pedal pisado?|Porque el pedal las golpea;Porque están libres de apagadores y vibran con los armónicos de otras notas;Porque se afinan|1|Con el pedal pisado, todas las cuerdas quedan libres y vibran con los armónicos compartidos.]]"
    "[[quiz:r7b|¿Qué hace el medio pedal?|Mantiene todo igual que el pedal completo;Deja los apagadores rozando las cuerdas, con menos resonancia;Sube la afinación|1|Es un matiz entre pedal pisado y levantado.]]"
    + errores([
        ["Uso pedal en todo", "Me gusta cómo suena", "Estudia sin pedal y añádelo al final, escuchando cada cambio"],
        ["Pierdo la claridad en los graves", "Los graves vibran más tiempo", "Usa medio pedal o cambia con más frecuencia en el registro grave"]]))) ]

# Módulo 8 · La forma musical -------------------------------------------------------------------------
TEORIA_EXTRA[8] = [(QUIZ, (
    "<h3>La forma musical: la arquitectura de una obra</h3>"
    "<p>Una obra se construye por niveles, de lo más pequeño a lo más grande, como un texto: palabras, frases, párrafos, capítulos.</p>"
    + tabla(["Nivel", "Qué es", "Duración habitual", "Equivale a…"], [
        ["Motivo", "La idea musical más pequeña y reconocible", "1-2 compases", "Una palabra"],
        ["Semifrase", "Un trozo de frase que termina con una pausa breve", "2 compases", "Una oración corta"],
        ["Frase", "Una idea musical completa que termina con una cadencia", "4 compases", "Una oración"],
        ["Periodo", "Dos frases: una «pregunta» (antecedente) y una «respuesta» (consecuente)", "8 compases", "Un párrafo"],
        ["Sección", "Una parte de la obra que se identifica con una letra (A, B…)", "8-32 compases", "Un capítulo"]])
    + "[[partitura:periodo]]"
    + "<p>La pareja <b>antecedente–consecuente</b> es la estructura más habitual: la primera frase deja la música «en el aire» (termina en el V: semicadencia) y la segunda la cierra (termina en el I: cadencia perfecta).</p>"
    + "<h4>Las formas más habituales</h4>"
    + tabla(["Forma", "Esquema", "Cómo se reconoce", "Ejemplos"], [
        ["Binaria", "A – B", "Dos secciones, cada una con su repetición. La primera suele modular a la dominante", "Danzas barrocas (minuetos, gavotas)"],
        ["Ternaria", "A – B – A", "La música vuelve al principio tras un contraste", "Nocturnos, canciones, minuetos con trío"],
        ["Rondó", "A – B – A – C – A", "Un estribillo que vuelve entre episodios distintos", "<i>Para Elisa</i> (Beethoven)"],
        ["Tema con variaciones", "A – A' – A'' – A'''", "El mismo tema, transformado cada vez", "Variaciones de Mozart o Beethoven"],
        ["Forma sonata", "Exposición – Desarrollo – Reexposición", "Dos temas, un episodio de tensión y la vuelta de los temas en la tonalidad principal", "Primer movimiento de una sonata clásica"]])
    + "[[partitura:forma_aba]]"
    + pasos([
        ("Escucha la obra entera sin partitura.",
         "levanta un dedo cada vez que aparezca algo <b>nuevo</b> y otro cada vez que vuelva algo <b>conocido</b>."),
        ("Pon letras a las secciones.",
         "la primera idea es A; lo que contrasta (otra tonalidad, otro ritmo, otro carácter) es B; si A vuelve, otra A."),
        ("Localiza las cadencias.",
         "los finales de frase y de sección suelen coincidir con una cadencia: te dicen dónde acaba cada parte."),
        ("Anota la tonalidad de cada sección.",
         "si B está en otra tonalidad, has encontrado una modulación."),
    ])
    + "[[quiz:r8a|¿Cuál es el esquema de un rondó?|A–B;A–B–A;A–B–A–C–A|2|El estribillo A vuelve entre episodios distintos (B, C…).]]"
    "[[quiz:r8b|En un periodo, ¿cómo termina normalmente la primera frase (el antecedente)?|En la dominante (semicadencia);En la tónica con cadencia perfecta;Con un silencio de compás completo|0|Deja la música «en el aire»; el consecuente la cierra.]]"
    "[[quiz:r8c|¿Qué diferencia una forma binaria (A–B) de una ternaria (A–B–A)?|En la ternaria la música vuelve al principio;En la binaria hay más tiempos;En la binaria se toca más rápido|0|La ternaria cierra volviendo a A.]]"
    + errores([
        ["No distingo las frases", "Escucho nota a nota", "Canta la melodía y busca dónde respirarías"],
        ["Confundo A–B–A con rondó", "Los dos vuelven a la idea inicial", "En el rondó A vuelve varias veces; en la ternaria, solo una"]]))) ]

# Módulo 9 · Ornamentos -------------------------------------------------------------------------------
TEORIA_EXTRA[9] = [(QUIZ, (
    "<h3>Los ornamentos: tabla de referencia</h3>"
    + tabla(["Ornamento", "Cómo se escribe", "Qué es", "Cómo se toca"], [
        ["Trino", "<i>tr</i> sobre la nota", "Alternancia rápida entre la nota y la superior", "En música barroca y clásica, empieza por la nota <b>superior</b>; termina con la nota real"],
        ["Mordente superior", "Zigzag corto", "Nota real – nota superior – nota real", "Tres notas rapidísimas sobre el pulso"],
        ["Mordente inferior", "Zigzag con raya", "Nota real – nota inferior – nota real", "Igual que el anterior, hacia abajo"],
        ["Grupeto", "Una «S» tumbada sobre la nota", "Nota superior – nota real – nota inferior – nota real", "Cuatro notas, la última sobre la siguiente nota"],
        ["Apoyatura larga", "Nota pequeña sin barra", "Una nota que «se apoya» y se resuelve por grado", "Toma la mitad (o dos tercios) del valor de la nota real"],
        ["Apoyatura breve (<i>acciaccatura</i>)", "Nota pequeña con barra", "Una nota rápida antes de la principal", "Cae sobre el pulso y la principal llega inmediatamente después"],
        ["Arpegio de acorde", "Línea ondulada junto al acorde", "El acorde se toca «desplegado», de abajo arriba", "Rápido, y la nota más aguda en el pulso"]])
    + "<h4>Reglas para cualquier ornamento</h4>"
    + lista(["<b>Primero la melodía, luego el adorno:</b> aprende la nota sin adorno y añádelo al final.",
             "<b>Despacio y regular:</b> en un ornamento todas las notas deben sonar iguales, sin acentos.",
             "<b>Los ornamentos dependen de la época:</b> en Bach se empieza en la nota superior; en el Romanticismo puede empezar en la real.",
             "<b>Siempre sobre el pulso del ritmo</b>, no antes."], "✨")
    + "[[quiz:r9a|En el Barroco, ¿por qué nota empieza normalmente un trino?|Por la nota real;Por la nota superior;Por la nota inferior|1|En el Barroco y el Clasicismo se empieza por la nota superior.]]"
    "[[quiz:r9b|¿Qué es una acciaccatura?|Una nota larga con puntillo;Una apoyatura breve (nota pequeña con barra);Un tipo de pedal|1|Es una nota rápida que precede a la principal.]]"
    + errores([
        ["El trino se desordena", "Dedos muy altos y tensos", "Trabájalo a ritmos regulares con metrónomo y dedos pegados a las teclas"],
        ["El adorno llega antes del pulso", "Me adelanto", "La nota real cae <b>sobre</b> el pulso; el adorno la prepara"]]))) ]

# Módulo 10 · Compases irregulares y hemiola ---------------------------------------------------------
TEORIA_EXTRA[10] = [(QUIZ, (
    "<h3>Compases de amalgama, hemiola y cambios de compás</h3>"
    "<h4>Compases de amalgama</h4>"
    "<p>Son los que no se dividen en grupos iguales: 5/4, 7/8, 11/8… Se tocan como <b>mezcla de grupos de 2 y 3</b>, y la partitura (o el compositor) indica cómo agruparlos.</p>"
    + tabla(["Compás", "Agrupación", "Cómo se cuenta", "Ejemplo famoso"], [
        ["5/4", "3 + 2 o 2 + 3", "UNO-dos-tres UNO-dos", "<i>Take Five</i> (Brubeck)"],
        ["7/8", "2 + 2 + 3", "UNO-dos UNO-dos UNO-dos-tres", "Danzas de los Balcanes"],
        ["5/8", "3 + 2", "UNO-dos-tres UNO-dos", "Folclore y rock progresivo"],
        ["11/8", "3 + 3 + 3 + 2", "Cuatro grupos", "Música de los Balcanes"]])
    + "<h4>La hemiola: cuando 3 se convierte en 2</h4>"
    "<p>Dos compases de 3/4 (seis pulsos) pueden agruparse <b>3+3</b> (normal) o <b>2+2+2</b> (hemiola). Es un efecto muy usado en el Barroco y en el Romanticismo, normalmente antes de una cadencia, para «frenar» la música antes del final.</p>"
    + "[[partitura:hemiola]]"
    + pasos([
        ("Toca los seis pulsos con el acento en 1-4 (3+3).",
         "es el ritmo normal: dos compases de 3/4."),
        ("Ahora acentúa 1-3-5 (2+2+2).",
         "es lo mismo, pero el acento cae cada dos pulsos. Mira cómo se mueve el pie."),
        ("Mantén el pulso con el pie y toca los dos acentos de la hemiola.",
         "tu pie no debe cambiar: el cambio es solo del acento."),
    ])
    + "<h4>Cambios de compás</h4>"
    + lista(["En ocasiones el compás cambia a mitad de la obra (por ejemplo, de 4/4 a 3/4). El <b>pulso</b> (negra) normalmente <b>se mantiene</b>: solo cambia cuántos pulsos hay en cada grupo.",
             "Si cambia el <b>pulso</b> (de negra a negra con puntillo, como de 3/4 a 6/8) la partitura lo indica con una igualdad: ♩ = ♩.",
             "Siempre que cambie el compás, vuelve a contar desde el 1 del nuevo compás."], "🔄")
    + "[[quiz:r10a|En una hemiola, ¿cómo se acentúan las seis negras de dos compases de 3/4?|En 1 y 4 (3+3);En 1, 3 y 5 (2+2+2);En todas por igual|1|La hemiola es 2+2+2, como si fuera un compás de 3/2.]]"
    "[[quiz:r10b|¿Cómo se agrupa normalmente un compás de 7/8?|3+4 o 2+2+3;1+6;Siete pulsos iguales|0|Los compases de amalgama se agrupan en 2 y 3.]]"
    + errores([
        ["Pierdo el pulso en los compases irregulares", "Intento sentir los siete o cinco a la vez", "Siente los grupos (2+2+3) y cuéntalos en voz alta"],
        ["La hemiola me suena «rara»", "Cambio el pulso en lugar del acento", "Mantén el pie constante y cambia solo dónde acentúas"]]))) ]

# Módulo 11 · Séptimas en la escala y extensiones ---------------------------------------------------
TEORIA_EXTRA[11] = [(QUIZ, (
    "<h3>Armonizar con séptimas</h3>"
    "<p>Si en la armonización de la escala se añade una cuarta nota (otra tercera encima), cada acorde se convierte en un acorde de <b>séptima</b>. Los tipos dependen, otra vez, de dónde caen los semitonos:</p>"
    + tabla(["Grado", "Do mayor", "Cifrado", "Notas", "Tipo"], [
        ["I", "Do mayor 7", "Cmaj7", "Do–Mi–Sol–Si", "Mayor con 7.ª mayor"],
        ["ii", "Re menor 7", "Dm7", "Re–Fa–La–Do", "Menor con 7.ª menor"],
        ["iii", "Mi menor 7", "Em7", "Mi–Sol–Si–Re", "Menor con 7.ª menor"],
        ["IV", "Fa mayor 7", "Fmaj7", "Fa–La–Do–Mi", "Mayor con 7.ª mayor"],
        ["V", "Sol 7 (dominante)", "G7", "Sol–Si–Re–Fa", "Mayor con 7.ª menor"],
        ["vi", "La menor 7", "Am7", "La–Do–Mi–Sol", "Menor con 7.ª menor"],
        ["vii", "Si semidisminuido", "Bm7♭5 (Bø7)", "Si–Re–Fa–La", "Disminuido con 7.ª menor"]])
    + caja("Para recordarlo:", "en toda tonalidad mayor: I y IV = <b>maj7</b>; ii, iii y vi = <b>m7</b>; V = <b>7</b> (el único dominante); vii = <b>m7♭5</b>.")
    + "<h4>El ii–V–I en tonalidad menor</h4>"
    + "<p>En menor, el ii es un acorde <b>semidisminuido</b> (m7♭5) y el V suele llevar la sensible, por lo que el acorde queda como 7 (con la 3.ª mayor). Se llama «ii–V–i» (la «i» pequeña indica tónica menor).</p>"
    + "[[partitura:iivi_menor]]"
    + "<h4>Extensiones: 9, 11 y 13</h4>"
    + "<p>Si se siguen apilando terceras sobre la 7.ª, se obtienen las «extensiones» o tensiones. Se numeran por intervalos <b>más allá de la octava</b>: 9.ª = 2.ª + octava, 11.ª = 4.ª + octava, 13.ª = 6.ª + octava.</p>"
    + tabla(["Extensión", "Intervalo desde la fundamental", "En C", "Cómo suena"], [
        ["9", "9.ª (Re)", "C9 = Do–Mi–Sol–Si♭–Re", "Color de jazz, brillante"],
        ["11", "11.ª (Fa)", "Cm11", "Abierto, a menudo en acordes menores"],
        ["13", "13.ª (La)", "C13 = Do–Mi–Si♭–La", "Color blues y swing"],
        ["♯11, ♭9, ♭13…", "Con alteración", "G7♭9 = Sol–Si–Re–Fa–La♭", "Tensión extra antes de resolver"]])
    + "<p>No hace falta tocar todas las notas: los pianistas de jazz tocan solo la <b>3.ª, la 7.ª y una o dos extensiones</b> (voicings), y dejan la fundamental al bajo.</p>"
    + "[[partitura:ej_septimas]]"
    + "[[quiz:r11a|En una tonalidad mayor, ¿qué tipo de acorde de séptima es el del V grado?|Mayor 7;Menor 7;Dominante (7)|2|Es el único acorde de séptima de dominante: G7 en Do mayor.]]"
    "[[quiz:r11b|¿Qué acorde es el vii de Do mayor con séptima?|Bm7♭5;Bmaj7;B7|0|Es un acorde semidisminuido: Si–Re–Fa–La.]]"
    "[[quiz:r11c|¿Qué notas se tocan en un voicing «de shell»?|Solo fundamental y quinta;La tercera y la séptima;Las siete notas de la escala|1|La 3.ª y la 7.ª definen el acorde.]]"
    + errores([
        ["Mi G7 suena como Gmaj7", "Toco Si natural y Fa♯", "G7 es Sol–Si–Re–Fa natural: la 7.ª es menor"],
        ["Confundo Cmaj7 y C7", "Solo miro la «7»", "maj7 lleva Si natural; 7 lleva Si♭"]]))) ]

# Módulo 12 · El blues a fondo -----------------------------------------------------------------------
TEORIA_EXTRA[12] = [(QUIZ, (
    "<h3>El blues de 12 compases, compás a compás</h3>"
    + tabla(["Compases", "Acorde (en Do)", "Grado", "Frase"], [
        ["1-4", "C7 · C7 · C7 · C7", "I7", "Primer verso: plantea la idea"],
        ["5-6", "F7 · F7", "IV7", "Cambio de color"],
        ["7-8", "C7 · C7", "I7", "Vuelta a casa"],
        ["9", "G7", "V7", "Tensión"],
        ["10", "F7", "IV7", "Bajada"],
        ["11", "C7", "I7", "Casa"],
        ["12", "G7 (turnaround)", "V7", "Prepara el siguiente coro"]])
    + "<p>El texto de un blues tradicional tiene tres versos: AAB. Se canta (o se toca) el primer verso, se repite casi igual y el tercero responde. Cada verso ocupa <b>4 compases</b>: dos para «cantar» la frase y dos de respuesta instrumental.</p>"
    + "<h4>¿Qué escalas sirven para improvisar?</h4>"
    + tabla(["Escala", "En Do", "Cuándo se usa", "Sonido"], [
        ["Pentatónica menor", "Do–Mi♭–Fa–Sol–Si♭", "Sobre todo el blues", "Clásico, oscuro"],
        ["Escala de blues", "Do–Mi♭–Fa–<b>Fa♯</b>–Sol–Si♭", "Cuando quieras «nota azul»", "Más cargado de blues"],
        ["Pentatónica mayor", "Do–Re–Mi–Sol–La", "Blues alegres, rock and roll", "Brillante"],
        ["Mixolidio", "Do–Re–Mi–Fa–Sol–La–Si♭", "Sobre los acordes dominantes", "Rico, con todas las notas del C7"]])
    + caja("La nota azul:", "es la nota que «no encaja» del todo (la 3.ª menor Mi♭ sobre un acorde con 3.ª mayor Mi). Se toca como un pequeño deslizamiento de Mi♭ a Mi. Es la que da el color del blues.")
    + "<h4>El turnaround</h4>"
    "<p>Los últimos compases (11-12) se llaman <b>turnaround</b> («vuelta»): preparan el regreso al principio. El más sencillo es C7 – G7. Otros más elaborados usan I–vi–ii–V (C7 – A7 – D7 – G7).</p>"
    + "[[quiz:r12a|¿En qué compases del blues de 12 compases aparece el acorde del IV grado por primera vez?|Compases 1 a 4;Compases 5 y 6;Compases 9 y 10|1|Compases 5 y 6: F7 en Do.]]"
    "[[quiz:r12b|¿Qué es un turnaround?|Un cambio de tonalidad;Los últimos compases que preparan la vuelta al principio;Un adorno de la mano izquierda|1|Suele ser I–V o I–vi–ii–V.]]"
    + errores([
        ["Pierdo el sitio en los 12 compases", "No tengo mapa mental", "Aprende el esquema 4 + 2 + 2 + 1 + 1 + 1 + 1 y cuéntalo en voz alta"],
        ["Mi improvisación suena a ejercicio", "Toco notas seguidas", "Usa silencios y repite ideas cambiando el final"]]))) ]

# Módulo 13 · Dinámica, articulación y carácter ------------------------------------------------------
TEORIA_EXTRA[13] = [('<h3>Haz un «mapa» de la obra</h3>', (
    "<h3>Dinámica, articulación y carácter</h3>"
    "<h4>1. Dinámica: cuánto suena</h4>"
    + tabla(["Signo", "Se lee", "Significa", "Cómo se consigue"], [
        ["<i>pp</i>", "pianissimo", "Muy suave", "Dedos pegados a las teclas, poco peso"],
        ["<i>p</i>", "piano", "Suave", "Peso ligero del brazo"],
        ["<i>mp</i>", "mezzopiano", "Medio suave", "Un poco más que <i>p</i>"],
        ["<i>mf</i>", "mezzoforte", "Medio fuerte", "El volumen de «hablar normal»"],
        ["<i>f</i>", "forte", "Fuerte", "Más peso de brazo, no más tensión"],
        ["<i>ff</i>", "fortissimo", "Muy fuerte", "El brazo entero, sin golpear"],
        ["<i>crescendo</i> (&lt;)", "creciendo", "Aumentar poco a poco", "Peso creciente del brazo"],
        ["<i>diminuendo</i> (&gt;)", "disminuyendo", "Disminuir poco a poco", "Peso decreciente"],
        ["<i>sf</i>, <i>sfz</i>", "sforzando", "Acento súbito y fuerte", "Un golpe de peso en una sola nota"]])
    + "<h4>2. Articulación: cómo se ataca y se suelta</h4>"
    + tabla(["Signo", "Nombre", "Cómo se toca"], [
        ["Arco sobre notas distintas", "Legato", "Unidas: no sueltes una tecla hasta tocar la siguiente"],
        ["Punto sobre la nota", "Staccato", "Cortada: dura la mitad o menos de su valor"],
        ["Raya sobre la nota", "Tenuto", "Mantenida el valor completo, con un ligero peso"],
        [">", "Acento", "Más fuerte que las notas que la rodean"],
        ["Cuña ▾", "Marcato", "Muy marcada y corta"],
        ["Punto + raya", "Portato", "Entre el legato y el staccato"]])
    + "[[partitura:dinamicas]]"
    + "<h4>3. Carácter: el «cómo» expresivo</h4>"
    + tabla(["Término", "Significa"], [
        ["<i>dolce</i>", "Dulce, suave"], ["<i>cantabile</i>", "Cantando"], ["<i>espressivo</i>", "Con expresión"],
        ["<i>maestoso</i>", "Majestuoso"], ["<i>leggiero</i>", "Ligero"], ["<i>con brio</i>", "Con energía"],
        ["<i>agitato</i>", "Agitado"], ["<i>tranquillo</i>", "Tranquilo"], ["<i>sempre</i>", "Siempre"],
        ["<i>poco a poco</i>", "Poco a poco"], ["<i>molto</i>", "Mucho"], ["<i>meno</i> / <i>più</i>", "Menos / más"]])
    + caja("Combina términos:", "<i>poco a poco crescendo</i> = ir creciendo lentamente; <i>più mosso</i> = un poco más rápido; <i>meno forte</i> = menos fuerte. Con una veintena de palabras italianas entiendes casi cualquier partitura.")
    + "[[quiz:r13a|¿Qué significa «mf»?|Muy fuerte;Mezzoforte: medio fuerte;Mezzopiano: medio suave|1|mf = mezzoforte.]]"
    "[[quiz:r13b|¿Cuál es la diferencia entre staccato y tenuto?|El staccato se corta y el tenuto se mantiene su valor;No hay diferencia;El tenuto es más rápido|0|El staccato acorta la nota y el tenuto la mantiene.]]"
    "[[quiz:r13c|«Poco a poco crescendo» significa…|Ir creciendo bruscamente;Ir creciendo muy poco a poco;Pasar a piano|1|Es un crescendo lento y gradual.]]"
    + errores([
        ["El crescendo me sale de golpe", "Empiezo demasiado fuerte", "Empieza más suave de lo que crees y reparte el peso en toda la frase"],
        ["Mi staccato suena duro", "Golpeo con los dedos", "Toca desde la muñeca, con la mano suelta, como si las teclas quemaran"]]))) ]
