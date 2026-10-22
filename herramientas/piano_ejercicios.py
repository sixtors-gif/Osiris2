"""Ejercicios prácticos y planning de 6 meses para el curso de piano (páginas ejercicios.html y planificacion.html)."""
import html

# (id, título, nivel 1-3, minutos, partituras, qué trabaja, pasos, meta)
# partituras: lista de claves de PIEZAS (puede estar vacía); un paso puede ser (paso, cómo se hace)
BLOQUES = [
 ("A", "Calentamiento y dedos", "🖐️", "Para empezar cada sesión y preparar las manos. Siempre despacio y sin tensión.", [
  ("A1", "Cinco dedos en Do", 1, 5, ["ej_5dedos"], "Igualdad de los dedos, forma de la mano y control del staccato y los acentos.",
   ["Mano derecha sola, ligado, a ♩ = 60. Cada dedo cae desde la yema, sin levantarse mucho.",
    "Repite con staccato (compás 2) y con acentos (compás 3).",
    "Haz lo mismo con la izquierda y luego manos juntas.",
    "Súbelo a ♩ = 80 cuando salga tres veces seguidas sin errores."],
   "Tocar los cuatro compases con las dos manos a ♩ = 80, sin tensión en hombros ni muñecas."),
  ("A2", "Notas largas con peso de brazo", 1, 3, [], "Sonido lleno y relajado: la base de la técnica avanzada.",
   [("Siéntate con los brazos colgando y apoya el 3.er dedo en una tecla.", "los codos quedan un poco por encima de las teclas y los hombros caídos. Imagina que la mano es un puente firme y el brazo, un peso que cae."),
    ("Deja que el peso del brazo baje la tecla, sin empujar.", "no «tocas»: dejas caer. Escucha el sonido: debe ser redondo, sin golpe."),
    "Mantén la nota 4 segundos, suelta y cambia de dedo. Repite con los cinco dedos de cada mano.",
    "Comprueba que el hombro y la muñeca están sueltos."],
   "Cinco notas largas, con cada dedo, de sonido igual y sin dolor ni tensión."),
  ("A3", "Paso del pulgar en grupos de tres", 2, 5, ["ej_pulgar"], "El paso del pulgar por debajo de la mano (y del 3.º por encima), base de las escalas.",
   [("Mano derecha sola, subiendo, a ♩. = 60: dedos 1-2-3, 1-2-3…", "al tocar el 3.º, el pulgar ya viaja por debajo de la mano hacia su próxima tecla; así llega «preparado», sin saltar."),
    "Baja con 3-2-1. Observa que el codo no se abre.",
    "Izquierda sola (al revés: sube 3-2-1 y baja 1-2-3).",
    "Manos juntas, muy lento."],
   "Subir y bajar un compás completo sin que se oiga el paso del pulgar."),
  ("A4", "Escala cromática", 2, 5, ["cromatica"], "Agilidad, independencia de los dedos y conocimiento del teclado.",
   [("Aprende la regla de los dedos antes de tocar.", "negras con 3; blancas con 1; en las parejas de blancas seguidas (Mi–Fa, Si–Do) la segunda va con 2."),
    "Toca despacio, una nota por pulso, con metrónomo.",
    "Sube a dos notas por pulso (corcheas) cuando salga limpio.",
    "Repite bajando y después con los ojos cerrados."],
   "Una octava ascendente y descendente a ♩ = 72 en corcheas, sin parar."),
 ]),
 ("B", "Escalas y arpegios", "🎼", "La gimnasia diaria del pianista. Varía cada día una cosa: el ritmo, el tono o el modo.", [
  ("B1", "La escala de Do con ritmos", 2, 8, ["ej_ritmos_escala"], "Igualdad de los dedos y control del ritmo.",
   ["Toca cada compás cuatro veces seguidas (largo-corto, corto-largo, tresillos).",
    "Mantén el pulso con metrónomo y cuenta en voz alta.",
    "Los dedos que tocan la nota corta lo hacen más ligeros, no más rápidos.",
    "Repite en Sol y en Fa mayor."],
   "Los tres ritmos a ♩ = 66, sin acelerar en las notas cortas."),
  ("B2", "Escalas de Do, Sol y Fa mayor", 1, 10, ["escala_do", "escala_sol", "escala_fa"], "Digitación, paso del pulgar y conocimiento de las tonalidades.",
   [("Manos separadas, una octava, a ♩ = 60.", "usa la digitación indicada. En Fa, la derecha usa 1-2-3-4-1-2-3-4 para que el pulgar no caiga en el Si♭."),
    "Manos juntas, dos octavas, a ♩ = 72.",
    "Varía la articulación: legato, staccato y con acento en el primer tiempo de cada grupo.",
    "Añade un crescendo subiendo y un diminuendo bajando."],
   "Las tres escalas a ♩ = 72, manos juntas, sin errores tres veces seguidas."),
  ("B3", "Arpegios de Do, Sol y Fa", 2, 8, ["ej_arpegios_tres"], "Desplazamiento lateral del brazo y paso del pulgar en los arpegios.",
   [("Toca primero cada acorde en bloque (todas las notas a la vez).", "así la mano aprende la forma. Solo después se «despliega» el acorde."),
    "Arpegio con una mano, subiendo y bajando, a ♩ = 60.",
    ("Lleva el brazo con la mano.", "el codo y el antebrazo se desplazan en horizontal; el pulgar no se estira."),
    "Manos juntas, con la izquierda una octava por debajo."],
   "Los tres arpegios a ♩ = 60, uniformes y sin saltos de volumen."),
  ("B4", "Los modos desde Do", 3, 10, ["modos_do"], "Oído de los colores de cada modo y conocimiento de las alteraciones.",
   ["Toca cada modo escuchando sus notas características (Mi♭, Fa♯, Si♭…).",
    "Toca solo la nota de partida y las características: ¿qué sensación da cada una?",
    "Inventa una melodía de cuatro notas en cada modo.",
    "Toca la melodía del modo dórico sobre un acorde de Dm7 en la izquierda."],
   "Identificar de oído el mayor, el dórico y el mixolidio tocados por otra persona."),
  ("B5", "La escala de La menor, en las tres formas", 2, 8, ["escala_lam"], "Escalas menores: natural, armónica y melódica.",
   ["Toca la natural, la armónica (Sol♯) y la melódica (Fa♯ y Sol♯ subiendo) en ese orden.",
    "Di en voz alta el patrón T–S–T–T–S–T–T mientras tocas la natural.",
    "Escucha la 2.ª aumentada entre Fa y Sol♯ en la armónica.",
    "Repite con Mi menor y Re menor."],
   "Las tres formas de La menor, manos juntas, a ♩ = 66."),
 ]),
 ("C", "Lectura", "👁️", "Leer rápido libera la cabeza para pensar en la música. Cada día, 10 minutos y música nueva.", [
  ("C1", "Lectura a primera vista · nivel 1", 1, 10, ["ej_lectura1"], "Lectura con notas vecinas y terceras, sin cambios de posición.",
   [("30 segundos de escaneo: armadura, compás, notas extremas y ritmos raros.", "di en voz alta la armadura («sin alteraciones»), el compás y el nombre de la primera nota de cada mano. Ponte el dedo en la posición."),
    "Pon el metrónomo a ♩ = 60 y toca sin parar, aunque falles.",
    "Mira siempre por delante de lo que tocas.",
    "Repítela una vez más: ¿qué ha mejorado?"],
   "Tocarla a ♩ = 72 sin detenerte."),
  ("C2", "Lectura a primera vista · nivel 2", 2, 10, ["ej_lectura2"], "Una alteración en la armadura y ritmo con puntillo, en 3/4.",
   ["Escaneo: ¿cuál es el Fa♯ de la armadura? ¿dónde aparece?",
    "Cuenta «1-2-3» en voz alta en el primer compás; la corchea con puntillo es «1-y-a».",
    "Toca sin parar a ♩ = 72.",
    "Repite y compara."],
   "Tocarla a ♩ = 88 sin detenerte."),
  ("C3", "Lectura a primera vista · nivel 3", 3, 10, ["ej_lectura3"], "Un bemol en la armadura, 6/8 y manos con ritmos distintos.",
   ["Escaneo: Si♭ en la armadura, 6/8 (dos pulsos).",
    "Marca los dos pulsos con el pie (♩.) y toca a un tempo lento.",
    "Mira dónde cambia la mano izquierda y prepárala antes.",
    "Repite subiendo el tempo en 4 bpm."],
   "Tocarla a ♩. = 60 sin detenerte."),
  ("C4", "Entrenador de notas «faro»", 1, 5, [], "Reconocer notas en las dos claves al instante.",
   ["Abre el entrenador de lectura (módulo 2) y elige «Sol y Fa mezcladas».",
    "Responde sin pensar «desde abajo»: identifica el faro más cercano y cuenta desde ahí.",
    "Hazlo 5 minutos al día.",
    "Anota tu racha de aciertos."],
   "Racha de 15 aciertos seguidos."),
  ("C5", "Entrenador de intervalos", 2, 5, [], "Reconocer número y calidad de un intervalo de un vistazo.",
   ["Abre el entrenador de intervalos (módulo 2).",
    "Primero decide el número contando los nombres de nota; luego la calidad contando semitonos.",
    "Cuando te equivoques, cuenta los semitonos en el teclado y tócalo.",
    "Repite 5 minutos al día."],
   "8 aciertos de 10."),
  ("C6", "Saltos e intervalos en bloque", 2, 8, ["ej_saltos", "ej_intervalos"], "Medir distancias con la mano sin mirar el teclado.",
   [("Toca cada salto diciendo en voz alta el intervalo.", "mira la nota de destino antes de saltar y coloca la mano en el aire sobre ella. No mires la nota de la que sales."),
    "Mantén el pulso: el salto es rápido y limpio, no frenado.",
    "Toca las terceras y quintas en bloque: las dos notas suenan a la vez y con el mismo peso.",
    "Repite con los ojos cerrados."],
   "Los ocho saltos sin mirar el teclado, a ♩ = 72."),
 ]),
 ("D", "Ritmo e independencia", "🥁", "Contar con la voz, marcar con el pie y mantener cada mano con su propia vida.", [
  ("D1", "Síncopas con las dos manos", 2, 8, ["ej_sincopas"], "Sentir el contratiempo sin perder el pulso.",
   [("Toca la mano izquierda sola hasta que sea automática.", "toca los acordes con un toque firme y regular; no pienses en las notas."),
    "Cuenta «1-y-2-y-3-y-4-y» en voz alta y toca el compás de la derecha en una sola nota.",
    "Une las dos manos muy despacio.",
    "Sube el tempo en pasos de 4 bpm."],
   "Los cuatro compases a ♩ = 72, contando en voz alta."),
  ("D2", "Ostinato y melodía", 3, 10, ["ej_independencia"], "Independencia entre manos y equilibrio de volumen.",
   ["Izquierda sola hasta que salga «sin pensar» (cuenta o habla mientras la tocas).",
    "Derecha sola, cantando la melodía.",
    ("Juntas, compás a compás, con la izquierda <i>p</i> y la derecha <i>mf</i>.", "toca la melodía con el brazo (más peso) y el ostinato con las yemas (más ligero)."),
    "Grábate y escucha: ¿se entiende la melodía sin esfuerzo?"],
   "Tocar los nueve compases a ♩ = 72 con el ostinato regular y la melodía cantada."),
  ("D3", "Hemiola", 2, 5, ["hemiola"], "Cambiar el acento sin cambiar el pulso.",
   ["Toca los seis primeros compases contando 1-2-3 en cada compás.",
    "En los compases 5 y 6, cambia el acento: cuenta 1-2 · 1-2 · 1-2 sin dejar de marcar el pulso con el pie.",
    "Escucha la grabación del módulo: ¿oyes el cambio de grupo?",
    "Repite con las dos manos."],
   "Mantener el pie en 3/4 mientras la derecha acentúa en 2+2+2."),
  ("D4", "Compases: cuenta y acentos", 1, 5, ["compases"], "Reconocer y sentir los cuatro compases principales.",
   ["Escucha la partitura y cuenta en voz alta con los números que aparecen escritos.",
    "Dale palmadas fuertes en el 1 y suaves en los demás.",
    "Toca cada compás con una sola nota, acentuando el primer tiempo.",
    "Repite con la mano izquierda."],
   "Acentuar bien el 1 en los cuatro compases, sin acelerar."),
  ("D5", "Tres contra dos", 3, 10, ["poli32"], "Coordinación de dos ritmos distintos.",
   ["Practica sobre una mesa: izquierda 2 golpes, derecha 3, durante un pulso.",
    "Cuenta la cuadrícula de 6 en voz alta (1-2-3-4-5-6).",
    "Pasa al piano con una nota por mano.",
    "Cuando salga, toca la partitura a velocidad 50 %."],
   "Mantener 3 contra 2 durante 8 compases sin perderte."),
 ]),
 ("E", "Armonía y acordes", "🧭", "Aplicar la teoría: acordes de la escala, progresiones, cadencias y transporte.", [
  ("E1", "Los siete acordes de Do mayor", 1, 8, ["armonizar_do"], "Armonizar la escala y conocer los tipos de acorde.",
   ["Toca el ejemplo y di el nombre y el tipo de cada acorde.",
    "Toca los siete acordes subiendo y bajando en las tres inversiones.",
    ("Repite en Sol mayor: antes de tocar, escribe los siete acordes.", "apila terceras sobre cada nota de la escala de Sol (con Fa♯) y aplica la regla: I, IV y V mayores; ii, iii y vi menores; vii°, disminuido."),
    "Comprueba tu escritura tocando cada acorde."],
   "Los siete acordes de Do y de Sol, sin dudar, subiendo y bajando."),
  ("E2", "Acordes sus y bajos distintos", 2, 5, ["sus_slash"], "Reconocer el color de los sus y de las inversiones por el bajo.",
   ["Toca el ejemplo escuchando cada acorde.",
    "Toca Csus2, Csus4 y C, y fíjate en qué «pide» cada uno.",
    "Practica C/E y C/G: la mano izquierda cambia el bajo y la derecha no se mueve.",
    "Inventa un enlace C – Csus4 – C – C/E – F."],
   "Distinguir de oído un acorde sus4 de un mayor."),
  ("E3", "Progresiones I–V–vi–IV y I–vi–IV–V", 2, 10, ["progresiones"], "Acompañar con las progresiones más usadas.",
   ["Toca las dos progresiones con bloque en la derecha y fundamental en la izquierda.",
    ("Transpórtalas a Sol y a Fa mayor.", "escribe primero los acordes: en Sol, I=Sol, V=Re, vi=Mi m, IV=Do. Luego toca."),
    "Toca una canción conocida (de memoria) con estos acordes.",
    "Prueba con otro patrón de la izquierda (arpegio, Alberti, vals)."],
   "Acompañar una canción de memoria con la progresión adecuada."),
  ("E4", "La progresión del Canon", 2, 10, ["canon_prog"], "Bajo descendente y cambio suave de acordes.",
   ["Toca solo el bajo (Do, Sol, La, Mi, Fa, Do, Fa, Sol) con la izquierda.",
    "Toca los acordes de la derecha sin cambiar de posición más de lo necesario.",
    "Une las dos manos a ♩ = 60.",
    "Inventa una melodía en la derecha sobre los mismos acordes (pentatónica)."],
   "Tocar los ocho compases sin parar a ♩ = 66."),
  ("E5", "Cadencia en La menor", 2, 5, ["ej_cadencia_lam"], "La sensible y el acorde de dominante mayor en la tonalidad menor.",
   ["Toca la cadencia lentamente y escucha el Sol♯.",
    "Toca la misma con Sol natural: ¿qué ha cambiado?",
    "Transpórtala a Mi menor y a Re menor.",
    "Escríbela en Si menor."],
   "Tocar la cadencia en tres tonalidades menores."),
  ("E6", "Arpegios de séptima", 3, 8, ["ej_septimas"], "Los acordes de cuatro notas y su color.",
   ["Toca los arpegios despacio y escucha cómo suena cada acorde.",
    ("Toca después los acordes en bloque y reconoce las 7.as.", "Cmaj7 = Do–Mi–Sol–Si; Dm7 = Re–Fa–La–Do; G7 = Sol–Si–Re–Fa."),
    "Repite en Fa mayor (Fmaj7 – Gm7 – C7 – Fmaj7).",
    "Inventa un enlace con las cuatro notas en la derecha."],
   "Los arpegios de los tres acordes en dos tonalidades, a ♩ = 66."),
  ("E7", "ii–V–i en menor", 3, 10, ["iivi_menor"], "Voice leading mínimo en tonalidad menor.",
   ["Toca los acordes lentamente y escucha el movimiento de las dos notas de arriba.",
    "Cántalas: D–D–C y A–G♯–G.",
    "Transpórtalo a Re menor (Em7♭5 – A7 – Dm).",
    "Añade un ritmo de bossa nova en la derecha."],
   "Tocar el ii–V–i en La menor y en Re menor sin mirar la partitura."),
  ("E8", "Transportar una melodía", 3, 10, ["ej_transporte"], "Leer los grados y reconocer las tonalidades.",
   ["Toca la melodía en Do mayor y piensa en los grados (1-3-5-3…).",
    "Escribe la misma melodía en Sol mayor y compárala con la partitura.",
    ("Tócala en Fa mayor y en Re mayor (sin partitura).", "cambia solo la nota de partida y la armadura. La forma de la mano es la misma."),
    "Toca la melodía con acompañamiento en las tres tonalidades."],
   "Tocar la melodía de memoria en cuatro tonalidades."),
  ("E9", "Entrenador de armaduras", 2, 5, [], "Reconocer tonalidades y armaduras al instante.",
   ["Abre el entrenador de armaduras (módulo 3).",
    "Reconoce primero los sostenidos o bemoles y luego aplica la regla.",
    "Cuando te equivoques, mira el círculo de quintas y averigua por qué.",
    "Repite 5 minutos al día."],
   "10 aciertos seguidos."),
 ]),
 ("F", "Oído e improvisación", "🎵", "Crear música propia y reconocer lo que suena. Se aprende improvisando poco, pero cada día.", [
  ("F1", "Improvisar con la pentatónica", 2, 10, ["pentatonica", "ej_pentatonica"], "Crear melodías con pocas notas, con ritmo y silencios.",
   ["Toca la escala pentatónica de Do mayor y la de La menor.",
    "Toca el ejemplo de pregunta y respuesta.",
    ("Improvisa una frase de dos compases con tres notas y otra que la conteste.", "empieza con un ritmo sencillo y repítelo cambiando las notas. Termina siempre en Do."),
    "Graba un minuto de improvisación y elige la mejor frase."],
   "Improvisar un minuto con la pentatónica sin bloquearte."),
  ("F2", "Blues: pregunta y respuesta", 3, 10, ["blues_frase"], "Fraseo y nota azul.",
   ["Toca el bajo boogie con la izquierda hasta que sea automático.",
    "Toca la frase de ejemplo con swing.",
    "Cambia el final de la frase y repítela.",
    "Añade la nota azul (Mi♭ → Mi)."],
   "Improvisar un coro de 12 compases con silencios y repetición de ideas."),
  ("F3", "Cantar y tocar", 1, 5, [], "Relacionar el oído con los dedos.",
   ["Canta una nota (por ejemplo, Do) y búscala en el teclado.",
    "Canta una frase sencilla de cuatro notas y tócala de oído.",
    "Haz lo mismo con una melodía conocida.",
    "Anota en cuántos intentos la encuentras."],
   "Sacar de oído una melodía de cuatro notas en tres intentos o menos."),
  ("F4", "Reconocer cadencias de oído", 2, 5, [], "Distinguir cadencias perfecta, plagal, semicadencia y rota.",
   ["Pide a alguien que toque I–IV–V7–I, I–IV–I, I–IV–V y I–IV–V7–vi sin decir cuál es cada una.",
    "Adivina cuál es. Si no hay nadie, grábalas y escúchalas pasado un día.",
    "Escribe la respuesta.",
    "Comprueba tus aciertos."],
   "Reconocer las cuatro cadencias 4 de 5 veces."),
 ]),
 ("G", "Interpretación", "🎹", "Convertir las notas en música: dinámica, frases, forma y memoria.", [
  ("G1", "Dinámica y articulación", 2, 8, ["dinamicas"], "Control del volumen y del ataque de la nota.",
   [("Toca el primer compás <i>p</i> y ligado, con el peso del brazo ligero.", "los dedos «acarician» la tecla sin dejarla caer de golpe."),
    "Haz el crescendo del segundo compás repartiendo el peso del brazo.",
    "El staccato sale de la muñeca, con la mano suelta.",
    "Graba y comprueba que se oyen los matices."],
   "Que un oyente distinga todos los matices de la grabación."),
  ("G2", "Antecedente y consecuente", 2, 8, ["periodo"], "Frasear: pregunta, respuesta y respiración.",
   ["Toca la primera frase terminando en el V con una pequeña pausa: «pregunta».",
    "Toca la segunda frase cerrando con calma en el I: «respuesta».",
    ("Marca las respiraciones con una coma al final de cada frase.", "acorta un poco la última nota de la frase y levanta la mano, como una pequeña pausa al hablar."),
    "Toca poniendo un crescendo al principio de cada frase y un diminuendo al final."],
   "Que se note dónde acaba cada frase sin que se pierda el pulso."),
  ("G3", "Forma A–B–A", 2, 8, ["forma_aba"], "Dar carácter distinto a cada sección.",
   ["Toca A con un carácter (por ejemplo, <i>dolce</i>) y B con otro (<i>más vivo</i>).",
    "Cuando vuelve A, toca un poco más suave que la primera vez.",
    "Ensaya el paso de A a B sin cortes.",
    "Graba y escucha: ¿distingues las tres secciones?"],
   "Que el oyente distinga las tres secciones sin ver la partitura."),
  ("G4", "El mapa de una obra", 3, 15, [], "Entender la obra antes de tocarla.",
   [("Divide la pieza en frases y numéralas.", "cantando la melodía, donde respiras acaba una frase. Casi todas duran 4 u 8 compases."),
    ("Marca el punto culminante de cada frase con un círculo.", "suele ser la nota más aguda, la más larga o la del acorde más tenso."),
    "Dibuja las flechas de crecimiento y relajación, y las respiraciones.",
    "Toca siguiendo el mapa, exagerando todo el doble."],
   "Un mapa completo de una obra de 16 compases."),
  ("G5", "Grabarse y autoevaluarse", 1, 10, [], "Escuchar lo que de verdad suena.",
   [("Graba la pieza con el móvil, sin repetir ni parar.", "colócalo encima del piano a un metro. Haz una sola toma: la que suena es la que importa."),
    ("Escucha con la partitura y rellena la tabla de abajo.", "puntúa de 1 a 5: pulso, notas, sonido, dinámica, frases y pedal. Anota en qué compás está cada problema."),
    "Elige un solo problema para la sesión siguiente.",
    "Compara con la grabación de la semana anterior."],
   "Una tabla de autoevaluación rellena cada sábado."),
 ]),
]

