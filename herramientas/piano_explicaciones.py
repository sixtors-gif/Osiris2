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


def como(texto):
    return f'<div class="como"><b>💡 Cómo se hace:</b> {texto}</div>'


def pasos(items):
    """items: texto del paso, o (paso, cómo se hace) para añadir la explicación práctica debajo."""
    def li(i):
        return f"<li>{i[0]}{como(i[1])}</li>" if isinstance(i, tuple) else f"<li>{i}</li>"
    return '<ol class="steps">' + "".join(li(i) for i in items) + "</ol>"


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
        ("<b>2 min</b> · Lee el pasaje sin tocar: digitación, notas, alteraciones.",
              "recorre el pasaje con la vista compás a compás. Rodea con lápiz las alteraciones que no están en la armadura y los cambios de posición de la mano (saltos o pasos del pulgar). Donde dudes de qué dedo usar, prueba sobre la tapa del piano y escribe el número encima de la nota."),
        ("<b>5 min</b> · Mano derecha sola, a la mitad del tempo, por trozos de 1-2 compases.",
              "si el tempo final es negra = 100, pon el metrónomo a 50. Toca el primer trozo <b>terminando en la primera nota del trozo siguiente</b> (así luego se enlazan). Cuando salga tres veces seguidas sin error, pasa al siguiente trozo."),
        "<b>5 min</b> · Mano izquierda sola, igual.",
        ("<b>5 min</b> · Manos juntas, todavía más lento; tres repeticiones limpias y subes 4 bpm.",
              "baja otros 10 bpm respecto a las manos separadas: juntar las manos es más difícil. Cuenta en voz alta las repeticiones correctas; si fallas, el contador vuelve a cero. Al llegar a tres, sube 4 bpm. Si fallas dos veces seguidas, baja 4."),
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
        ("No mires las manos: mantén los ojos en la partitura, un poco por delante de lo que tocas.",
              "antes de empezar, pon la mano en su sitio y busca con las yemas los grupos de 2 y 3 teclas negras: son tus «señales» para orientarte sin mirar. Si necesitas mirar, mueve solo los ojos, un instante, sin girar la cabeza. Para leer por delante, tapa con una tarjeta el compás que estás tocando: te obliga a mirar el siguiente."),
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
    + pasos([("Escribe las siete notas seguidas desde la nota inicial (Sol, La, Si, Do, Re, Mi, Fa, Sol).",
              "escribe los nombres por orden (Do, Re, Mi, Fa, Sol, La, Si) empezando por la nota que quieras y vuelve a ella al final: 8 notas en total. Cada nombre debe aparecer <b>una sola vez</b>; por eso más tarde se escribe Fa♯ y no Sol♭."),
             ("Comprueba el patrón T-T-S-T-T-T-S entre cada pareja.",
              "mira el teclado (o el dibujo de arriba) y cuenta entre cada pareja de notas: si entre las dos teclas hay otra en medio (blanca o negra), es un <b>tono</b>; si están pegadas, sin nada en medio, es un <b>semitono</b>. Escribe T o S debajo de cada pareja y compáralo con T-T-S-T-T-T-S."),
             ("Donde no se cumpla, sube o baja la nota con ♯ o ♭. En Sol mayor, de Mi a Fa hay un semitono y debería haber un tono: por eso Fa se convierte en <b>Fa♯</b>.",
              "si la distancia es <b>más pequeña</b> de la que pide el patrón, sube la nota de arriba con ♯; si es <b>más grande</b>, bájala con ♭. Al cambiar una nota cambian dos distancias (la de antes y la de después), así que vuelve a comprobar la pareja siguiente: en Sol mayor, al subir Fa a Fa♯ queda Fa♯–Sol = semitono, justo lo que pide el final del patrón."),
             ("Las alteraciones que te salen son la <b>armadura</b> de esa tonalidad.",
              "copia las alteraciones al principio del pentagrama, en el orden de siempre: los sostenidos en el orden Fa–Do–Sol–Re–La–Mi–Si y los bemoles en el orden Si–Mi–La–Re–Sol–Do–Fa. Compruébalo con el círculo de quintas del módulo.")])
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
        ("Repite cada acorde en sus tres posiciones: fundamental, 1.ª y 2.ª inversión.",
              "toca el acorde (Do–Mi–Sol), luego sube la nota de abajo una octava (Mi–Sol–Do) y repite (Sol–Do–Mi). Digitación de la derecha: 1-3-5 en la fundamental y 1-2-5 en las inversiones. Mira el teclado: la mano se desplaza sin girar la muñeca."),
        "Toca la fundamental con la mano izquierda y el acorde con la derecha.",
        "Haz lo mismo en Sol mayor y en Fa mayor (recuerda Fa♯ y Si♭).",
        ("Arpegia cada acorde despacio, con el brazo acompañando a la mano.",
              "toca las notas del acorde una tras otra (Do, Mi, Sol, Do…). Antes de que el pulgar tenga que estirarse, deja que el codo y el antebrazo se desplacen hacia la siguiente posición: la mano «viaja» con el brazo, no se abre como un abanico.")])
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
        ("Pide a alguien que toque una de las tres y adivina cuál es.",
              "si no tienes a nadie, grábate en el móvil tocando las tres cadencias varias veces en un orden al azar (sin decirlo en voz alta), espera un día y escucha la grabación anotando cuál crees que es cada una. Pista: si suena a «punto final», es perfecta; si se queda «en el aire», semicadencia; si sorprende, rota."),
        "Repite todo en Sol mayor con la partitura de arriba."])
    + errores([
        ["Muevo la mano entera de un acorde a otro", "Pienso cada acorde por separado", "Busca las notas comunes y déjalas quietas; mueve solo las demás"],
        ["El V7 suena «raro»", "Falta la 7.ª o la sensible", "Comprueba que el acorde tiene la sensible (Si en Do) y la 7.ª (Fa)"],
        ["No sé en qué tonalidad estoy", "No miro la armadura ni el final", "Mira la armadura y el último acorde de la obra: suele ser la tónica"]])
)

