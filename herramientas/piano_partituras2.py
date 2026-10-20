"""Partituras de la ampliación: teoría (compases, modos, armonización, forma…) y ejercicios prácticos.
Todas son originales del curso."""
from piano_partituras import GRAN, pieza

# ---------------------------------------------------------------------------------------------
# Teoría
# ---------------------------------------------------------------------------------------------
pieza("compases", "Compases: dónde cae el acento", """
X:33
T:El acento marca el compás
C:El primer tiempo de cada compás se siente más fuerte
M:2/4
L:1/4
Q:1/4=90
K:C clef=treble
"^2/4"!>!c c | !>!c c || [M:3/4]"^3/4"!>!c c c | !>!c c c || [M:4/4]"^4/4"!>!c c c c | !>!c c c c || [M:6/8][L:1/8]"^6/8"!>!c c c c c c | !>!c c c c c c |]
w: 1 2 | 1 2 | 1 2 3 | 1 2 3 | 1 2 3 4 | 1 2 3 4 | 1 2 3 4 5 6 | 1 2 3 4 5 6
""", "En 2/4, 3/4 y 4/4 cada número es un pulso. En 6/8 se cuentan seis corcheas, pero solo se sienten dos pulsos: el 1 y el 4.")

pieza("anacrusa", "Anacrusa: empezar «antes» del primer compás", """
X:34
T:Melodía con anacrusa
C:Ejercicio original del curso
M:3/4
L:1/4
Q:1/4=100
K:C clef=treble
"^anacrusa"G | "C"c2 e | "G7"d2 B | "C"c2 G | "C"c2 e | "F"f2 d | "G7"d2 B | "C"c2 |]
""", "El primer compás solo tiene un pulso (la anacrusa). Por eso el último compás está incompleto: lo que falta (un pulso) estaba al principio.")

pieza("hemiola", "Hemiola: dos compases de 3/4 sentidos «de a dos»", """
X:35
T:Hemiola
C:Ejercicio original del curso
M:3/4
L:1/4
Q:1/4=108
""" + GRAN + """K:C
[V:RH] !>!E G c | !>!e c G | !>!E G c | !>!e c G | !>!E G !>!c | e !>!c G | d2 B | !>!c3 |]
[V:LH] C,3 | C,3 | C,3 | C,3 | C,3 | C,3 | G,,3 | C,3 |]
""", "En los compases 1 a 4 el acento cae en el primer tiempo de cada compás (3+3). En los compases 5 y 6 caen cada dos tiempos (2+2+2): las seis negras parecen un compás de 3/2.")

pieza("modos_do", "Seis modos sobre la misma nota: Do", """
X:36
T:Los modos a partir de Do
C:Se diferencian en las notas que cambian respecto al modo mayor
M:4/4
L:1/4
Q:1/4=76
K:C clef=treble
"^Jónico (mayor)"C D E F | G A B c || "^Dórico (Mi♭, Si♭)"C D _E F | G A _B c || "^Frigio (Re♭, Mi♭, La♭, Si♭)"C _D _E F | G _A _B c || "^Lidio (Fa♯)"C D E ^F | G A B c || "^Mixolidio (Si♭)"C D E F | G A _B c || "^Eólico (menor natural)"C D _E F | G _A _B c |]
""", "Mismo punto de partida, seis «colores». El jónico es el mayor y el eólico, el menor natural. El dórico y el mixolidio son los más usados en jazz, folk y rock.")

pieza("pentatonica", "Las escalas pentatónicas", """
X:37
T:Pentatónicas de Do mayor y La menor
C:Cinco notas, sin semitonos: es difícil que suenen mal
M:4/4
L:1/4
Q:1/4=88
""" + GRAN + """K:C
[V:RH] "^Do mayor pentatónica"C D E G | A c A G | E D C2 || "^La menor pentatónica"A, C D E | G A G E | D C A,2 |]
[V:LH] C,2 G,2 | C,2 G,2 | C,4 || A,,2 E,2 | A,,2 E,2 | A,,4 |]
""", "Son las cinco teclas blancas Do–Re–Mi–Sol–La (o La–Do–Re–Mi–Sol): la misma escala, con dos «casas» posibles.")

