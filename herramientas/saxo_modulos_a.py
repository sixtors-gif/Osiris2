"""Módulos 1 a 7 del curso de saxofón alto: el instrumento, el montaje, la postura, la embocadura, las primeras notas,
las notas del registro grave y medio y la articulación."""
from saxo_helpers import actividad, caja, como, errores, fig, kp, lista, palabras, partitura, pasos, practica, quiz, tabla

MODULOS = []

# 1 --------------------------------------------------------------------------------------------------
MODULOS.append(("🎷", "Conoce tu saxo alto", "Qué es, cómo funciona, qué partes tiene y qué necesitas para empezar.",
    palabras("El saxofón es un instrumento de <b>viento-madera de caña simple</b>: soplas aire, la <b>caña</b> vibra contra la boquilla y el tubo cónico de metal convierte esa vibración en notas. Con <b>una sola digitación</b> aprendida puedes tocar toda la familia.")
    + """
      <h2>El instrumento</h2>
      <h3>1. Qué es el saxofón</h3>
      <p>Lo inventó en la década de 1840 el belga <b>Adolphe Sax</b>, que lo patentó en París en 1846. Quería un instrumento con la potencia de un viento-metal y la agilidad y el color de un viento-madera. Aunque su cuerpo es de metal (normalmente latón), se clasifica como <b>viento-madera</b> porque el sonido nace de una <b>lengüeta</b> —la caña— y no de los labios, como en la trompeta.</p>
      <p>Es muy parecido al clarinete en lo que respecta al sonido (una sola caña), pero el tubo del saxo es <b>cónico</b> (se va ensanchando), lo que hace que, al abrir un pequeño orificio —la llave de octava—, la nota suene una <b>octava</b> más aguda. Esto simplifica la digitación y es una de las razones por las que el saxo se aprende con rapidez.</p>
      <h3>2. La familia del saxofón</h3>"""
    + fig("saxo_familia.svg", "Familia del saxofón: soprano, alto, tenor y barítono", "Cuanto más grande es el saxo, más grave es su sonido. Todos usan los mismos dedos para la misma nota escrita.")
    + tabla(["Saxo", "Afinación", "Tamaño y sonido", "Se usa en…"], [
        ["Sopranino", "Mi♭", "Muy pequeño y agudo", "Orquestas y conjuntos de saxos"],
        ["Soprano", "Si♭", "Recto como un clarinete (o curvo)", "Jazz, clásica, saxofón cantante"],
        ["<b>Alto</b>", "<b>Mi♭</b>", "<b>Mediano: es el saxo más habitual para empezar</b>", "<b>Banda, jazz, clásica, pop y rock</b>"],
        ["Tenor", "Si♭", "Grande, sonido cálido y grave", "Jazz, rock, soul, big band"],
        ["Barítono", "Mi♭", "Muy grande, sonido profundo", "Big band, secciones de saxos, bajos de banda"],
        ["Bajo", "Si♭", "Gigante: muy raro", "Conjuntos de saxos"]])
    + caja("¿Por qué empezar con el alto?", "Porque es de tamaño manejable, pesa lo justo, necesita menos aire que el tenor o el barítono y tiene muchísimo repertorio. Además, lo que aprendas con el alto te vale para pasar después al tenor o al soprano con solo adaptarte a su tamaño.")
    + """<h3>3. Partes del saxo alto</h3>"""
    + fig("saxo_partes.svg", "Esquema del saxo alto con sus partes", "Las partes principales: boquilla con caña y abrazadera, cuello, cuerpo con llaves, curva en U y campana.")
    + tabla(["Parte", "Qué es y para qué sirve"], [
        ["<b>Boquilla</b>", "Pieza (ebonita, metal o plástico) sobre la que vibra la caña. Es la «embocadura» del instrumento."],
        ["<b>Caña</b>", "Lámina de caña (<i>Arundo donax</i>) que vibra contra la boquilla al soplar. Se gasta y hay que cambiarla."],
        ["<b>Abrazadera</b>", "Anillo metálico con tornillos que sujeta la caña a la boquilla."],
        ["<b>Cuello (tudel)</b>", "Tubo curvo que une la boquilla con el cuerpo. Lleva el corcho donde se encaja la boquilla y una llave de octava."],
        ["<b>Cuerpo</b>", "El tubo principal, con las llaves y las almohadillas (zapatillas) que tapan los orificios."],
        ["<b>Llaves y mecanismo</b>", "Palancas, varillas y resortes que cierran los orificios que tus dedos no alcanzan."],
        ["<b>Llave de octava</b>", "La pulsa el pulgar izquierdo para tocar el registro agudo."],
        ["<b>Arco (curva en U)</b>", "El tramo en forma de U de la parte inferior."],
        ["<b>Campana</b>", "La abertura final, por la que sale el sonido."],
        ["<b>Correa</b>", "Cinta que cuelga del cuello y sostiene el peso del saxo."],
        ["<b>Apoyo del pulgar derecho</b>", "Gancho o anilla donde se apoya el pulgar derecho."]])
    + """<h3>4. Cómo funciona</h3>"""
    + pasos([
        ("Soplas aire por la boquilla.", "el aire pasa por el estrecho espacio entre la caña y la boquilla."),
        ("La caña vibra.", "se abre y cierra cientos de veces por segundo, como una lengüeta. Esa vibración se convierte en una columna de aire que oscila dentro del tubo."),
        ("Los orificios y llaves cambian la longitud del tubo.", "cuantos más orificios cierras con los dedos, más largo es el tubo vibrante y más grave suena la nota."),
        ("La llave de octava cambia de registro.", "al abrir un pequeño orificio cerca del cuello, la columna de aire vibra en dos mitades y suena una octava más aguda."),
    ])
    + """<h3>5. Qué necesitas para empezar</h3>"""
    + tabla(["Material", "Para qué", "¿Imprescindible?"], [
        ["Saxo alto en buen estado", "El instrumento (compra o alquiler, siempre revisado)", "Sí"],
        ["Boquilla de principiante", "Abertura cerrada o media, que facilita el sonido", "Sí"],
        ["Cañas (dureza 1½ a 2½)", "Mejor comprar varias: se gastan", "Sí"],
        ["Abrazadera y correa", "Normalmente vienen con el saxo", "Sí"],
        ["Paño de limpieza (microfibra) y escobillón", "Secar y limpiar después de cada sesión", "Sí"],
        ["Grasa para corcho", "Para montar el cuello y la boquilla sin forzar", "Sí"],
        ["Estuche para cañas", "Guardarlas planas y protegidas", "Muy recomendable"],
        ["Atril, metrónomo y afinador", "Estudiar con la partitura a la altura de los ojos y marcar el pulso", "Muy recomendable"],
        ["Protector de dientes (parche)", "Protege los dientes superiores de la vibración", "Recomendable"],
        ["Un/a profesor/a", "Corrige lo que tú no puedes oír ni ver", "Lo más recomendable"]])
    + """<h3>6. Escucha antes de tocar</h3>
      <p>Para formarte un oído y unas ganas de sonar de cierta manera, escucha a distintos saxofonistas con la partitura (o con un lápiz) en la mano: el sonido, el fraseo, cómo respiran y dónde ponen la intención.</p>"""
    + tabla(["Estilo", "Saxofonistas para empezar a escuchar"], [
        ["Clásica", "Marcel Mule, Sigurd Raschèr, Jean-Yves Fourmeau"],
        ["Jazz (bebop y cool)", "Charlie Parker, Cannonball Adderley, Paul Desmond, Lee Konitz, Phil Woods"],
        ["Jazz moderno y contemporáneo", "Kenny Garrett, Joshua Redman (tenor), Miguel Zenón"],
        ["Pop, soul y funk", "David Sanborn, Candy Dulfer, Maceo Parker"]])
    + quiz("s1a", "¿Qué hace vibrar al saxofón para producir el sonido?", ["Los labios del intérprete", "La caña contra la boquilla", "El metal del cuerpo"], 1, "La caña vibra contra la boquilla cuando soplas; el cuerpo da forma al sonido.")
    + quiz("s1b", "¿En qué tonalidad está afinado el saxo alto?", ["Si♭", "Mi♭", "Do"], 1, "El saxo alto es un instrumento en Mi♭; el tenor y el soprano son en Si♭.")
    + quiz("s1c", "¿Por qué el saxofón se considera de viento-madera si es de metal?", ["Porque el sonido nace de una caña, no de los labios", "Porque suena como una flauta", "Porque lleva llaves"], 0, "La clasificación depende de cómo se produce el sonido: con caña, como el clarinete.")
    + actividad("Tu primera escucha", "Elige un saxofonista de la tabla, escucha cinco minutos de una grabación suya y escribe tres cosas sobre su sonido (¿suave o brillante? ¿cómo respira? ¿qué te gustaría imitar?).", "Escribe aquí…")
    + '<div class="summary-box"><b>Resumen:</b> el saxo alto es un viento-madera en Mi♭ de caña simple; la caña vibra, el tubo cónico da la nota y la llave de octava cambia de registro.</div>'))

