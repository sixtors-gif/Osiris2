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
