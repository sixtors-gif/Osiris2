"""Partituras del curso de saxofón alto (notación ABC, dibujadas con abcjs).

Todas se escriben en el tono ESCRITO del saxo alto (clave de Sol); el audio las transpone a Mi♭
(transpose=-9) y suena con el timbre de saxo alto (programa MIDI 65). Los acordes de las piezas con
acompañamiento están en el tono escrito, como en las partituras de saxo; también se transportan al sonar.
Las melodías tradicionales (Hot Cross Buns, Frère Jacques, Au clair de la lune, Mary Had a Little Lamb,
Twinkle Twinkle, «Oda a la Alegría» de Beethoven) son de dominio público; el resto son originales del curso.
"""
import re

PIEZAS = {}


def pieza(clave, titulo, cuerpo, nota="", key="C", meter="4/4", L="1/4", Q="1/4=80", sub="", acomp=False, ajuste=True):
    n = len(PIEZAS) + 1
    cab = (f"X:{n}\nT:{titulo}\n" + (f"C:{sub}\n" if sub else "") + f"M:{meter}\nL:{L}\nQ:{Q}\n"
           + ("" if ajuste else "% sin-ajuste\n") + "%%MIDI program 65\n%%MIDI chordprog 0\n")
    abc = cab + f"K:{key} clef=treble transpose=-9\n" + cuerpo.strip() + "\n"
    PIEZAS[clave] = {"titulo": titulo, "abc": abc, "nota": nota, "acomp": acomp, "cab": cab, "key": key}
    return abc


def silenciar_melodia(abc):
    """Devuelve el mismo ABC con la melodía convertida en silencios, para escuchar solo el acompañamiento."""
    sal = []
    for linea in abc.split("\n"):
        if re.match(r"^[A-Za-z]:", linea) or linea.startswith("%") or not linea.strip():
            if linea.startswith("K:"):
                sal.append(linea)
            elif not linea.startswith("w:"):
                sal.append(linea)
            continue
        partes = re.split(r'("[^"]*")', linea)
        for i, p in enumerate(partes):
            if i % 2:  # texto de acordes o anotaciones
                continue
            p = re.sub(r"!\w+[()]?!", "", p)                 # decoraciones
            p = re.sub(r"\{[^}]*\}", "", p)                  # notas de adorno
            p = re.sub(r"\[[^\]]*\](\d*(?:/\d*)?)", lambda m: "z" + m.group(1), p)   # acordes de notas
            p = re.sub(r"[_^=]*[A-Ga-g][,']*(\d*(?:/\d*)?)", lambda m: "z" + m.group(1), p)
            p = re.sub(r"(?<=z)\d*(?:/\d*)?-", lambda m: m.group(0)[:-1], p)   # ligaduras de unión
            p = re.sub(r"\((?!\d)", "", p)
            p = p.replace(")", "").replace(".", "")
            partes[i] = p
        sal.append("".join(partes))
    return "\n".join(sal)


# ---------------------------------------------------------------------------------------------
# Módulo 3 y 4 · Respiración y primer sonido
# ---------------------------------------------------------------------------------------------
pieza("respirar", "Respirar y soplar con el sonido", """
"^inspira (4 tiempos)"z4 | "^sopla (8 tiempos)"G4- | G4 | "^inspira"z4 | G4- | G4 |]
""", "Cuenta 4 tiempos para tomar aire y 8 para soplar. Cuando lo domines, sopla 12 y luego 16.", Q="1/4=60")

pieza("primer_sonido", "Cuatro notas largas", """
G4 | G4 | G4 | G4 |]
""", "Cada redonda dura cuatro tiempos. Busca un sonido igual del principio al final de cada nota, sin cambiar la presión de la boca.", Q="1/4=60")

# ---------------------------------------------------------------------------------------------
# Módulo 5 · Si, La y Sol
# ---------------------------------------------------------------------------------------------
pieza("p5_largas", "Si – La – Sol con redondas", """
B4 | A4 | G4 | A4 | B4 | B4 | A4 | G4 |]
""", "Mantén cada nota los cuatro tiempos y cambia de dedos sin que el sonido se interrumpa.", Q="1/4=60")

