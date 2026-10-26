"""Dibujos realistas del saxo (SVG): instrumento con sus partes, familia del saxofón y diagramas de digitación.

El tubo se construye a partir de su línea central y su anchura en cada punto (polígono con bordes, brillo y sombra),
de modo que el cono, el cuello y la curva se ven con volumen y con aspecto de latón lacado.
"""
import html
import math

LATON_OSC, LATON, LATON_CLARO, BRILLO = "#8a5a14", "#d4a63a", "#f0d27a", "#fff4c8"
NEGRO, PLATA, PLATA_OSC = "#1d1a18", "#c9ccd1", "#7c8189"
F = 'font-family="Segoe UI,Tahoma,sans-serif"'

DEFS = f"""<defs>
<linearGradient id="sxLaton" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{LATON_OSC}"/><stop offset=".25" stop-color="{LATON}"/>
<stop offset=".45" stop-color="{LATON_CLARO}"/><stop offset=".6" stop-color="{LATON}"/><stop offset="1" stop-color="{LATON_OSC}"/></linearGradient>
<radialGradient id="sxPerla" cx=".35" cy=".3" r=".75"><stop offset="0" stop-color="#ffffff"/><stop offset=".55" stop-color="#f1ece4"/><stop offset="1" stop-color="#cfc6b8"/></radialGradient>
<radialGradient id="sxPerlaOn" cx=".35" cy=".3" r=".75"><stop offset="0" stop-color="#8a5a3c"/><stop offset=".6" stop-color="#4a2c16"/><stop offset="1" stop-color="#24140a"/></radialGradient>
<radialGradient id="sxCazo" cx=".4" cy=".35" r=".7"><stop offset="0" stop-color="{BRILLO}"/><stop offset=".5" stop-color="{LATON}"/><stop offset="1" stop-color="{LATON_OSC}"/></radialGradient>
<linearGradient id="sxBoq" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#4a4540"/><stop offset=".4" stop-color="{NEGRO}"/><stop offset="1" stop-color="#000"/></linearGradient>
<linearGradient id="sxPlata" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f4f5f7"/><stop offset=".5" stop-color="{PLATA}"/><stop offset="1" stop-color="{PLATA_OSC}"/></linearGradient>
<linearGradient id="sxFondo" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fffaf0"/><stop offset="1" stop-color="#f6ecd8"/></linearGradient>
</defs>"""


# ---- Geometría --------------------------------------------------------------------------------------------
def _bez(p0, p1, p2, p3, n=24):
    out = []
    for k in range(n + 1):
        t = k / n
        a, b, c, d = (1 - t) ** 3, 3 * t * (1 - t) ** 2, 3 * t * t * (1 - t), t ** 3
        out.append((a * p0[0] + b * p1[0] + c * p2[0] + d * p3[0], a * p0[1] + b * p1[1] + c * p2[1] + d * p3[1]))
    return out


def _arco(c, r, a0, a1, n=30):
    return [(c[0] + r * math.cos(math.radians(a0 + (a1 - a0) * k / n)), c[1] + r * math.sin(math.radians(a0 + (a1 - a0) * k / n))) for k in range(n + 1)]


def _linea(a, b, n=12):
    return [(a[0] + (b[0] - a[0]) * k / n, a[1] + (b[1] - a[1]) * k / n) for k in range(n + 1)]


def _normales(pts):
    out = []
    for i in range(len(pts)):
        a, b = pts[max(i - 1, 0)], pts[min(i + 1, len(pts) - 1)]
        dx, dy = b[0] - a[0], b[1] - a[1]
        L = math.hypot(dx, dy) or 1
        out.append((-dy / L, dx / L))
    return out


def _d(pts, cerrar=True):
    return "M" + " L".join(f"{x:.1f} {y:.1f}" for x, y in pts) + (" Z" if cerrar else "")