NIVELES = {1: "★☆☆", 2: "★★☆", 3: "★★★"}


def lista_ejercicios():
    return [e for b in BLOQUES for e in b[4]]


def ejercicio_html(e, partitura):
    id_, titulo, nivel, minutos, partituras, trabaja, pasos, meta = e
    li = "".join(f"<li>{p[0]}<details class=\"como\"><summary>💡 Cómo se hace</summary><div class=\"como-cuerpo\">{p[1]}</div></details></li>" if isinstance(p, tuple) else f"<li>{p}</li>" for p in pasos)
    return (f'<div class="ejercicio" id="{id_}"><h4><span class="ej-id">{id_}</span> {titulo} <span class="ej-meta">{NIVELES[nivel]} · ⏱ {minutos} min</span></h4>'
            f'<p><b>Qué trabaja:</b> {trabaja}</p>' + "".join(partitura(k) for k in partituras)
            + f'<ol class="steps">{li}</ol><p class="ej-meta-fin">🎯 <b>Meta:</b> {meta}</p></div>')


def ejercicios_html(partitura):
    sal = ['<div class="palabras"><span class="pal-tag">Cómo usar esta página</span>'
           '<p>Es un <b>gimnasio</b>: cada ejercicio tiene un código (A1, B2, C3…) que el <b>planning de 6 meses</b> usa para decirte qué hacer cada semana. '
           'Cada uno indica qué trabaja, los pasos, cuánto dura, el nivel (★) y una <b>meta medible</b>. No hace falta hacerlos todos cada día: elige los de la semana.</p></div>',
           '<div class="box tip"><b>Regla de oro de cada ejercicio:</b> lento, sin tensión, con metrónomo y contando en voz alta. '
           'Cuando salga tres veces seguidas sin errores, sube 4 bpm. Si fallas dos veces seguidas, baja 4 bpm.</div>']
    sal.append("<h3>Índice</h3><div class=\"tabla-wrap\"><table class=\"tabla\"><tr><th>Bloque</th><th>Ejercicios</th></tr>"
               + "".join(f"<tr><td>{b[2]} <b>{b[0]} · {b[1]}</b></td><td>" + " · ".join(f'<a href="#{e[0]}">{e[0]}</a> {e[1]}' for e in b[4]) + "</td></tr>" for b in BLOQUES)
               + "</table></div>")
    for letra, titulo, ico, intro, ejs in BLOQUES:
        sal.append(f'<h2>{ico} {letra} · {titulo}</h2><p>{intro}</p>')
        sal += [ejercicio_html(e, partitura) for e in ejs]
    sal.append('<h3>Tabla de autoevaluación (para el ejercicio G5)</h3>' + tabla_autoeval())
    return "\n".join(sal)