# 2 --------------------------------------------------------------------------------------------------
MODULOS.append(("🔧", "Montaje, cuidado y mantenimiento", "Montar y desmontar sin forzar nada, limpiar tras cada sesión y escoger cañas y boquilla.",
    palabras("Monta el saxo <b>con calma y sin forzar nada</b>, sécalo después de cada sesión y no dejes nunca la caña pegada a la boquilla. Un saxo cuidado suena mejor y dura décadas.")
    + """
      <h2>El saxo, listo para tocar</h2>
      <div class="alert-box"><b>Antes de empezar:</b> lávate las manos, no comas ni bebas bebidas dulces justo antes y trabaja sobre una mesa limpia o con el saxo siempre en su soporte o en su estuche abierto. Nunca cojas el saxo por las llaves ni lo apoyes con la campana hacia abajo.</div>
      <h3>1. Montaje paso a paso</h3>"""
    + pasos([
        ("Engrasa el corcho del cuello.", "extiende una capa muy fina de grasa especial para corcho; con demasiada se pone todo resbaladizo. Si el corcho está seco o duro, la boquilla cuesta de montar."),
        ("Cuelga la correa del cuello y engancha el cuerpo.", "pásate la correa por la cabeza y engancha la anilla del cuerpo. Sostén el instrumento por el arco (la curva en U), no por las llaves."),
        ("Monta el cuello en el cuerpo.", "afloja el tornillo del cuerpo, introduce el cuello con un giro suave y alinea la llave de octava del cuello con el mecanismo del cuerpo. Aprieta el tornillo lo justo para que no se mueva."),
        ("Monta la boquilla en el corcho.", "agárrala con una mano por el lado, gira ligeramente al empujar y para cuando esté más o menos a la mitad del corcho. Más adelante la ajustarás para afinar."),
        ("Humedece la caña y colócala.", "mójala en tu boca unos segundos. La cara plana va contra la boquilla, con la punta de la caña casi a ras del extremo (se ve una línea finísima de boquilla)."),
        ("Pon la abrazadera.", "colócala encima de la caña, por detrás de la ventana, y aprieta los tornillos lo justo para que la caña no se mueva. Si la aprietas demasiado, la caña no vibra libremente."),
    ])
    + """<h3>2. Desmontaje y limpieza (¡después de cada sesión!)</h3>"""
    + pasos([
        ("Afloja la abrazadera y quita la caña.", "séquala con un papel o con el dedo, sin tocarle la punta, y guárdala <b>plana</b> en su estuche o funda. Nunca la dejes pegada a la boquilla: se deforma."),
        ("Saca la boquilla y límpiala.", "pasa un paño de microfibra por dentro, sin apretar la parte de la ventana, y sécala por fuera. Una vez a la semana, lávala con agua tibia (no hirviendo) y jabón suave."),
        ("Quita el cuello y pasa el paño o el escobillón.", "limpia por dentro de la boquilla a la campana. La humedad es el enemigo del instrumento."),
        ("Pasa el escobillón por el cuerpo.", "mételo por la campana y sácalo por el otro extremo, con cuidado de no golpear las llaves. Tira siempre en la misma dirección."),
        ("Seca las llaves por fuera y guarda.", "usa un paño seco, sin productos de limpieza. Deja el saxo en su soporte o en el estuche, con la campana arriba."),
    ])
    + """<h3>3. Las cañas</h3>
      <p>La dureza se indica con un número (1, 1½, 2, 2½, 3…): cuanto mayor, más dura. <b>Para empezar, de 1½ a 2½</b> (la 2 es la más habitual). Una caña demasiado dura cuesta de hacer sonar; una demasiado blanda suena «sorda» y chirría.</p>"""
    + lista(["<b>Ten 3 o 4 cañas</b> y alterna su uso: duran más y siempre tendrás una buena.",
             "<b>Guárdalas planas</b> en un estuche, nunca sueltas en el bolsillo.",
             "<b>Cámbiala</b> cuando esté mellada, rizada o tenga la punta hundida, o cuando el sonido sea siempre apagado.",
             "<b>No la muerdas ni la chupes</b>: se arruina enseguida.",
             "Si empiezas con una caña nueva, <b>tócala poco a poco</b> los primeros días (5 minutos más cada día)."], "🌿")
    + """<h3>4. La boquilla</h3>
      <p>Las boquillas de principiante tienen una <b>abertura cerrada o media</b>, que da un sonido más fácil y estable. No es necesario comprar una cara: primero aprende y luego podrás compararlas con tu profesor/a. La abrazadera puede ser de metal o de tela; lo importante es que sujete la caña bien y sin apretar demasiado.</p>
      <h3>5. Mantenimiento general</h3>"""
    + tabla(["Hábito", "Frecuencia", "Por qué"], [
        ["Secar el interior", "Siempre que termines", "La humedad estropea las almohadillas y favorece los hongos"],
        ["Limpiar la boquilla con agua tibia", "Una vez a la semana", "Elimina sarro y bacterias"],
        ["Revisar tornillos y resortes", "Cada mes", "Un tornillo suelto produce zumbidos"],
        ["Engrasar el corcho", "Cuando haga falta", "Evita forzar y que se rompa"],
        ["Llevarlo a revisar al luthier o técnico", "Una vez al año", "Ajusta almohadillas y corchos; un saxo con fugas de aire no suena bien"]])
    + caja("Comprar o alquilar:", "para empezar, lo más sensato es <b>alquilar o comprar uno de estudio</b> revisado por un/a profesor/a. Comprueba que las llaves cierran bien (que ningún orificio pierda aire), que no tiene golpes importantes en el tubo y que la boquilla es adecuada. Un saxo barato en mal estado desanima mucho.")
    + errores([
        ["La boquilla cuesta de montar", "El corcho está seco", "Engrasa una capa fina y gira suavemente; nunca fuerces con la boquilla torcida"],
        ["Las llaves se tuercen", "Se apoya el saxo en ellas o se agarra por ellas", "Sostén el saxo por el arco y el cuerpo; guárdalo siempre en su soporte o estuche"],
        ["La caña se astilla", "Se ha mordido o se ha guardado húmeda y sin protección", "Guárdala plana en su estuche y no la muerdas"],
        ["Se oyen ruidos de aire al tocar", "Una almohadilla no cierra bien", "Llévalo a un técnico: no intentes arreglarlo tú"]])
    + quiz("s2a", "¿Cómo se guarda una caña después de tocar?", ["Pegada a la boquilla", "Plana, en su estuche", "En el bolsillo"], 1, "Una caña guardada plana y protegida no se deforma.")
    + quiz("s2b", "¿Con qué dureza de caña es recomendable empezar?", ["De 1½ a 2½", "De 4 a 5", "No importa"], 0, "Una caña demasiado dura cuesta de soplar; una demasiado blanda suena apagada.")
    + quiz("s2c", "¿Con qué se limpia el interior del cuerpo del saxo?", ["Con un escobillón o paño que pasa por la campana", "Con agua y jabón", "Con alcohol"], 0, "El agua o los productos químicos dañan las almohadillas.")
    + '<div class="activity checklist"><h3>✔️ Lista de comprobación del montaje</h3>'
      '<label><input type="checkbox"> El corcho está engrasado con una capa fina</label>'
      '<label><input type="checkbox"> El cuello está bien alineado con la llave de octava</label>'
      '<label><input type="checkbox"> La caña está mojada y a ras de la boquilla</label>'
      '<label><input type="checkbox"> La abrazadera está apretada lo justo</label>'
      '<label><input type="checkbox"> Al terminar: caña seca y plana, boquilla y cuerpo secos</label></div>'
    + '<div class="summary-box"><b>Resumen:</b> monta con calma, seca siempre el interior, guarda la caña plana y alterna varias cañas. Revisa el saxo cada año.</div>'))