def tubo(centro, anchos, brillo=True):
    """Tubo de latón a partir de su línea central y su anchura en cada punto."""
    nor = _normales(centro)
    izq = [(x + nx * w / 2, y + ny * w / 2) for (x, y), (nx, ny), w in zip(centro, nor, anchos)]
    der = [(x - nx * w / 2, y - ny * w / 2) for (x, y), (nx, ny), w in zip(centro, nor, anchos)]
    s = f'<path d="{_d(izq + der[::-1])}" fill="{LATON}" stroke="{LATON_OSC}" stroke-width="2" stroke-linejoin="round"/>'
    # sombra (lado derecho) y brillo (lado izquierdo): bandas paralelas al eje
    for frac, ancho_rel, color, op in ((-0.3, 0.32, LATON_OSC, .55), (0.18, 0.22, LATON_CLARO, .9), (0.26, 0.07, BRILLO, .95)):
        banda = [(x + nx * w * frac, y + ny * w * frac) for (x, y), (nx, ny), w in zip(centro, nor, anchos)]
        wmed = sum(anchos) / len(anchos) * ancho_rel
        if brillo or color == LATON_OSC:
            s += f'<path d="{_d(banda, False)}" fill="none" stroke="{color}" stroke-width="{wmed:.1f}" stroke-linecap="round" opacity="{op}"/>'
    return s


def _interp(a, b, n):
    return [a + (b - a) * k / (n - 1) for k in range(n)]