pieza("cromatica", "Escala cromática de una octava", """
X:38
T:Escala cromática
C:Todos los semitonos · mano derecha
M:4/4
L:1/8
Q:1/4=72
K:C clef=treble
!1!C!3!^C!1!D!3!^D!1!E!2!F!3!^F!1!G | !3!^G!1!A!3!^A!1!B!2!c B _B A | _A G _G F E _E D _D | C4 z4 |]
""", "Subiendo: dedo 3 en las teclas negras, dedo 1 en las blancas y, si hay dos blancas seguidas (Mi–Fa, Si–Do), la segunda con el 2. Bajando se aplica la misma regla.")

pieza("armonizar_do", "Los siete acordes de Do mayor", """
X:39
T:Armonizar la escala
C:Una tríada sobre cada grado, con la fundamental en el bajo
M:4/4
L:1/4
Q:1/4=60
""" + GRAN + """K:C
[V:RH] "C"[CEG]2 "Dm"[DFA]2 | "Em"[EGB]2 "F"[FAc]2 | "G"[GBd]2 "Am"[Ace]2 | "Bdim"[Bdf]2 "C"[ceg]2 |]
[V:LH] "_I"C,2 "_ii"D,2 | "_iii"E,2 "_IV"F,2 | "_V"G,2 "_vi"A,2 | "_vii°"B,2 "_I"C2 |]
""", "Tres mayores (I, IV, V), tres menores (ii, iii, vi) y un disminuido (vii°): el mismo reparto en todas las tonalidades mayores.")

pieza("sus_slash", "Acordes sus y acordes con otro bajo", """
X:40
T:Sus2, sus4 y bajos distintos
C:Ejercicio original del curso
M:4/4
L:1/4
Q:1/4=60
""" + GRAN + """K:C
[V:RH] "Csus2"[CDG]2 "C"[CEG]2 | "Csus4"[CFG]2 "C"[CEG]2 | "C"[CEG]2 "C/E"[CEG]2 | "C/G"[CEG]2 "C"[CEG]2 |]
[V:LH] C,2 C,2 | C,2 C,2 | C,2 E,2 | G,,2 C,2 |]
""", "En sus2 y sus4 la tercera se sustituye por la 2.ª o la 4.ª: el acorde queda «en suspenso». En C/E o C/G solo cambia la nota del bajo.")

pieza("progresiones", "Dos progresiones muy usadas", """
X:41
T:I–V–vi–IV y I–vi–IV–V
C:Ejercicio original del curso
M:4/4
L:1/4
Q:1/4=76
""" + GRAN + """K:C
[V:RH] "^I – V – vi – IV""C"[EGc]2 [EGc]2 | "G"[DGB]2 [DGB]2 | "Am"[CEA]2 [CEA]2 | "F"[CFA]2 [CFA]2 || "^I – vi – IV – V""C"[EGc]2 [EGc]2 | "Am"[CEA]2 [CEA]2 | "F"[CFA]2 [CFA]2 | "G"[DGB]2 [DGB]2 |]
[V:LH] C,2 G,2 | G,,2 D,2 | A,,2 E,2 | F,,2 C,2 || C,2 G,2 | A,,2 E,2 | F,,2 C,2 | G,,2 D,2 |]
""", "Las posiciones de los acordes de la mano derecha están elegidas para que la mano se mueva lo menos posible. Con estas dos progresiones se acompañan cientos de canciones.")

