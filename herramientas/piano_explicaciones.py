"""Ampliación del curso de piano: explicaciones más completas y fáciles de entender.

PALABRAS[n]  → recuadro «En pocas palabras» al principio del módulo n.
EXTRA[n]     → explicaciones, plan de práctica y errores frecuentes (se insertan antes de las autoevaluaciones).
GLOSARIO     → términos para la portada.
Marcadores que sustituye el generador:
  [[partitura:clave]]            → partitura interactiva de piano_partituras.py
  [[fig:archivo|alt|pie]]        → imagen de img/
"""


def caja(titulo, texto, clase="box tip"):
    return f'<div class="{clase}"><b>{titulo}</b> {texto}</div>'


def lista(items, ico):
    return '<ul class="key-points">' + "".join(f"<li>{ico} <span>{i}</span></li>" for i in items) + "</ul>"


def pasos(items):
    return '<ol class="steps">' + "".join(f"<li>{i}</li>" for i in items) + "</ol>"


def tabla(cab, filas):
    return ('<div class="tabla-wrap"><table class="tabla"><tr>' + "".join(f"<th>{c}</th>" for c in cab) + "</tr>"
            + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in f) + "</tr>" for f in filas) + "</table></div>")


def errores(filas):
    return "<h3>⚠️ Errores frecuentes y cómo corregirlos</h3>" + tabla(["Lo que pasa", "Por qué", "Cómo corregirlo"], filas)


def practica(titulo, items):
    return f'<div class="practica"><h3>🗓️ {titulo}</h3>' + pasos(items) + "</div>"


def palabras(texto):
    return f'<div class="palabras"><span class="pal-tag">En pocas palabras</span><p>{texto}</p></div>'


PALABRAS = {
    1: palabras("Estudiar bien no es estudiar más horas: es <b>tocar despacio, por trozos pequeños y sin errores</b>, y subir la velocidad poco a poco con el metrónomo."),
    2: palabras("Leer bien es <b>reconocer dibujos</b> (saltos, escalas, acordes) en lugar de deletrear nota a nota, y <b>sentir el pulso</b> antes de tocar."),
    3: palabras("Todas las escalas mayores siguen el <b>mismo patrón de distancias</b>: tono, tono, semitono, tono, tono, tono, semitono. Las alteraciones de la armadura existen para que ese patrón se cumpla."),
    4: palabras("Un acorde se forma <b>tocando una nota sí y otra no</b>: Do-(Re)-Mi-(Fa)-Sol. Si la nota del medio baja un semitono, el acorde pasa de mayor a menor."),
    5: palabras("Los acordes tienen papeles, como en una historia: <b>la tónica (I) es «casa»</b>, la subdominante (IV) es «salir de paseo» y la dominante (V) es «querer volver a casa»."),
    6: palabras("Primero cada mano sola, hasta que salga «en automático»; después, juntas y muy despacio. Y siempre: <b>la melodía más fuerte que el acompañamiento</b>."),
    7: palabras("El pedal derecho deja sonar las cuerdas. Se cambia <b>cada vez que cambia el acorde, un instante después</b> de tocarlo, nunca a la vez."),
    8: palabras("Antes de tocar una obra, <b>entiéndela</b>: en qué partes se divide, qué acordes usa y dónde están los pasajes difíciles. Así la estudias la mitad de tiempo."),
    9: palabras("La fuerza en el piano viene del <b>peso del brazo</b>, no de apretar. Mano firme, muñeca y hombro sueltos, y pausas frecuentes."),
    10: palabras("Para tocar dos ritmos a la vez, <b>busca una cuadrícula común</b> a las dos manos y coloca cada nota en su casilla. Primero se cuenta; con la práctica, se siente."),
    11: palabras("Un acorde de séptima es una tríada con <b>una nota más encima</b>. La 3.ª y la 7.ª le dan el carácter; la fundamental la puede tocar el bajo."),
    12: palabras("Improvisar es <b>conversar con notas</b>: frases cortas, silencios, preguntas y respuestas. Con tres notas bien elegidas ya se puede hacer música."),
    13: palabras("Interpretar es <b>tomar decisiones</b>: dónde respira cada frase, hacia dónde crece, qué se destaca. Las notas son el punto de partida, no la meta."),
    14: palabras("Una buena actuación se prepara: <b>memoria apoyada en varias capas</b>, puntos de entrada seguros y ensayos delante de otras personas."),
}

EXTRA = {}