pieza("p5_blancas", "Si – La – Sol con blancas", """
B2 A2 | G2 A2 | B2 A2 | G4 |]
""", "Cada blanca dura dos tiempos. Cuenta «1-2» en cada nota.", Q="1/4=66")

pieza("p5_negras", "Si – La – Sol con negras", """
B B A A | G G A A | B B B B | A A G2 |]
""", "Una nota por cada pulso. Mantén el aire continuo aunque cambies de dedos.", Q="1/4=72")

pieza("p5_pan", "Pan caliente (Hot Cross Buns)", """
"G"B A G2 | "G"B A G2 | "G"G G G G | "D7"A A A A | "G"B A G2 |]
""", "Melodía tradicional (dominio público), en versión sencilla. Escucha la grabación con acompañamiento y toca con ella.", acomp=True, Q="1/4=84")

pieza("p5_eco", "Pregunta y respuesta con Si, La y Sol", """
B A G2 | G A B2 | A G A B | G4 |]
""", "Los dos primeros compases «preguntan» y los dos siguientes «responden». Inventa después tu propia pregunta y respuesta con las tres notas.", Q="1/4=72")

# ---------------------------------------------------------------------------------------------
# Módulo 6 · Más notas
# ---------------------------------------------------------------------------------------------
pieza("p6_clair", "Au clair de la lune", """
"G"G G G A | "G"B2 A2 | "D7"G B A A | "G"G4 |]
""", "Canción tradicional francesa (dominio público). Solo usa Sol, La y Si.", key="G", acomp=True, Q="1/4=80")

pieza("p6_mary", "Mary tenía un corderito (Mary Had a Little Lamb)", """
"F"A G F G | A A A2 | "C7"G G G2 | "F"A c c2 | A G F G | "F"A A A A | "C7"G G A G | "F"F4 |]
""", "Canción tradicional (dominio público). El Do agudo (c) se toca con el dedo 2 izquierdo y sin la llave de octava.", key="F", acomp=True, Q="1/4=84")

pieza("p6_fa", "Descendiendo con el Fa♯", """
G F E D | E F G2 | F G A B | A G F2 | G4 |]
""", "En Sol mayor todos los Fa son Fa♯: se tocan con el 123 de la izquierda y el 2 de la derecha.", key="G", Q="1/4=72")

pieza("p6_sib", "Pasando por el Si♭", """
F G A B | c B A G | F A c A | F4 |]
""", "En Fa mayor todos los Si son Si♭. Fíjate en que la armadura (un bemol) lo indica.", key="F", Q="1/4=72")

pieza("p6_grave", "Las notas graves: Sol, Fa, Mi y Re", """
G F E D | E F G A | B c B A | G4 |]
""", "Primero el Re (seis dedos) y después sube poco a poco: los dedos de la mano derecha se levantan uno a uno.", Q="1/4=72")

# ---------------------------------------------------------------------------------------------
# Módulo 7 · Articulación
# ---------------------------------------------------------------------------------------------
pieza("p7_picado", "Notas picadas (staccato)", """
.G .G .G .G | .A .A .A .A | .B .B .B .B | .A .A .G2 |]
""", "Cada nota empieza con la lengua («tu») y se corta con ella. No pares el aire: la lengua solo lo interrumpe un momento.", Q="1/4=80")

pieza("p7_ligado", "Notas ligadas (legato)", """
(G A B A) | (G A B2) | (B A G A) | G4 |]
""", "Solo la primera nota de cada ligadura se articula con la lengua. Las demás se cambian solo con los dedos.", Q="1/4=72")

pieza("p7_mixto", "Ligado y picado combinados", """
(G A) B .A | (G A) B2 | G .G .G .G | (A B A G) | G4 |]
""", "Las notas con arco se ligan y las que tienen punto se pican. Cuenta mentalmente cada compás.", Q="1/4=72")

