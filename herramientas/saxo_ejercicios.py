"""Gimnasio de ejercicios y planning de 6 meses del curso de saxofón alto."""

# (id, título, nivel 1-3, minutos, partituras, qué trabaja, pasos, meta); un paso puede ser (paso, cómo se hace)
BLOQUES = [
 ("A", "Calentamiento y sonido", "🔥", "Para empezar cada sesión. Primero el cuerpo y el aire, después el saxo. Siempre sin prisas.", [
  ("A1", "Respirar 4-2-8", 1, 3, ["respirar"], "Capacidad de aire y relajación.",
   ["Inspira por la boca contando 4, con el aire hacia el abdomen.", "Aguanta 2 tiempos.",
    ("Suelta el aire contando 8, como si empañaras un cristal.", "el aire es cálido y constante; los hombros no suben."), "Repite cinco veces y sube a 12 y 16 tiempos cuando lo domines."],
   "Soltar el aire 16 tiempos sin que se corte ni cambie de velocidad."),
  ("A2", "Notas largas con Sol", 1, 5, ["primer_sonido"], "Sonido estable y control del aire.",
   ["Respira, empieza la nota sin lengua y mantén 8 tiempos (♩ = 60).", "Escucha el sonido: ¿es igual al principio y al final?",
    "Descansa 4 tiempos y repite.", ("Haz cuatro notas largas y para a descansar.", "los labios se cansan: no sigas si notas dolor.")],
   "Cuatro notas de 8 tiempos sin que cambie la afinación ni el volumen."),
  ("A3", "Crescendo y diminuendo", 2, 5, ["p12_largas"], "Control del aire y la afinación al cambiar de volumen.",
   ["Toca la primera nota <i>p</i> (suave) y mantén los 4 tiempos.", ("Al hacer el crescendo, sube el aire poco a poco sin morder.", "si muerdes la nota sube de afinación."),
    "Haz el diminuendo bajando el aire sin que baje la afinación.", "Grábate y escucha la afinación."],
   "Un crescendo y un diminuendo de 8 tiempos sin que cambie la altura de la nota."),
  ("A4", "Embocadura sin saxo", 1, 3, [], "Formar la embocadura sin forzar.",
   [("Forma la «u» con los labios, sin boquilla.", "como al silbar: la boca forma un círculo y los labios están firmes, no tensos."),
    "Sopla aire cálido durante 8 segundos.", "Repite con un lápiz entre los labios (sin morder).", "Comprueba en un espejo que el mentón queda plano."],
   "Sostener la embocadura 30 segundos sin tensar el cuello."),
 ]),
 ("B", "Dedos y registro", "🖐️", "Las notas, los cambios de dedo y el paso de un registro a otro.", [
  ("B1", "Si, La y Sol", 1, 5, ["p5_largas", "p5_negras"], "Posición de los dedos y cambios sin ruido.",
   ["Toca las redondas con un cambio de dedo limpio cada cuatro tiempos.", "Pasa a las negras: un cambio por pulso.", "Fíjate en que los dedos bajan y suben juntos.", "Sube el tempo en 4 bpm cuando salga tres veces seguidas."],
   "Las negras a ♩ = 72, sin ruidos ni golpes al cambiar."),
  ("B2", "Bajando hacia el Re", 2, 5, ["p6_grave"], "Mano derecha y notas graves.",
   [("Toca Sol–Fa–Mi–Re muy despacio, una nota por pulso.", "levanta y baja los dedos de la mano derecha de uno en uno, cubriendo las llaves con la yema."),
    "Sube de nuevo: Re–Mi–Fa–Sol.", "Comprueba que ninguna nota suena «sucia».", "Sube el tempo poco a poco."],
   "Subir y bajar del Sol al Re a ♩ = 72 con las cuatro notas limpias."),
  ("B3", "Fa♯ y Si♭", 2, 5, ["p6_fa", "p6_sib"], "Las alteraciones más habituales.",
   ["Antes de tocar, di en voz alta qué alteración tiene la armadura.", ("Toca la melodía muy despacio, comprobando los dedos del Fa♯ y del Si♭.", "Fa♯: izq 1-2-3 y der 2. Si♭: izq 1 y der 1."),
    "Repite sin mirar los dedos.", "Sube el tempo."],
   "Las dos melodías a ♩ = 72 sin errores de alteraciones."),
  ("B4", "Octavas", 3, 8, ["p8_octavas", "e_octavas_ligadas"], "La llave de octava y el cambio de registro.",
   [("Toca el Sol grave y luego el agudo, sin cambiar la boca.", "pulsa la llave a tiempo y da un poco más de velocidad al aire."), "Haz las octavas ligadas con una sola lengua.",
    "Fíjate en que el sonido agudo tenga la misma calidad que el grave.", "Haz los cuatro pares de notas y descansa."],
   "Las ocho octavas ligadas a ♩ = 60 sin que se pierda el sonido."),
  ("B5", "Terceras y quintas", 3, 6, ["e_terceras", "e_quintas"], "Saltos y precisión de los dedos.",
   ["Mira el intervalo antes de tocar.", "Prepara la llave de octava en los saltos de quinta.", "Toca despacio y sube el tempo.", "Haz los saltos con los ojos cerrados."],
   "Los saltos limpios a ♩ = 66, sin aire en el cambio."),
  ("B6", "Escala cromática", 3, 6, ["p10_cromatica"], "Dominio de todos los dedos en el registro grave.",
   ["Repasa las digitaciones de las alteraciones.", "Sube nota a nota con metrónomo a ♩ = 52.", "Baja con bemoles.", "Haz la escala dos veces seguidas sin parar."],
   "La cromática completa (subiendo y bajando) a ♩ = 60."),
 ]),
 ("C", "Escalas y arpegios", "📈", "La gimnasia de la técnica: una tonalidad nueva cada semana.", [
  ("C1", "Sol mayor", 1, 8, ["p8_sol"], "Dedos, paso Do–Re y registro agudo.",
   ["Una octava lenta, nota larga a nota larga.", "Ligada, subiendo y bajando.", "Picada con ritmo regular.", "Con matices: crescendo subiendo y diminuendo bajando."],
   "La escala a ♩ = 80 ligada, sin errores."),
  ("C2", "Fa mayor y Do mayor", 2, 8, ["p10_fa", "p10_do"], "Si♭ y paso al registro agudo.",
   ["Toca una octava lenta de cada una.", ("Cuida el Si♭: izquierdo 1 y derecho 1.", "en Do mayor el primer Do se toca sin llave de octava; el resto, con ella."), "Ligada, picada y con ritmos.", "Sube de 4 en 4 bpm."],
   "Ambas escalas a ♩ = 72."),
  ("C3", "Re mayor", 2, 8, ["p10_re"], "Fa♯ y Do♯ en la misma escala.",
   ["Antes de empezar, di las alteraciones: Fa♯ y Do♯.", "Una octava lenta, notas largas.", "Ligada y picada.", "Sube el tempo."],
   "La escala a ♩ = 72."),
  ("C4", "Escalas menores", 3, 10, ["p10_lam", "p10_mim", "p10_rem"], "La menor, Mi menor y Re menor (naturales).",
   ["Toca la menor natural de cada una.", "Compara con la mayor relativa: ¿en qué se diferencia?", "Ligada, picada y con ritmos.", "Escucha cómo cambia el carácter."],
   "Las tres escalas a ♩ = 66."),
  ("C5", "Arpegios", 3, 8, ["p10_arpegios"], "Tónica, tercera, quinta y octava.",
   ["Toca cada arpegio despacio, con aire constante.", "Ligados y picados.", "Sube y baja sin cortes.", "Repite con matices."],
   "Los cuatro arpegios a ♩ = 72."),
 ]),
 ("D", "Lengua y articulación", "🗣️", "Una lengua precisa, ligera y rápida.", [
  ("D1", "Notas picadas", 1, 5, ["p7_picado"], "Pronunciación regular de la lengua.",
   ["Sin saxo: di «tu-tu-tu-tu» con aire.", "Con el saxo: Sol picada, una por pulso.", "Sube a La y Si.", "Escucha: las notas deben ser iguales."],
   "La melodía a ♩ = 80 sin acentos irregulares."),
  ("D2", "Notas ligadas", 1, 5, ["p7_ligado"], "Cambio de dedos sin interrumpir el aire.",
   ["Lengua solo en la primera nota de cada arco.", "Los dedos van juntos.", "El aire no se detiene.", "Repite subiendo el tempo."],
   "La melodía ligada a ♩ = 72 sin cortes."),
  ("D3", "Ligado, picado y acentos", 2, 6, ["p7_mixto", "p7_acentos"], "Combinar articulaciones.",
   ["Toca solo el ligado y luego solo el picado.", "Combina las dos.", "Añade los acentos con aire.", "Graba y escucha."],
   "Distinguir con claridad cada articulación en la grabación."),
  ("D4", "Corcheas picadas", 3, 6, ["p7_corcheas", "e_picado_cambios"], "Velocidad de la lengua.",
   ["Empieza despacio (♩ = 60).", "Sube 4 bpm cada vez que salga limpia.", "Si se traba, vuelve al tempo anterior.", "Repite con distintas notas."],
   "Las corcheas picadas a ♩ = 80 sin trabarte."),
 ]),
 ("E", "Ritmo y lectura", "🥁", "Contar, leer y reconocer: lo que separa tocar bien de tocar deprisa.", [
  ("E1", "Pulso y silencios", 1, 5, ["p11_pulso"], "Sentir el pulso y respetar los silencios.",
   ["Marca el pulso con el pie.", "Cuenta en voz alta.", "Toca sin acortar los silencios.", "Sube el tempo."],
   "Tocar con el pie y la cuenta en voz alta sin perder el pulso."),
  ("E2", "Corcheas y puntillo", 2, 6, ["p11_corcheas", "p11_puntillo"], "Subdivisión del pulso.",
   ["Cuenta «1-y-2-y» mientras tocas.", "Toca primero las corcheas y luego el puntillo.", "Marca cada pulso con el pie.", "Repite subiendo el tempo."],
   "Los dos ejercicios a ♩ = 72 sin perder el pulso."),
  ("E3", "Síncopas", 3, 6, ["p11_sincopa"], "Acento en la parte débil del compás.",
   ["Cuenta en voz alta mientras tocas.", "Marca el pulso con el pie.", "Toca primero sin síncopa y luego con ella.", "Sube el tempo en 4 bpm."],
   "Las síncopas a ♩ = 72 sin perder el pulso."),
  ("E4", "Vals y 6/8", 2, 6, ["p11_vals", "p11_68"], "Compases ternarios.",
   ["Cuenta «UNO-dos-tres» en el vals con el primero marcado.", "En 6/8, cuenta dos pulsos de tres.", "Toca con el acompañamiento del vals.", "Repite sin el acompañamiento."],
   "Tocar el vals con el acompañamiento sin perder el compás."),
  ("E5", "Lectura a primera vista", 2, 8, ["e_lectura1", "e_lectura2", "e_lectura3"], "Leer música nueva sin parar.",
   [("Escanea 30 segundos: armadura, compás y notas más agudas y más graves.", "di en voz alta las alteraciones de la armadura y busca las notas altas y bajas."),
    "Pon el metrónomo lento y toca sin parar aunque falles.", "Mira siempre por delante de lo que tocas.", "Repite y compara."],
   "Tocar las tres lecturas sin detenerte."),
  ("E6", "Entrenadores del curso", 1, 5, [], "Lectura, digitaciones y transposición.",
   ["Abre el entrenador de lectura (módulo 6).", "Pasa al de digitaciones (módulo 6).", "Termina con el de transposición (módulo 9).", "Anota tus aciertos."],
   "8 de 10 aciertos en cada entrenador."),
  ("E7", "Frases y respiraciones", 2, 5, ["p11_frase"], "Fraseo y respiración sin romper la música.",
   ["Canta la melodía e identifica las frases.", "Marca las respiraciones con una coma.", "Respira rápido y sin ruido en los silencios.", "Haz un diminuendo al final de cada frase."],
   "Tocarla con respiraciones silenciosas y sin perder el pulso."),
 ]),
 ("F", "Afinación y sonido", "📏", "Afinar y cuidar el sonido en todo el registro.", [
  ("F1", "Afinar con una referencia", 2, 5, ["p12_afinacion"], "Oído y ajuste de la boquilla.",
   ["Calienta el instrumento antes de afinar.", "Toca el Fa♯ (La concierto) y compara con el tono de referencia.", "Ajusta la boquilla si hace falta.", "Comprueba el Sol, el Mi y el Si."],
   "Afinar el Fa♯ con un margen de ±5 cents."),
  ("F2", "Frase con matices", 2, 6, ["e_dinamicas_frase"], "Control del volumen sin perder la afinación.",
   ["Toca la frase con los matices de la partitura.", "Crece hacia el punto más agudo.", "Baja la dinámica al final.", "Grábate y escucha."],
   "Que la grabación mantenga la afinación en el crescendo."),
 ]),
 ("G", "Repertorio", "🎼", "Piezas del curso. Primero sin acompañamiento, luego con él.", [
  ("G1", "Pan caliente y Au clair de la lune", 1, 8, ["p5_pan", "p6_clair"], "Primeras melodías.",
   ["Toca sin acompañamiento hasta que salga.", "Escucha el modo «Saxo + acompañamiento».", "Toca con el modo «Solo acompañamiento».", "Grábate."], "Tocar ambas con el acompañamiento."),
  ("G2", "Mary tenía un corderito y Estrellita", 2, 8, ["p6_mary", "p8_twinkle"], "Registro medio y agudo en melodías conocidas.",
   ["Toca la melodía despacio.", "Marca las respiraciones.", "Une con el acompañamiento.", "Graba."], "Tocar ambas a tempo."),
  ("G3", "Himno de la alegría", 2, 8, ["p8_ode"], "Ritmo con puntillo y registro agudo.",
   ["Toca despacio, con el ritmo de corchea con puntillo.", "Cuenta en voz alta.", "Une con el acompañamiento.", "Graba."], "Tocarlo con el acompañamiento a ♩ = 88."),
  ("G4", "Frère Jacques", 2, 8, ["r_frere"], "Corcheas y registro agudo.",
   ["Toca despacio y ligado.", "Marca las respiraciones.", "Toca con acompañamiento.", "Toca en canon con otra persona."], "Tocar a ♩ = 96 con acompañamiento."),
  ("G5", "Marcha de los saxofones", 3, 10, ["r_marcha"], "Fa mayor con Si♭ y registro agudo.",
   ["Antes de tocar, revisa la armadura (Si♭).", "Trabaja por trozos de 2 compases.", "Une con el acompañamiento.", "Graba y evalúa."], "Tocarla a ♩ = 104 con el acompañamiento."),
  ("G6", "Balada del atardecer", 3, 10, ["r_balada"], "Sonido cantado, La menor y Sol♯.",
   ["Toca las notas largas con sonido lleno.", "Practica el Sol♯ por separado.", "Une con el acompañamiento.", "Graba y evalúa."], "Tocarla con sonido estable y matices."),
  ("G7", "Samba fácil", 3, 10, ["r_samba"], "Compás de 2/4, corcheas y registro agudo.",
   ["Cuenta «1-y-2-y» en voz alta.", "Trabaja los cambios de octava.", "Une con el acompañamiento.", "Graba."], "Tocarla a ♩ = 100 con el acompañamiento."),
 ]),
 ("H", "Blues e improvisación", "🎷", "Jugar con las notas: blues, swing y frases propias.", [
  ("H1", "Escala de blues", 2, 8, ["p14_escala"], "La base de la improvisación.",
   ["Toca la escala despacio, subiendo y bajando.", "Practica la nota azul: Mi♭ → Mi.", "Toca solo tres notas: La, Do y Re.", "Repite en distintos ritmos."], "Tocar la escala de memoria a ♩ = 80."),
  ("H2", "Corcheas con swing", 3, 8, ["p14_swing"], "El balanceo de las corcheas.",
   ["Escucha la grabación.", "Canta el balanceo («du-ba, du-ba»).", "Toca despacio primero.", "Acelera poco a poco."], "Que se note el swing en la grabación."),
  ("H3", "Pregunta y respuesta", 2, 8, ["p14_pregunta"], "Frases con sentido.",
   ["Toca la frase de ejemplo.", "Cambia el final y repítela.", "Inventa tu propia pregunta.", "Inventa la respuesta."], "Improvisar una pregunta y una respuesta."),
  ("H4", "Blues de 12 compases", 3, 10, ["p14_blues"], "Forma y acordes del blues.",
   ["Toca la melodía con el acompañamiento.", "Cuenta los 12 compases.", "Improvisa con el modo «Solo acompañamiento».", "Graba un coro."], "Improvisar un coro de 12 compases con silencios."),
  ("H5", "Grabarte y evaluarte", 1, 10, [], "Escuchar lo que de verdad suena.",
   [("Graba la pieza con el móvil, sin repetir ni parar.", "colócalo a un metro y haz una sola toma."), "Escucha con la partitura y puntúa de 1 a 5: pulso, notas, sonido, afinación y respiración.",
    "Elige un solo problema para la sesión siguiente.", "Compara con la grabación de la semana anterior."], "Una tabla de autoevaluación rellena cada sábado."),
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


def tabla_autoeval():
    filas = ["Pulso (¿se mantiene estable?)", "Notas (¿correctas?)", "Sonido (¿limpio y estable?)", "Afinación (¿afinado?)", "Articulación (¿clara?)", "Respiración (¿entre frases?)"]
    return ('<div class="tabla-wrap"><table class="tabla"><tr><th>Criterio</th><th>1</th><th>2</th><th>3</th><th>4</th><th>5</th><th>Compás del problema</th></tr>'
            + "".join(f"<tr><td>{f}</td>" + "".join('<td><input type="radio" name="ev-%d" style="width:auto"></td>' % i for _ in range(5)) + '<td><input type="text" style="width:90px"></td></tr>' for i, f in enumerate(filas))
            + "</table></div>")


def ejercicios_html(partitura):
    sal = ['<div class="palabras"><span class="pal-tag">Cómo usar esta página</span>'
           '<p>Es un <b>gimnasio</b>: cada ejercicio tiene un código (A1, B2, C3…) que el <b>planning de 6 meses</b> usa para decirte qué hacer cada semana. '
           'Indica qué trabaja, los pasos, cuánto dura, el nivel (★) y una <b>meta medible</b>. No hace falta hacerlos todos cada día: elige los de la semana.</p></div>',
           '<div class="box tip"><b>Regla de oro de cada ejercicio:</b> lento, sin tensión, con metrónomo y descansando los labios. '
           'Cuando salga tres veces seguidas sin errores, sube 4 bpm. Si fallas dos veces seguidas, baja 4 bpm.</div>',
           "<h3>Índice</h3><div class=\"tabla-wrap\"><table class=\"tabla\"><tr><th>Bloque</th><th>Ejercicios</th></tr>"
           + "".join(f"<tr><td>{b[2]} <b>{b[0]} · {b[1]}</b></td><td>" + " · ".join(f'<a href="#{e[0]}">{e[0]}</a> {e[1]}' for e in b[4]) + "</td></tr>" for b in BLOQUES)
           + "</table></div>"]
    for letra, titulo, ico, intro, ejs in BLOQUES:
        sal.append(f'<h2>{ico} {letra} · {titulo}</h2><p>{intro}</p>')
        sal += [ejercicio_html(e, partitura) for e in ejs]
    sal.append('<h3>Tabla de autoevaluación (para el ejercicio H5)</h3>' + tabla_autoeval())
    return "\n".join(sal)


# ---------------------------------------------------------------------------------------------
# Planning
# ---------------------------------------------------------------------------------------------
MESES = [
 ("Mes 1 · Montaje, sonido y primeras notas", "Semanas 1-4", "Montar el saxo, conseguir un sonido estable y tocar las tres primeras notas.",
  ["Montar y desmontar el saxo sin ayuda y dejarlo limpio.", "Mantener un Sol de 8 tiempos con sonido estable.", "Respirar con el 4-2-8 sin subir los hombros.", "Tocar «Pan caliente» completa a ♩ = 72."]),
 ("Mes 2 · Más notas y la lengua", "Semanas 5-8", "Ampliar el registro y empezar a articular.",
  ["Tocar del Sol al Re y volver, con las cuatro notas limpias.", "Tocar «Au clair de la lune» y «Mary tenía un corderito».", "Distinguir ligado y picado al tocar.", "Hacer el ejercicio mixto a ♩ = 72."]),
 ("Mes 3 · Registro agudo y transposición", "Semanas 9-13", "Usar la llave de octava y entender el saxo en Mi♭.",
  ["Tocar la escala de Sol mayor a ♩ = 72.", "Tocar «Estrellita» y el «Himno de la alegría».", "Acertar 8 de 10 en el entrenador de transposición.", "Pasar la armadura del piano a la del saxo."]),
 ("Mes 4 · Escalas y ritmo", "Semanas 14-17", "Dominar las escalas básicas y la lectura rítmica.",
  ["Tocar Sol, Fa, Do y Re mayor a ♩ = 72.", "Tocar La, Mi y Re menor (naturales).", "Tocar las síncopas y el vals con acompañamiento.", "Respirar entre frases sin romper el pulso."]),
 ("Mes 5 · Sonido, afinación y repertorio", "Semanas 18-21", "Sonido estable, afinación y piezas completas.",
  ["Afinar el Fa♯ (La concierto) con ±5 cents.", "Tocar «Frère Jacques» y la «Marcha de los saxofones» con acompañamiento.", "Tocar la «Balada del atardecer» con matices.", "Hacer un crescendo y un diminuendo sin cambiar la afinación."]),
 ("Mes 6 · Blues, improvisación y recital", "Semanas 22-26", "Improvisar con la escala de blues y tocar un pequeño recital.",
  ["Tocar la escala de blues de memoria.", "Improvisar un coro de blues de 12 compases.", "Grabar un recital de 10 minutos con tres piezas.", "Aprobar el examen final (70 %)."]),
]

SEMANAS = [
 (1, "M1-M2", "Conoce y monta tu saxo", "A1 A4", "Montar y desmontar; sonido con la boquilla", "Montar y desmontar solo y sacar sonido con la boquilla"),
 (2, "M3", "Postura y respiración", "A1 A2 A4", "Notas largas de Sol (con el saxo)", "Respirar 4-2-8 y mantener Sol 8 tiempos"),
 (3, "M4", "La embocadura y el primer sonido", "A2 A4", "Sol largo, 4 y 8 tiempos", "Sol de 8 tiempos estable, sin chirridos"),
 (4, "M5", "Si, La y Sol", "B1 E1", "«Pan caliente»", "«Pan caliente» a ♩ = 72 (prueba del mes 1)"),
 (5, "M6", "Mano derecha: Fa, Mi y Re", "B2 E5 E6", "«Au clair de la lune»", "Sol–Fa–Mi–Re y vuelta a ♩ = 60"),
 (6, "M6", "Do, Do♯, Fa♯ y Si♭", "B3 E6", "«Mary tenía un corderito»", "Las melodías en Sol y Fa mayor sin errores"),
 (7, "M7", "La lengua: picado y ligado", "D1 D2", "Ejercicios de articulación", "Distinguir picado y ligado"),
 (8, "M7", "Acentos y corcheas", "D3 D4 G1", "«Pan caliente» y «Au clair» con acompañamiento", "El ejercicio mixto a ♩ = 72 (prueba del mes 2)"),
 (9, "M8", "La llave de octava", "B4 A3", "Notas largas con octava", "Sol–sol–Sol–sol ligadas a ♩ = 60"),
 (10, "M8", "Escala de Sol mayor", "C1 B5", "Escala de Sol y «Estrellita» (compases 1-4)", "Escala de Sol a ♩ = 72"),
 (11, "M8", "Melodías en el registro agudo", "B4 G2", "«Estrellita» completa", "«Estrellita» con acompañamiento"),
 (12, "M9", "Transposición: el saxo en Mi♭", "E6 E5", "«Himno de la alegría» (compases 1-4)", "8/10 en el entrenador de transposición"),
 (13, "M9", "Las tonalidades escritas", "C1 E6", "«Himno de la alegría» completo", "El Himno con acompañamiento (prueba del mes 3)"),
 (14, "M10", "Fa y Do mayor", "C2 B6", "«Frère Jacques»: leer y marcar frases", "Fa y Do a ♩ = 72"),
 (15, "M10", "Re mayor y escalas menores", "C3 C4", "«Frère Jacques»: compases 1-4", "Re mayor y La menor a ♩ = 66"),
 (16, "M10", "Arpegios y cromática", "C5 B6", "«Frère Jacques»: compases 5-8", "Los cuatro arpegios a ♩ = 72"),
 (17, "M11", "Ritmo, compases y frases", "E1 E2 E3 E4 E7", "«Frère Jacques» completo", "Síncopas y vals con acompañamiento (prueba del mes 4)"),
 (18, "M12", "El sonido", "A3 F2", "«Marcha de los saxofones»: leer y analizar", "Crescendo y diminuendo sin cambiar la afinación"),
 (19, "M12", "La afinación", "F1 A3", "«Marcha»: compases 1-4", "Afinar el Fa♯ con ±5 cents"),
 (20, "M13", "Repertorio: la Marcha", "G5 E5", "«Marcha»: compases 5-8", "La Marcha con acompañamiento a ♩ = 104"),
 (21, "M13", "Repertorio: la Balada", "G6 F2", "«Balada del atardecer»", "La Balada con matices (prueba del mes 5)"),
 (22, "M14", "Swing", "H2 E3", "«Samba fácil»: leer y analizar", "Corcheas con swing"),
 (23, "M14", "La escala de blues", "H1 C4", "«Samba fácil»: compases 1-4", "La escala de blues de memoria a ♩ = 80"),
 (24, "M14", "Improvisación", "H3 H4", "«Samba fácil» completa", "Una pregunta y una respuesta improvisadas"),
 (25, "M14", "Ensayo general", "H4 G7 H5", "Tres piezas y un blues improvisado", "Recital de 10 minutos grabado, sin parar"),
 (26, "—", "Recital y examen final", "H5", "Recital ante otras personas; examen final del curso", "Aprobar el examen final y dar el recital"),
]

DIAS = [
 ("Lunes", "Lectura a primera vista y entrenadores (E5, E6)", "<b>Teoría nueva:</b> lee el apartado de la semana y haz sus autoevaluaciones"),
 ("Martes", "Ritmo y metrónomo (E1-E4)", "<b>Teoría en el saxo:</b> toca las partituras y ejemplos de la semana"),
 ("Miércoles", "Escalas y arpegios (C)", "<b>Transposición y tonalidades:</b> convertidor y entrenador del módulo 9"),
 ("Jueves", "Lengua y articulación (D)", "<b>Afinación y sonido</b> (F)"),
 ("Viernes", "Lectura a primera vista y saltos (B5)", "<b>Improvisación</b> (H) o piezas del repertorio (G)"),
 ("Sábado", "Repaso de lo más difícil de la semana", "<b>Autoevaluación:</b> test del módulo y grabación de la pieza (H5)"),
 ("Domingo", "<b>Descanso o 20 minutos de música libre</b>, sin metrónomo ni objetivos", "—"),
]

HORA = [
 ("0-5 min", "Calentamiento", "Respiración 4-2-8 (A1), embocadura sin saxo (A4) y notas largas con peso de aire (A2).", "5"),
 ("5-15 min", "Sonido y técnica", "Notas largas, escalas y arpegios, y articulación de la semana (bloques A, B, C y D).", "10"),
 ("15-22 min", "Lectura y ritmo", "Lectura a primera vista (E5), ritmo con metrónomo (E1-E4) y entrenadores (E6).", "7"),
 ("22-37 min", "Repertorio", "La pieza de la semana: trozos de 2 compases, tempo lento, tres repeticiones limpias y acompañamiento al final.", "15"),
 ("37-42 min", "Teoría, oído e improvisación", "Según el día: teoría nueva, afinación, transposición o improvisación (F, H).", "5"),
 ("42-45 min", "Cierre", "Repasa lo más difícil, limpia el saxo, anota el tempo de hoy en el diario y descansa los labios.", "3"),
]


def planning_html(n_examen):
    s = []
    s.append('<div class="palabras"><span class="pal-tag">En pocas palabras</span>'
             '<p>Seis meses, <b>45 minutos al día</b> (30 el primer mes, hasta 60 a partir del cuarto): <b>26 semanas</b>, cada una con su tema, sus ejercicios, su pieza y una <b>meta medible</b>. '
             'Los labios y el aire se entrenan poco a poco: <b>más no es mejor</b>. Son unas <b>105 horas</b> de saxo.</p></div>')
    s.append('<div class="dl-box">📥 <b>Planning para imprimir:</b> descárgalo en '
             '<a href="Planning_6_meses_saxo.pdf" target="_blank" rel="noopener">PDF</a> (incluye la sesión, la semana tipo, las 26 semanas y el diario de práctica).</div>')
    s.append('<h2>1. La sesión de estudio</h2><p>La sesión de 45 minutos está dividida en seis bloques. Si un día tienes menos tiempo, quita minutos al <i>repertorio</i>, pero <b>nunca al calentamiento ni al cierre</b>.</p>')
    s.append('<div class="tabla-wrap"><table class="tabla"><tr><th>Minutos</th><th>Bloque</th><th>Qué haces</th><th>Total</th></tr>'
             + "".join(f"<tr><td>{a}</td><td><b>{b}</b></td><td>{c}</td><td>{d} min</td></tr>" for a, b, c, d in HORA) + "</table></div>")
    s.append('<div class="box tip"><b>Cómo crece el tiempo:</b> <b>mes 1</b>: 30 minutos (calentamiento, sonido y técnica, repertorio y cierre). '
             '<b>Meses 2 y 3</b>: 40 minutos. <b>Meses 4 a 6</b>: 45 minutos, ampliables a 60 si el labio y la concentración lo permiten (añade 15 minutos de repertorio). '
             'Descansa 1 minuto cada 5 minutos de práctica los primeros días.</div>')
    s.append('<h2>2. La semana tipo</h2><p>Cambian los bloques de <b>lectura y ritmo</b> (7 min) y de <b>teoría, oído e improvisación</b> (5 min). El resto de la sesión es igual todos los días.</p>')
    s.append('<div class="tabla-wrap"><table class="tabla"><tr><th>Día</th><th>Lectura y ritmo (15-22 min)</th><th>Teoría, oído e improvisación (37-42 min)</th></tr>'
             + "".join(f"<tr><td><b>{d}</b></td><td>{a}</td><td>{b}</td></tr>" for d, a, b in DIAS) + "</table></div>")
    s.append('<h2>3. Temporizador de práctica</h2><p>Pon un tiempo, concéntrate y descansa los labios al terminar.</p>'
             '<div class="activity"><div style="font-size:2.6em;font-weight:700;color:#6b3f0e;text-align:center" id="tm-pant">00:00</div>'
             '<div class="lect-btns" style="justify-content:center"><button onclick="tmIniciar(5)">5 min</button><button onclick="tmIniciar(10)">10 min</button><button onclick="tmIniciar(15)">15 min</button>'
             '<button onclick="tmIniciar(20)">20 min</button><button onclick="tmIniciar(30)">30 min</button><button onclick="tmParar()">■ Parar</button></div>'
             '<p class="feedback" id="tm-msg" style="text-align:center"></p></div>')
    s.append('<h2>4. Los seis meses de un vistazo</h2>')
    for n, (t, sem, obj, pruebas) in enumerate(MESES, 1):
        s.append(f'<div class="mes"><h3>{t} <span class="small">({sem})</span></h3><p><b>Objetivo:</b> {obj}</p><p><b>Prueba de fin de mes:</b></p>'
                 + '<ul class="checklist">' + "".join(f'<li><label><input type="checkbox" class="chk-plan" data-k="m{n}-{i}"> {p}</label></li>' for i, p in enumerate(pruebas)) + "</ul></div>")
    s.append('<h2>5. Semana a semana</h2><p>Marca cada semana al terminarla. Los códigos (A1, B2…) son los ejercicios de la página «Gimnasio»; M1, M2… son los módulos del curso.</p>')
    s.append('<p class="plan-prog"><b>Semanas completadas:</b> <span id="plan-n">0</span> de 26 <span class="plan-barra"><span id="plan-b"></span></span></p>')
    filas = []
    for n, m, tema, ejs, obra, hito in SEMANAS:
        mes = 1 + (n > 4) + (n > 8) + (n > 13) + (n > 17) + (n > 21)
        filas.append(f'<tr class="mes{mes}"><td><input type="checkbox" class="chk-plan" data-k="s{n}" aria-label="Semana {n} completada"></td><td><b>{n}</b></td><td>{m}</td><td><b>{tema}</b></td><td>{ejs}</td><td>{obra}</td><td>🎯 {hito}</td></tr>')
    s.append('<div class="tabla-wrap"><table class="tabla tabla-plan"><tr><th>✔</th><th>Sem.</th><th>Módulo</th><th>Tema</th><th>Ejercicios</th><th>Pieza de la semana</th><th>Meta</th></tr>' + "".join(filas) + "</table></div>")
    s.append('<h2>6. Reglas para avanzar</h2>' + '<ul class="key-points">'
             + "".join(f"<li>{i} <span>{t}</span></li>" for i, t in [
                 ("📈", "<b>Regla del tres:</b> cuando un pasaje salga tres veces seguidas sin errores, sube 4 bpm. Si fallas dos veces seguidas, baja 4 bpm."),
                 ("👄", "<b>Cuida el labio:</b> si el labio o la mandíbula duelen, para. Es mejor tocar poco cada día que mucho un día."),
                 ("🗓️", "<b>Si te saltas un día:</b> no lo recuperes duplicando. Sigue con el plan del día siguiente."),
                 ("🔁", "<b>Si una semana se te atraganta:</b> repítela y quita ese tiempo al repertorio de la semana siguiente; el calentamiento no se recorta."),
                 ("⏱️", "<b>Si tienes menos tiempo:</b> haz solo calentamiento, repertorio y cierre (20 minutos)."),
                 ("🎧", "<b>Cada sábado graba</b> la pieza de la semana y compárala con la del sábado anterior: verás el progreso."),
                 ("🧼", "<b>Limpia el saxo</b> cada día al terminar: seca la caña y pasa el escobillón."),
                 ("🏥", "<b>Salud:</b> bebe agua, descansa 1 minuto cada 5 minutos al principio y avisa a tu profesor/a si notas dolor.")]) + "</ul>")
    s.append('<h2>7. Diario de práctica (imprimible)</h2><p>Una hoja por semana. Apunta cada día lo que hiciste y qué mejorar mañana.</p>')
    s.append('<div class="tabla-wrap"><table class="tabla tabla-diario"><tr><th>Día</th><th>Minutos</th><th>Qué estudié</th><th>Tempo (bpm)</th><th>Qué mejorar mañana</th><th>Ánimo 1-5</th></tr>'
             + "".join(f"<tr><td><b>{d[0]}</b></td><td></td><td></td><td></td><td></td><td></td></tr>" for d in DIAS) + "</table></div>")
    s.append(f'<h2>8. Cuando termines</h2><p>Haz el <b>examen final</b> del curso ({n_examen} preguntas, 70 % para aprobar). Después, sigue con un profesor/a: vibrato, notas agudas, más repertorio y una agrupación.</p>')
    return "\n".join(s)


PLAN_JS = """
(function(){
  var K='saxo_plan_v1',est={};
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