EXTRA[1] = (
    "<h3>¿Por qué funciona estudiar despacio?</h3>"
    "<p>Cuando repites un movimiento, el cerebro lo va «grabando» hasta que sale solo (es la <b>memoria motora</b>, la misma que usas para escribir o ir en bici). El problema es que <b>graba todo lo que repites, también los errores</b>. Si tocas un pasaje diez veces deprisa y fallas cinco, has «entrenado» el fallo cinco veces.</p>"
    "<p>Tocar despacio da tiempo al cerebro a dar la orden correcta a cada dedo. Es como aprender un camino nuevo por la ciudad: primero vas mirando cada calle; después de muchas veces, llegas sin pensar.</p>"
    + caja("La regla de oro:", "si te equivocas dos veces seguidas en el mismo sitio, <b>el tempo es demasiado rápido</b>. Bájalo hasta que salga bien tres veces seguidas.")
    + "<h3>Cinco preguntas antes de sentarte al piano</h3>"
    + lista(["¿Qué quiero mejorar hoy? (no «la obra», sino «los compases 9 a 12»).", "¿A qué tempo voy a empezar? Apúntalo.", "¿Qué digitación voy a usar? Escríbela en la partitura.", "¿Cómo sabré que lo he conseguido? Por ejemplo: «tres veces seguidas sin errores a negra = 80».", "¿Cuánto tiempo le voy a dedicar? Mejor 15 minutos concentrados que una hora distraída."], "❓")
    + "<h3>Cuatro trucos de estudio que usan los profesionales</h3>"
    + tabla(["Truco", "Cómo se hace", "Para qué sirve"], [
        ["Con ritmos", "Toca el pasaje con ritmo largo-corto (corchea con puntillo + semicorchea) y luego corto-largo", "Iguala los dedos y hace más fácil el ritmo regular"],
        ["Por bloques", "Toca juntas, como un acorde, las notas de cada posición de la mano", "La mano aprende las «formas» y los cambios de posición"],
        ["Desde el final", "Aprende el último compás, luego los dos últimos, y así hacia atrás", "El final queda tan seguro como el principio"],
        ["Pausa antes del salto", "Para justo antes de un cambio de posición, prepara la mano y toca", "Elimina las dudas en los saltos"]])
    + practica("Plan de 20 minutos para un pasaje difícil", [
        "<b>2 min</b> · Lee el pasaje sin tocar: digitación, notas, alteraciones.",
        "<b>5 min</b> · Mano derecha sola, a la mitad del tempo, por trozos de 1-2 compases.",
        "<b>5 min</b> · Mano izquierda sola, igual.",
        "<b>5 min</b> · Manos juntas, todavía más lento; tres repeticiones limpias y subes 4 bpm.",
        "<b>3 min</b> · Toca el pasaje dentro de su contexto: desde dos compases antes hasta dos después."])
    + errores([
        ["Siempre empiezo la obra desde el principio", "Es lo más cómodo", "Trabaja primero el trozo difícil; la obra entera, al final de la sesión"],
        ["Acelero en lo fácil y freno en lo difícil", "El tempo lo marca lo que ya sale", "Usa metrónomo y elige el tempo del pasaje más difícil"],
        ["Me canso enseguida", "Tensión en hombros y muñecas", "Comprueba cada pocos minutos que hombros y muñecas están sueltos; descansa 5 min cada 25"],
        ["Mañana no me acuerdo de lo de hoy", "Faltan repeticiones correctas y descanso", "Repasa al día siguiente lo del día anterior antes de seguir"]])
)

EXTRA[2] = (
    "<h3>El pentagrama, explicado fácil</h3>"
    "<p>Cada línea y cada espacio es una nota, y van subiendo de una en una (Do, Re, Mi…): si una nota está en una línea, la siguiente está en el espacio de encima. Por eso no hace falta «contar líneas»: basta con mirar <b>la distancia</b> entre notas.</p>"
    + tabla(["Lo que ves", "Lo que significa", "Ejemplo desde Do"], [
        ["Línea → espacio de al lado (o al revés)", "Una 2.ª (nota vecina)", "Do → Re"],
        ["Línea → línea siguiente (o espacio → espacio)", "Una 3.ª", "Do → Mi"],
        ["Salta una línea entera", "Una 5.ª", "Do → Sol"],
        ["Misma posición, una octava más arriba", "Una 8.ª (octava)", "Do → Do"]])
    + "<h3>Las figuras: cuánto dura cada nota</h3>"
    + tabla(["Figura", "Dura (en negras)", "Truco"], [["Redonda", "4", "Un compás entero de 4/4"], ["Blanca", "2", "La mitad de la redonda"], ["Negra", "1", "El pulso más habitual"], ["Corchea", "½", "Dos por pulso: «1-y»"], ["Semicorchea", "¼", "Cuatro por pulso: «1-e-y-a»"], ["Puntillo (·)", "+ la mitad", "Negra con puntillo = 1 + ½ = 1½"]])
    + "<h3>Compás simple y compás compuesto</h3>"
    "<p>En <b>3/4</b> y en <b>6/8</b> caben las mismas seis corcheas, pero se agrupan distinto. En 3/4 se cuentan <b>tres pulsos</b>, cada uno partido en dos. En 6/8 se cuentan <b>dos pulsos</b>, cada uno partido en tres. Escúchalo y cuenta los números escritos bajo las notas:</p>"
    "[[partitura:pulso_68]]"
    "[[partitura:ritmos]]"
    + caja("Para contar en voz alta:", "di los números del pulso más fuerte y las subdivisiones más flojo: «<b>UNO</b>-y-<b>DOS</b>-y». Si al tocar no puedes contar, el tempo es demasiado rápido.")
    + practica("Cinco minutos diarios de lectura a primera vista", [
        "Elige una pieza más fácil que las que estudias (dos niveles por debajo).",
        "30 segundos de «escaneo»: armadura, compás, notas más agudas y más graves, ritmos raros.",
        "Pon el metrónomo lento y toca <b>sin parar</b>, aunque falles: el pulso manda.",
        "No mires las manos: mantén los ojos en la partitura, un poco por delante de lo que tocas.",
        "Cambia de pieza cada día: la primera vista se entrena con música nueva."])
    + errores([
        ["Paro cada vez que fallo una nota", "Costumbre de corregir", "En lectura a primera vista, sigue: el pulso es más importante que una nota"],
        ["Toco notas «naturales» que debían ser sostenidas", "No miré la armadura", "Antes de tocar, di en voz alta las alteraciones de la armadura"],
        ["Pierdo el sitio en la partitura", "Miro las manos", "Aprende la posición de las teclas por tacto y deja los ojos en el papel"]])
)

