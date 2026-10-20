"""Partituras del curso de piano en notación ABC (https://abcnotation.com).

Convenciones: C = Do central (Do4), c = Do5, C, = Do3, C,, = Do2.
Las digitaciones van como decoraciones (!1!…!5!) y el cifrado entre comillas.
Todas las piezas son ejercicios originales del curso salvo los fragmentos de
obras de dominio público indicados (Bach, Beethoven).
"""

PIEZAS = {}


def pieza(clave, titulo, abc, nota=""):
    PIEZAS[clave] = {"titulo": titulo, "abc": abc.strip() + "\n", "nota": nota}


GRAN = "%%score {RH | LH}\nV:RH clef=treble name=\"M.D.\"\nV:LH clef=bass name=\"M.I.\"\n"

pieza("escala_do", "Escala de Do mayor · 2 octavas, manos juntas", f"""
X:1
T:Escala de Do mayor
C:Ejercicio · digitación estándar
M:4/4
L:1/8
Q:1/4=72
{GRAN}K:C
[V:RH] !1!C!2!D!3!E!1!F !2!G!3!A!4!B!1!c | !2!d!3!e!1!f!2!g !3!a!4!b!5!c'!4!b | !3!a!2!g!1!f!3!e !2!d!1!c!4!B!3!A | !2!G!1!F!3!E!2!D !1!C4 |]
[V:LH] !5!C,,!4!D,,!3!E,,!2!F,, !1!G,,!3!A,,!2!B,,!1!C, | !4!D,!3!E,!2!F,!1!G, !3!A,!2!B,!1!C!2!B, | !3!A,!1!G,!2!F,!3!E, !4!D,!1!C,!2!B,,!3!A,, | !1!G,,!2!F,,!3!E,,!4!D,, !5!C,,4 |]
""", "Dedos: el pulgar «pasa por debajo» tras el 3.º y el 4.º dedo; los dedos largos «pasan por encima» al bajar.")

pieza("escala_lam", "Escala de La menor armónica · 1 octava, manos juntas", f"""
X:2
T:La menor armónica
C:Ejercicio
M:4/4
L:1/8
Q:1/4=72
{GRAN}K:Am
[V:RH] !1!A!2!B!3!c!1!d !2!e!3!f!4!^g!5!a | !4!^g!3!f!2!e!1!d !3!c!2!B !1!A2 |]
[V:LH] !5!A,!4!B,!3!C!2!D !1!E!3!F!2!^G!1!A | !2!^G!3!F!1!E!2!D !3!C!4!B, !5!A,2 |]
""", "El 7.º grado elevado (Sol♯) crea la sensible y el intervalo característico de 2.ª aumentada Fa–Sol♯.")

pieza("arpegio_do", "Arpegio de Do mayor · 2 octavas, manos juntas", f"""
X:3
T:Arpegio de Do mayor
C:Ejercicio
M:4/4
L:1/8
Q:1/4=60
{GRAN}K:C
[V:RH] (3!1!C!2!E!3!G (3!1!c!2!e!3!g (3!5!c'!3!g!2!e (3!1!c!3!G!2!E | !1!C8 |]
[V:LH] (3!5!C,,!4!E,,!2!G,, (3!1!C,!4!E,!2!G, (3!1!C!2!G,!4!E, (3!1!C,!2!G,,!4!E,, | !5!C,,8 |]
""", "Mantén la muñeca a la altura del teclado y desplaza el brazo lateralmente: el pulgar solo «guía», no se retuerce.")

pieza("inversiones", "Acorde de Do mayor y sus inversiones", """
X:4
T:Do mayor: estado fundamental e inversiones
C:Ejercicio
M:4/4
L:1/4
Q:1/4=60
K:C
"^Estado fundamental""_1-3-5"[CEG]2 "^1.ª inversión""_1-2-5"[EGc]2 | "^2.ª inversión""_1-3-5"[Gce]2 "^Fundamental (8.ª arriba)""_1-3-5"[ceg]2 |]
""", "Digitación de la mano derecha bajo cada acorde. En la 1.ª inversión se usa 1-2-5 porque la 4.ª queda arriba.")