pieza("canon_prog", "La progresión del «Canon» de Pachelbel, en Do", """
X:42
T:I–V–vi–iii–IV–I–IV–V
C:Basada en la progresión del Canon de J. Pachelbel (siglo XVII, dominio público)
M:4/4
L:1/4
Q:1/4=66
""" + GRAN + """K:C
[V:RH] "C"[EGc]2 [EGc]2 | "G"[DGB]2 [DGB]2 | "Am"[CEA]2 [CEA]2 | "Em"[B,EG]2 [B,EG]2 | "F"[CFA]2 [CFA]2 | "C"[EGc]2 [EGc]2 | "F"[CFA]2 [CFA]2 | "G"[DGB]2 [DGB]2 |]
[V:LH] C,4 | G,,4 | A,,4 | E,4 | F,,4 | C,4 | F,,4 | G,,4 |]
""", "El bajo desciende casi por grados (Do, Sol, La, Mi, Fa, Do, Fa, Sol). Ha servido de base a canciones de casi todos los estilos.")

pieza("periodo", "Un periodo: antecedente y consecuente", """
X:43
T:Pregunta y respuesta
C:Ejercicio original del curso
M:4/4
L:1/4
Q:1/4=88
""" + GRAN + """K:C
[V:RH] "^antecedente""C"E2 G2 | "F"A2 F2 | "C"E C D E | "G7"D4 || "^consecuente""C"E2 G2 | "F"A2 F2 | "G7"D F E D | "C"C4 |]
[V:LH] C,2 G,2 | F,,2 C,2 | C,2 G,,2 | G,,2 D,2 || C,2 G,2 | F,,2 C,2 | G,,2 D,2 | C,4 |]
""", "Las dos frases empiezan igual. La primera termina en el V (semicadencia, «pregunta») y la segunda en el I (cadencia perfecta, «respuesta»).")

pieza("forma_aba", "Forma ternaria A–B–A", """
X:44
T:Forma ternaria
C:Ejercicio original del curso
M:4/4
L:1/4
Q:1/4=88
""" + GRAN + """K:C
[V:RH] "^A""C"E2 G2 | "F"A2 G2 | "G7"F E D F | "C"E4 || "^B""G"D2 G2 | "C"E2 G2 | "D7"^F2 A2 | "G"G4 || "^A""C"E2 G2 | "F"A2 G2 | "G7"F E D F | "C"C4 |]
[V:LH] C,2 G,2 | F,,2 C,2 | G,,2 D,2 | C,4 || G,,2 D,2 | C,2 G,,2 | D,2 A,,2 | G,,4 || C,2 G,2 | F,,2 C,2 | G,,2 D,2 | C,4 |]
""", "A está en Do mayor, B en Sol mayor (hay un Fa♯) y A vuelve con un final distinto que termina en la tónica.")

pieza("iivi_menor", "ii–V–i en La menor", """
X:45
T:ii–V–i en tonalidad menor
C:Ejercicio original del curso · 3.ª y 7.ª de cada acorde
M:4/4
L:1/1
Q:1/4=60
""" + GRAN + """K:Am
[V:RH] "Bm7b5"[DA] | "E7"[D^G] | "Am7"[CG] | "Am"[CEA] |]
[V:LH] B,, | E,, | A,, | A,, |]
""", "El ii es un acorde semidisminuido (Bø7). Fíjate en cómo se mueven las dos notas de arriba: D→D→C y A→G♯→G, y en el G♯ de la dominante, la sensible de La menor.")

pieza("dinamicas", "Dinámica y articulación en una sola frase", """
X:46
T:Matices
C:p, crescendo, f, staccato, diminuendo, acentos, tenuto y calderón
M:4/4
L:1/4
Q:1/4=84
K:C clef=treble
"^p, ligado"!p!(C D E F) | "^crescendo"!crescendo(!(G A B c) | "^f, staccato"!crescendo)!!f!.c .B .A .G | "^diminuendo"!diminuendo(!.F .E .D !diminuendo)!.C |
"^acentos"!>!E E !>!E E | "^tenuto"!tenuto!G !tenuto!G !tenuto!G !tenuto!G | "^calderón"!fermata!c4 |]
""", "El signo de las letras es la dinámica (p, f); las líneas abiertas y cerradas, el crescendo y el diminuendo; el punto, el staccato; la raya, el tenuto; el calderón alarga la nota.")

