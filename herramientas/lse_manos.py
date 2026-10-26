"""Dibujo de manos en SVG a partir de un modelo 3D sencillo (mano derecha, vista por el interlocutor).

Cada dedo es una cadena de tres falanges con flexión en cada articulación; el pulgar se orienta segmento a segmento.
La mano se gira entera (orientación) y se proyecta en ortográfica. Las piezas se ordenan por profundidad y se pintan
con un degradado que les da volumen; se añaden uñas, pliegues y líneas de la palma cuando quedan a la vista.

Ejes de la mano: x hacia el pulgar, y hacia los dedos, z saliendo de la palma (hacia quien mira en la postura neutra).
"""
import math

PIEL, LUZ, SOMBRA, LINEA, UNA = "#f2c9a7", "#fbe3cf", "#d79f7c", "#8b5a3f", "#f7e1d6"

# Dedos: base del nudillo (x, y), longitudes de las falanges y radio en la base y en la punta.
DEDOS = {
    "i": ((2.75, 9.4), (4.3, 2.5, 2.1), 0.92, 0.74),
    "m": ((0.9, 9.75), (4.8, 2.9, 2.2), 0.95, 0.76),
    "a": ((-0.95, 9.45), (4.4, 2.7, 2.1), 0.9, 0.72),
    "p": ((-2.75, 8.75), (3.5, 2.0, 1.85), 0.8, 0.64),
}
ABRE = {"i": 7, "m": 1, "a": -5, "p": -12}   # separación natural (grados, + hacia el pulgar)
FORMAS = {  # flexión de nudillo, articulación media y punta (grados)
    "e": (0, 0, 0), "c": (28, 40, 25), "o": (42, 62, 35), "f": (88, 105, 55), "b": (85, 8, 5),
    "g": (12, 92, 62), "h": (70, 92, 40), "s": (12, 6, 3), "d": (55, 92, 50),
}
PULGARES = {  # cada segmento: (ángulo en el plano desde y hacia x, elevación hacia z, longitud)
    "lado": ((18, 18, 4.2), (4, 24, 3.0), (-2, 14, 2.4)),
    "palma": ((22, 34, 4.2), (-62, 34, 2.9), (-100, 12, 2.3)),
    "fuera": ((48, 8, 4.0), (70, 6, 3.0), (78, 2, 2.4)),
    "arriba": ((22, 10, 4.2), (14, 8, 3.0), (8, 4, 2.4)),
    "cruzado": ((10, 38, 4.4), (-42, 46, 3.0), (-98, 8, 2.4)),
    "bajo": ((24, 30, 4.0), (-48, 30, 2.8), (-88, 8, 2.3)),
    "pinza": ((32, 40, 4.0), (8, 62, 2.8), (-14, 70, 2.3)),
    "c": ((25, 55, 4.0), (10, 70, 2.9), (0, 72, 2.3)),
    "k": ((14, 34, 4.3), (-6, 40, 3.0), (-22, 32, 2.4)),
    "t": ((12, 40, 4.3), (-24, 52, 2.9), (-58, 28, 2.2)),
    "anular": ((18, 38, 4.3), (-44, 46, 3.0), (-82, 22, 2.4)),
}
CMC = (2.6, 2.3, -0.9)
GROSOR = 2.3


def _v(*a):
    return list(a)


def _suma(a, b, k=1.0):
    return [a[0] + k * b[0], a[1] + k * b[1], a[2] + k * b[2]]


def _norm(a):
    n = math.sqrt(sum(x * x for x in a)) or 1.0
    return [x / n for x in a]