def tabla_autoeval():
    filas = ["Pulso (¿se mantiene estable?)", "Notas (¿correctas?)", "Sonido (¿igual y sin golpes?)", "Dinámica (¿se oyen los matices?)", "Frases (¿se oyen las respiraciones?)", "Pedal (¿limpio?)"]
    return ('<div class="tabla-wrap"><table class="tabla"><tr><th>Criterio</th><th>1</th><th>2</th><th>3</th><th>4</th><th>5</th><th>Compás del problema</th></tr>'
            + "".join(f"<tr><td>{f}</td>" + "".join('<td><input type="radio" name="ev-%d" style="width:auto"></td>' % i for _ in range(5)) + '<td><input type="text" style="width:90px"></td></tr>' for i, f in enumerate(filas))
            + "</table></div>")


# ---------------------------------------------------------------------------------------------
# Planning de 6 meses
# ---------------------------------------------------------------------------------------------
MESES = [
 ("Mes 1 · Cimientos", "Semanas 1-4", "Estudiar bien, leer con seguridad y dominar las primeras escalas.",
  ["Tocar las escalas de Do, Sol y Fa mayor, manos juntas, dos octavas, a ♩ = 72 sin errores tres veces seguidas.",
   "Acertar 8 de 10 en el entrenador de intervalos y en el de notas faro.",
   "Tocar la lectura C1 sin detenerte y contar en voz alta compases de 2/4, 3/4, 4/4 y 6/8.",
   "Aplicar el plan de 20 minutos a un pasaje difícil."]),
 ("Mes 2 · Tonalidades y acordes", "Semanas 5-8", "Conocer el círculo de quintas y construir acordes.",
  ["Acertar 8 de 10 en el entrenador de armaduras.",
   "Tocar la escala de La menor en sus tres formas.",
   "Tocar las tríadas de Do, Sol y Fa en estado fundamental y en sus dos inversiones.",
   "Tocar el Minueto en Sol completo a ♩ = 80."]),
 ("Mes 3 · Armonía y primeras obras", "Semanas 9-13", "Entender la armonía y acompañar; empezar el repertorio.",
  ["Acompañar con las progresiones I–IV–V–I y I–V–vi–IV en tres tonalidades.",
   "Tocar el ostinato D2 con melodía a ♩ = 72.",
   "Hacer el pedal sincopado sin «hueco» ni «mezcla».",
   "Tocar los 24 primeros compases de la Sonatina y analizar el Preludio de Bach."]),
 ("Mes 4 · Repertorio y técnica", "Semanas 14-17", "Repertorio de Bach y Beethoven; octavas, terceras y adornos.",
  ["Tocar el tema A de «Para Elisa» a tempo.",
   "Tocar el Preludio BWV 846 completo y regular.",
   "Hacer trinos medidos y octavas sin tensión.",
   "Mantener 3 contra 2 durante 8 compases."]),
 ("Mes 5 · Jazz y blues", "Semanas 18-21", "Acordes de séptima, voicings, blues e improvisación.",
  ["Tocar los arpegios de séptima en dos tonalidades.",
   "Tocar el ii–V–I en Do mayor y el ii–V–i en La menor.",
   "Improvisar un coro de blues de 12 compases con silencios.",
   "Tocar las secciones A y B de la Gymnopédie n.º 1."]),
 ("Mes 6 · Interpretación y recital", "Semanas 22-26", "Frasear, memorizar y actuar.",
  ["Tener el mapa completo de la obra de recital.",
   "Tocar de memoria desde cualquier punto de entrada.",
   "Grabar un recital de 10 minutos con dos obras y un blues improvisado.",
   "Aprobar el examen final (70 %)."]),
]