# ---------------------------------------------------------------------------------------------
# Ejercicios prácticos
# ---------------------------------------------------------------------------------------------
pieza("ej_5dedos", "A1 · Cinco dedos en Do", """
X:47
T:Posición de cinco dedos
C:Ligado, staccato y con acentos
M:4/4
L:1/8
Q:1/4=80
""" + GRAN + """K:C
[V:RH] !1!C!2!D!3!E!4!F !5!G!4!F!3!E!2!D | !1!.C!2!.D!3!.E!4!.F !5!.G!4!.F!3!.E!2!.D | !>!C D E F !>!G F E D | C4 z4 |]
[V:LH] !5!C,!4!D,!3!E,!2!F, !1!G,!2!F,!3!E,!4!D, | !5!.C,!4!.D,!3!.E,!2!.F, !1!.G,!2!.F,!3!.E,!4!.D, | !>!C, D, E, F, !>!G, F, E, D, | C,4 z4 |]
""", "Cada mano sola en el primer compás y luego juntas. Los dedos «caen» desde la yema, con la mano redondeada, sin levantarlos demasiado.")

pieza("ej_pulgar", "A3 · Paso del pulgar en grupos de tres", """
X:48
T:Paso del pulgar
C:Dedos 1-2-3 subiendo y 3-2-1 bajando
M:6/8
L:1/8
Q:3/8=60
""" + GRAN + """K:C
[V:RH] !1!C!2!D!3!E !1!F!2!G!3!A | !1!B!2!c!3!d !1!e!2!f!3!g | !3!g!2!f!1!e !3!d!2!c!1!B | !3!A!2!G!1!F !3!E!2!D!1!C |]
[V:LH] !3!C,!2!D,!1!E, !3!F,!2!G,!1!A, | !3!B,!2!C!1!D !3!E!2!F!1!G | !1!G!2!F!3!E !1!D!2!C!3!B, | !1!A,!2!G,!3!F, !1!E,!2!D,!3!C, |]
""", "El pulgar pasa por debajo (derecha subiendo e izquierda bajando) o el tercer dedo pasa por encima (al revés). Sin sacudir el codo y sin acentos.")

pieza("ej_ritmos_escala", "B1 · La escala de Do con ritmos", """
X:49
T:Escala con ritmos
C:Largo-corto, corto-largo y tresillos
M:4/4
L:1/8
Q:1/4=66
K:C clef=treble
!1!C3!2!D !3!E3!1!F | !2!G3!3!A !4!B3!5!c | !1!C!2!D3 !3!E!1!F3 | !2!G!3!A3 !4!B!5!c3 | (3CDE (3FGA (3Bcd (3efg | c'8 |]
""", "Los ritmos con puntillo y los tresillos igualan los dedos: los largos dan tiempo a preparar la mano y los cortos obligan a ser rápidos y ligeros.")

pieza("ej_arpegios_tres", "B3 · Arpegios de Do, Sol y Fa", """
X:50
T:Arpegios en tres tonalidades
C:Una octava, subiendo y bajando
M:4/4
L:1/8
Q:1/4=60
""" + GRAN + """K:C
[V:RH] "C"!1!C!2!E!3!G!5!c !3!G!2!E!1!C2 | "G"!1!G!2!B!3!d!5!g !3!d!2!B!1!G2 | "F"!1!F!2!A!3!c!5!f !3!c!2!A!1!F2 | "C"[CEGc]8 |]
[V:LH] !5!C,!3!E,!2!G,!1!C !2!G,!3!E,!5!C,2 | !5!G,,!3!B,,!2!D,!1!G, !2!D,!3!B,,!5!G,,2 | !5!F,,!3!A,,!2!C,!1!F, !2!C,!3!A,,!5!F,,2 | [C,E,G,C]8 |]
""", "Haz el movimiento del brazo, no de los dedos: el codo y el antebrazo acompañan a la mano, el pulgar no se estira.")