# 3 --------------------------------------------------------------------------------------------------
MODULOS.append(("🧍", "Postura, sujeción y respiración", "Cómo colocarte, cómo sujetar el saxo sin tensión y cómo respirar para tocar.",
    palabras("El saxo debe <b>llegar a ti</b>, no tú a él: correa a la altura justa, espalda recta y hombros sueltos, manos curvadas y un <b>aire grande y relajado</b>. Sin tensión se toca más y mejor.")
    + """
      <h2>El cuerpo, el saxo y el aire</h2>
      <h3>1. La postura</h3>"""
    + lista(["<b>De pie:</b> pies separados a la anchura de los hombros, peso repartido, rodillas sueltas.",
             "<b>Sentado:</b> en el borde de una silla sin reposabrazos, pies apoyados en el suelo, espalda erguida sin apoyarla en el respaldo.",
             "<b>Cabeza:</b> recta y relajada; la boquilla llega a ti, sin bajar ni subir la barbilla.",
             "<b>Hombros:</b> bajos y sueltos; el peso del saxo lo lleva la correa, no los brazos.",
             "<b>Respiración:</b> el abdomen y los costados se mueven al respirar, el pecho no se levanta."], "🧍")
    + """<h3>2. La correa y la altura del saxo</h3>"""
    + pasos([
        ("Cuelga el saxo en la correa y deja que cuelgue en diagonal a tu derecha.", "debe quedar un poco inclinado hacia delante y apoyado en el lado derecho de tu cuerpo."),
        ("Ajusta la altura de la correa.", "la boquilla debe llegar a tu boca <b>con la cabeza recta</b>, sin que tengas que agacharte ni estirarte."),
        ("Comprueba la distancia con los brazos.", "los codos quedan sueltos y ligeramente separados del cuerpo."),
    ])
    + """<h3>3. Las manos</h3>"""
    + tabla(["Mano", "Pulgar", "Dedos", "Meñique"], [
        ["<b>Izquierda</b> (arriba)", "Apoyado en la placa y sobre la llave de octava", "1, 2 y 3 sobre las tres llaves superiores", "Sobre las llaves de la mesa (G♯, C♯, B, B♭)"],
        ["<b>Derecha</b> (abajo)", "Bajo el gancho de apoyo, sosteniendo el peso", "1, 2 y 3 sobre las tres llaves inferiores", "Sobre las llaves de Mi♭ y Do"]])
    + caja("Dedos curvados:", "imagina que sostienes una pelota pequeña. Los dedos van <b>curvos</b>, con las yemas sobre las llaves, a 1 cm de ellas; no las aprietes ni las golpees: solo basta con cerrarlas con firmeza. Las muñecas rectas, sin doblarlas hacia dentro ni hacia fuera.")
    + """<h3>4. La respiración</h3>
      <p>Para tocar necesitas <b>mucho más aire</b> que para hablar, y hay que tomarlo rápido y sin ruido. Se respira por la boca, abriendo las comisuras sin romper la embocadura, y llevando el aire <b>hacia el abdomen, los costados y la espalda baja</b>.</p>"""
    + practica("Ejercicios de respiración (5 minutos, sin saxo)", [
        "<b>Mano en el abdomen:</b> inspira por la boca llevando el aire hacia la mano; los hombros no suben.",
        "<b>4-2-8:</b> inspira contando 4, aguanta 2 y suelta el aire contando 8, como si empañaras un cristal (aire cálido).",
        "<b>El papel en la pared:</b> pega una hoja a la pared con el aire de la boca y mantenla pegada el mayor tiempo posible.",
        "<b>«Sssss» largo:</b> suelta aire con un «sss» constante durante 10, 15 y 20 segundos.",
        "<b>Respirar con la boquilla:</b> haz estos ejercicios con la boquilla en la boca, sin caña y sin sonar."])
    + partitura("respirar")
    + """<h3>5. Calentamiento del cuerpo (2 minutos)</h3>"""
    + lista(["Gira lentamente los hombros hacia atrás y hacia delante.",
             "Inclina la cabeza a los lados sin forzar y vuelve al centro.",
             "Estira los brazos por encima de la cabeza y suéltalos.",
             "Abre y cierra las manos y mueve los dedos uno a uno."], "🤸")
    + """<h3>6. Hábitos saludables</h3>"""
    + lista(["<b>Descansa</b> cada 15-20 minutos de estudio: el labio se cansa.",
             "<b>Bebe agua</b> (no bebidas azucaradas) y no comas justo antes.",
             "Si te <b>mareas</b> (a veces pasa por respirar demasiado), para y respira con normalidad.",
             "No toques si tienes <b>dolor</b> en los labios, el cuello o las muñecas: avísalo a tu profesor/a."], "🏥")
    + errores([
        ["Me duele el cuello", "El saxo cuelga demasiado bajo y bajo la cabeza", "Sube la correa para que la boquilla llegue a la boca con la cabeza recta"],
        ["Los hombros suben al inspirar", "Respiro con el pecho", "Pon una mano en el abdomen y lleva el aire allí"],
        ["Me quedo sin aire enseguida", "Inspiro poco y soplo demasiado deprisa", "Practica el 4-2-8 y aprovecha el aire poco a poco"],
        ["Me duelen las muñecas", "Las doblo o aprieto las llaves", "Muñecas rectas y dedos curvados, sin apretar"]])
    + quiz("s3a", "¿Qué mano va en la parte superior del saxo?", ["La izquierda", "La derecha", "Da igual"], 0, "La mano izquierda controla las llaves de arriba y la derecha las de abajo.")
    + quiz("s3b", "¿Dónde debe estar la boquilla respecto a tu boca al ajustar la correa?", ["Debe llegar sin bajar ni subir la cabeza", "Debes agacharte para alcanzarla", "No importa"], 0, "La postura debe ser natural, sin tensión.")
    + quiz("s3c", "¿Hacia dónde se lleva el aire al respirar para tocar?", ["Hacia el abdomen y los costados", "Hacia los hombros", "Solo hacia el pecho"], 0, "La respiración abdominal permite más aire con menos esfuerzo.")
    + '<div class="summary-box"><b>Resumen:</b> postura erguida, correa a la altura justa, manos curvadas sin apretar y respiración abdominal. Descansa a menudo.</div>'))