# (semana, módulo, tema, ejercicios, obra de la semana, hito)
SEMANAS = [
 (1, "M1", "Método de estudio y metrónomo", "A1 A2 B2", "Minueto en Sol (Petzold): leer y analizar, manos separadas compases 1-8", "Escala de Do manos separadas a ♩ = 60 y plan de 20 minutos conocido"),
 (2, "M2", "Notas faro e intervalos", "A3 C1 C4 C5", "Minueto: manos separadas compases 9-16", "8/10 en el entrenador de notas faro y en el de intervalos"),
 (3, "M2", "El ritmo y los compases", "D4 D1 B1", "Minueto: manos juntas compases 1-8", "Contar en voz alta 2/4, 3/4, 4/4 y 6/8 y tocar la síncopa D1"),
 (4, "M3", "Escalas mayores: Do, Sol y Fa", "B2 B1 A3 C2", "Minueto: manos juntas, 16 compases", "Tres escalas mayores a ♩ = 72 (prueba del mes 1)"),
 (5, "M3", "Círculo de quintas y armaduras", "E9 E8 B2", "Minueto completo, lento", "8/10 en el entrenador de armaduras"),
 (6, "M3", "Escalas menores, pentatónica y cromática", "B5 A4 F1", "Minueto a ♩ = 80", "La menor en sus tres formas y la cromática a ♩ = 72"),
 (7, "M4", "Acordes, tríadas e inversiones", "E1 E2 C3", "Sonatina de Clementi op. 36 n.º 1: leer, analizar la forma", "Tríadas de Do y Sol en tres posiciones, sin dudar"),
 (8, "M4", "Arpegios, sus y bajos distintos", "B3 E2 A3", "Sonatina: compases 1-8, manos juntas", "Arpegios de Do, Sol y Fa a ♩ = 60 (prueba del mes 2)"),
 (9, "M5", "Funciones y cadencias", "E3 E5 F4", "Sonatina: compases 9-16", "Reconocer de oído cuatro cadencias 4 de 5 veces"),
 (10, "M5", "Progresiones, tonalidad y modulación", "E3 E4 E8", "Sonatina: compases 17-24", "Acompañar con I–V–vi–IV en tres tonalidades"),
 (11, "M6", "Independencia y acompañamientos", "D2 C6 A1", "Sonatina completa, lento", "Ostinato D2 a ♩ = 72"),
 (12, "M7", "El pedal", "A2 G1 D3", "Sonatina con dinámicas; pedal en una pieza lenta", "Pedal sincopado sin «hueco» ni «mezcla»"),
 (13, "M8", "Análisis de una obra: Preludio de Bach", "G4 E6 B1", "Preludio BWV 846: compases 1-8 en bloques, luego en arpegio", "Análisis armónico de los 8 primeros compases (prueba del mes 3)"),
 (14, "M8", "«Para Elisa» y análisis de la forma", "G2 G3 D4", "Para Elisa: tema A, manos separadas", "Forma del rondó escrita; mano derecha del tema A a ♩ = 60"),
 (15, "M9", "Técnica avanzada: octavas y terceras", "A2 A4 C6", "Para Elisa: tema A, manos juntas; BWV 846 compases 9-16", "Octavas y terceras sin tensión ni dolor"),
 (16, "M9", "Adornos y trinos", "D3 B3 F3", "Para Elisa: tema A a tempo; BWV 846 compases 17-24", "Trino medido a cuatro, tres y dos notas por pulso"),
 (17, "M10", "Polirritmia, hemiola y compases irregulares", "D5 D3 D1", "BWV 846 completo, regular", "3 contra 2 durante 8 compases (prueba del mes 4)"),
 (18, "M11", "Acordes de séptima", "E6 E1 B4", "Gymnopédie n.º 1 (Satie): leer y analizar la armonía", "Arpegios de séptima en dos tonalidades"),
 (19, "M11", "Voicings y ii–V–I", "E7 E6 F4", "Gymnopédie: compases 1-16", "ii–V–I en Do mayor y ii–V–i en La menor"),
 (20, "M12", "El blues a fondo", "F2 F1 D1", "Blues propio: 12 compases con bajo boogie", "Bajo boogie automático y frase de pregunta-respuesta"),
 (21, "M12", "Improvisación y reharmonización", "F1 F2 F3", "Blues: improvisar un coro; Gymnopédie completa", "Coro de 12 compases improvisado con silencios (prueba del mes 5)"),
 (22, "M13", "Estilos y expresión", "G1 G4 G5", "Obra del recital: elegir y hacer el mapa", "Mapa completo de la obra de recital"),
 (23, "M13", "Frases, forma y rubato", "G2 G3 G5", "Obra del recital: secciones A y B con dinámicas", "Grabación con las dinámicas del mapa"),
 (24, "M14", "Memoria y puntos de entrada", "A2 F3 G5", "Obra del recital: memorizar por capas", "Tocar de memoria desde 4 puntos de entrada"),
 (25, "M14", "Ensayo general", "G5 A1 B2", "Dos obras y un blues improvisado: pasada completa", "Recital de 10 minutos grabado, sin parar"),
 (26, "—", "Recital y examen final", "G5", "Recital ante otras personas; examen final del curso", "Aprobar el examen final y dar el recital"),
]