pieza("p7_acentos", "Acentos", """
!>!G G !>!G G | !>!A A !>!A A | !>!B B B2 | !>!G4 |]
""", "Una nota acentuada se ataca con más aire y con una «ta» más marcada, pero sin morder la caña.", Q="1/4=76")

pieza("p7_corcheas", "Corcheas picadas", """
.G.G.G.G .A.A.A.A | .B.B.B.B .A.A G2 |]
""", "Dos notas por cada pulso. Si la lengua se te cansa, baja el tempo.", L="1/8", Q="1/4=72")

# ---------------------------------------------------------------------------------------------
# Módulo 8 · Registro agudo
# ---------------------------------------------------------------------------------------------
pieza("p8_octavas", "La llave de octava: la misma nota una octava más aguda", """
"^sin octava"G2 "^con octava"g2 | "^sin"A2 "^con"a2 | "^sin"B2 "^con"b2 | "^sin"c2 "^con"c'2 |]
""", "Con la llave de octava, la misma digitación suena una octava más aguda. Mantén la boca igual: la llave hace el trabajo.", Q="1/4=60")

pieza("p8_sol", "Escala de Sol mayor, una octava", """
G A B c | d e f g | g f e d | c B A G |]
""", "Los Fa son Fa♯. Del Do al Re cambia el registro: el Re se toca con la llave de octava.", key="G", Q="1/4=72")

pieza("p8_twinkle", "Estrellita, ¿dónde estás? (Twinkle, Twinkle)", """
"G"G G d d | "C"e e "G"d2 | "C"c c "G"B B | "D7"A A "G"G2 | "G"d d c c | "G"B B "D7"A2 | "G"d d c c | "G"B B "D7"A2 | "G"G G d d | "C"e e "G"d2 | "C"c c "G"B B | "D7"A A "G"G2 |]
""", "Melodía tradicional (dominio público). El salto de Sol a Re es una quinta: prepara la llave de octava.", key="G", acomp=True, Q="1/4=84")

pieza("p8_ode", "Himno de la alegría (L. van Beethoven)", """
"G"B B c d | "G"d c B A | "G"G G A B | "D7"B3/2 A/ A2 | "G"B B c d | "G"d c B A | "G"G G A B | "D7"A3/2 "G"G/ G2 |]
""", "Tema de la Novena sinfonía (1824, dominio público), transportado a Sol mayor escrito. El ritmo de la corchea con puntillo se cuenta «1-2-3-y».", key="G", acomp=True, Q="1/4=88")

# ---------------------------------------------------------------------------------------------
# Módulo 9 · Transposición
# ---------------------------------------------------------------------------------------------
pieza("p9_ode_tres", "La misma melodía en tres tonalidades escritas", """
"^escrito en Do: suena Mi♭"E E F G | G F E D | C C D E | E3/2 D/ D2 |
K:G
"^escrito en Sol: suena Si♭"B B c d | d c B A | G G A B | B3/2 A/ A2 |
K:D
"^escrito en Re: suena Fa"F F G A | A G F E | D D E F | F3/2 E/ E2 |]
""", "Es la misma música. Un piano que la toca en Mi♭ mayor, en Si♭ mayor o en Fa mayor necesita que el saxo alto la lea en Do, Sol o Re.", key="C", ajuste=False, Q="1/4=88")