pieza("cadencia", "Cadencias: I–IV–V7–I y I–vi–ii7–V7–I en Do mayor", f"""
X:5
T:Cadencias en Do mayor
C:Ejercicio
M:4/4
L:1/4
Q:1/4=60
{GRAN}K:C
[V:RH] "C"[CEG]2 "F"[CFA]2 | "G7"[B,FG]2 "C"[CEG]2 || "C"[CEG]2 "Am"[CEA]2 | "Dm7"[CFA]2 "G7"[B,FG]2 | "C"[CEG]4 |]
[V:LH] "_I"C,2 "_IV"F,2 | "_V7"G,2 "_I"C,2 || "_I"C,2 "_vi"A,,2 | "_ii7"D,2 "_V7"G,,2 | "_I"C,4 |]
""", "Observa la conducción de voces: las notas comunes se mantienen y las demás se mueven por grado conjunto.")

pieza("alberti", "Melodía con bajo Alberti", f"""
X:6
T:Estudio con bajo Alberti
C:Ejercicio original del curso
M:4/4
L:1/8
Q:1/4=88
{GRAN}K:C
[V:RH] "C"G4 E2 G2 | "G7"F4 D2 F2 | "C"E2 G2 c2 B2 | "C"c8 |]
[V:LH] C,G,E,G, C,G,E,G, | B,,G,D,G, B,,G,D,G, | C,G,E,G, C,G,E,G, | [C,E,G,]8 |]
""", "El bajo Alberti arpegia el acorde en orden grave–agudo–medio–agudo. La mano izquierda siempre más suave que la melodía.")

pieza("pedal", "Pedal sincopado (legato)", f"""
X:7
T:Estudio de pedal sincopado
C:Ejercicio original del curso
M:4/4
L:1/4
Q:1/4=66
{GRAN}K:C
[V:RH] "C"e2 g2 | "Am"e2 c2 | "F"f2 a2 | "G7"g2 f2 | "C"e4 |]
[V:LH] "_Ped."C, G, C G, | "_✱ Ped."A,, E, A, E, | "_✱ Ped."F,, C, F, C, | "_✱ Ped."G,, D, F, D, | "_✱ Ped."[C,G,]4 |]
""", "«✱ Ped.» sobre el bajo nuevo: levanta el pedal justo cuando suena el acorde nuevo y vuelve a pisarlo inmediatamente después. Así se enlazan los acordes sin mezclarlos ni dejar huecos.")

pieza("octavas", "Octavas en Re mayor", """
X:8
T:Octavas (mano derecha)
C:Ejercicio
M:4/4
L:1/4
Q:1/4=60
K:D
!5![Dd]!5![Ee]!4![Ff]!5![Gg] | !5![Aa]!5![Bb]!4![cc']!5![dd'] |]
""", "Pulgar abajo; arriba el 5.º en teclas blancas y el 4.º en negras (Fa♯, Do♯). Muñeca suelta: la mano «rebota» desde la muñeca.")

pieza("terceras", "Terceras dobles en Do mayor", """
X:9
T:Terceras dobles (mano derecha)
C:Ejercicio · una digitación habitual (hay variantes)
M:4/4
L:1/4
Q:1/4=50
K:C
"^1-3"[CE]"^2-4"[DF]"^3-5"[EG]"^1-3"[FA] | "^2-4"[GB]"^1-3"[Ac]"^2-4"[Bd]"^3-5"[ce] |]
""", "Estudia primero ligando solo la voz superior; después, la inferior; por último, las dos.")

pieza("adornos", "Adornos: cómo se escriben y cómo se tocan", """
X:10
T:Trino, mordente y grupeto
C:Ejercicio · realización en estilo barroco-clásico
M:4/4
L:1/16
Q:1/4=60
K:C
"^Escrito"!trill!d8 !mordent!c8 | !turn!e8 z8 || "^Se toca"edededed cBc6 | fede e4 z8 |]
""", "Trino: empieza por la nota superior. Mordente: nota real–inferior–real. Grupeto: superior–real–inferior–real.")

pieza("poli32", "Polirritmia 3 contra 2", f"""
X:11
T:3 contra 2
C:Ejercicio
M:2/4
L:1/8
Q:1/4=50
{GRAN}K:C
[V:RH] (3CEG (3cGE | (3CEG (3cGE |]
[V:LH] C,G, C,G, | C,G, C,G, |]
""", "Cuadrícula de 6: la mano derecha toca en 1-3-5 y la izquierda en 1-4. Solo coinciden en el 1.")