DIAS = [
 ("Lunes", "Lectura a primera vista (C1-C3) y entrenadores", "<b>Teoría nueva:</b> lee el apartado de la semana y haz sus autoevaluaciones"),
 ("Martes", "Ritmo e independencia (D)", "<b>Teoría en el teclado:</b> toca todas las partituras y ejemplos de la semana"),
 ("Miércoles", "Lectura a primera vista y saltos (C)", "<b>Armonía:</b> acordes, progresiones y transporte (E)"),
 ("Jueves", "Ritmo e independencia (D)", "<b>Oído e improvisación</b> (F)"),
 ("Viernes", "Lectura a primera vista y entrenadores", "<b>Interpretación:</b> dinámica, frases y mapa de la obra (G)"),
 ("Sábado", "Repaso de lo más difícil de la semana", "<b>Autoevaluación:</b> test del módulo y grabación de la obra (G5)"),
 ("Domingo", "<b>Libre:</b> una hora para tocar lo que te guste, sin metrónomo ni objetivos", "—"),
]

HORA = [
 ("0-5 min", "Calentamiento", "Relajar hombros y manos. Notas largas con peso de brazo (A2) y cinco dedos (A1).", "5"),
 ("5-15 min", "Técnica", "Escalas, arpegios y ejercicios de la semana (bloques A y B). Cambia cada día una variable: ritmo, articulación o tonalidad.", "10"),
 ("15-25 min", "Lectura y ritmo", "Lectura a primera vista (C), entrenadores de notas, intervalos y armaduras, y ritmos (D). Música nueva cada día.", "10"),
 ("25-45 min", "Repertorio", "La obra de la semana con el plan de 20 minutos del módulo 1: trozos cortos, mano por mano, tempo lento, tres repeticiones limpias.", "20"),
 ("45-55 min", "Teoría aplicada", "Según el día: teoría nueva, ejemplos de la partitura, armonía (E), oído e improvisación (F) o interpretación (G).", "10"),
 ("55-60 min", "Cierre", "Repasa lo más difícil, anota el tempo de hoy en el diario y deja preparado lo de mañana.", "5"),
]