# ---------------------------------------------------------------------------------------------
# Módulo 10 · Escalas y arpegios
# ---------------------------------------------------------------------------------------------
pieza("p10_do", "Escala de Do mayor (Do5–Do6)", """
c d e f | g a b c' | c' b a g | f e d c |]
""", "Solo el primer Do se toca sin llave de octava. Todas las demás notas y el Do agudo, con octava.", Q="1/4=72")
pieza("p10_fa", "Escala de Fa mayor", """
F G A B | c d e f | f e d c | B A G F |]
""", "El Si es Si♭ (dedo 1 izquierdo y 1 derecho). El Do es el del dedo 2 izquierdo.", key="F", Q="1/4=72")
pieza("p10_re", "Escala de Re mayor", """
D E F G | A B c d | d c B A | G F E D |]
""", "Dos sostenidos: Fa♯ y Do♯. El Do♯ agudo se toca con todos los dedos levantados.", key="D", Q="1/4=72")
pieza("p10_lam", "Escala de La menor natural", """
A B c d | e f g a | a g f e | d c B A |]
""", "La menor es la relativa de Do mayor: misma armadura, distinta nota de partida.", key="Am", Q="1/4=72")
pieza("p10_mim", "Escala de Mi menor natural", """
E F G A | B c d e | e d c B | A G F E |]
""", "Un sostenido (Fa♯). Mi menor es la relativa de Sol mayor.", key="Em", Q="1/4=72")
pieza("p10_rem", "Escala de Re menor natural", """
D E F G | A B c d | d c B A | G F E D |]
""", "Un bemol (Si♭). Re menor es la relativa de Fa mayor.", key="Dm", Q="1/4=72")
pieza("p10_arpegios", "Arpegios de Do, Sol, Fa y Re mayor", """
"^Do mayor"c e g c' | c' g e c |
K:G
"^Sol mayor"G B d g | g d B G |
K:F
"^Fa mayor"F A c f | f c A F |
K:D
"^Re mayor"D F A d | d A F D |]
""", "Tónica, tercera, quinta y octava. Sube y baja sin cortar el aire entre las notas.", ajuste=False, Q="1/4=72")
pieza("p10_cromatica", "Escala cromática, de Re4 a Do♯5 y vuelta", """
D _E E F | ^F G ^G A | _B B c ^c | ^c c B _B | A _A G ^F | F E _E D |]
""", "Doce notas, una por semitono. Sube con sostenidos y baja con bemoles. Las digitaciones de todas ellas están en la tabla del módulo 6.", Q="1/4=60")

# ---------------------------------------------------------------------------------------------
# Módulo 11 · Ritmo
# ---------------------------------------------------------------------------------------------
pieza("p11_pulso", "Pulso, blancas, negras y silencios", """
G G G G | G2 G2 | G G z2 | G4 |]
""", "Los silencios también se cuentan: el aire se corta, pero el pulso sigue.", Q="1/4=72")
pieza("p11_corcheas", "Corcheas y negras", """
G G G G A A A A | B2 B2 A2 G2 | G A B A G2 z2 | G8 |]
""", "Dos corcheas por cada pulso. Cuenta «1-y-2-y-3-y-4-y» en voz alta.", L="1/8", Q="1/4=72")
pieza("p11_puntillo", "Negra con puntillo y corchea", """
G3 A B3 A | G3 A B4 | A3 B c3 B | A4 G4 |]
""", "El puntillo añade la mitad: la negra con puntillo dura tres corcheas. Cuenta «1-2-3-y».", L="1/8", Q="1/4=66")
pieza("p11_sincopa", "Síncopas", """
G2 B2 A2 G2 | G B2 B2 A2 G | z B B2 z A A2 | G8 |]
""", "En las notas síncopadas el acento cae en la «y». Marca el pulso con el pie y no lo cambies.", L="1/8", Q="1/4=66")
pieza("p11_68", "Compás de 6/8", """
G2 G A2 A | B2 B A3 | G2 G A2 A | B3 G3 |]
""", "Seis corcheas por compás, sentidas en dos pulsos de tres: «UNO-dos-tres CUATRO-cinco-seis».", meter="6/8", L="1/8", Q="3/8=60")
pieza("p11_vals", "Vals sencillo", """
"G"G A B | "G"d2 B | "C"c B A | "D7"B3 | "G"G A B | "G"d2 B | "D7"A B A | "G"G3 |]
""", "Tres pulsos por compás, con el primero un poco más marcado. Toca con el acompañamiento y escucha el «UM-pa-pa».", key="G", meter="3/4", acomp=True, Q="1/4=120")
pieza("p11_frase", "Frases y respiraciones", """
(G A B c | d2 c2) | (B c d e | d4) | "^respira"z4 | (d c B A | G2 A2) | (B A G A | G4) |]
""", "Cada arco es una frase. Respira donde está el silencio y no a mitad de frase: así la melodía «habla».", Q="1/4=72")