# ---- El saxo alto ---------------------------------------------------------------------------------------------
def _saxo(tx=0, ty=0, esc=1.0, llaves=True, cuello="alto"):
    """Saxo de perfil (boquilla arriba a la izquierda, campana a la derecha). Devuelve (svg, puntos de interés)."""
    P = {}
    g = [f'<g transform="translate({tx} {ty}) scale({esc})">']
    # Cuerpo cónico: de (360,165) a (360,445)
    cuerpo = _linea((360, 160), (360, 445), 20)
    g_cuerpo = tubo(cuerpo, _interp(30, 54, len(cuerpo)))
    # Curva en U: semicírculo de la base del cuerpo al tubo de la campana
    curva = _arco((418, 445), 58, 180, 0, 36)[::-1][::-1]
    g_curva = tubo(curva, _interp(54, 64, len(curva)))
    # Tubo de la campana y pabellón
    subida = _linea((476, 445), (480, 268), 18)
    g_subida = tubo(subida, _interp(64, 84, len(subida)))
    # Pabellón (campana abierta, ligeramente inclinada)
    pab_izq = _bez((438, 270), (436, 232), (420, 205), (392, 178), 20)
    pab_der = _bez((522, 266), (530, 228), (556, 200), (590, 186), 20)
    g_pab = (f'<path d="{_d(pab_izq + pab_der[::-1])}" fill="url(#sxLaton)" stroke="{LATON_OSC}" stroke-width="2"/>'
             f'<path d="{_d(_bez((452, 262), (450, 230), (440, 206), (420, 186), 14), False)}" fill="none" stroke="{BRILLO}" stroke-width="6" stroke-linecap="round" opacity=".8"/>')
    # boca de la campana (elipse con borde)
    g_boca = (f'<ellipse cx="491" cy="182" rx="101" ry="20" transform="rotate(5 491 182)" fill="{LATON_OSC}" stroke="{LATON_OSC}" stroke-width="2"/>'
              f'<ellipse cx="491" cy="181" rx="93" ry="14" transform="rotate(5 491 181)" fill="#5a3a0c"/>'
              f'<ellipse cx="491" cy="182" rx="101" ry="20" transform="rotate(5 491 182)" fill="none" stroke="{LATON_CLARO}" stroke-width="5"/>')
    # Cuello (tudel): sube del cuerpo y se curva hacia la izquierda
    if cuello == "alto":
        tud = _bez((360, 166), (360, 110), (336, 78), (290, 72), 24) + _bez((290, 72), (262, 68), (240, 70), (222, 76), 10)[1:]
    else:   # cuello de tenor con su curva en «S»
        tud = _bez((360, 166), (364, 96), (330, 56), (286, 62), 24) + _bez((286, 62), (262, 66), (244, 82), (222, 84), 10)[1:]
    g_tud = tubo(tud, _interp(29, 15, len(tud)))
    # Boquilla, caña y abrazadera
    ang = math.degrees(math.atan2(tud[-1][1] - tud[-2][1], tud[-1][0] - tud[-2][0]))
    bx, by = tud[-1]
    g_boq = (f'<g transform="translate({bx:.1f} {by:.1f}) rotate({ang:.1f})">'
             f'<path d="M-4 -9 L58 -7 Q72 -5 76 0 Q72 5 58 7 L-4 9 Z" fill="url(#sxBoq)" stroke="#000" stroke-width="1"/>'
             f'<path d="M14 7 L70 5 Q74 6 74 8 L14 11 Z" fill="#e9d8a6" stroke="#a88f55" stroke-width="1"/>'
             f'<rect x="14" y="-10.5" width="20" height="22" rx="3" fill="url(#sxPlata)" stroke="{PLATA_OSC}"/>'
             f'<line x1="19" y1="-10" x2="19" y2="11" stroke="{PLATA_OSC}"/><line x1="29" y1="-10" x2="29" y2="11" stroke="{PLATA_OSC}"/>'
             f'<circle cx="24" cy="14" r="3" fill="url(#sxPlata)" stroke="{PLATA_OSC}"/>'
             '</g>')
    def rot(px, py):
        a = math.radians(ang)
        return (bx + px * math.cos(a) - py * math.sin(a), by + px * math.sin(a) + py * math.cos(a))
    P["boquilla"] = rot(58, 0)
    P["cana"] = rot(24, 0)
    P["cuello"] = tud[int(len(tud) * 0.62)]
    P["cuerpo"] = (360, 330)
    P["curva"] = (418, 503)
    P["campana"] = (520, 232)
    g += [g_subida, g_curva, g_cuerpo, g_pab, g_boca, g_tud, g_boq]
    # Abrazadera de unión cuello-cuerpo (tornillo)
    g.append(f'<rect x="343" y="156" width="34" height="13" rx="3" fill="url(#sxLaton)" stroke="{LATON_OSC}"/>'
             f'<circle cx="381" cy="162" r="5" fill="url(#sxCazo)" stroke="{LATON_OSC}"/>')
    if llaves:
        # Varillas a lo largo del cuerpo
        g.append(f'<line x1="336" y1="190" x2="336" y2="430" stroke="{LATON_OSC}" stroke-width="3"/>'
                 f'<line x1="386" y1="190" x2="386" y2="420" stroke="{LATON_OSC}" stroke-width="2.5"/>')
        # Llave de octava en el cuello y su palanca
        g.append(f'<path d="M352 150 Q346 128 330 106 Q326 100 318 98" fill="none" stroke="{LATON_OSC}" stroke-width="3.5" stroke-linecap="round"/>'
                 f'<ellipse cx="318" cy="99" rx="7" ry="5" fill="url(#sxCazo)" stroke="{LATON_OSC}"/>')
        P["octava"] = (330, 108)
        # Botón de octava del pulgar (parte trasera) y apoyo
        g.append(f'<ellipse cx="333" cy="205" rx="9" ry="7" fill="url(#sxPerla)" stroke="{LATON_OSC}" stroke-width="2"/>')
        P["pulgar_oct"] = (333, 205)
        # Cazoletas con zapatillas (laterales) y perlas (teclas de los dedos)
        for y in (220, 252, 284):        # mano izquierda
            g.append(f'<ellipse cx="392" cy="{y}" rx="9" ry="13" fill="url(#sxCazo)" stroke="{LATON_OSC}"/>'
                     f'<circle cx="368" cy="{y}" r="8.5" fill="url(#sxPerla)" stroke="{LATON_OSC}" stroke-width="2.2"/>')
        for y in (330, 362, 394):        # mano derecha
            g.append(f'<ellipse cx="394" cy="{y}" rx="10" ry="14" fill="url(#sxCazo)" stroke="{LATON_OSC}"/>'
                     f'<circle cx="370" cy="{y}" r="9" fill="url(#sxPerla)" stroke="{LATON_OSC}" stroke-width="2.2"/>')
        P["llaves"] = (368, 252)
        # Palmeras (llaves de la palma izquierda) y llaves laterales
        g.append(f'<path d="M346 180 q-10 6 -8 18" fill="none" stroke="{LATON_OSC}" stroke-width="5" stroke-linecap="round"/>'
                 f'<path d="M386 300 l14 0 m-14 10 l14 0" stroke="{LATON_OSC}" stroke-width="4" stroke-linecap="round"/>')
        # Mesa del meñique izquierdo
        g.append(f'<path d="M332 294 q-14 4 -14 16 q0 10 12 10 z" fill="url(#sxLaton)" stroke="{LATON_OSC}"/>')
        # Llaves graves en la campana (grandes cazoletas) y espátulas del meñique derecho
        for cx, cy, r in ((474, 418, 16), (480, 376, 17), (484, 334, 18), (486, 292, 18)):
            g.append(f'<ellipse cx="{cx-28}" cy="{cy}" rx="{r*0.55:.1f}" ry="{r}" fill="url(#sxCazo)" stroke="{LATON_OSC}"/>')
        g.append(f'<path d="M386 416 q22 2 30 16" fill="none" stroke="{LATON_OSC}" stroke-width="6" stroke-linecap="round"/>'
                 f'<path d="M386 432 q18 4 24 18" fill="none" stroke="{LATON_OSC}" stroke-width="6" stroke-linecap="round"/>')
        # Guardallaves (protector de las llaves graves)
        g.append(f'<path d="M500 300 q16 60 0 130" fill="none" stroke="{LATON_CLARO}" stroke-width="3"/>'
                 f'<path d="M500 300 q16 60 0 130" fill="none" stroke="{LATON_OSC}" stroke-width="1" stroke-dasharray="2 6"/>')
        # Apoyo del pulgar derecho y anilla de la correa
        g.append(f'<path d="M334 372 q-14 0 -14 10 q0 8 12 8" fill="none" stroke="{LATON_OSC}" stroke-width="5" stroke-linecap="round"/>'
                 f'<circle cx="329" cy="196" r="5" fill="none" stroke="{LATON_OSC}" stroke-width="3"/>')
        P["pulgar_der"] = (322, 382)
        P["anilla"] = (329, 196)
    g.append("</g>")
    P = {k: (tx + x * esc, ty + y * esc) for k, (x, y) in P.items()}
    return "".join(g), P