pieza("poli43", "Polirritmia 4 contra 3", f"""
X:12
T:4 contra 3
C:Ejercicio
M:2/4
L:1/16
Q:1/4=40
{GRAN}K:C
[V:RH] cdef gfed | cdef gfed |]
[V:LH] (3C,2G,2C2 (3C,2G,2C2 | (3C,2G,2C2 (3C,2G,2C2 |]
""", "Cuadrícula de 12: la mano derecha toca en 1-4-7-10 y la izquierda en 1-5-9.")

pieza("iivi", "ii–V–I con voicings sin fundamental", f"""
X:13
T:ii–V–I en Do mayor y en Fa mayor
C:Ejercicio
M:4/4
L:1/4
Q:1/4=80
{GRAN}K:C
[V:RH] "Dm7"[FAce]4 | "G7"[FABe]4 | "Cmaj7"[EGBd]4 || [K:F] "Gm7"[B,DFA]4 | "C7"[B,DEA]4 | "Fmaj7"[A,CEG]4 |]
[V:LH] D,4 | G,,4 | C,4 || [K:F] G,,4 | C,4 | F,,4 |]
""", "La mano derecha toca 3.ª, 5.ª, 7.ª y 9.ª (o 7.ª, 9.ª, 3.ª y 13.ª en el V7); la izquierda, la fundamental. Casi no se mueven los dedos entre acordes.")

pieza("blues", "Blues de 12 compases en Do (boogie)", f"""
X:14
T:Blues en Do
C:Ejercicio original del curso · tocar con swing
M:4/4
L:1/8
Q:1/4=104
{GRAN}K:C
[V:RH] "C7"z2 [E_B]2 z2 [E_B]2 | "C7"z2 [E_B]2 z2 [E_B]2 | "C7"z2 [E_B]2 z2 [E_B]2 | "C7"z2 [E_B]2 z2 [E_B]2 |
[V:LH] C,G, C,A, C,_B, C,A, | C,G, C,A, C,_B, C,A, | C,G, C,A, C,_B, C,A, | C,G, C,A, C,_B, C,A, |
[V:RH] "F7"z2 [_EA]2 z2 [_EA]2 | "F7"z2 [_EA]2 z2 [_EA]2 | "C7"z2 [E_B]2 z2 [E_B]2 | "C7"z2 [E_B]2 z2 [E_B]2 |
[V:LH] F,C F,D F,_E F,D | F,C F,D F,_E F,D | C,G, C,A, C,_B, C,A, | C,G, C,A, C,_B, C,A, |
[V:RH] "G7"z2 [FB]2 z2 [FB]2 | "F7"z2 [_EA]2 z2 [_EA]2 | "C7"z2 [E_B]2 z2 [E_B]2 | "G7"z2 [FB]2 z2 [FB]2 |]
[V:LH] G,D G,E G,F G,E | F,C F,D F,_E F,D | C,G, C,A, C,_B, C,A, | G,D G,E G,F G,E |]
""", "Mano derecha: 3.ª y 7.ª de cada acorde (shell voicing). Mano izquierda: patrón boogie fundamental–5.ª–6.ª–7.ª.")

pieza("bach846", "J. S. Bach · Preludio en Do mayor, BWV 846 (c. 1-4)", """
X:15
T:Preludio en Do mayor, BWV 846
C:J. S. Bach · El clave bien temperado, libro I
M:4/4
L:1/16
Q:1/4=66
K:C
"C"CEGc eGce CEGc eGce | "Dm7/C"CDAd fAdf CDAd fAdf | "G7/B"B,DGd fGdf B,DGd fGdf | "C"CEGc eGce CEGc eGce |]
""", "Fragmento: los cuatro primeros compases reducidos a una sola línea para ver el patrón armónico. En el original, las dos primeras notas de cada grupo las toca la mano izquierda y se mantienen. Obra completa en IMSLP.")