# 4 --------------------------------------------------------------------------------------------------
MODULOS.append(("👄", "La embocadura y el primer sonido", "Cómo colocar los labios y los dientes y conseguir tu primer sonido estable.",
    palabras("La embocadura es un <b>cojín</b>: los dientes de arriba descansan sobre la boquilla, el labio de abajo la envuelve como un colchón, las comisuras se cierran como para decir «u» y el aire hace todo el trabajo. <b>No se muerde</b>.")
    + """
      <h2>Tu primer sonido</h2>
      <h3>1. Cómo se coloca la embocadura</h3>"""
    + pasos([
        ("Dientes superiores sobre la boquilla.", "apoya los dientes de arriba directamente sobre la boquilla, a unos 1-1,5 cm de la punta (donde la caña se separa de la boquilla). Usar un protector (parche) evita que resbalen."),
        ("Labio inferior sobre los dientes inferiores.", "dobla el labio inferior ligeramente hacia dentro, como un cojín, y apoya la caña sobre él. Los dientes inferiores no tocan la caña."),
        ("Cierra las comisuras.", "como si dijeras «u» o fueras a silbar: la boca forma un círculo alrededor de la boquilla, sin dejar escapar el aire por los lados."),
        ("Mentón plano.", "no lo frunzas ni lo eleves; debe quedar liso, como cuando sonríes ligeramente."),
        ("Lengua baja y relajada.", "la lengua descansa atrás y abajo, como al decir «oh», sin tocar la caña."),
    ])
    + caja("Lo que NO se hace:", "morder la boquilla, apretar los labios como una pinza, subir la barbilla o hinchar las mejillas. Si te duele el labio inferior o los dientes, estás apretando demasiado.", "box")
    + """<h3>2. Primeros pasos, de menos a más</h3>"""
    + pasos([
        ("Sin saxo: forma la embocadura.", "con un lápiz o dedo y sin boquilla, forma el círculo y suelta aire cálido (como empañar un cristal) durante 8 segundos."),
        ("Con la boquilla sola (con caña, sin cuello).", "colócala en la boca, ciérrala con las comisuras y sopla. Debe salir un sonido estable y agudo. Si chirría, relaja el labio; si no suena, sopla un poco más fuerte."),
        ("Con el cuello y la boquilla.", "monta la boquilla en el cuello y repite. El sonido será más grave que solo con la boquilla. Mantén 4, 8 y 12 tiempos."),
        ("Con todo el saxo, sin pulsar llaves.", "sin colocar ningún dedo, sopla: sonará la nota Do♯ escrita (todos los orificios abiertos). Es una nota fácil de producir y muy útil para comprobar que la embocadura está bien."),
        ("Con el saxo y la nota Sol.", "coloca los tres dedos de la mano izquierda (1, 2 y 3) sobre las llaves y sopla: tu primera nota larga."),
    ])
    + partitura("primer_sonido")
    + """<h3>3. Cuando algo no sale</h3>"""
    + tabla(["Problema", "Causa probable", "Qué hacer"], [
        ["No suena nada", "Poca presión del aire, caña mal colocada o muy poca boquilla", "Comprueba la caña (mojada y a ras), mete algo más de boquilla y sopla más aire"],
        ["Chirrido agudo", "Demasiada presión de los labios, mucha boquilla o caña muy blanda", "Relaja la embocadura y saca un poco la boquilla"],
        ["Sonido débil y «sordo»", "Poca boquilla, labios flojos o caña gastada", "Aumenta la presión del aire, mete un poco de boquilla y revisa la caña"],
        ["Sonido «sucio» y con ruido de aire", "El aire se escapa por las comisuras", "Cierra más las comisuras, como para silbar"],
        ["Sonido muy agudo", "Mordida fuerte", "Relaja y abre la boca (di «oh»)"],
        ["Sonido muy grave y flojo", "Embocadura muy suelta", "Cierra algo más las comisuras y aumenta la velocidad del aire"],
        ["Dolor en el labio inferior", "Apretar los dientes inferiores", "Dobla más el labio sobre los dientes y descansa"]])
    + """<h3>4. Tu primer minuto de sonido</h3>"""
    + practica("Cinco minutos para el primer sonido", [
        "<b>1 min</b> · Sopla con la boquilla sola, notas largas de 8 tiempos.",
        "<b>1 min</b> · Con el cuello y la boquilla, 8 tiempos.",
        "<b>2 min</b> · Con todo el saxo, Sol largo de 4 tiempos, con descansos.",
        "<b>1 min</b> · Escucha tu sonido: ¿es igual al principio y al final de la nota? Si no, respira y repite.",
    ])
    + caja("Protege tus dientes y labios:", "con un protector de dientes (parche adhesivo) evitas que la boquilla resbale y proteges el esmalte. Descansa 1 minuto cada 5 minutos de práctica los primeros días.")
    + errores([
        ["Muerdo la boquilla para que suene", "Creo que apretar da más sonido", "Más aire y menos presión; el sonido sale del aire"],
        ["El sonido se corta a mitad de nota", "Aire insuficiente o presión variable", "Respira más y mantén la misma presión desde el principio"],
        ["Siento saliva en la boquilla", "Es normal", "Traga antes de empezar y sécala después de tocar"]])
    + quiz("s4a", "¿Dónde apoyan los dientes superiores?", ["Sobre la boquilla", "Sobre la caña", "Sobre el cuello"], 0, "Los dientes superiores descansan directamente sobre la boquilla.")
    + quiz("s4b", "¿Cómo debe colocarse el labio inferior?", ["Sobre los dientes inferiores, como un cojín", "Separado de la caña", "Mordiendo la caña"], 0, "El labio forma un cojín entre los dientes y la caña.")
    + quiz("s4c", "El sonido es un chirrido agudo. ¿Qué haces?", ["Relajar la embocadura y sacar un poco la boquilla", "Apretar más", "Soplar más flojo"], 0, "El chirrido suele indicar exceso de presión o demasiada boquilla.")
    + '<div class="summary-box"><b>Resumen:</b> dientes arriba sobre la boquilla, labio abajo como cojín, comisuras cerradas, lengua baja y aire cálido. Sin morder.</div>'))