PARTES_VB = (-40, 0, 980, 545)   # viewBox del dibujo de las partes


def svg_partes(etiquetas=True, puntos=False):
    """Saxo alto con sus partes. Con puntos=True devuelve además las posiciones (en %) de cada parte."""
    x0, y0, W, H = PARTES_VB
    sax, P = _saxo(90, 10)
    c = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{x0} {y0} {W} {H}" width="{W}" height="{H}" role="img" '
         f'aria-label="Saxo alto con sus partes: boquilla, caña, abrazadera, cuello, cuerpo, llaves, curva, campana y correa" {F}>',
         DEFS, f'<rect x="{x0}" y="{y0}" width="{W}" height="{H}" fill="url(#sxFondo)"/>',
         f'<ellipse cx="420" cy="528" rx="170" ry="9" fill="#000" opacity=".08"/>']
    # Correa: del gancho a la anilla
    ax, ay = P["anilla"]
    c.append(f'<path d="M{ax:.0f} {ay:.0f} q-8 -14 -2 -26" fill="none" stroke="{PLATA_OSC}" stroke-width="3"/>'
             f'<path d="M{ax-2:.0f} {ay-26:.0f} C{ax-12:.0f} {ay-80:.0f} {ax-40:.0f} {ay-150:.0f} {ax-74:.0f} {ay-215:.0f}" fill="none" stroke="#2c2c2c" stroke-width="9" stroke-linecap="round"/>'
             f'<path d="M{ax-2:.0f} {ay-26:.0f} C{ax-12:.0f} {ay-80:.0f} {ax-40:.0f} {ay-150:.0f} {ax-74:.0f} {ay-215:.0f}" fill="none" stroke="#555" stroke-width="2" stroke-dasharray="5 6"/>')
    P["correa"] = _bez((ax - 2, ay - 26), (ax - 12, ay - 80), (ax - 40, ay - 150), (ax - 74, ay - 215), 10)[2]
    c.append(sax)
    izq = [("boquilla", "Boquilla"), ("cana", "Caña y abrazadera"), ("cuello", "Cuello (tudel)"), ("correa", "Correa"),
           ("octava", "Llave de octava"), ("llaves", "Llaves y almohadillas"), ("cuerpo", "Cuerpo"), ("pulgar_der", "Apoyo del pulgar derecho")]
    der = [("pulgar_oct", "Pulgar izquierdo (octava)"), ("campana", "Campana (pabellón)")]
    if etiquetas:
        def poner(lista, lx, y_ini, y_fin, fin):
            lista = sorted(lista, key=lambda t: P[t[0]][1])
            for n, (k, txt) in enumerate(lista):
                ly = y_ini + (y_fin - y_ini) * n / max(len(lista) - 1, 1)
                px, py = P[k]
                ex = lx + (6 if fin == "end" else -6)
                c.append(f'<line x1="{px:.0f}" y1="{py:.0f}" x2="{ex:.0f}" y2="{ly-5:.0f}" stroke="#5a4630" stroke-width="1.2"/>'
                         f'<circle cx="{px:.0f}" cy="{py:.0f}" r="3.5" fill="#c0392b"/>'
                         f'<text x="{lx}" y="{ly:.0f}" font-size="15" font-weight="700" fill="#3b2410" text-anchor="{fin}">{txt}</text>')
        poner(izq, 200, 40, 440, "end")
        poner(der, 740, 120, 300, "start")
        px, py = P["curva"]
        c.append(f'<circle cx="{px:.0f}" cy="{py:.0f}" r="3.5" fill="#c0392b"/><line x1="{px:.0f}" y1="{py:.0f}" x2="{px+90:.0f}" y2="{py+14:.0f}" stroke="#5a4630" stroke-width="1.2"/>'
                 f'<text x="{px+96:.0f}" y="{py+19:.0f}" font-size="15" font-weight="700" fill="#3b2410">Curva en U (arco)</text>')
    c.append("</svg>")
    svg = "\n".join(c)
    if puntos:
        return svg, {k: (round((x - x0) * 100 / W, 1), round((y - y0) * 100 / H, 1)) for k, (x, y) in P.items()}
    return svg