pieza("elise", "L. van Beethoven · Para Elisa, WoO 59 (c. 1-8)", f"""
X:16
T:Para Elisa (Für Elise), WoO 59
C:L. van Beethoven
M:3/8
L:1/16
Q:3/8=50
{GRAN}K:Am
[V:RH] !pp!e^d | e^d e B =d c | A2 z C E A | B2 z E ^G B | c2 z E e^d |
[V:LH] z2 | z6 | A,,E,A, z3 | E,,E,^G, z3 | A,,E,A, z3 |
[V:RH] e^d e B =d c | A2 z C E A | B2 z E c B | A2 z4 |]
[V:LH] z6 | A,,E,A, z3 | E,,E,^G, z3 | A,,E,A, z3 |]
""", "Fragmento: tema inicial. Obra completa en IMSLP.")

# ---------------------------------------------------------------------------------------------
# Ampliación: partituras para las explicaciones «fáciles»
# ---------------------------------------------------------------------------------------------

pieza("pulso_68", "Contar el pulso: 3/4 frente a 6/8", """
X:17
T:3/4 y 6/8: las mismas seis corcheas, distinto pulso
C:Ejercicio · cuenta en voz alta los números de debajo
M:3/4
L:1/8
Q:1/4=80
K:C
"^3/4: tres pulsos de negra"!>!C E !>!G c !>!G E | !>!C2 !>!E2 !>!G2 |
w: 1 y 2 y 3 y 1 2 3
[M:6/8][Q:3/8=60] "^6/8: dos pulsos de negra con puntillo"!>!C E G !>!c G E | !>!C3 !>!G3 |]
w: 1 2 3 4 5 6 1 4
""", "En 3/4 las corcheas van de dos en dos (1-y, 2-y, 3-y); en 6/8, de tres en tres (1-2-3, 4-5-6). Los acentos (>) marcan el pulso.")

pieza("ritmos", "Corcheas, tresillos, síncopa y puntillo", """
X:18
T:Ritmos que hay que saber contar
C:Ejercicio · cuenta en voz alta
M:2/4
L:1/8
Q:1/4=66
K:C
"^Corcheas"C D E F | "^Tresillos"(3CDE (3FGA | "^Síncopa"C D2 E | "^Puntillo"D3 C | D4 |]
w: 1 y 2 y 1-o-la 2-o-la 1 y y 1 y 1
""", "Síncopa: la nota larga empieza en un tiempo débil («y») y se mantiene sobre el fuerte. Puntillo: alarga la nota la mitad de su valor.")

pieza("escala_sol", "Escala de Sol mayor · manos juntas", f"""
X:19
T:Sol mayor
C:Ejercicio · misma digitación que Do mayor
M:4/4
L:1/8
Q:1/4=72
{GRAN}K:G
[V:RH] !1!G!2!A!3!B!1!c !2!d!3!e!4!f!5!g | !4!f!3!e!2!d!1!c !3!B!2!A !1!G2 |]
[V:LH] !5!G,!4!A,!3!B,!2!C !1!D!3!E!2!F!1!G | !2!F!3!E!1!D!2!C !3!B,!4!A, !5!G,2 |]
""", "La armadura (un sostenido) convierte todos los Fa en Fa♯: así la escala cumple el patrón T-T-S-T-T-T-S.")

pieza("escala_fa", "Escala de Fa mayor · manos juntas", f"""
X:20
T:Fa mayor
C:Ejercicio · la mano derecha cambia la digitación
M:4/4
L:1/8
Q:1/4=72
{GRAN}K:F
[V:RH] !1!F!2!G!3!A!4!B !1!c!2!d!3!e!4!f | !3!e!2!d!1!c!4!B !3!A!2!G !1!F2 |]
[V:LH] !5!F,!4!G,!3!A,!2!B, !1!C!3!D!2!E!1!F | !2!E!3!D!1!C!2!B, !3!A,!4!G, !5!F,2 |]
""", "Mano derecha 1-2-3-4, 1-2-3-4: así el pulgar no cae en el Si♭ (tecla negra). La izquierda sigue como en Do.")

pieza("cadencia_sol", "Cadencia I–IV–V7–I transportada a Sol mayor", f"""
X:21
T:La misma cadencia, en Sol mayor
C:Ejercicio · compárala con la de Do
M:4/4
L:1/4
Q:1/4=60
{GRAN}K:G
[V:RH] "G"[GBd]2 "C"[Gce]2 | "D7"[Fcd]2 "G"[GBd]2 |]
[V:LH] "_I"G,2 "_IV"C,2 | "_V7"D,2 "_I"G,2 |]
""", "Son las mismas «formas» de la mano que en Do, desplazadas: I, IV y V7 siempre suenan con la misma función.")