EXTRA[3] = (
    "<h3>Tono y semitono: la «regla» del teclado</h3>"
    "<p>Un <b>semitono</b> es la distancia más pequeña del piano: de una tecla a la de al lado, sea blanca o negra, sin saltarte ninguna. Un <b>tono</b> son dos semitonos. Fíjate en que <b>Mi–Fa</b> y <b>Si–Do</b> no tienen tecla negra en medio: son semitonos.</p>"
    "[[fig:teclado_pasos_do.svg|Escala de Do mayor con los tonos y semitonos entre sus notas|Do mayor: tono, tono, semitono, tono, tono, tono, semitono. Todas las escalas mayores siguen este patrón.]]"
    "<h3>Construir cualquier escala mayor</h3>"
    + pasos(["Escribe las siete notas seguidas desde la nota inicial (Sol, La, Si, Do, Re, Mi, Fa, Sol).",
             "Comprueba el patrón T-T-S-T-T-T-S entre cada pareja.",
             "Donde no se cumpla, sube o baja la nota con ♯ o ♭. En Sol mayor, de Mi a Fa hay un semitono y debería haber un tono: por eso Fa se convierte en <b>Fa♯</b>.",
             "Las alteraciones que te salen son la <b>armadura</b> de esa tonalidad."])
    + "[[partitura:escala_sol]]"
    "<p>En Fa mayor ocurre lo contrario: entre La y Si debería haber un semitono, así que Si baja a <b>Si♭</b>. Y como el pulgar no debe caer en una tecla negra, la mano derecha cambia de digitación:</p>"
    "[[partitura:escala_fa]]"
    + practica("Cómo practicar las escalas cada día (10 minutos)", [
        "Elige dos tonalidades vecinas del círculo de quintas (por ejemplo, Sol y Re). Cambia cada semana.",
        "Manos separadas, una octava, a negra = 60: atención al paso del pulgar, sin acentos.",
        "Manos juntas, dos octavas, en corcheas.",
        "Con ritmos (largo-corto y corto-largo) y en staccato y legato.",
        "Termina tocando la escala con los ojos cerrados: el tacto se convierte en tu mapa."])
    + errores([
        ["Se oye un «golpe» al pasar el pulgar", "El pulgar llega tarde y cae de golpe", "Mueve el pulgar por debajo de la mano antes de necesitarlo, ya preparado sobre su tecla"],
        ["El codo se abre al pasar el pulgar", "La mano gira en lugar de desplazarse", "Desplaza el antebrazo en horizontal y deja el codo cerca del cuerpo"],
        ["Las dos manos no van juntas", "Los pasos de pulgar no coinciden y una mano se adelanta", "Practica manos juntas solo el tramo donde se desajustan, muy lento"]])
)