# 5 --------------------------------------------------------------------------------------------------
MODULOS.append(("🎵", "Primeras notas: Si, La y Sol", "Tres notas con la mano izquierda, primera lectura de partituras y primeras melodías.",
    palabras("Con <b>solo la mano izquierda</b> ya tocas tres notas: <b>Si</b> (un dedo), <b>La</b> (dos) y <b>Sol</b> (tres). Cada nota que baja en el pentagrama pide un dedo más.")
    + """
      <h2>Si, La y Sol</h2>
      <h3>1. Cómo se leen: el pentagrama y la clave de Sol</h3>
      <p>El saxofonista lee en <b>clave de Sol</b>. Las notas que ves escritas no son exactamente las que suenan (el saxo alto suena una sexta mayor más grave; lo verás en el módulo 9), así que de momento solo nos importa <b>qué nota escrita corresponde a qué dedos</b>.</p>
      <p>Cada línea y cada espacio del pentagrama es una nota. De abajo arriba, las líneas son <b>Mi–Sol–Si–Re–Fa</b> y los espacios, <b>Fa–La–Do–Mi</b>. Las notas de este módulo están en la parte media del pentagrama:</p>"""
    + lista(["<b>Si:</b> en la tercera línea (la del medio).", "<b>La:</b> en el segundo espacio.", "<b>Sol:</b> en la segunda línea (donde se enrosca la clave)."], "🎼")
    + """<h3>2. Los dedos de la mano izquierda</h3>"""
    + fig("dig_basicas.svg", "Digitaciones de Si, La y Sol", "Si: dedo 1 de la mano izquierda. La: dedos 1 y 2. Sol: dedos 1, 2 y 3. La mano derecha no pulsa nada y el pulgar izquierdo no toca la llave de octava.")
    + tabla(["Nota escrita", "Dedos", "Cómo recordarlo"], [
        ["Si (Si4)", "1 (índice izquierdo)", "El primer dedo: la nota más aguda de las tres"],
        ["La (La4)", "1 y 2", "Añade el siguiente dedo y baja un escalón"],
        ["Sol (Sol4)", "1, 2 y 3", "Todos los dedos de la mano izquierda: la más grave de las tres"]])
    + como("Mueve los dedos sin hacer ruido. Para pasar de Si a La, el dedo 2 baja con la yema <b>sin golpear</b> la llave, y el dedo 1 sigue abajo. Para pasar de La a Sol, solo baja el 3. Cuando subas, levanta los dedos hacia arriba, sin separarlos mucho de las llaves.")
    + """<h3>3. Las duraciones</h3>"""
    + tabla(["Figura", "Dura", "Cómo contarla"], [
        ["Redonda", "4 tiempos", "1-2-3-4"],
        ["Blanca", "2 tiempos", "1-2"],
        ["Negra", "1 tiempo", "1"],
        ["Silencio de negra", "1 tiempo sin sonido", "El pulso sigue contando"]])
    + """<p>La partitura empieza con un <b>compás de 4/4</b>: cuatro tiempos por compás. Marca el pulso con el pie y cuenta en voz alta «1-2-3-4».</p>"""
    + partitura("p5_largas") + partitura("p5_blancas") + partitura("p5_negras")
    + """<h3>4. Tu primera melodía</h3>
      <p>Con Si, La y Sol ya puedes tocar una melodía tradicional. Escúchala con el acompañamiento y luego tócala tú.</p>"""
    + partitura("p5_pan") + partitura("p5_eco")
    + practica("Plan de estudio de 10 minutos", [
        "<b>2 min</b> · Sol largo (4 tiempos), La largo y Si largo, respirando entre notas.",
        "<b>3 min</b> · Las redondas, las blancas y las negras de este módulo, con metrónomo a 60.",
        "<b>3 min</b> · La melodía «Pan caliente», despacio y sin parar.",
        "<b>2 min</b> · Invéntate una melodía de cuatro compases con las tres notas y apúntala."])
    + errores([
        ["El sonido se corta al cambiar de nota", "Los dedos van a destiempo", "Mueve los dedos juntos y sin golpearlos; haz el cambio a un tempo lento"],
        ["Sale una nota más aguda de la esperada", "Una llave no está cerrada del todo", "Cubre las llaves con la yema, no con la punta, y comprueba que no se escapa aire"],
        ["Pierdo el pulso", "Estoy más atento a los dedos que al ritmo", "Marca el pulso con el pie y cuenta en voz alta"]])
    + quiz("s5a", "¿Qué dedos se usan para el Sol?", ["1, 2 y 3 de la izquierda", "Solo el 1", "1 y 2"], 0, "Sol: los tres dedos de la mano izquierda.")
    + quiz("s5b", "¿Qué nota se toca con el dedo 1 solo (izquierdo)?", ["Si", "La", "Sol"], 0, "Si se toca con el índice izquierdo.")
    + quiz("s5c", "¿Cuánto dura una blanca en 4/4?", ["1 tiempo", "2 tiempos", "4 tiempos"], 1, "La blanca dura dos tiempos.")
    + '<div class="summary-box"><b>Resumen:</b> Si (1), La (1-2) y Sol (1-2-3) con la mano izquierda; redonda, blanca y negra; cambio de nota sin golpear.</div>'))