# ---------------------------------------------------------------------------------------------
# Módulo 12 · Sonido y afinación
# ---------------------------------------------------------------------------------------------
pieza("p12_largas", "Notas largas con matices", """
!p!G4 | !crescendo(!A4 | !crescendo)!!f!B4 | !diminuendo(!A4 | !diminuendo)!!p!G4 |]
""", "Crescendo: empieza suave y sube el aire poco a poco sin que cambie la altura. Diminuendo: al revés.", Q="1/4=60")
pieza("p12_afinacion", "Notas de referencia para afinar", """
"^escrito Fa♯ → suena La 440"!fermata!^f4 | "^escrito Sol → suena Si♭"!fermata!g4 |]
""", "El saxo alto afina con el La de concierto, que se escribe Fa♯ (Fa♯5), o con el Si♭ de concierto, que se escribe Sol (Sol5).", Q="1/4=50")

# ---------------------------------------------------------------------------------------------
# Módulo 13 · Repertorio
# ---------------------------------------------------------------------------------------------
pieza("r_frere", "Frère Jacques", """
"G"G A B G | "G"G A B G | "G"B c d2 | "G"B c d2 | "D7"d/e/ d/c/ B G | "G"d/e/ d/c/ B G | "G"G D G2 | "G"G D G2 |]
""", "Canon tradicional (dominio público). Puedes tocarlo en canon con otra persona, entrando dos compases más tarde.", key="G", acomp=True, Q="1/4=96")
pieza("r_marcha", "Marcha de los saxofones", """
"F"F F A A | c2 A2 | "Bb"B B d d | c2 A2 | "C7"G G B B | A2 F2 | "F"F A c A | F4 |]
""", "Pieza original del curso, en Fa mayor escrito. Respira donde caen las blancas y marca el pulso con el pie.", key="F", acomp=True, Q="1/4=104")
pieza("r_balada", "Balada del atardecer", """
"Am"A2 c2 | "Dm"d2 c2 | "E7"B2 ^G2 | "Am"A4 | "F"c2 d2 | "Dm"e2 d2 | "E7"c2 B2 | "Am"A4 |]
""", "Pieza original del curso, en La menor escrito. Toca despacio y con un sonido cantado; hay un Sol♯ en el compás 3.", key="Am", acomp=True, Q="1/4=60")
pieza("r_samba", "Samba fácil", """
"C"c2 c e | g2 g e | "G7"d2 d B | G2 z2 | "C"c2 c e | g2 g e | "G7"d B d B | "C"c4 |]
""", "Pieza original del curso, en Do mayor escrito. Dos corcheas por pulso y mucho cuidado con la llave de octava.", key="C", meter="2/4", L="1/8", acomp=True, Q="1/4=100")