EXTRA[4] = (
    "<h3>Mayor o menor: cuenta los semitonos</h3>"
    "<p>La diferencia está en la nota del medio (la <b>tercera</b>). Desde la fundamental cuenta las teclas, blancas y negras: si hay <b>4 semitonos</b> es una 3.ª mayor (acorde alegre, mayor); si hay <b>3</b>, es una 3.ª menor (acorde más triste, menor).</p>"
    "[[fig:teclado_3M.svg|Tercera mayor Do–Mi: cuatro semitonos|Do → Mi: 4 semitonos = 3.ª mayor → Do mayor.]]"
    "[[fig:teclado_3m.svg|Tercera menor Do–Mi bemol: tres semitonos|Do → Mi♭ (la tecla negra marcada con 3): 3 semitonos = 3.ª menor → Do menor.]]"
    + caja("Truco rápido:", "para pasar de un acorde mayor a uno menor, <b>baja un semitono la nota del medio</b>. Do–Mi–Sol → Do–Mi♭–Sol.")
    + "<h3>Las inversiones, como una rueda</h3>"
    "<p>Invertir un acorde es «hacerlo rodar»: la nota de abajo sube una octava y se coloca arriba. Do–Mi–Sol → Mi–Sol–Do → Sol–Do–Mi. Las notas son las mismas; cambia cuál queda en el bajo. Para reconocer un acorde invertido, reordénalo mentalmente en terceras («una sí, una no»): la nota de abajo de esa torre es la fundamental.</p>"
    + tabla(["Tonalidad de Do mayor: acordes de cada grado", "Notas", "Tipo"], [["I", "Do–Mi–Sol", "Mayor"], ["ii", "Re–Fa–La", "Menor"], ["iii", "Mi–Sol–Si", "Menor"], ["IV", "Fa–La–Do", "Mayor"], ["V", "Sol–Si–Re", "Mayor"], ["vi", "La–Do–Mi", "Menor"], ["vii°", "Si–Re–Fa", "Disminuido"]])
    + practica("Ejercicio diario de acordes (8 minutos)", [
        "Toca los siete acordes de Do mayor de la tabla, subiendo, con la mano derecha en bloque (1-3-5).",
        "Repite cada acorde en sus tres posiciones: fundamental, 1.ª y 2.ª inversión.",
        "Toca la fundamental con la mano izquierda y el acorde con la derecha.",
        "Haz lo mismo en Sol mayor y en Fa mayor (recuerda Fa♯ y Si♭).",
        "Arpegia cada acorde despacio, con el brazo acompañando a la mano."])
    + errores([
        ["El arpegio suena «a saltos»", "El pulgar se estira y la muñeca baja", "Deja que el antebrazo se desplace y mantén la muñeca a la altura de las teclas"],
        ["Confundo mayor y menor", "Miro solo las teclas blancas", "Cuenta los semitonos de la 3.ª: 4 = mayor, 3 = menor"],
        ["No reconozco un acorde invertido", "Busco la fundamental en el bajo", "Reordena las notas en terceras: la de abajo de la torre es la fundamental"]])
)

EXTRA[5] = (
    "<h3>La armonía como una historia</h3>"
    "<p>Imagina que cada acorde es un lugar. La <b>tónica (I)</b> es tu casa: allí todo está en reposo. La <b>subdominante (IV)</b> es salir de paseo: te alejas, pero tranquilo. La <b>dominante (V)</b> es el camino de vuelta: notas que falta algo hasta que llegas a casa. Por eso casi todas las canciones terminan V → I.</p>"
    "<p>¿Por qué el V «quiere» ir al I? Porque contiene la <b>sensible</b> (en Do mayor, Si), que está a solo un semitono de la tónica (Do) y «tira» hacia ella. Si además añades la 7.ª (Fa), esta «cae» al Mi. Dos notas tirando hacia el acorde de casa: tensión que pide resolverse.</p>"
    + caja("Los números romanos:", "en mayúscula (I, IV, V) los acordes mayores; en minúscula (ii, iii, vi) los menores; con ° el disminuido. Así una progresión sirve para cualquier tonalidad: I–IV–V–I es Do–Fa–Sol–Do en Do mayor y Sol–Do–Re–Sol en Sol mayor.")
    + "[[partitura:cadencia_sol]]"
    + practica("Entrenar el oído armónico (5 minutos)", [
        "Toca I–IV–V7–I en Do y escucha cómo el último acorde «cierra».",
        "Toca I–IV–V7 y para: notarás que la música se queda «en el aire» (semicadencia).",
        "Toca I–IV–V7–vi: sorpresa, es la cadencia rota.",
        "Pide a alguien que toque una de las tres y adivina cuál es.",
        "Repite todo en Sol mayor con la partitura de arriba."])
    + errores([
        ["Muevo la mano entera de un acorde a otro", "Pienso cada acorde por separado", "Busca las notas comunes y déjalas quietas; mueve solo las demás"],
        ["El V7 suena «raro»", "Falta la 7.ª o la sensible", "Comprueba que el acorde tiene la sensible (Si en Do) y la 7.ª (Fa)"],
        ["No sé en qué tonalidad estoy", "No miro la armadura ni el final", "Mira la armadura y el último acorde de la obra: suele ser la tónica"]])
)

EXTRA[6] = (
    "<h3>¿Por qué cuesta tanto separar las manos?</h3>"
    "<p>El cerebro tiende a que las dos manos hagan lo mismo a la vez (prueba a dibujar un círculo con una mano y un cuadrado con la otra). Para separarlas hay que conseguir que una de las dos funcione <b>en automático</b>, sin pensar, y dedicar la atención a la otra.</p>"
    + pasos(["Toca el acompañamiento solo hasta poder hacerlo mientras hablas o cuentas en voz alta.",
             "Toca la melodía sola, cantándola.",
             "Junta las manos <b>muy despacio</b>, compás a compás, y vigila dónde coinciden las notas.",
             "Cuando salga, ajusta el volumen: melodía <i>mf</i>, acompañamiento <i>p</i>."])
    + "<h3>El vals: «UM-pa-pa»</h3>"
    "<p>En el vals la mano izquierda toca el <b>bajo en el primer tiempo</b> (con más peso) y el <b>acorde en el segundo y el tercero</b> (ligeros). El salto entre el bajo y el acorde se prepara: la mano se mueve justo después de tocar, no en el último instante.</p>"
    "[[partitura:vals]]"
    + practica("Ejercicio de equilibrio entre manos (5 minutos)", [
        "Toca un acorde de Do con las dos manos a la vez: izquierda <i>pp</i>, derecha <i>f</i>.",
        "Cambia: izquierda <i>f</i>, derecha <i>pp</i>.",
        "Toca el vals con la izquierda casi en susurro y la melodía «cantando».",
        "Grábate y escucha: ¿se entiende la melodía sin esfuerzo?"])
    + errores([
        ["El acompañamiento tapa la melodía", "Las dos manos tocan con el mismo peso", "Practica la izquierda sola en <i>pp</i> y luego junta las manos sin cambiarla"],
        ["En el bajo Alberti se oye cada nota acentuada", "Los dedos «golpean» una a una", "Deja que la mano oscile ligeramente desde la muñeca, como un balanceo"],
        ["En el vals llego tarde al acorde", "Muevo la mano en el último momento", "Mueve la mano hacia el acorde justo después de tocar el bajo"]])
)