# 6 --------------------------------------------------------------------------------------------------
MODULOS.append(("🎶", "Más notas: grave y medio", "Mano derecha, Do agudo del registro grave y las primeras alteraciones.",
    palabras("Con la <b>mano derecha</b> bajas hacia el Re, y con la izquierda subes hacia el Do y el Do♯. Cada nota nueva es <b>un dedo más o un dedo menos</b> que la anterior. Lo importante: cierres sin escapes de aire.")
    + """
      <h2>Ampliar el registro</h2>
      <div class="alert-box"><b>Aviso:</b> las digitaciones de este curso son las del saxo alto estándar (sistema Boehm moderno). Algunos modelos tienen llaves extra o digitaciones alternativas; si tu profesor/a prefiere otras, sigue sus indicaciones.</div>
      <h3>1. Mano derecha: Fa, Mi y Re</h3>"""
    + fig("dig_derecha.svg", "Digitaciones de Fa, Mi y Re", "Fa: izquierda 1-2-3 y derecha 1. Mi: izquierda 1-2-3 y derecha 1-2. Re: seis dedos, los tres de cada mano.")
    + tabla(["Nota escrita", "Mano izquierda", "Mano derecha"], [
        ["Sol (Sol4)", "1-2-3", "—"],
        ["Fa (Fa4)", "1-2-3", "1"],
        ["Mi (Mi4)", "1-2-3", "1-2"],
        ["Re (Re4)", "1-2-3", "1-2-3"]])
    + """<h3>2. Do y Do♯ del registro grave</h3>"""
    + fig("dig_do.svg", "Digitaciones de Do5 y Do♯5", "Do (Do5): solo el dedo 2 de la izquierda. Do♯ (Do♯5): todos los dedos levantados.")
    + como("El Do agudo se toca con el dedo 2 izquierdo solo: levanta el 1 y el 3 y deja el 2. Para el Do♯, levanta todos los dedos: es la nota «abierta». No es una nota fácil de afinar: apóyala con aire.")
    + """<h3>3. Las alteraciones: Fa♯, Si♭, Sol♯ y Mi♭</h3>"""
    + fig("dig_alteradas.svg", "Digitaciones de Fa♯, Si♭, Sol♯ y Mi♭", "Fa♯: izquierda 1-2-3 y derecha 2. Si♭: dedo 1 izquierdo y dedo 1 derecho. Sol♯: izquierda 1-2-3 y llave G♯ con el meñique izquierdo. Mi♭: seis dedos y llave E♭ con el meñique derecho.")
    + tabla(["Nota", "Dedos", "Nota"], [
        ["Fa♯", "Izq 1-2-3 + der 2", "El Fa♯ «bifurcado» (la derecha deja el 1 y baja el 2)"],
        ["Si♭", "Izq 1 + der 1", "Una alternativa muy usada es la llave «bis» (pregunta a tu profesor/a)"],
        ["Sol♯", "Izq 1-2-3 + meñique izquierdo (G♯)", "El meñique pulsa la llave más alta de la mesa"],
        ["Mi♭", "Seis dedos + meñique derecho (E♭)", "Meñique derecho en la llave Mi♭"]])
    + """<h3>4. Las notas graves: Do, Do♯, Si y Si♭</h3>
      <p>En la parte baja del saxo hay notas que se tocan con los <b>meñiques</b>. Son más difíciles porque los meñiques son los dedos con menos fuerza y precisión. No las trabajes hasta dominar el Re.</p>"""
    + fig("dig_graves.svg", "Digitaciones de Do4, Do♯4, Si3 y Si♭3", "Do: seis dedos y llave C del meñique derecho. Do♯, Si y Si♭: seis dedos y la llave correspondiente de la mesa de la mano izquierda (C♯, B, B♭).")
    + """<h3>5. Practica con melodías</h3>"""
    + partitura("p6_clair") + partitura("p6_mary") + partitura("p6_fa") + partitura("p6_sib") + partitura("p6_grave")
    + """<h3>6. Entrenadores</h3>
      <h4>Lectura de notas escritas</h4>
      <p>Aparece una nota escrita en el pentagrama (desde el Si grave hasta el Do agudo). Pulsa su nombre.</p>
      <div class="activity"><div id="lect-pent" style="max-width:260px"></div><p class="feedback" id="lect-fb">Pulsa «Empezar».</p>
        <div class="lect-btns" id="lect-btns">__LECT_BTNS__</div><p><button class="btn" onclick="lectNueva()">Empezar / otra nota</button></p></div>
      <h4>Digitaciones</h4>
      <p>Aparece una digitación. Elige a qué nota escrita corresponde. Puedes escoger el nivel.</p>
      <div class="activity"><label>Nivel: <select id="dig-nivel" onchange="digNueva()"><option value="basico">Básico (Re4–Do5)</option><option value="grave">Registro grave completo</option><option value="agudo">Registro agudo</option><option value="todo">Todo</option></select></label>
        <div id="dig-svg" style="margin:10px 0;max-width:140px"></div><p class="feedback" id="dig-fb">Pulsa «Empezar».</p>
        <div class="lect-btns" id="dig-opts"></div><div id="dig-pent" style="max-width:200px"></div>
        <p><button class="btn" onclick="digNueva()">Empezar / otra digitación</button></p></div>"""
    + practica("Cómo practicar las notas nuevas", [
        "<b>Una nota nueva cada día.</b> Tócala larga (4 tiempos) varias veces y comprueba que suena limpia.",
        "<b>Enlaza con la anterior:</b> toca Sol–Fa–Sol–Fa muy despacio, atento al paso de un dedo.",
        "<b>Sube y baja por grados:</b> Sol–Fa–Mi–Re–Mi–Fa–Sol, con metrónomo a 60.",
        "<b>Las alteraciones, aparte:</b> la armadura te dice cuáles son (Fa♯ en Sol mayor, Si♭ en Fa mayor).",
    ])
    + errores([
        ["Una nota no suena o suena «sucia»", "Un dedo no cubre del todo la llave", "Cubre con la yema y repasa dónde cae el dedo; comprueba que no hay holgura"],
        ["El Fa♯ me sale como Fa", "Bajo el dedo derecho equivocado", "El Fa♯ lleva el dedo 2 derecho; el 1 derecho es el Fa natural"],
        ["No salen las notas graves", "Poco aire o los meñiques no cierran", "Más aire, y practica solo el cambio de meñique"],
        ["Me confundo con el Si♭", "Lo confundo con el Si", "En Fa mayor, el Si es siempre Si♭ (índice izquierdo + índice derecho)"]])
    + quiz("s6a", "¿Qué dedos se usan para el Fa (Fa4)?", ["Izquierda 1-2-3 y derecha 1", "Izquierda 1-2 y derecha 1-2", "Los seis dedos"], 0, "Fa: tres dedos izquierdos y el primero de la derecha.")
    + quiz("s6b", "¿Cuántos dedos hay abajo en la nota Re (Re4)?", ["Seis (los tres de cada mano)", "Tres", "Solo uno"], 0, "Re se toca con todos los dedos.")
    + quiz("s6c", "Estás en Fa mayor. ¿Cómo se toca el Si?", ["Como Si♭: dedo 1 izquierdo y 1 derecho", "Como Si natural: solo el dedo 1", "Con el meñique"], 0, "La armadura de Fa mayor lleva Si♭.")
    + '<div class="summary-box"><b>Resumen:</b> Fa (+1 der), Mi (+1-2), Re (+1-2-3); Do con el dedo 2 y Do♯ abierto; Fa♯, Si♭, Sol♯ y Mi♭ con sus dedos; graves con los meñiques.</div>'))