# ---------------------------------------------------------------------------------------------
# Módulo 14 · Blues y jazz
# ---------------------------------------------------------------------------------------------
pieza("p14_escala", "Escala de blues de La (suena en Do)", """
A c d _e | e g a2 | a g _e d | c A2 z |]
""", "La, Do, Re, Mi♭, Mi y Sol: la «nota azul» es el Mi♭. Escrita en La, suena en Do de concierto.", Q="1/4=80")
pieza("p14_blues", "Blues de 12 compases (La escrito = Do de concierto)", """
"A7"A c d2 | "A7"d c A2 | "A7"A c d _e | "A7"e2 c2 | "D7"d2 d c | "D7"d2 c2 | "A7"A c e2 | "A7"d c A2 | "E7"B2 d2 | "D7"A c d c | "A7"A2 c2 | "E7"B2 A2 |]
""", "Melodía original del curso sobre el blues clásico: A7 – D7 – A7 – E7. Escúchala y luego improvisa con la escala de blues sobre el acompañamiento.", key="C", acomp=True, Q="1/4=96")
pieza("p14_swing", "Corcheas con swing", """
"A7"A B c d e d c A | "D7"d e d c A2 z2 | "A7"A B c d e g e c | "E7"B A G A B2 z2 |]
""", "Las corcheas se escriben iguales pero se tocan «largas-cortas» (como un tresillo con las dos primeras unidas). Escucha el swing de la grabación.", L="1/8", acomp=True, Q="1/4=104")
pieza("p14_pregunta", "Pregunta y respuesta sobre el blues", """
"A7"A c d2 | "A7"A c e2 | "D7"d c A2 | "A7"A4 |]
""", "Los dos primeros compases preguntan, el tercero responde y el cuarto cierra. Es la base de la improvisación.", acomp=True, Q="1/4=88")

# ---------------------------------------------------------------------------------------------
# Gimnasio de ejercicios
# ---------------------------------------------------------------------------------------------
pieza("e_largas_escalera", "Escalera de notas largas", """
G4 | A4 | B4 | c4 | d4 | c4 | B4 | A4 | G4 |]
""", "Cada nota dura cuatro tiempos. Cambia de nota sin que el sonido se «rompa» y mantén la afinación.", Q="1/4=60")
pieza("e_terceras", "Terceras", """
G B A c | B d c e | d c B A | G4 |]
""", "Cada salto es una tercera: la nota de abajo y la de dos pasos más arriba. Mira el intervalo antes de tocar.", key="G", Q="1/4=72")
pieza("e_quintas", "Saltos de quinta", """
G d G d | A e A e | B f B f | G4 |]
""", "El salto de quinta cruza al registro agudo: pulsa la llave de octava a tiempo.", key="G", Q="1/4=60")
pieza("e_lectura1", "Lectura a primera vista · nivel 1", """
G A B A | G2 B2 | A G F G | A4 |]
""", "Notas vecinas en Sol mayor, sin llave de octava. Escanea la armadura (un sostenido) y el compás antes de empezar.", key="G", Q="1/4=72")
pieza("e_lectura2", "Lectura a primera vista · nivel 2", """
F G A B | c2 A2 | B c d c | B A G F | F4 |]
""", "Fa mayor con Si♭ y un Re agudo con llave de octava. Escanea los bemoles y las notas más altas y más bajas.", key="F", Q="1/4=76")
pieza("e_lectura3", "Lectura a primera vista · nivel 3", """
D E F G | A2 B2 | c d c B | A G F E | D4 |]
""", "Re mayor: dos sostenidos (Fa♯ y Do♯). Toca sin parar aunque falles.", key="D", Q="1/4=80")
pieza("e_picado_cambios", "Picado con cambios de nota", """
.G .A .B .A | .G .A .B2 | .B .A .G .A | G4 |]
""", "Cada nota empieza con la lengua. Las notas cortas no deben sonar «con hipo»: suelta el aire con regularidad.", Q="1/4=76")
pieza("e_octavas_ligadas", "Octavas ligadas", """
(G g) (A a) | (B b) (c c') | (c' c) (b B) | (a A) (g G) |]
""", "Liga la nota con su octava sin volver a atacar con la lengua. El aire y la forma de la boca se mantienen.", Q="1/4=60")
pieza("e_dinamicas_frase", "Frase con matices", """
!p!G A B c | !crescendo(!d2 e2 | !crescendo)!!f!d2 c2 | !diminuendo(!B A G2 | !diminuendo)!!p!G4 |]
""", "Los matices se hacen con el aire, no con la mordida. Crece hacia el punto más agudo y relaja hacia el final.", key="G", Q="1/4=72")

# Comprobaciones de integridad
for _k, _p in PIEZAS.items():
    assert "K:" in _p["abc"], _k