EXTRA[7] = (
    "<h3>Cómo funciona el pedal por dentro</h3>"
    "<p>Dentro del piano, cada cuerda tiene un <b>apagador</b>: un trocito de fieltro que la toca y la hace callar cuando sueltas la tecla. El pedal derecho <b>levanta todos los apagadores</b>: las cuerdas siguen sonando aunque sueltes las teclas, y además vibran por simpatía otras cuerdas, lo que da al sonido más riqueza.</p>"
    + caja("Por eso hay que cambiarlo:", "si mantienes el pedal al cambiar de acorde, las notas del acorde anterior siguen sonando y se mezclan con el nuevo: es lo que los pianistas llaman «ensuciar» o «emborronar».")
    + "<h3>El pedal sincopado, paso a paso</h3>"
    + pasos(["Toca el acorde con el pie arriba.",
             "<b>Después</b> de que suene, pisa el pedal.",
             "Toca el acorde siguiente y, <b>en ese instante</b>, levanta el pie…",
             "…y vuelve a pisar enseguida. Di en voz alta: «toca — sube — baja»."])
    + "<p>El talón se queda siempre apoyado en el suelo y el movimiento sale del tobillo. No hace falta pisar hasta el fondo: a menudo basta con medio recorrido.</p>"
    + practica("Ejercicio progresivo de pedal (10 minutos)", [
        "Sin piano, con el pie: «toca-sube-baja» siguiendo el metrónomo.",
        "Acordes de Do, La menor, Fa y Sol en blancas, con pedal sincopado en cada uno.",
        "Los mismos acordes en negras: el cambio de pedal se vuelve más rápido.",
        "La partitura de pedal del módulo, con la melodía.",
        "Escucha: si hay un corte de sonido, has levantado demasiado pronto; si hay mezcla, demasiado tarde."])
    + errores([
        ["Se oye un «hueco» entre acordes", "Levanto el pedal antes de tocar el acorde nuevo", "Primero toca, luego cambia el pedal"],
        ["Todo suena mezclado", "No cambio el pedal o lo cambio tarde", "Cambia en cada cambio de armonía; escucha más que mires"],
        ["El pie hace ruido al pisar", "Golpeo el pedal o levanto el talón", "Pie siempre en contacto con el pedal y talón apoyado"]])
)

EXTRA[8] = (
    "<h3>Analizar una obra en 5 preguntas</h3>"
    + tabla(["Pregunta", "Dónde mirar", "En «Para Elisa»"], [
        ["¿En qué tonalidad está?", "Armadura y último acorde", "La menor"],
        ["¿En qué partes se divide?", "Repeticiones, cambios de carácter, dobles barras", "A–B–A–C–A (rondó)"],
        ["¿Qué patrón se repite?", "Dibujos de acompañamiento y melodía", "Arpegio de la mano izquierda que continúa la derecha"],
        ["¿Dónde está lo difícil?", "Saltos, notas rápidas, cambios de mano", "La alternancia Mi–Re♯ y el paso de una mano a otra sin cortes"],
        ["¿Cuál es el punto culminante?", "Notas más agudas o más intensas", "En la sección B, más enérgica"]])
    + "<h3>Cómo estudiar el preludio de Bach</h3>"
    + pasos(["Toca cada compás como un <b>acorde en bloque</b>: así ves la armonía.",
             "Escucha la sucesión de acordes y decide hacia dónde «va» la música.",
             "Toca el patrón de arpegio despacio, sin pedal, con todas las notas iguales.",
             "En la versión original, la mano izquierda <b>mantiene</b> sus dos primeras notas: practícalo sintiendo el bajo."])
    + "<h3>Cómo estudiar «Para Elisa»</h3>"
    "<p>El reto es que las dos manos se pasen la melodía sin que se note el cambio. Practica la línea de semicorcheas como si fuera de una sola mano: escúchala con los ojos cerrados y busca que no haya ni hueco ni acento al pasar de la derecha a la izquierda.</p>"
    + practica("Plan de dos semanas para una obra corta", [
        "<b>Días 1-2</b> · Escuchar, analizar (tabla de arriba) y escribir digitaciones.",
        "<b>Días 3-6</b> · Sección por sección, manos separadas y luego juntas, lento.",
        "<b>Días 7-10</b> · Unir secciones; pedal y dinámicas.",
        "<b>Días 11-14</b> · Subir al tempo final; pasadas completas; grabarte."])
    + errores([
        ["Me sé el principio y el resto no", "Siempre empiezo desde el principio", "Estudia cada sección por separado y empieza cada día por una distinta"],
        ["Las semicorcheas de Para Elisa suenan desiguales", "Los dedos 4-5 son más débiles", "Practica Mi–Re♯ con ritmos y con la mano relajada"],
        ["El preludio de Bach suena mecánico", "Todas las notas a la vez y sin dirección", "Piensa en la armonía: crece hacia los acordes con más tensión y relaja en los de reposo"]])
)