EXTRA[6] = (
    "<h3>¿Por qué cuesta tanto separar las manos?</h3>"
    "<p>El cerebro tiende a que las dos manos hagan lo mismo a la vez (prueba a dibujar un círculo con una mano y un cuadrado con la otra). Para separarlas hay que conseguir que una de las dos funcione <b>en automático</b>, sin pensar, y dedicar la atención a la otra.</p>"
    + pasos([("Toca el acompañamiento solo hasta poder hacerlo mientras hablas o cuentas en voz alta.",
              "repite un compás «en bucle», sin parar entre repeticiones, a un tempo lento. Cuando salga cinco veces seguidas sin pensar, cuenta en voz alta «1, 2, 3…»; después di los nombres de las notas de la melodía o cualquier frase («hoy hace sol»). Si al hablar te paras o te equivocas, todavía no es automático: sigue repitiendo."),
             ("Toca la melodía sola, cantándola.",
              "canta o tararea («la, la, la») a la vez que tocas. No importa afinar bien: cantar te obliga a respirar donde respira la frase y a oír la melodía como una línea continua, no como notas sueltas."),
             ("Junta las manos <b>muy despacio</b>, compás a compás, y vigila dónde coinciden las notas.",
              "antes de tocar, busca en la partitura las notas de las dos manos que están <b>una encima de otra</b> (suenan a la vez) y únelas con una rayita vertical de lápiz: son los «puntos de encuentro». Toca primero solo esos puntos, en su ritmo; después rellena las notas que hay entre ellos. Metrónomo a la mitad del tempo o menos."),
             ("Cuando salga, ajusta el volumen: melodía <i>mf</i>, acompañamiento <i>p</i>.",
              "la mano de la melodía baja la tecla con el dedo firme y un poco de peso del brazo; la del acompañamiento toca «desde la superficie», muy cerca de la tecla y bajándola más despacio. Haz el ejercicio de equilibrio de abajo para notar la diferencia.")])
    + "<h3>El vals: «UM-pa-pa»</h3>"
    "<p>En el vals la mano izquierda toca el <b>bajo en el primer tiempo</b> (con más peso) y el <b>acorde en el segundo y el tercero</b> (ligeros). El salto entre el bajo y el acorde se prepara: la mano se mueve justo después de tocar, no en el último instante.</p>"
    "[[partitura:vals]]"
    + practica("Ejercicio de equilibrio entre manos (5 minutos)", [
        "Toca un acorde de Do con las dos manos a la vez: izquierda <i>pp</i>, derecha <i>f</i>.",
        "Cambia: izquierda <i>f</i>, derecha <i>pp</i>.",
        "Toca el vals con la izquierda casi en susurro y la melodía «cantando».",
        ("Grábate y escucha: ¿se entiende la melodía sin esfuerzo?",
              "escucha la grabación sin mirar la partitura. Si puedes tararear la melodía de principio a fin sin «buscarla», el equilibrio es bueno; si tienes que concentrarte para oírla, baja todavía más el acompañamiento.")])
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
    + pasos([("Toca el acorde con el pie arriba.",
              "el pie descansa sobre el pedal sin pisarlo, con el talón apoyado en el suelo. Toca un acorde de Do en blanca y mantén los dedos hundidos."),
             ("<b>Después</b> de que suene, pisa el pedal.",
              "cuenta «1» al tocar y «y» al pisar: el pie baja un instante después de los dedos, suave, sin golpe. Mantén los dedos en las teclas mientras pisas."),
             ("Toca el acorde siguiente y, <b>en ese instante</b>, levanta el pie…",
              "piensa en un balancín: <b>los dedos bajan y el pie sube a la vez</b>. No hace falta subir el pedal del todo; basta con que oigas que el acorde anterior se apaga."),
             ("…y vuelve a pisar enseguida. Di en voz alta: «toca — sube — baja».",
              "en cuanto se apague el acorde anterior (una fracción de segundo), vuelve a bajar el pie; el acorde nuevo sigue sonando porque sigues con los dedos hundidos. Comprobación: suelta los dedos después de pisar; si el acorde nuevo suena limpio, sin restos del anterior, lo has hecho bien.")])
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
    + pasos([("Toca cada compás como un <b>acorde en bloque</b>: así ves la armonía.",
              "en cada compás, junta todas las notas distintas del arpegio y tócalas a la vez: las dos graves con la mano izquierda y las tres agudas con la derecha. Son cinco notas que la mano ya tiene colocadas; escribe encima del compás el nombre del acorde si lo reconoces."),
             ("Escucha la sucesión de acordes y decide hacia dónde «va» la música.",
              "toca los bloques seguidos, uno por pulso lento. Escribe con lápiz <b>T</b> (tensión) en los que suenan inestables y «piden» seguir, y <b>R</b> (reposo) en los que suenan a llegada. Al tocar el preludio, la música crece hacia las T y se relaja en las R."),
             ("Toca el patrón de arpegio despacio, sin pedal, con todas las notas iguales.",
              "metrónomo lento, una nota por clic. Escucha que ninguna sobresalga: si una suena más fuerte (suele ser la del pulgar), tócala a propósito más suave. Cuando todas suenen igual, sube el tempo poco a poco."),
             ("En la versión original, la mano izquierda <b>mantiene</b> sus dos primeras notas: practícalo sintiendo el bajo.",
              "después de tocar las dos notas de la mano izquierda, <b>no levantes esos dedos</b>: déjalos hundidos mientras la derecha arpegia. Así el bajo sigue sonando sin necesidad de pedal.")])
    + "<h3>Cómo estudiar «Para Elisa»</h3>"
    "<p>El reto es que las dos manos se pasen la melodía sin que se note el cambio. Practica la línea de semicorcheas como si fuera de una sola mano: escúchala con los ojos cerrados y busca que no haya ni hueco ni acento al pasar de la derecha a la izquierda.</p>"
    + practica("Plan de dos semanas para una obra corta", [
        "<b>Días 1-2</b> · Escuchar, analizar (tabla de arriba) y escribir digitaciones.",
        "<b>Días 3-6</b> · Sección por sección, manos separadas y luego juntas, lento.",
        ("<b>Días 7-10</b> · Unir secciones; pedal y dinámicas.",
              "el pedal y las dinámicas se añaden cuando las notas ya salen seguras. Une las secciones de dos en dos, tocando desde el final de una hasta el principio de la siguiente. Después añade el pedal en una sección cada día y las dinámicas siguiendo el «mapa» del módulo 13."),
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
    + pasos([("Coloca la mano en octava (pulgar y 5.º) y déjala firme como un puente.",
              "pon el pulgar y el meñique sobre dos Do (en las teclas negras puedes usar el 4.º en lugar del 5.º). Los dedos del medio quedan recogidos, sin tocar. La mano forma un arco firme pero no rígido: comprueba que puedes mover la muñeca arriba y abajo sin que la mano se deforme."),
             ("Repite una sola octava, «rebotando» desde la muñeca, como si botaras una pelota.",
              "con la mano en su sitio, levántala 2-3 cm desde la muñeca y déjala caer sobre la octava; al llegar al fondo de la tecla, deja que «rebote» hacia arriba sola. El antebrazo casi no se mueve. Haz cuatro rebotes y descansa la mano sobre las rodillas."),
             ("Avanza por grupos de cuatro notas y para: la pausa evita la tensión.",
              "toca en octavas Do–Re–Mi–Fa y para con la mano apoyada y suelta sobre el Fa. Comprueba que hombro y muñeca están relajados y continúa desde ahí: Fa–Sol–La–Si, y así sucesivamente."),
             ("Sube el tempo solo cuando el rebote sea suelto.",
              "sube de 4 en 4 bpm. Si notas cansancio o calor en el antebrazo, baja el tempo y descansa. El dolor nunca es normal: si aparece, para.")])
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
    + pasos([("Sobre la mesa, la mano izquierda da 2 golpes por pulso y la derecha 3.",
              "siéntate ante una mesa y golpea con las yemas. Primero cada mano por separado sobre un mismo pulso lento: la izquierda dice «ta-ta» y la derecha «ta-ta-ta», repartidos de forma igual dentro del pulso."),
             ("Primero cuenta la cuadrícula de 6 en voz alta: 1-2-3-4-5-6.",
              "di los números a velocidad constante, como el tictac de un reloj, y marca el «1» más fuerte: cada grupo de seis números es un pulso. Si tienes metrónomo, pon un clic por número."),
             ("Mano derecha en 1-3-5; mano izquierda en 1-4. Muy lento.",
              "mientras cuentas los seis números, golpea primero solo con la derecha en 1, 3 y 5; después solo con la izquierda en 1 y 4; por último, las dos. Fíjate en que solo coinciden en el 1. Mira la tabla de la cuadrícula del módulo si te pierdes."),
             ("Cuando salga, cambia los números por la frase rítmica «<b>jun</b>-tas, de-re-cha, iz-quier-da, de-re-cha».",
              "cada palabra dice quién toca: «juntas» cae en el 1 (las dos manos), «derecha» en el 3, «izquierda» en el 4 y «derecha» en el 5. Dila primero sin manos, encajando cada palabra en su número; después golpea a la vez que la dices."),
             ("Lleva el ritmo al piano con una sola nota por mano y, por último, con la partitura.",
              "izquierda en un Do grave y derecha en un Sol agudo: repite el ritmo hasta que salga cinco veces seguidas. Después toca la partitura de 3 contra 2 del módulo empezando a velocidad 50 %.")])
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
        ("Toca el ii–V–I con un ritmo de swing en la mano derecha.",
              "toca los acordes con corcheas «largo-corto» («DUU-ba, DUU-ba», como en el módulo 12) o pon los acordes solo en los tiempos 2 y 4, como los golpes de una batería, mientras la izquierda toca la fundamental en el 1 y el 3.")])
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
    + pasos([("Con lápiz, marca dónde empieza y termina cada frase (como las frases de un texto).",
              "<b>canta la melodía</b>: donde necesitas respirar de forma natural, ahí suele acabar una frase. Otras pistas: casi todas las frases duran <b>4 u 8 compases</b> (a veces en dos mitades de 2 + 2 o 4 + 4); terminan en una <b>nota larga, un silencio o una cadencia</b> (el V → I del módulo 5); las <b>ligaduras de expresión</b> (arcos largos sobre varias notas) suelen abarcar una frase, y cuando la melodía <b>vuelve a empezar</b> con el mismo motivo, empieza una frase nueva. Dibuja un arco de lápiz encima del pentagrama desde la primera hasta la última nota de cada frase."),
             ("En cada frase, marca la nota más importante: el punto culminante.",
              "suele ser la nota <b>más aguda</b> de la frase, la <b>más larga</b> o la que cae sobre el acorde <b>más tenso</b> (una dominante o una disonancia). Casi nunca está al principio: es frecuente encontrarla hacia los dos tercios de la frase. Si dudas, canta la frase y fíjate en qué nota pondrías más intención. Marca <b>solo una por frase</b> con un círculo o un asterisco."),
             ("Dibuja flechas: hacia dónde crece y hacia dónde se relaja la música.",
              "la música <b>crece</b> cuando la melodía sube, las notas se hacen más rápidas o la armonía se aleja de la tónica (IV, V, acordes con alteraciones); se <b>relaja</b> cuando la melodía baja, las notas se alargan y llega a la tónica en la cadencia. Dibuja un regulador abierto (&lt;) desde el comienzo de la frase hasta el punto culminante y uno cerrado (&gt;) desde ahí hasta el final. Tus flechas son matices <b>dentro</b> de las indicaciones del compositor (<i>cresc.</i>, <i>dim.</i>, <i>p</i>, <i>f</i>), nunca en contra de ellas."),
             ("Marca las respiraciones: pequeños espacios antes de cada nueva frase.",
              "pon una coma pequeña (’) encima del pentagrama al final de cada frase. Al tocar, <b>acorta un poco la última nota</b> de la frase y levanta la mano un instante, como la pausa que haces en un punto al leer en voz alta. El pulso no se detiene: el tiempo de la respiración se le «quita» a la última nota, no se añade. Si usas pedal, levántalo con la respiración."),
             ("Toca la obra siguiendo el mapa, aunque al principio parezca exagerado.",
              "empieza con una sola frase y <b>exagera el doble</b> todo lo marcado (crecimientos, punto culminante, respiración): lo que a ti te parece mucho, desde fuera apenas se nota. Grábate y escucha con el mapa delante; después ajusta hasta que suene natural y pasa a la frase siguiente.")])
    + "<h3>El rubato bien hecho</h3>"
    "<p>«Rubato» significa «robado»: alargas un poco unas notas y lo compensas acelerando otras. La clave es que <b>el tiempo que robas se devuelve</b>: al final de la frase el pulso general sigue en su sitio. Si cada frase se alarga sin compensar, ya no es rubato, es ir cada vez más lento.</p>"
    + caja("Escucha comparando:", "elige una obra y escucha dos versiones de pianistas distintos. Anota las diferencias de tempo, dinámica y pedal. Descubrirás que no hay una sola manera correcta: hay decisiones coherentes.")
    + practica("Trabajo de interpretación (15 minutos)", [
        ("Canta la melodía de la primera frase: imita al piano cómo la has cantado.",
              "canta en voz alta, sin vergüenza, y fíjate en dos cosas: dónde respiras y en qué nota pones más fuerza. Luego tócala buscando lo mismo: la respiración es un pequeño corte antes de la frase siguiente y la fuerza es un poco más de peso del brazo en esa nota."),
        "Toca la frase tres veces: <i>p</i>, <i>mf</i> y <i>f</i>; elige la que mejor encaje.",
        "Toca solo el bajo y la melodía, sin las voces intermedias, para oír la estructura.",
        ("Grábate y escucha con la partitura: ¿se oyen tus decisiones?",
              "escucha con el mapa de la obra delante y comprueba frase a frase: ¿se oye el punto culminante?, ¿se nota la respiración?, ¿crece y se relaja donde dibujaste las flechas? Lo que no se oye en la grabación hay que exagerarlo más.")])
    + errores([
        ["Todo suena igual de fuerte", "No hay plan dinámico", "Haz el mapa de la obra y exagera los contrastes al estudiar"],
        ["El rubato suena a «tocar irregular»", "No devuelvo el tiempo robado", "Practica la frase con metrónomo y luego libera solo un poco el tempo"],
        ["Bach suena como Chopin", "Mismo pedal y rubato para todo", "Repasa la tabla de estilos: cada época tiene su manera de tocar"]])
)