pieza("vals", "Acompañamiento de vals", f"""
X:22
T:Pequeño vals
C:Ejercicio original del curso
M:3/4
L:1/4
Q:1/4=120
{GRAN}K:C
[V:RH] "C"e2 g | "G7"f2 d | "C"e c G | "C"c3 |]
[V:LH] !>!C, [E,G,] [E,G,] | !>!G,, [B,,F,] [B,,F,] | !>!C, [E,G,] [E,G,] | C,3 |]
""", "Bajo con peso en el 1 y acordes ligeros en el 2 y el 3: «UM-pa-pa». La melodía, siempre por encima del acompañamiento.")

pieza("blues_frase", "Frase de blues: pregunta y respuesta", f"""
X:23
T:Improvisación de ejemplo sobre Do7
C:Ejercicio original del curso · tocar con swing
M:4/4
L:1/8
Q:1/4=96
{GRAN}K:C
[V:RH] "^pregunta""C7"c2 _e f ^f g3 | "^respuesta"z2 _b g f _e c2 | "^nota azul"_e2 =e c G2 c2 | c6 z2 |]
[V:LH] C,G, C,A, C,_B, C,A, | C,G, C,A, C,_B, C,A, | C,G, C,A, C,_B, C,A, | C,G, C,A, C,_B, C,A, |]
""", "Solo con la escala de blues: dos compases que «preguntan», dos que «responden» y la nota azul (Mi♭) que resuelve en Mi.")

# Teoría a fondo: notas faro, intervalos, armaduras, tonalidad y modulación ---------------------------
pieza("faros_sol", "Notas faro en clave de Sol", """
X:24
T:Notas faro · clave de Sol
C:Apréndelas de memoria: las demás se calculan desde ellas
M:4/4
L:1/4
Q:1/4=100
K:C clef=treble
"^Do4"C4 | "^Mi4"E4 | "^Sol4"G4 | "^Do5"c4 | "^Fa5"f4 | "^Sol5"g4 | "^La5"a4 |]
""", "Do4: 1.ª línea adicional abajo · Mi4: 1.ª línea · Sol4: 2.ª línea (donde se enrosca la clave) · Do5: 3.er espacio · Fa5: 5.ª línea · Sol5: espacio de encima · La5: 1.ª línea adicional arriba.")

pieza("faros_fa", "Notas faro en clave de Fa", """
X:25
T:Notas faro · clave de Fa
C:Apréndelas de memoria: las demás se calculan desde ellas
M:4/4
L:1/4
Q:1/4=100
K:C clef=bass
"^Do2"C,,4 | "^Sol2"G,,4 | "^Do3"C,4 | "^Fa3"F,4 | "^La3"A,4 | "^Do4"C4 |]
""", "Do2: 2.ª línea adicional abajo · Sol2: 1.ª línea · Do3: 2.º espacio · Fa3: 4.ª línea (entre los dos puntos de la clave) · La3: 5.ª línea · Do4: 1.ª línea adicional arriba (el mismo Do central de la clave de Sol).")

pieza("intervalos", "Los intervalos desde Do: escúchalos y míralos", """
X:26
T:Intervalos desde Do4
C:Melódicos (una nota tras otra) y armónicos (a la vez)
M:4/4
L:1/4
Q:1/4=80
K:C clef=treble
C2 "^2.ª"D2 | C2 "^3.ª"E2 | C2 "^4.ª"F2 | C2 "^5.ª"G2 | C2 "^6.ª"A2 | C2 "^7.ª"B2 | C2 "^8.ª"c2 |
"^3.ª"[CE]4 | "^5.ª"[CG]4 | "^6.ª"[CA]4 | "^8.ª"[Cc]4 |]
""", "Fíjate en el dibujo: 3.ª, 5.ª y 7.ª van de línea a línea (o de espacio a espacio); 2.ª, 4.ª, 6.ª y 8.ª, de línea a espacio (o al revés).")