EXTRA[9] = (
    "<h3>El peso del brazo</h3>"
    "<p>Prueba esto: deja el brazo colgando, relajado, y apoya el 3.er dedo sobre una tecla. Deja que el peso del brazo la baje, sin empujar. Ese sonido lleno y sin esfuerzo es la base de la técnica avanzada. La mano hace de <b>puente firme</b> que transmite el peso; la muñeca y el hombro, en cambio, están sueltos.</p>"
    "<h3>Octavas sin dolor</h3>"
    + pasos(["Coloca la mano en octava (pulgar y 5.º) y déjala firme como un puente.",
             "Repite una sola octava, «rebotando» desde la muñeca, como si botaras una pelota.",
             "Avanza por grupos de cuatro notas y para: la pausa evita la tensión.",
             "Sube el tempo solo cuando el rebote sea suelto."])
    + "<h3>Trinos regulares</h3>"
    "<p>Usa dedos vecinos fuertes (2-3 o 1-3). Los dedos no se levantan mucho: trabajan <b>desde la superficie de la tecla</b>. Practícalo con ritmo medido: 2, 3, 4 y 6 notas por pulso, y después libre.</p>"
    + practica("Calentamiento seguro (5 minutos) antes de la técnica", [
        "Rota los hombros y deja caer los brazos varias veces.",
        "Notas largas con peso de brazo en cada dedo.",
        "Escala lenta de Do en legato, dos octavas.",
        "Solo entonces, octavas o terceras: tres series cortas con pausas."])
    + errores([
        ["Me duele la muñeca o el antebrazo", "Aprieto en lugar de dejar caer el peso", "Para, descansa y vuelve a empezar más lento. Si el dolor persiste, consulta a un profesional"],
        ["Las octavas suenan duras", "Brazo rígido", "Rebote desde la muñeca y sonido «hacia dentro» de la tecla"],
        ["El trino se acelera y se descontrola", "Dedos levantados y tensos", "Practica medido con metrónomo y dedos pegados a las teclas"]])
)

EXTRA[10] = (
    "<h3>Paso a paso, sin piano</h3>"
    + pasos(["Sobre la mesa, la mano izquierda da 2 golpes por pulso y la derecha 3.",
             "Primero cuenta la cuadrícula de 6 en voz alta: 1-2-3-4-5-6.",
             "Mano derecha en 1-3-5; mano izquierda en 1-4. Muy lento.",
             "Cuando salga, cambia los números por la frase rítmica «<b>jun</b>-tas, de-re-cha, iz-quier-da, de-re-cha».",
             "Lleva el ritmo al piano con una sola nota por mano y, por último, con la partitura."])
    + tabla(["4 contra 3 (cuadrícula de 12)", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"], [
        ["Mano de 4", "●", "", "", "●", "", "", "●", "", "", "●", "", ""],
        ["Mano de 3", "●", "", "", "", "●", "", "", "", "●", "", "", ""]])
    + caja("Del contar al sentir:", "cuando te salga contando, pon el metrónomo marcando solo el pulso y deja de contar subdivisiones. Siente la mano lenta como el pulso y la rápida «fluyendo» por encima.")
    + errores([
        ["Las dos manos acaban tocando el mismo ritmo", "El cerebro tiende a igualarlas", "Vuelve a la mesa y a la cuadrícula; exagera la diferencia"],
        ["El 3 contra 2 suena como un ritmo con puntillo", "La nota central se desplaza", "Cuenta 6 subdivisiones exactas; la nota de la derecha en el 3 y la de la izquierda en el 4"],
        ["Me pierdo al subir el tempo", "Subo demasiado rápido", "Sube de 4 en 4 bpm y solo con tres repeticiones correctas"]])
)