EXTRA[14] = (
    "<h3>Memorizar por capas, paso a paso</h3>"
    + pasos([("<b>Análisis:</b> escribe en la partitura los acordes y las secciones. Es la memoria más fiable.",
              "escribe el cifrado de cada compás encima del pentagrama (como en el módulo 5) y marca las secciones con letras A, B, C… Después intenta decir la secuencia de memoria, en voz alta: «A: Do, Fa, Sol, Do; B: La menor…». Si puedes decirla sin mirar, ya tienes el mapa de la obra en la cabeza."),
             ("<b>Visual:</b> mira un trozo, cierra los ojos y «visualiza» la página y las teclas.",
              "mira dos compases durante 30 segundos fijándote en los dibujos (sube, baja, salta, se repite). Cierra los ojos y descríbelos en voz alta o imagina qué teclas bajan. Abre los ojos y comprueba qué se te había olvidado."),
             ("<b>Auditiva:</b> canta la melodía y el bajo sin tocar.",
              "canta la melodía sin partitura, de principio a fin; después canta solo el bajo. Si puedes cantar las dos líneas (una cada vez), sabes cómo «suena» la obra y, si un día los dedos dudan, el oído te guiará."),
             ("<b>Motriz:</b> tócalo de memoria, despacio, en un piano o incluso sobre la mesa.",
              "toca muy despacio y sin partitura, pensando en cada movimiento. Sobre la mesa (o con la tapa del piano cerrada), mueve los dedos imaginando el sonido. Si dudas en algún punto, abre la partitura <b>solo</b> en ese punto, míralo y vuelve a intentarlo."),
             ("<b>Prueba de fuego:</b> empieza desde cualquier punto de entrada y toca la obra mentalmente, lejos del piano.",
              "marca en la partitura 4-6 «puntos de entrada» (el principio de cada sección) y numéralos. Pide a alguien que diga un número al azar y empieza desde ese punto. Después, lejos del piano y con los ojos cerrados, «toca» la obra mentalmente nota a nota: donde te pierdas, ahí falta memoria.")])
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