pieza("ej_lectura1", "C1 · Lectura a primera vista, nivel 1", """
X:51
T:Lectura 1 · notas vecinas y terceras
C:Do mayor · 4/4 · posición de cinco dedos
M:4/4
L:1/4
Q:1/4=72
""" + GRAN + """K:C
[V:RH] E F G E | F E D2 | E G c G | E D C2 | D F A F | E G E C | D E F D | C4 |]
[V:LH] C,2 G,,2 | C,2 G,,2 | C,2 E,2 | G,,2 C,2 | D,2 F,2 | C,2 E,2 | G,,2 G,,2 | C,4 |]
""", "Antes de tocar, mira la armadura, el compás y la nota de la que parte cada mano. Toca sin parar, aunque falles.")

pieza("ej_lectura2", "C2 · Lectura a primera vista, nivel 2", """
X:52
T:Lectura 2 · Sol mayor, 3/4 y ritmo con puntillo
C:Sol mayor · 3/4 · un Fa♯
M:3/4
L:1/4
Q:1/4=88
""" + GRAN + """K:G
[V:RH] G2 B | d>c B | c2 A | B3 | G2 B | d2 g | f2 d | g3 |]
[V:LH] G,,3 | G,,3 | D,3 | G,,3 | G,,3 | C,3 | D,3 | G,,3 |]
""", "El Fa de la armadura es Fa♯ (aparece en el compás 7). El ritmo «largo-corto» del compás 2 es una corchea con puntillo y una semicorchea: cuéntalo en voz alta.")

pieza("ej_lectura3", "C3 · Lectura a primera vista, nivel 3", """
X:53
T:Lectura 3 · Fa mayor y 6/8
C:Fa mayor · 6/8 · un Si♭
M:6/8
L:1/8
Q:3/8=60
""" + GRAN + """K:F
[V:RH] F2 A c2 A | B2 d c3 | A2 c f2 c | A2 G F3 | G2 B d2 B | c2 e g2 e | f2 c A2 G | F6 |]
[V:LH] F,,3 C,3 | B,,3 F,,3 | F,,3 C,3 | C,3 F,,3 | C,3 G,,3 | C,3 C,3 | F,,3 C,3 | F,,6 |]
""", "Seis corcheas por compás, sentidas en dos pulsos. El Si♭ de la armadura afecta a todos los Si.")

pieza("ej_saltos", "C6 · Saltos de tercera, cuarta, quinta, sexta, séptima y octava", """
X:54
T:Saltos desde Do
C:Mira el intervalo antes de tocarlo y prepara el dedo
M:4/4
L:1/4
Q:1/4=72
""" + GRAN + """K:C
[V:RH] !1!C "^3.ª"!3!E !1!C "^4.ª"!4!F | !1!C "^5.ª"!5!G !1!C "^6.ª"!5!A | !1!C "^7.ª"!5!B !1!C "^8.ª"!5!c | !1!C4 |]
[V:LH] C,4 | C,4 | C,4 | C,4 |]
""", "Antes de saltar, la mano ya debe estar sobre la tecla de destino. Mira la nota que va a sonar, no la que acabas de tocar.")

pieza("ej_intervalos", "Terceras en la derecha y quintas en la izquierda", """
X:55
T:Intervalos en bloque
C:Terceras subiendo y bajando por la escala de Do
M:4/4
L:1/4
Q:1/4=66
""" + GRAN + """K:C
[V:RH] [CE] [DF] [EG] [FA] | [GB] [FA] [EG] [DF] | [CE]4 |]
[V:LH] [C,G,] [D,A,] [E,B,] [F,C] | [G,D] [F,C] [E,B,] [D,A,] | [C,G,]4 |]
""", "Las dos notas de cada intervalo se tocan a la vez y con el mismo peso. Comprueba que no suena una más fuerte que la otra.")

pieza("ej_sincopas", "D1 · Síncopas con las dos manos", """
X:56
T:Síncopas
C:La izquierda va firme y la derecha se desplaza
M:4/4
L:1/8
Q:1/4=72
""" + GRAN + """K:C
[V:RH] "^recto"c2 c2 c2 c2 | "^síncopa"c c2 c2 c2 c | "^síncopa"z c c2 z c c2 | c4 z4 |]
[V:LH] C,2 G,2 C,2 G,2 | C,2 G,2 C,2 G,2 | C,2 G,2 C,2 G,2 | C,4 z4 |]
""", "Cuenta «1-y-2-y-3-y-4-y» en voz alta. Las notas de la derecha que caen en la «y» son las síncopas.")