EXTRA[11] = (
    "<h3>Construir las séptimas contando semitonos</h3>"
    + tabla(["Acorde", "Semitonos entre notas", "En Do", "Cómo suena"], [
        ["Cmaj7", "4 + 3 + 4", "Do–Mi–Sol–Si", "Luminoso, tranquilo"],
        ["C7", "4 + 3 + 3", "Do–Mi–Sol–Si♭", "Tenso, pide resolver (dominante)"],
        ["Cm7", "3 + 4 + 3", "Do–Mi♭–Sol–Si♭", "Suave, melancólico"],
        ["Cm7♭5 (Cø)", "3 + 3 + 4", "Do–Mi♭–Sol♭–Si♭", "Inestable"],
        ["C°7", "3 + 3 + 3", "Do–Mi♭–Sol♭–La", "Muy tenso, misterioso"]])
    + "<h3>¿Por qué se puede quitar la fundamental?</h3>"
    "<p>Piensa en un equipo: si el bajista ya toca la fundamental, el pianista no necesita repetirla. Sus dedos quedan libres para las notas que dan <b>color</b> (3.ª, 7.ª y tensiones). Además, los voicings sin fundamental cambian muy poco de un acorde a otro, así que suenan más «enlazados».</p>"
    + "<h3>Leer el cifrado moderno</h3>"
    + tabla(["Símbolo", "Significa", "Ejemplo"], [["m", "Menor", "Am = La menor"], ["7", "Séptima menor (dominante si el acorde es mayor)", "G7 = Sol–Si–Re–Fa"], ["maj7 / Δ", "Séptima mayor", "Fmaj7 = Fa–La–Do–Mi"], ["ø / m7♭5", "Semidisminuido", "Bø = Si–Re–Fa–La"], ["(9), (13)", "Tensión añadida", "C7(9) = C7 + Re"], ["/", "Nota del bajo", "C/E = Do con Mi en el bajo"]])
    + caja("El ii–V–I es la «cadencia del jazz»:", "es la misma historia del módulo 5 (subdominante → dominante → tónica), pero con acordes de cuatro notas. Las líneas de 3.ª y 7.ª se mueven por grado conjunto: escúchalas tocando solo esas dos notas de cada acorde.")
    + practica("Ejercicio de voicings (10 minutos)", [
        "Toca el ii–V–I de Do solo con 3.ª y 7.ª (shell voicings) en la mano derecha y la fundamental en la izquierda.",
        "Añade la 5.ª y la 9.ª (el voicing completo de la partitura).",
        "Repite en Fa mayor (partitura) y en Si♭ mayor (siguiente en el círculo de quintas).",
        "Toca el ii–V–I con un ritmo de swing en la mano derecha."])
    + errores([
        ["Los acordes suenan «pesados»", "Toco la fundamental en las dos manos y muy grave", "Deja la fundamental al bajo y coloca los voicings en el registro central"],
        ["Me pierdo entre tantas notas", "Intento pensar las cuatro a la vez", "Piensa primero en 3.ª y 7.ª; las demás se añaden alrededor"]])
)

EXTRA[12] = (
    "<h3>Una frase de ejemplo</h3>"
    "<p>Escucha esta frase hecha solo con la escala de blues. Fíjate en cómo los dos primeros compases «preguntan» y los dos siguientes «responden», y en la <b>nota azul</b> (Mi♭) que se desliza al Mi.</p>"
    "[[partitura:blues_frase]]"
    + "<h3>Cinco reglas para empezar a improvisar</h3>"
    + lista(["<b>Pocas notas:</b> empieza con tres (Do, Mi♭, Fa). Las limitaciones liberan.",
             "<b>Ritmo antes que notas:</b> una nota repetida con buen ritmo ya suena a blues.",
             "<b>Repite tus ideas:</b> tocar una frase dos veces y cambiar el final suena intencionado.",
             "<b>Deja silencios:</b> si tocas sin parar, nadie entiende la «conversación».",
             "<b>Termina en una nota del acorde:</b> Do, Mi o Sol sobre Do7 suenan a «punto final»."], "🎵")
    + caja("El swing:", "las corcheas no se tocan iguales, sino «larga-corta», como un tresillo en el que las dos primeras notas van unidas: «<b>DUU</b>-ba, <b>DUU</b>-ba». Escucha jazz o blues y lo notarás enseguida.")
    + practica("10 minutos de improvisación al día", [
        "2 min · Bajo boogie solo con la izquierda hasta que vaya en automático.",
        "3 min · Derecha con 3 notas: frases de 2 compases y 2 compases de silencio.",
        "3 min · Toda la escala de blues; pregunta y respuesta.",
        "2 min · Grábate y escucha: ¿qué frase repetirías?"])
    + errores([
        ["Me bloqueo y no sé qué tocar", "Demasiadas opciones", "Limítate a tres notas y juega solo con el ritmo"],
        ["Suena a escala subiendo y bajando", "Toco las notas en orden", "Salta entre notas, repite y deja silencios"],
        ["Pierdo el sitio en los 12 compases", "Me concentro solo en la derecha", "Cuenta los compases en voz alta o piensa en los acordes mientras tocas"]])
)