pieza("armaduras_sost", "Armaduras con sostenidos (girando a la derecha en el círculo)", """
X:27
T:Armaduras con sostenidos
C:Cada quinta hacia arriba añade un sostenido
% sin-ajuste
M:none
L:1/1
Q:1/2=40
K:C clef=treble
"^Do · La m"[CEG] || [K:G]"^Sol · Mi m"[GBd] || [K:D]"^Re · Si m"[DFA] || [K:A]"^La · Fa♯ m"[Ace] ||
K:E
"^Mi · Do♯ m"[EGB] || [K:B]"^Si · Sol♯ m"[Bdf] || [K:F#]"^Fa♯ · Re♯ m"[FAc] || [K:C#]"^Do♯ · La♯ m"[ceg] |]
""", "Cada compás suena el acorde de la tónica mayor. Orden de los sostenidos: Fa – Do – Sol – Re – La – Mi – Si. El último sostenido es la sensible: la tónica mayor está un semitono por encima.")

pieza("armaduras_bem", "Armaduras con bemoles (girando a la izquierda en el círculo)", """
X:28
T:Armaduras con bemoles
C:Cada quinta hacia abajo añade un bemol
% sin-ajuste
M:none
L:1/1
Q:1/2=40
K:C clef=treble
"^Do · La m"[CEG] || [K:F]"^Fa · Re m"[FAc] || [K:Bb]"^Si♭ · Sol m"[Bdf] || [K:Eb]"^Mi♭ · Do m"[EGB] ||
K:Ab
"^La♭ · Fa m"[Ace] || [K:Db]"^Re♭ · Si♭ m"[DFA] || [K:Gb]"^Sol♭ · Mi♭ m"[GBd] || [K:Cb]"^Do♭ · La♭ m"[CEG] |]
""", "Cada compás suena el acorde de la tónica mayor. Orden de los bemoles: Si – Mi – La – Re – Sol – Do – Fa (el de los sostenidos al revés). El penúltimo bemol es la tónica mayor.")

pieza("tono_do", "Misma armadura, dos tonalidades (1): Do mayor", """
X:29
T:Melodía A
C:Sin alteraciones · ¿mayor o menor?
M:4/4
L:1/4
Q:1/4=88
K:C clef=treble
"C"c2 e g | "G"d2 B G | "F"A c "C"G E | "G7"F D "C"C2 |]
""", "Empieza y termina en Do, los acordes giran alrededor de Do y no aparece ningún Sol♯: es Do mayor.")

pieza("tono_lam", "Misma armadura, dos tonalidades (2): La menor", """
X:30
T:Melodía B
C:Sin armadura · ¿mayor o menor?
M:4/4
L:1/4
Q:1/4=88
K:Am clef=treble
"Am"A2 c e | "E"^g2 e B | "Am"c B A E | "E"^G B "Am"A2 |]
""", "Empieza y termina en La y aparece Sol♯ (la sensible de La menor) como alteración accidental: es La menor, la relativa de Do mayor.")

pieza("modulacion", "Una modulación: de Do mayor a Sol mayor", """
X:31
T:Modulación a la dominante
C:Ejercicio original del curso
M:4/4
L:1/4
Q:1/4=84
K:C clef=treble
"^Do mayor""C"c2 e g | "F"a2 f d | "^→ Sol mayor""D7"^f e d c | "G"B2 d g | "D7"a ^f d c | "G"B4 |]
""", "A partir del compás 3 aparece Fa♯ una y otra vez y la frase cierra con D7 → G (V7 → I de Sol): la música ha cambiado de «casa».")

pieza("calidades", "Mayor, menor, justa, aumentada y disminuida: escucha la diferencia", """
X:32
T:El apellido de los intervalos
C:Cada compás: nota a nota y después a la vez
M:4/4
L:1/4
Q:1/4=80
K:C clef=treble
"^3.ª mayor (4)"C E [CE]2 | "^3.ª menor (3)"C _E [C_E]2 | "^5.ª justa (7)"C G [CG]2 | "^5.ª aumentada (8)"C ^G [C^G]2 |
"^5.ª disminuida (6)"C _G [C_G]2 | "^4.ª justa (5)"C F [CF]2 | "^4.ª aumentada (6)"C ^F [C^F]2 | "^6.ª mayor (9)"C A [CA]2 | "^6.ª menor (8)"C _A [C_A]2 |]
""", "Entre paréntesis, los semitonos. La 5.ª disminuida y la 4.ª aumentada suenan igual (6 semitonos, el tritono), pero se escriben distinto: Sol♭ es un tipo de Sol (5.ª) y Fa♯ un tipo de Fa (4.ª).")