pieza("ej_independencia", "D2 · Ostinato en la izquierda y melodía en la derecha", """
X:57
T:Ostinato
C:Mano izquierda p, derecha mf
M:4/4
L:1/8
Q:1/4=72
""" + GRAN + """K:C
[V:RH] !mf!"C"e4 g4 | "Am"e4 c4 | "F"a4 f4 | "G"d4 B4 | "C"e4 g4 | "Am"c'4 a4 | "F"f4 c4 | "G"d4 B4 | "C"[ceg]8 |]
[V:LH] !p!C,G,E,G, C,G,E,G, | A,,E,C,E, A,,E,C,E, | F,,C,A,,C, F,,C,A,,C, | G,,D,B,D, G,,D,B,D, | C,G,E,G, C,G,E,G, | A,,E,C,E, A,,E,C,E, | F,,C,A,,C, F,,C,A,,C, | G,,D,B,D, G,,D,B,D, | C,8 |]
""", "El dibujo de la izquierda (fundamental, quinta, tercera, quinta) se repite en cada acorde y debe salir «solo». La melodía canta por encima.")

pieza("ej_pentatonica", "F1 · Improvisar con la pentatónica", """
X:58
T:Pregunta y respuesta con la pentatónica
C:Ejemplo para copiar y variar
M:4/4
L:1/4
Q:1/4=84
""" + GRAN + """K:C
[V:RH] "^pregunta"C E G A | G E D2 | "^respuesta"E G A c | G E C2 |]
[V:LH] C,2 G,2 | C,2 G,2 | A,,2 E,2 | C,2 G,2 |]
""", "Toca esta frase y después invéntate otra con las mismas cinco notas: cambia el orden y el ritmo, pero empieza y termina en Do.")

pieza("ej_transporte", "E8 · La misma melodía en Do, Sol y Fa", """
X:59
T:Transporte
C:Misma música, tres tonalidades
% sin-ajuste
M:4/4
L:1/4
Q:1/4=88
K:C clef=treble
"^Do mayor""C"C E G E | "F"F A F D | "C"E G c G | "C"E C C2 |
K:G
"^Sol mayor""G"G B d B | "C"c e c A | "G"B d g d | "G"B G G2 |
K:F
"^Fa mayor""F"F A c A | "Bb"B d B G | "F"A c f c | "F"A F F2 |]
""", "Los grados no cambian: I–IV–I–I en las tres. Cambian las notas y las armaduras. Al leer, mira siempre la armadura.")

pieza("ej_cadencia_lam", "E5 · Cadencia i–iv–V7–i en La menor", """
X:60
T:Cadencia en menor
C:Ejercicio original del curso
M:4/4
L:1/4
Q:1/4=60
""" + GRAN + """K:Am
[V:RH] "Am"[CEA]2 "Dm"[DFA]2 | "E7"[D^GB]2 "Am"[CEA]2 |]
[V:LH] A,,2 D,2 | E,2 A,,2 |]
""", "Compáralo con la cadencia en Do mayor: aquí el acorde de dominante lleva el Sol♯ (la sensible) como alteración.")

pieza("ej_septimas", "E6 · Arpegios de séptima: Cmaj7, Dm7, G7", """
X:61
T:Arpegios de acordes de cuatro notas
C:Ejercicio original del curso
M:4/4
L:1/8
Q:1/4=66
""" + GRAN + """K:C
[V:RH] "Cmaj7"C E G B c B G E | "Dm7"D F A c d c A F | "G7"G B d f g f d B | "Cmaj7"[CEGB]8 |]
[V:LH] C,8 | D,8 | G,,8 | C,8 |]
""", "Cuatro notas por acorde: sube y baja el arpegio y para en la última, con las cuatro notas a la vez. Escucha cómo cambia el color del Cmaj7 al G7.")