EXTRA[13] = (
    "<h3>Haz un «mapa» de la obra</h3>"
    + pasos(["Con lápiz, marca dónde empieza y termina cada frase (como las frases de un texto).",
             "En cada frase, marca la nota más importante: el punto culminante.",
             "Dibuja flechas: hacia dónde crece y hacia dónde se relaja la música.",
             "Marca las respiraciones: pequeños espacios antes de cada nueva frase.",
             "Toca la obra siguiendo el mapa, aunque al principio parezca exagerado."])
    + "<h3>El rubato bien hecho</h3>"
    "<p>«Rubato» significa «robado»: alargas un poco unas notas y lo compensas acelerando otras. La clave es que <b>el tiempo que robas se devuelve</b>: al final de la frase el pulso general sigue en su sitio. Si cada frase se alarga sin compensar, ya no es rubato, es ir cada vez más lento.</p>"
    + caja("Escucha comparando:", "elige una obra y escucha dos versiones de pianistas distintos. Anota las diferencias de tempo, dinámica y pedal. Descubrirás que no hay una sola manera correcta: hay decisiones coherentes.")
    + practica("Trabajo de interpretación (15 minutos)", [
        "Canta la melodía de la primera frase: imita al piano cómo la has cantado.",
        "Toca la frase tres veces: <i>p</i>, <i>mf</i> y <i>f</i>; elige la que mejor encaje.",
        "Toca solo el bajo y la melodía, sin las voces intermedias, para oír la estructura.",
        "Grábate y escucha con la partitura: ¿se oyen tus decisiones?"])
    + errores([
        ["Todo suena igual de fuerte", "No hay plan dinámico", "Haz el mapa de la obra y exagera los contrastes al estudiar"],
        ["El rubato suena a «tocar irregular»", "No devuelvo el tiempo robado", "Practica la frase con metrónomo y luego libera solo un poco el tempo"],
        ["Bach suena como Chopin", "Mismo pedal y rubato para todo", "Repasa la tabla de estilos: cada época tiene su manera de tocar"]])
)

EXTRA[14] = (
    "<h3>Memorizar por capas, paso a paso</h3>"
    + pasos(["<b>Análisis:</b> escribe en la partitura los acordes y las secciones. Es la memoria más fiable.",
             "<b>Visual:</b> mira un trozo, cierra los ojos y «visualiza» la página y las teclas.",
             "<b>Auditiva:</b> canta la melodía y el bajo sin tocar.",
             "<b>Motriz:</b> tócalo de memoria, despacio, en un piano o incluso sobre la mesa.",
             "<b>Prueba de fuego:</b> empieza desde cualquier punto de entrada y toca la obra mentalmente, lejos del piano."])
    + tabla(["El día de la actuación", "Qué hacer"], [
        ["Por la mañana", "Repaso lento y tranquilo, sin pasadas a toda velocidad"],
        ["Una hora antes", "Calentamiento suave: escalas lentas y notas largas"],
        ["Justo antes", "Respiración lenta (inspira 4 segundos, espira 6); piensa en el carácter del principio"],
        ["Al sentarte", "Ajusta la banqueta, pon las manos sobre las rodillas, escucha mentalmente los primeros compases y empieza"],
        ["Después", "Anota qué salió bien y qué mejorarías: es tu plan para la próxima vez"]])
    + errores([
        ["Me quedo en blanco", "Memoria solo motriz", "Refuerza la memoria analítica y practica desde los puntos de entrada"],
        ["Toco mucho más rápido que en casa", "Los nervios aceleran", "Imagina el pulso de los primeros compases antes de empezar"],
        ["Me tiemblan las manos", "Adrenalina", "Respiración lenta y ensayos previos ante otras personas: la costumbre reduce el temblor"]])
)

GLOSARIO = [
    ("Acorde", "Tres o más notas que suenan a la vez."), ("Armadura", "Alteraciones al principio del pentagrama que afectan a toda la obra."),
    ("Arpegio", "Acorde tocado nota a nota."), ("bpm", "Pulsos por minuto: la velocidad del metrónomo."),
    ("Cadencia", "Enlace de acordes que cierra una frase (por ejemplo, V–I)."), ("Cifrado", "Nombre de un acorde con letras y símbolos (C, Am, G7…)."),
    ("Compás", "Agrupación de pulsos (2/4, 3/4, 4/4, 6/8…)."), ("Digitación", "Número de dedo para cada nota: 1 pulgar … 5 meñique."),
    ("Dinámica", "Intensidad del sonido: <i>p</i> (suave), <i>f</i> (fuerte)…"), ("Dominante (V)", "Acorde de tensión que pide volver a la tónica."),
    ("Escala", "Sucesión ordenada de notas con un patrón de tonos y semitonos."), ("Fraseo", "Manera de agrupar y dar forma a las frases musicales."),
    ("Intervalo", "Distancia entre dos notas."), ("Inversión", "Acorde cuya nota más grave no es la fundamental."),
    ("Legato", "Notas ligadas, sin cortes entre ellas."), ("Octava", "Distancia entre dos notas del mismo nombre (Do–Do)."),
    ("Polirritmia", "Dos ritmos distintos a la vez (3 contra 2…)."), ("Rubato", "Flexibilidad expresiva del tempo."),
    ("Semitono", "La distancia más pequeña del piano: de una tecla a la de al lado."), ("Sensible", "7.º grado de la escala, a un semitono de la tónica."),
    ("Staccato", "Notas cortas y separadas."), ("Tónica (I)", "Primer grado: la nota y el acorde de «reposo»."),
    ("Tono", "Dos semitonos."), ("Tresillo", "Tres notas en el tiempo de dos."),
    ("Voicing", "Forma concreta de colocar las notas de un acorde."),
]