def planning_html(n_examen):
    s = []
    s.append('<div class="palabras"><span class="pal-tag">En pocas palabras</span>'
             '<p>Seis meses, una hora al día: <b>26 semanas</b>, cada una con su tema, sus ejercicios, su obra y una <b>meta medible</b>. '
             'Cada día la hora se reparte igual para que no tengas que decidir nada: solo sentarte y empezar. '
             'Son unas <b>180 horas</b> de piano.</p></div>')
    s.append('<div class="dl-box">📥 <b>Planning para imprimir:</b> descárgalo en '
             '<a href="Planning_6_meses_piano.pdf" target="_blank" rel="noopener">PDF</a> (incluye la hora de piano, la semana tipo, las 26 semanas y el diario de práctica).</div>')
    s.append('<h2>1. La hora de piano</h2><p>La hora está dividida en seis bloques. Los tiempos son una guía: si un día tienes menos tiempo, quita minutos al <i>repertorio</i>, pero <b>nunca al calentamiento ni al cierre</b>.</p>')
    s.append('<div class="tabla-wrap"><table class="tabla"><tr><th>Minutos</th><th>Bloque</th><th>Qué haces</th><th>Total</th></tr>'
             + "".join(f"<tr><td>{a}</td><td><b>{b}</b></td><td>{c}</td><td>{d} min</td></tr>" for a, b, c, d in HORA) + "</table></div>")
    s.append('<div class="box tip"><b>Reparto de las 156 horas guiadas (6 días × 26 semanas):</b> repertorio 52 h · técnica 26 h · lectura y ritmo 26 h · teoría aplicada 26 h · calentamiento 13 h · cierre 13 h. Los domingos son aparte: 26 horas de piano libre.</div>')
    s.append('<h2>2. La semana tipo</h2><p>Cambian los bloques de <b>lectura y ritmo</b> (10 min) y de <b>teoría aplicada</b> (10 min). El resto de la hora es igual todos los días.</p>')
    s.append('<div class="tabla-wrap"><table class="tabla"><tr><th>Día</th><th>Lectura y ritmo (15-25 min)</th><th>Teoría aplicada (45-55 min)</th></tr>'
             + "".join(f"<tr><td><b>{d}</b></td><td>{a}</td><td>{b}</td></tr>" for d, a, b in DIAS) + "</table></div>")
    s.append('<h2>3. Los seis meses de un vistazo</h2>')
    meses_html = []
    for n, (t, sem, obj, pruebas) in enumerate(MESES, 1):
        meses_html.append(f'<div class="mes"><h3>{t} <span class="small">({sem})</span></h3><p><b>Objetivo:</b> {obj}</p><p><b>Prueba de fin de mes:</b></p>'
                          + '<ul class="checklist">' + "".join(f'<li><label><input type="checkbox" class="chk-plan" data-k="m{n}-{i}"> {p}</label></li>' for i, p in enumerate(pruebas)) + "</ul></div>")
    s.append("".join(meses_html))
    s.append('<h2>4. Semana a semana</h2><p>Marca cada semana al terminarla. Los códigos (A1, B2…) son los ejercicios de la página «Gimnasio»; M1, M2… son los módulos del curso.</p>')
    s.append('<p class="plan-prog"><b>Semanas completadas:</b> <span id="plan-n">0</span> de 26 <span class="plan-barra"><span id="plan-b"></span></span></p>')
    filas = []
    for n, m, tema, ejs, obra, hito in SEMANAS:
        mes = 1 + (n > 4) + (n > 8) + (n > 13) + (n > 17) + (n > 21)
        filas.append(f'<tr class="mes{mes}"><td><input type="checkbox" class="chk-plan" data-k="s{n}" aria-label="Semana {n} completada"></td><td><b>{n}</b></td><td>{m}</td><td><b>{tema}</b></td><td>{ejs}</td><td>{obra}</td><td>🎯 {hito}</td></tr>')
    s.append('<div class="tabla-wrap"><table class="tabla tabla-plan"><tr><th>✔</th><th>Sem.</th><th>Módulo</th><th>Tema</th><th>Ejercicios</th><th>Obra de la semana</th><th>Meta</th></tr>' + "".join(filas) + "</table></div>")
    s.append('<div class="box"><b>Obras del plan (dominio público):</b> Minueto en Sol (Ch. Petzold, BWV Anh. 114) · Sonatina op. 36 n.º 1 (M. Clementi) · Preludio en Do mayor BWV 846 (J. S. Bach) · <i>Para Elisa</i> (L. van Beethoven) · Gymnopédie n.º 1 (E. Satie). Las partituras completas están en IMSLP (imslp.org). Si prefieres otras obras de nivel parecido, sigue el mismo reparto.</div>')
    s.append('<h2>5. Reglas para avanzar</h2>' + '<ul class="key-points">'
             + "".join(f"<li>{i} <span>{t}</span></li>" for i, t in [
                 ("📈", "<b>Regla del tres:</b> cuando un pasaje salga tres veces seguidas sin errores, sube 4 bpm. Si fallas dos veces seguidas, baja 4 bpm."),
                 ("🐢", "<b>Más lento de lo que crees:</b> si no puedes tocar un compás sin fallos, el tempo es demasiado rápido."),
                 ("🗓️", "<b>Si te saltas un día:</b> no lo recuperes duplicando. Sigue con el plan del día siguiente."),
                 ("🔁", "<b>Si una semana se te atraganta:</b> repítela, y quita ese tiempo al repertorio de la semana siguiente; los ejercicios básicos no se recortan."),
                 ("⏱️", "<b>Si tienes menos de una hora:</b> haz solo calentamiento, repertorio y cierre (30 minutos). Mejor poco cada día que mucho un día."),
                 ("📝", "<b>El sábado es de prueba:</b> graba, escucha y apunta. Es lo que más te hará progresar."),
                 ("🎧", "<b>Cada mes</b> compara la grabación del sábado con la del mes anterior: verás el progreso."),
                 ("🏥", "<b>Salud:</b> si notas dolor en la muñeca, el antebrazo o la espalda, para y descansa. Calienta siempre antes de la técnica.")]) + "</ul>")
    s.append('<h2>6. Diario de práctica (imprimible)</h2><p>Una hoja por semana. Apunta cada día lo que hiciste y qué mejorar mañana.</p>')
    s.append('<div class="tabla-wrap"><table class="tabla tabla-diario"><tr><th>Día</th><th>Minutos</th><th>Qué estudié</th><th>Tempo (bpm)</th><th>Qué mejorar mañana</th><th>Ánimo 1-5</th></tr>'
             + "".join(f"<tr><td><b>{d[0]}</b></td><td></td><td></td><td></td><td></td><td></td></tr>" for d in DIAS) + "</table></div>")
    s.append(f'<h2>7. Cuando termines</h2><p>Haz el <b>examen final</b> del curso ({n_examen} preguntas, 70 % para aprobar). Después, planifica los seis meses siguientes: más repertorio, más improvisación y las obras que te gustaría tocar de principio a fin.</p>')
    return "\n".join(s)


PLAN_JS = """
(function(){
  var K='piano_plan_v1',est={};
  function leer(){try{est=JSON.parse(localStorage.getItem(K)||'{}')||{};}catch(e){est={};}}
  function guardar(){try{localStorage.setItem(K,JSON.stringify(est));}catch(e){}}
  function pintar(){
    var n=0;document.querySelectorAll('.chk-plan').forEach(function(c){var k=c.getAttribute('data-k');c.checked=!!est[k];if(/^s\\d+$/.test(k)&&c.checked)n++;});
    var a=document.getElementById('plan-n'),b=document.getElementById('plan-b');
    if(a)a.textContent=n;if(b)b.style.width=Math.round(n*100/26)+'%';
  }
  leer();pintar();
  document.querySelectorAll('.chk-plan').forEach(function(c){c.addEventListener('change',function(){est[c.getAttribute('data-k')]=c.checked;guardar();pintar();});});
})();
"""