def svg_familia():
    """La familia del saxofón, con su tamaño aproximado y su afinación."""
    c = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 420" width="800" height="420" role="img" aria-label="La familia del saxofón: soprano, alto, tenor y barítono, con su afinación" {F}>',
         DEFS, '<rect width="800" height="420" fill="url(#sxFondo)"/>',
         '<text x="400" y="26" font-size="15" fill="#555" text-anchor="middle">Cuanto más grande, más grave. Este curso es del saxo alto (en rojo).</text>']
    # Soprano recto
    sop = _linea((95, 120), (100, 330), 20)
    c.append(tubo(sop, _interp(9, 20, len(sop))))
    c.append(f'<path d="M88 328 Q86 348 74 362 L128 362 Q114 348 112 328 Z" fill="url(#sxLaton)" stroke="{LATON_OSC}" stroke-width="1.5"/>'
             f'<ellipse cx="101" cy="362" rx="27" ry="5" fill="#5a3a0c" stroke="{LATON_OSC}"/>'
             f'<path d="M95 120 L93 92" stroke="{NEGRO}" stroke-width="8" stroke-linecap="round"/>')
    for y in range(160, 320, 26):
        c.append(f'<circle cx="104" cy="{y}" r="4" fill="url(#sxPerla)" stroke="{LATON_OSC}"/>')
    datos = [("Soprano", "Si♭", 100)]
    for nombre, afin, x, esc, cuello in (("Alto", "Mi♭", 150, 0.5, "alto"), ("Tenor", "Si♭", 315, 0.61, "tenor"), ("Barítono", "Mi♭", 500, 0.68, "bar")):
        base_y = 362 - 530 * esc
        sx, _ = _saxo(x - 200 * esc, base_y + 30 * esc, esc, llaves=True, cuello="alto" if cuello == "alto" else "tenor")
        c.append(sx)
        if cuello == "bar":   # bucle característico del barítono
            bx, by = x - 200 * esc + 360 * esc, base_y + 30 * esc + 150 * esc
            lazo = _bez((bx, by), (bx + 10, by - 70), (bx + 70, by - 80), (bx + 66, by - 30), 16) + _bez((bx + 66, by - 30), (bx + 62, by + 6), (bx + 20, by - 6), (bx + 10, by - 40), 12)[1:]
            c.append(tubo(lazo, _interp(18, 14, len(lazo))))
        datos.append((nombre, afin, x - 200 * esc + 430 * esc))
    for nombre, afin, cx in datos:
        resalta = nombre == "Alto"
        c.append(f'<text x="{cx:.0f}" y="392" font-size="16" font-weight="700" fill="{"#c0392b" if resalta else "#3b2410"}" text-anchor="middle">{nombre}</text>'
                 f'<text x="{cx:.0f}" y="410" font-size="12" fill="#555" text-anchor="middle">en {afin}</text>')
    c.append("</svg>")
    return "\n".join(c)