# 7 --------------------------------------------------------------------------------------------------
MODULOS.append(("🗣️", "La articulación: la lengua", "Cómo empezar y terminar cada nota con la lengua: picado, ligado y acentos.",
    palabras("La lengua es el «interruptor» del sonido: toca <b>la punta de la caña</b> y la detiene un instante; al soltarla, el aire vuelve a hacerla vibrar. El aire <b>nunca se para</b>: solo la lengua interrumpe la vibración.")
    + """
      <h2>Empezar y cortar las notas</h2>
      <h3>1. Qué es la articulación</h3>
      <p>La <b>articulación</b> es la forma de empezar, unir y terminar las notas. Se usa para dar claridad, carácter y expresión a la música: unas notas se «dicen» una a una (picado), otras se enlazan sin separación (ligado) y otras se acentúan.</p>
      <h3>2. Cómo se hace con la lengua</h3>"""
    + pasos([
        ("Sin saxo: di «tu» en voz alta.", "observa que la punta de la lengua toca por detrás de los dientes superiores."),
        ("Ahora di «tu» sin voz, solo con aire.", "es el mismo movimiento, pero soplando: «tu-tu-tu-tu»."),
        ("Con la boquilla (con caña): repite «tu».", "la punta de la lengua toca la <b>punta de la caña</b>, muy ligeramente, y se retira. Las primeras notas pueden sonar con «hipo»: es normal."),
        ("Con el saxo: Sol larga y luego «tu-tu-tu-tu».", "el aire fluye continuamente; la lengua solo hace de interruptor."),
    ])
    + como("El movimiento es de la <b>punta de la lengua</b>, pequeño y rápido. No muevas la mandíbula ni cierres la garganta. Si el sonido «explota» al empezar, tocas la caña con demasiada fuerza; si no sale, apenas la rozas.")
    + """<h3>3. Los tipos de articulación</h3>"""
    + tabla(["Signo", "Nombre", "Cómo se toca"], [
        ["Un arco sobre varias notas distintas", "Ligado (<i>legato</i>)", "Solo la primera nota con la lengua; las demás, solo con los dedos y sin interrumpir el aire"],
        ["Un punto sobre o bajo la nota", "Picado (<i>staccato</i>)", "Cada nota con la lengua y más corta que su valor; el aire sigue"],
        ["Una raya sobre la nota", "Tenuto", "Cada nota con la lengua, pero mantenida todo su valor"],
        ["El signo &gt;", "Acento", "Más fuerte y marcada al empezar, sin morder"]])
    + partitura("p7_picado") + partitura("p7_ligado") + partitura("p7_mixto") + partitura("p7_acentos") + partitura("p7_corcheas")
    + practica("Ejercicio de lengua (5 minutos)", [
        "<b>Una nota larga con lengua al principio y al final:</b> «tu…» (4 tiempos) «…tu».",
        "<b>Una nota, notas cortas:</b> Sol picado en negras con metrónomo a 60: «tu-tu-tu-tu».",
        "<b>Dos notas:</b> Sol–La con articulación en cada una; luego ligadas (una sola lengua).",
        "<b>Corcheas:</b> dos «tu» por pulso, a 60, y sube de 4 en 4 bpm si sale limpio.",
        "<b>Escucha:</b> las notas deben sonar iguales, sin acentos extraños ni silencios irregulares.",
    ])
    + errores([
        ["Cada nota «explota»", "La lengua toca la caña con demasiada fuerza", "Roza solo con la punta; piensa «du» más que «tu»"],
        ["El sonido se corta del todo entre notas", "Se para el aire a la vez que la lengua", "Mantén el aire constante: la lengua solo interrumpe la vibración"],
        ["Las notas ligadas suenan picadas", "Se articula con la lengua o los dedos van a destiempo", "Lengua solo en la primera nota; dedos coordinados"],
        ["Muevo la mandíbula al articular", "Intento ayudarme con la boca entera", "Mantén la boca quieta: solo se mueve la punta de la lengua"]])
    + quiz("s7a", "¿Con qué parte de la lengua se articula?", ["Con la punta", "Con la base", "No se usa la lengua"], 0, "La punta de la lengua toca la punta de la caña.")
    + quiz("s7b", "En una ligadura de varias notas, ¿cuántas se articulan con la lengua?", ["Solo la primera", "Todas", "Ninguna"], 0, "Las demás se enlazan solo con los dedos.")
    + quiz("s7c", "¿Qué indica un punto sobre una nota?", ["Que se toca más corta (picado)", "Que se toca más fuerte", "Que se liga con la siguiente"], 0, "El punto indica staccato: se toca más corta.")
    + '<div class="summary-box"><b>Resumen:</b> la punta de la lengua toca la punta de la caña; el aire no se detiene. Ligado (solo dedos), picado (cortas), tenuto (mantenidas) y acento (marcadas).</div>'))