def _rot(o):
    """Matriz de giro: primero en y (mostrar el canto), luego en x (inclinar) y luego en z (girar en el plano)."""
    ry, rx, rz = (math.radians(o.get(k, 0)) for k in ("ry", "rx", "rz"))
    cy, sy, cx, sx, cz, sz = math.cos(ry), math.sin(ry), math.cos(rx), math.sin(rx), math.cos(rz), math.sin(rz)
    Ry = [[cy, 0, sy], [0, 1, 0], [-sy, 0, cy]]
    Rx = [[1, 0, 0], [0, cx, -sx], [0, sx, cx]]
    Rz = [[cz, -sz, 0], [sz, cz, 0], [0, 0, 1]]

    def mul(A, B):
        return [[sum(A[i][k] * B[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
    M = mul(Rz, mul(Rx, Ry))
    return lambda p: [sum(M[i][k] * p[k] for k in range(3)) for i in range(3)]


def _dir(az, el):
    a, e = math.radians(az), math.radians(el)
    return [math.sin(a) * math.cos(e), math.cos(a) * math.cos(e), math.sin(e)]


def _hull(pts):
    pts = sorted(set((round(x, 3), round(y, 3)) for x, y in pts))
    if len(pts) < 3:
        return pts

    def cr(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
    lo, up = [], []
    for p in pts:
        while len(lo) >= 2 and cr(lo[-2], lo[-1], p) <= 0:
            lo.pop()
        lo.append(p)
    for p in reversed(pts):
        while len(up) >= 2 and cr(up[-2], up[-1], p) <= 0:
            up.pop()
        up.append(p)
    return lo[:-1] + up[:-1]


def _circ(c, r, n=28):
    return [(c[0] + r * math.cos(2 * math.pi * k / n), c[1] + r * math.sin(2 * math.pi * k / n)) for k in range(n)]


_CONTADOR = [0]


class _Lienzo:
    def __init__(self, esc, cx, cy):
        _CONTADOR[0] += 1
        self.pre = f"h{_CONTADOR[0]}"
        self.esc, self.cx, self.cy = esc, cx, cy
        self.piezas, self.defs, self.n, self.puntos = [], [], 0, []

    def p2(self, p):
        return (self.cx + p[0] * self.esc, self.cy - p[1] * self.esc)

    def grad(self, a, b, r):
        """Degradado perpendicular al eje a-b: claro hacia arriba a la izquierda, oscuro al otro lado."""
        dx, dy = b[0] - a[0], b[1] - a[1]
        L = math.hypot(dx, dy) or 1
        nx, ny = -dy / L, dx / L
        if nx + ny > 0:
            nx, ny = -nx, -ny
        mx, my = (a[0] + b[0]) / 2, (a[1] + b[1]) / 2
        self.n += 1
        gid = f"{self.pre}g{self.n}"
        self.defs.append(f'<linearGradient id="{gid}" gradientUnits="userSpaceOnUse" x1="{mx+nx*r:.1f}" y1="{my+ny*r:.1f}" x2="{mx-nx*r:.1f}" y2="{my-ny*r:.1f}">'
                         f'<stop offset="0" stop-color="{LUZ}"/><stop offset=".45" stop-color="{PIEL}"/><stop offset="1" stop-color="{SOMBRA}"/></linearGradient>')
        return gid

    def poligono(self, pts, fill, registrar=True):
        if registrar:
            self.puntos.extend(pts)
        d = "M" + " L".join(f"{x:.1f} {y:.1f}" for x, y in pts) + " Z"
        return f'<path d="{d}" fill="{fill}" stroke="{LINEA}" stroke-width="1.3" stroke-linejoin="round" vector-effect="non-scaling-stroke"/>'


def _cadena(segs):
    p, pts = list(CMC), [list(CMC)]
    for az, el, lg in segs:
        p = _suma(p, _dir(az, el), lg)
        pts.append(p)
    return pts


def _ajusta_pulgar(segs, toca, art, hueco=1.35):
    """Busca la postura del pulgar más parecida a la de partida cuya punta toque el punto indicado.

    toca: "i" (punta del índice), ("m", 2) (articulación 2 del corazón) o una lista de ellos (punto medio)."""
    objetivos = toca if isinstance(toca, list) else [toca]
    pts = []
    for o in objetivos:
        k, j = (o, 3) if isinstance(o, str) else o
        pts.append(art[k][j])
    obj = [sum(p[i] for p in pts) / len(pts) for i in range(3)]
    base = [list(s) for s in segs]

    def coste(x):
        sg = [(x[2 * j], x[2 * j + 1], base[j][2]) for j in range(3)]
        cad = _cadena(sg)
        d = math.dist(cad[-1], obj)
        c = (d - hueco) ** 2 * 10
        for p in cad[1:]:
            if -3.9 < p[0] < 3.9 and 0.3 < p[1] < 10 and p[2] < 0.95:   # no atravesar la palma
                c += (0.95 - p[2]) ** 2 * 30
        for j in range(3):
            c += 0.0006 * ((x[2 * j] - base[j][0]) ** 2 + (x[2 * j + 1] - base[j][1]) ** 2)
        for j in (1, 2):   # articulaciones del pulgar: giros moderados
            c += 0.0004 * max(0, abs(x[2 * j] - x[2 * j - 2]) - 60) ** 2
        return c
    x = [v for s in base for v in s[:2]]
    mejor = coste(x)
    for paso in (24, 12, 6, 3, 1.5, 0.75):
        mejoro = True
        while mejoro:
            mejoro = False
            for i in range(6):
                for sg in (1, -1):
                    y = list(x)
                    y[i] += sg * paso
                    c = coste(y)
                    if c < mejor - 1e-9:
                        x, mejor, mejoro = y, c, True
    return [(x[2 * j], x[2 * j + 1], base[j][2]) for j in range(3)]


def mano(pose, tam=200, etiqueta=None, flecha=None):
    """Devuelve un SVG con la mano en la postura indicada.

    pose: {"i": "e", "m": "f", ..., "pulgar": "lado", "abre": {"i": 10}, "flex": {"m": (a, b, c)}, "ry":…, "rx":…, "rz":…}
    flecha: None | "J" | "Z" | "onda" (movimiento de la letra).
    """
    R = _rot(pose)
    esc = 10.0
    L = _Lienzo(esc, 0, 0)
    piezas = []  # (profundidad, svg)

    def capsula(a3, b3, ra, rb, prof_extra=0.0, detalle=None):
        a, b = R(a3), R(b3)
        A, B = L.p2(a), L.p2(b)
        pts = _hull(_circ(A, ra * esc) + _circ(B, rb * esc))
        gid = L.grad(A, B, max(ra, rb) * esc)
        svg = L.poligono(pts, f"url(#{gid})") + (detalle(a, b, A, B) if detalle else "")
        piezas.append(((a[2] + b[2]) / 2 + prof_extra, svg))

    # Antebrazo (siempre detrás)
    sec = []   # antebrazo con sección elíptica (más ancho que grueso)
    for y, rx_, rz_ in ((0.8, 2.9, 1.35), (-3, 3.1, 1.6), (-14, 3.3, 1.8)):
        for k in range(24):
            t = 2 * math.pi * k / 24
            sec.append(L.p2(R(_v(rx_ * math.cos(t) - 0.1, y, -GROSOR / 2 + rz_ * math.sin(t)))))
    A, B = L.p2(R(_v(0, 0.6, -GROSOR / 2))), L.p2(R(_v(0, -14, -GROSOR / 2)))
    gid = L.grad(A, B, 3.0 * esc)
    antebrazo = L.poligono(_hull(sec), f"url(#{gid})", registrar=False)

    # Palma: casco convexo de su contorno por delante y por detrás
    cont = [(-2.9, 0.2), (-3.5, 3), (-3.9, 6), (-3.8, 8.6), (-2.2, 9.6), (0.9, 10.1), (2.9, 9.8), (3.7, 8.4), (3.6, 5.5), (3.2, 2.6), (2.6, 0.2)]
    pal = []
    for t in (0, 0.2, 0.5, 0.8, 1):        # sección redondeada: el contorno se estrecha hacia las caras
        enc = 1 - 0.09 * (1 - math.sin(math.pi * t))
        for x, y in cont:
            pal.append(L.p2(R(_v(x * enc, 5 + (y - 5) * (1 - 0.04 * (1 - math.sin(math.pi * t))), -GROSOR * t))))
    c0 = L.p2(R(_v(0.8, 6.2, 0)))
    L.n += 1
    gid2 = f"{L.pre}g{L.n}"
    L.defs.append(f'<radialGradient id="{gid2}" gradientUnits="userSpaceOnUse" cx="{c0[0]-1.5*esc:.1f}" cy="{c0[1]-1.5*esc:.1f}" r="{7.5*esc:.1f}">'
                  f'<stop offset="0" stop-color="{LUZ}"/><stop offset=".55" stop-color="{PIEL}"/><stop offset="1" stop-color="{SOMBRA}"/></radialGradient>')
    frente = R(_v(0, 0, 1))[2]   # >0: se ve la palma; <0: se ve el dorso
    palma_svg = L.poligono(_hull(pal), f"url(#{gid2})")
    if frente > 0.25:   # líneas de la palma
        op = min(1, (frente - 0.25) * 1.6)
        lineas = [[(-3.6, 7.5), (-1.5, 7.9), (0.8, 7.9), (2.4, 8.3)], [(3.5, 6.6), (1.5, 5.9), (-0.8, 5.4), (-2.6, 4.6)],
                  [(3.3, 6.4), (1.8, 4.8), (1.4, 3.0), (1.7, 1.0)]]
        for ln in lineas:
            q = [L.p2(R(_v(x, y, 0.02))) for x, y in ln]
            d = f"M{q[0][0]:.1f} {q[0][1]:.1f} C{q[1][0]:.1f} {q[1][1]:.1f} {q[2][0]:.1f} {q[2][1]:.1f} {q[3][0]:.1f} {q[3][1]:.1f}"
            palma_svg += f'<path d="{d}" fill="none" stroke="{SOMBRA}" stroke-width="1.4" stroke-linecap="round" vector-effect="non-scaling-stroke" opacity="{op:.2f}"/>'
    elif frente < -0.25:   # nudillos en el dorso
        for k, (bx, by) in ((k, DEDOS[k][0]) for k in "imap"):
            q = L.p2(R(_v(bx, by - 0.4, -GROSOR - 0.05)))
            palma_svg += f'<ellipse cx="{q[0]:.1f}" cy="{q[1]:.1f}" rx="{0.45*esc:.1f}" ry="{0.3*esc:.1f}" fill="{LUZ}" opacity=".7"/>'
    piezas.append((R(_v(0, 5, -GROSOR / 2))[2], palma_svg))
    # Eminencia tenar (base del pulgar)
    capsula(_v(1.6, 0.9, -0.7), _suma(CMC, [0.3, 1.2, 0.2]), 1.9, 1.55, prof_extra=0.15)

    def detalle_dedo(dorso, palmar, ultima):
        def f(a, b, A, B):
            s = ""
            dz = R(dorso)[2]
            if ultima and dz > 0.15:   # uña
                t = 0.72
                c = (A[0] + (B[0] - A[0]) * t, A[1] + (B[1] - A[1]) * t)
                ang = math.degrees(math.atan2(B[1] - A[1], B[0] - A[0]))
                largo = math.hypot(B[0] - A[0], B[1] - A[1]) * 0.42 + 0.25 * esc
                s += (f'<ellipse cx="{c[0]:.1f}" cy="{c[1]:.1f}" rx="{max(largo, 0.3*esc):.1f}" ry="{0.46*esc*min(1, dz+0.3):.1f}" '
                      f'transform="rotate({ang:.1f} {c[0]:.1f} {c[1]:.1f})" fill="{UNA}" stroke="{LINEA}" stroke-width=".9" vector-effect="non-scaling-stroke" opacity="{min(1, dz*1.6):.2f}"/>')
            pz = R(palmar)[2]
            if not ultima and pz > 0.3 and math.hypot(B[0] - A[0], B[1] - A[1]) > 1.2 * esc:   # pliegue de la articulación
                ux, uy = (B[0] - A[0]), (B[1] - A[1])
                n = math.hypot(ux, uy)
                ux, uy = ux / n, uy / n
                cx, cy = B[0] - ux * 0.15 * esc, B[1] - uy * 0.15 * esc
                w = 0.5 * esc
                s += f'<path d="M{cx-uy*w:.1f} {cy+ux*w:.1f} L{cx+uy*w:.1f} {cy-ux*w:.1f}" stroke="{SOMBRA}" stroke-width="1.1" stroke-linecap="round" vector-effect="non-scaling-stroke" opacity=".8"/>'
            return s
        return f

    # Dedos largos
    articulaciones = {}
    for k, ((bx, by), largos, r0, r1) in DEDOS.items():
        forma = pose.get(k, "e")
        flex = pose.get("flex", {}).get(k, FORMAS[forma])
        ab = math.radians(pose.get("abre", {}).get(k, ABRE[k] * (0.35 if forma in "fbd" else 1)))
        u = [math.sin(ab), math.cos(ab), 0]
        n = [0, 0, 1]
        p = _v(bx, by - 0.5, -GROSOR / 2 + 0.15)
        f = 0.0
        radios = [r0, r0 * 0.92 + r1 * 0.08, (r0 + r1) / 2, r1]
        articulaciones[k] = [p]
        for j in range(3):
            f += math.radians(flex[j])
            d = _suma([x * math.cos(f) for x in u], [x * math.sin(f) for x in n])
            q = _suma(p, d, largos[j])
            dorso = _suma([x * math.sin(f) for x in u], [-x * math.cos(f) for x in n])
            palmar = [-x for x in dorso]
            capsula(p, q, radios[j], radios[j + 1], prof_extra=0.35 + 0.02 * j, detalle=detalle_dedo(dorso, palmar, j == 2))
            p = q
            articulaciones[k].append(q)

    # Pulgar
    segs = PULGARES[pose.get("pulgar", "lado")]
    if "toca" in pose:
        segs = _ajusta_pulgar(segs, pose["toca"], articulaciones, pose.get("hueco", 1.35))
    p = list(CMC)
    rad = [1.25, 1.12, 1.0, 0.86]
    una = pose.get("una_pulgar")
    for j, (az, el, lg) in enumerate(segs):
        d = _dir(az, el)
        q = _suma(p, d, lg)
        if una is None:
            lado = _norm([d[1], -d[0], 0]) if abs(d[2]) < 0.95 else [1, 0, 0]
            dorso = _norm(_suma([x * -0.75 for x in [0, 0, 1]], lado, 0.65))
        else:
            dorso = _norm(una)
        capsula(p, q, rad[j], rad[j + 1], prof_extra=0.4 + 0.02 * j, detalle=detalle_dedo(dorso, [-x for x in dorso], j == 2))
        p = q

    piezas.sort(key=lambda t: t[0])
    cuerpo = antebrazo + "".join(s for _, s in piezas)
    xs = [p[0] for p in L.puntos]
    ys = [p[1] for p in L.puntos]
    k = tam * 0.9 / (22 * esc)          # misma escala para todas las manos
    cx, cy = (min(xs) + max(xs)) / 2, (min(ys) + max(ys)) / 2
    tx, ty = tam / 2 - cx * k, tam / 2 - cy * k + tam * 0.03
    extra = ""
    if flecha:   # movimiento de la letra, en coordenadas finales y dentro del marco
        col = "#f97316"
        dedo = articulaciones["p" if flecha == "J" else "i"][3]
        X, Y = L.p2(R(dedo))
        x = min(max(tx + X * k, tam * 0.22), tam * 0.78)
        y = min(max(ty + Y * k, tam * 0.12), tam * 0.6)
        if flecha == "J":
            d = f"M{x-tam*0.1:.0f} {y:.0f} l0 {tam*0.16:.0f} q0 {tam*0.1:.0f} {-tam*0.1:.0f} {tam*0.08:.0f}"
        elif flecha == "Z":
            w = tam * 0.1
            x, y = min(x + tam * 0.16, tam - w - 8), max(y - tam * 0.02, w + 6)
            d = f"M{x-w:.0f} {y-w:.0f} l{2*w:.0f} 0 l{-2*w:.0f} {w*1.4:.0f} l{2*w:.0f} 0"
        else:
            w = tam * 0.05
            y = max(ty + min(ys) * k - 12, 12)
            d = f"M{x-3*w:.0f} {y:.0f} q{w:.0f} {-w*1.5:.0f} {2*w:.0f} 0 t{2*w:.0f} 0 t{2*w:.0f} 0"
        extra = (f'<path d="{d}" fill="none" stroke="{col}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" '
                 f'stroke-dasharray="6 4" marker-end="url(#{L.pre}fl)"/>')
        L.defs.append(f'<marker id="{L.pre}fl" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="4" markerHeight="4" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 z" fill="{col}"/></marker>')
    alto = tam + (34 if etiqueta else 0)
    et = (f'<text x="{tam/2}" y="{tam+26}" text-anchor="middle" font-family="Segoe UI,Tahoma,sans-serif" font-size="{24 if len(etiqueta) < 3 else 15}" font-weight="700" fill="#0f766e">{etiqueta}</text>'
          if etiqueta else "")
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {tam} {alto}" width="{tam}" height="{alto}" role="img" aria-label="Mano: {etiqueta or "configuración"}">'
            f'<defs>{"".join(L.defs)}</defs><g transform="translate({tx:.1f} {ty:.1f}) scale({k:.4f})">{cuerpo}</g>{extra}{et}</svg>')


# Posturas del alfabeto manual (orientativas) ------------------------------------------------------------------
PUNO = {"i": "f", "m": "f", "a": "f", "p": "f"}
LETRAS = {
    "A": dict(PUNO, pulgar="lado"),
    "B": dict(i="e", m="e", a="e", p="e", pulgar="palma", abre={"i": 2, "m": 0, "a": -2, "p": -4}),
    "C": dict(i="c", m="c", a="c", p="c", pulgar="c", toca="m", hueco=4.2, abre={"i": 2, "m": 0, "a": -2, "p": -4}, ry=62),
    "D": dict(i="e", m="o", a="o", p="o", pulgar="pinza", toca="m", flex={"m": (40, 68, 40), "a": (46, 70, 40), "p": (50, 70, 40)}),
    "E": dict(i="d", m="d", a="d", p="d", pulgar="bajo"),
    "F": dict(i="o", m="e", a="e", p="e", pulgar="pinza", toca="i", abre={"m": 4, "a": -6, "p": -14}),
    "G": dict(PUNO, i="e", pulgar="arriba", rz=-90, ry=-30),
    "H": dict(PUNO, i="e", m="e", pulgar="anular", abre={"i": 2, "m": -1}, rz=-90, ry=-30),
    "I": dict(PUNO, p="e", pulgar="cruzado"),
    "J": dict(PUNO, p="e", pulgar="cruzado"),
    "K": dict(PUNO, i="e", m="e", pulgar="k", toca=("m", 1), abre={"i": 10, "m": -10}, flex={"m": (25, 0, 0)}),
    "L": dict(PUNO, i="e", pulgar="fuera"),
    "M": dict(i="h", m="h", a="h", p="f", pulgar="bajo", ry=-35),
    "N": dict(i="h", m="h", a="f", p="f", pulgar="bajo", ry=-35),
    "Ñ": dict(i="h", m="h", a="f", p="f", pulgar="bajo", ry=-35),
    "O": dict(i="o", m="o", a="o", p="o", pulgar="pinza", toca=["i", "m"], ry=60, flex={"i": (40, 60, 30), "m": (42, 62, 30), "a": (46, 64, 32), "p": (50, 64, 32)}),
    "P": dict(PUNO, i="e", m="e", pulgar="k", toca=("m", 1), abre={"i": 10, "m": -10}, flex={"m": (25, 0, 0)}, rz=180),
    "Q": dict(PUNO, i="e", pulgar="arriba", rz=180, ry=30),
    "R": dict(PUNO, i="e", m="e", pulgar="anular", abre={"i": -6, "m": 17}, flex={"m": (12, 0, 0)}),
    "S": dict(PUNO, pulgar="cruzado"),
    "T": dict(PUNO, pulgar="t"),
    "U": dict(PUNO, i="e", m="e", pulgar="anular", abre={"i": 2, "m": -1}),
    "V": dict(PUNO, i="e", m="e", pulgar="anular", abre={"i": 14, "m": -10}),
    "W": dict(i="e", m="e", a="e", p="f", pulgar="bajo", abre={"i": 16, "m": 1, "a": -14}),
    "X": dict(PUNO, i="g", pulgar="cruzado"),
    "Y": dict(PUNO, p="e", pulgar="fuera", abre={"p": -22}),
    "Z": dict(PUNO, i="e", pulgar="cruzado"),
}
FLECHAS = {"J": "J", "Z": "Z", "Ñ": "onda"}

# Configuraciones básicas (para el esquema del módulo 3)
CONFIGS = [
    ("Mano plana", dict(i="e", m="e", a="e", p="e", pulgar="palma", abre={"i": 2, "m": 0, "a": -2, "p": -4})),
    ("Puño", dict(PUNO, pulgar="cruzado")),
    ("Índice", dict(PUNO, i="e", pulgar="cruzado")),
    ("Mano en C", LETRAS["C"]),
    ("Pinza o círculo", LETRAS["F"]),
    ("Mano en V", LETRAS["V"]),
    ("Mano abierta", dict(i="e", m="e", a="e", p="e", pulgar="fuera", abre={"i": 16, "m": 2, "a": -12, "p": -26})),
    ("Meñique", LETRAS["I"]),
    ("Pulgar", dict(PUNO, pulgar="arriba")),
    ("Cuerno", dict(PUNO, i="e", p="e", pulgar="cruzado", abre={"i": 10, "p": -18})),
]


def letra(l, tam=200, etiqueta=True):
    return mano(LETRAS[l], tam, l if etiqueta else None, FLECHAS.get(l))


def nombre_fichero(l):
    return {"Ñ": "NN"}.get(l, l)


def rejilla(items, cols, tam=180, titulo=None):
    """Compone varias manos (lista de (etiqueta, svg)) en un único SVG."""
    alto1 = tam + 34
    cab = 40 if titulo else 0
    filas = (len(items) + cols - 1) // cols
    W, H = cols * tam, filas * alto1 + cab
    c = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="{titulo or "Manos"}">',
         f'<rect width="{W}" height="{H}" fill="#fff"/>']
    if titulo:
        c.append(f'<text x="{W/2}" y="27" text-anchor="middle" font-family="Segoe UI,Tahoma,sans-serif" font-size="20" font-weight="700" fill="#0f766e">{titulo}</text>')
    for n, (_, svg) in enumerate(items):
        x, y = (n % cols) * tam, cab + (n // cols) * alto1
        c.append(svg.replace("<svg ", f'<svg x="{x}" y="{y}" ', 1))
    c.append("</svg>")
    return "".join(c)