# ---- Diagramas de digitación ----------------------------------------------------------------------------------
NOMBRE_LLAVE = {"G♯": "Sol♯", "C♯": "Do♯", "B": "Si", "B♭": "Si♭", "E♭": "Mi♭", "C": "Do"}
MARRON = "#3b2410"


def _perla(cx, cy, r, on, num=None):
    s = (f'<circle cx="{cx}" cy="{cy}" r="{r+3}" fill="url(#sxCazo)" stroke="{LATON_OSC}" stroke-width="1.2"/>'
         f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="url(#{"sxPerlaOn" if on else "sxPerla"})" stroke="{LATON_OSC}" stroke-width="1"/>')
    if num is not None:
        s += f'<text x="{cx}" y="{cy+4}" font-size="11" text-anchor="middle" fill="{"#fff" if on else "#9a8e7c"}" font-weight="700">{num}</text>'
    return s


def _espatula(x, y, w, h, on, txt):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{min(w, h)/2:.1f}" fill="url(#{"sxPerlaOn" if on else "sxCazo"})" stroke="{LATON_OSC}" stroke-width="1.2"/>'
            f'<text x="{x + w/2:.1f}" y="{y + h/2 + 3:.1f}" font-size="8" text-anchor="middle" fill="{"#fff" if on else MARRON}" font-weight="700">{txt}</text>')


def diagrama(x, nombre, f, con_nombre=True):
    """Digitación dibujada sobre un tramo del cuerpo del saxo. Devuelve (svg, ancho). Mismo marco que el esquema anterior."""
    g = [f'<g transform="translate({x},0)">']
    # tramo del cuerpo (tubo de latón) y varilla
    g.append(tubo(_linea((58, 58), (58, 252), 10), [30] * 11))
    g.append(f'<line x1="78" y1="62" x2="78" y2="248" stroke="{LATON_OSC}" stroke-width="2.5"/>')
    # botón de octava del pulgar izquierdo (en la parte de atrás)
    on = f["oct"]
    g.append(f'<text x="25" y="18" font-size="9" text-anchor="middle" fill="#6b5a45">pulgar</text>'
             f'<ellipse cx="25" cy="34" rx="17" ry="9" fill="url(#{"sxPerlaOn" if on else "sxPerla"})" stroke="{LATON_OSC}" stroke-width="2"/>'
             f'<text x="25" y="38" font-size="10" text-anchor="middle" fill="{"#fff" if on else MARRON}" font-weight="700">8.ª</text>'
             f'<path d="M42 34 L50 40" stroke="{LATON_OSC}" stroke-width="2"/>')
    g.append('<text x="58" y="52" font-size="9" text-anchor="middle" fill="#6b5a45">izquierda</text>')
    for i, y in enumerate((72, 102, 132), 1):
        g.append(_perla(58, y, 10, i in f["lh"], i))
    # mesa del meñique izquierdo: Sol♯ arriba, Do♯, Si y Si♭ debajo
    lp = f.get("lp")
    g.append(f'<path d="M8 112 L38 112 L38 162 L8 162 Z" fill="#000" opacity=".05"/>')
    g.append(_espatula(9, 113, 28, 11, lp == "G♯", "Sol♯"))
    g.append(_espatula(9, 126, 28, 11, lp == "C♯", "Do♯"))
    g.append(_espatula(9, 139, 13, 21, lp == "B", "Si"))
    g.append(_espatula(24, 139, 13, 21, lp == "B♭", "Si♭"))
    g.append(f'<rect x="41" y="152" width="34" height="8" rx="2" fill="url(#sxLaton)" stroke="{LATON_OSC}"/>'
             '<text x="99" y="160" font-size="9" text-anchor="middle" fill="#6b5a45">derecha</text>')
    for i, y in enumerate((180, 210, 240), 1):
        g.append(_perla(58, y, 10, i in f["rh"], i))
    # espátulas del meñique derecho
    rp = f.get("rp")
    g.append(_espatula(78, 250, 32, 13, rp == "E♭", "Mi♭"))
    g.append(_espatula(78, 266, 32, 13, rp == "C", "Do"))
    if con_nombre:
        g.append(f'<text x="58" y="304" font-size="14" text-anchor="middle" fill="{MARRON}" font-weight="700">{html.escape(nombre)}</text>')
    g.append("</g>")
    return "".join(g), 118
