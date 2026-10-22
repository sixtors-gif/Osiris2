"""Digitaciones del saxo alto (tono escrito) y dibujos SVG del curso.

FING[nota] = dict(oct=bool, lh=[dedos de la mano izquierda], rh=[dedos de la mano derecha],
                  lp='G♯'|'C♯'|'B'|'B♭'|None (meñique izquierdo), rp='E♭'|'C'|None (meñique derecho))
Las notas se nombran con el sistema español y número de octava científica (Do4 = Do central).
El registro agudo (Re5-Do♯6) repite la digitación del grave con la llave de octava.
"""
import html

SEIS = dict(lh=[1, 2, 3], rh=[1, 2, 3])
BASE = {
    "Si♭3": dict(**SEIS, lp="B♭"),
    "Si3": dict(**SEIS, lp="B"),
    "Do4": dict(**SEIS, rp="C"),
    "Do♯4": dict(**SEIS, lp="C♯"),
    "Re4": dict(**SEIS),
    "Mi♭4": dict(**SEIS, rp="E♭"),
    "Mi4": dict(lh=[1, 2, 3], rh=[1, 2]),
    "Fa4": dict(lh=[1, 2, 3], rh=[1]),
    "Fa♯4": dict(lh=[1, 2, 3], rh=[2]),
    "Sol4": dict(lh=[1, 2, 3], rh=[]),
    "Sol♯4": dict(lh=[1, 2, 3], rh=[], lp="G♯"),
    "La4": dict(lh=[1, 2], rh=[]),
    "Si♭4": dict(lh=[1], rh=[1]),
    "Si4": dict(lh=[1], rh=[]),
    "Do5": dict(lh=[2], rh=[]),
    "Do♯5": dict(lh=[], rh=[]),
}
FING = {k: dict(oct=False, lh=v["lh"], rh=v["rh"], lp=v.get("lp"), rp=v.get("rp")) for k, v in BASE.items()}
# Registro agudo: la misma digitación que una octava más grave, con la llave de octava pulsada
for grave, agudo in (("Re4", "Re5"), ("Mi♭4", "Mi♭5"), ("Mi4", "Mi5"), ("Fa4", "Fa5"), ("Fa♯4", "Fa♯5"), ("Sol4", "Sol5"), ("Sol♯4", "Sol♯5"),
                     ("La4", "La5"), ("Si♭4", "Si♭5"), ("Si4", "Si5"), ("Do5", "Do6"), ("Do♯5", "Do♯6")):
    FING[agudo] = dict(FING[grave], oct=True)

REGISTRO_GRAVE = ["Si♭3", "Si3", "Do4", "Do♯4", "Re4", "Mi♭4", "Mi4", "Fa4", "Fa♯4", "Sol4", "Sol♯4", "La4", "Si♭4", "Si4", "Do5", "Do♯5"]
REGISTRO_AGUDO = ["Re5", "Mi♭5", "Mi5", "Fa5", "Fa♯5", "Sol5", "Sol♯5", "La5", "Si♭5", "Si5", "Do6", "Do♯6"]


def _notas_validas():
    for n in REGISTRO_GRAVE + REGISTRO_AGUDO:
        assert n in FING, n


_notas_validas()

OSCURO, CLARO, LATON = "#3b2410", "#ffffff", "#c9962b"


def _diagrama(x, nombre, f, con_nombre=True):
    """Dibuja el diagrama de una digitación con el origen en x. Devuelve (svg, ancho)."""
    g = [f'<g transform="translate({x},0)">']
    # llave de octava (pulgar izquierdo)
    g.append(f'<rect x="6" y="26" width="38" height="16" rx="8" fill="{OSCURO if f["oct"] else CLARO}" stroke="{OSCURO}" stroke-width="1.5"/>')
    g.append(f'<text x="25" y="38" font-size="10" text-anchor="middle" fill="{CLARO if f["oct"] else OSCURO}" font-weight="700">8.ª</text>')
    g.append(f'<text x="25" y="20" font-size="9" text-anchor="middle" fill="#666">pulgar</text>')
    # mano izquierda
    for i, y in enumerate((70, 100, 130), 1):
        on = i in f["lh"]
        g.append(f'<circle cx="58" cy="{y}" r="12" fill="{OSCURO if on else CLARO}" stroke="{OSCURO}" stroke-width="1.5"/>')
        g.append(f'<text x="58" y="{y+4}" font-size="11" text-anchor="middle" fill="{CLARO if on else "#999"}" font-weight="700">{i}</text>')
    g.append('<text x="58" y="52" font-size="9" text-anchor="middle" fill="#666">izquierda</text>')
    # meñique izquierdo (mesa de llaves)
    lp = f.get("lp")
    g.append(f'<rect x="10" y="118" width="26" height="34" rx="6" fill="{OSCURO if lp else CLARO}" stroke="{OSCURO}" stroke-width="1.5"/>')
    g.append(f'<text x="23" y="140" font-size="9" text-anchor="middle" fill="{CLARO if lp else "#999"}" font-weight="700">{html.escape(lp) if lp else "meñ."}</text>')
    # mano derecha
    for i, y in enumerate((178, 208, 238), 1):
        on = i in f["rh"]
        g.append(f'<circle cx="58" cy="{y}" r="12" fill="{OSCURO if on else CLARO}" stroke="{OSCURO}" stroke-width="1.5"/>')
        g.append(f'<text x="58" y="{y+4}" font-size="11" text-anchor="middle" fill="{CLARO if on else "#999"}" font-weight="700">{i}</text>')
    g.append('<text x="58" y="160" font-size="9" text-anchor="middle" fill="#666">derecha</text>')
    # meñique derecho: llaves Mi♭ y Do
    rp = f.get("rp")
    for etiqueta, y in (("E♭", 252), ("C", 272)):
        on = rp == etiqueta
        g.append(f'<rect x="76" y="{y-9}" width="30" height="16" rx="6" fill="{OSCURO if on else CLARO}" stroke="{OSCURO}" stroke-width="1.5"/>')
        g.append(f'<text x="91" y="{y+3}" font-size="9" text-anchor="middle" fill="{CLARO if on else "#999"}" font-weight="700">{etiqueta}</text>')
    if con_nombre:
        g.append(f'<text x="58" y="304" font-size="14" text-anchor="middle" fill="{OSCURO}" font-weight="700">{html.escape(nombre)}</text>')
    g.append("</g>")
    return "".join(g), 118


def svg_digitaciones(nombres, titulo, con_nombre=True):
    """Un dibujo con varias digitaciones, una junto a otra."""
    cuerpo, x = [], 0
    for n in nombres:
        d, w = _diagrama(x, n, FING[n], con_nombre)
        cuerpo.append(d); x += w
    ancho = x + 6
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {ancho} 316" width="{ancho}" height="316" role="img" aria-label="{html.escape(titulo, quote=True)}" '
            f'font-family="Segoe UI,Tahoma,sans-serif"><rect width="{ancho}" height="316" fill="#fffaf0"/>' + "".join(cuerpo) + "</svg>")


def svg_diagrama_digitacion_js():
    """JSON con las digitaciones para el entrenador de digitaciones."""
    import json
    return json.dumps({k: FING[k] for k in REGISTRO_GRAVE + REGISTRO_AGUDO}, ensure_ascii=False)


def svg_partes(etiquetas=True):
    """Esquema del saxo alto con sus partes."""
    c = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="-110 0 880 520" width="880" height="520" role="img" '
         'aria-label="Esquema del saxo alto con sus partes: boquilla, caña, abrazadera, cuello, cuerpo, llaves, tudel, campana y correa" '
         'font-family="Segoe UI,Tahoma,sans-serif"><rect x="-110" width="880" height="520" fill="#fffaf0"/>']
    # tubo: cuello curvo + cuerpo recto + arco en U + campana
    c.append('<path d="M214 70 Q282 54 296 108 L296 380 Q296 452 360 452 Q424 452 424 380 L424 300" fill="none" stroke="#c9962b" stroke-width="30" stroke-linecap="round" stroke-linejoin="round"/>')
    c.append('<path d="M214 70 Q282 54 296 108 L296 380 Q296 452 360 452 Q424 452 424 380 L424 300" fill="none" stroke="#e8c868" stroke-width="20" stroke-linecap="round" stroke-linejoin="round"/>')
    # campana
    c.append('<path d="M404 300 L384 244 Q424 232 464 244 L444 300 Z" fill="#c9962b" stroke="#8a5a14" stroke-width="2"/>')
    # boquilla y caña
    c.append('<path d="M214 70 L152 46 L146 60 L204 84 Z" fill="#3b2410"/>')
    c.append('<path d="M156 52 L204 70" stroke="#e8d9a8" stroke-width="7" stroke-linecap="round"/>')
    c.append('<rect x="176" y="46" width="22" height="30" rx="4" transform="rotate(20 187 61)" fill="#8a8a8a" stroke="#555"/>')
    # llaves
    for y in range(140, 360, 34):
        c.append(f'<circle cx="296" cy="{y}" r="11" fill="#fff" stroke="#3b2410" stroke-width="2"/>')
    c.append('<rect x="276" y="112" width="40" height="12" rx="6" fill="#8a5a14"/>')
    # correa
    c.append('<path d="M296 150 Q230 20 150 14" fill="none" stroke="#c0392b" stroke-width="3" stroke-dasharray="6 5"/>')
    # etiquetas
    def etiqueta(x, y, tx, ty, txt, anchor="start"):
        c.append(f'<line x1="{x}" y1="{y}" x2="{tx}" y2="{ty-4}" stroke="#555" stroke-width="1"/>')
        c.append(f'<text x="{tx}" y="{ty}" font-size="15" font-weight="700" fill="#3b2410" text-anchor="{anchor}">{txt}</text>')
    if etiquetas:
        etiqueta(152, 52, 80, 34, "Boquilla", "end")
        etiqueta(188, 62, 120, 100, "Caña y abrazadera", "end")
        etiqueta(246, 78, 90, 150, "Cuello (tudel)", "end")
        etiqueta(296, 126, 90, 200, "Llave de octava", "end")
        etiqueta(296, 210, 90, 250, "Llaves y almohadillas", "end")
        etiqueta(296, 300, 90, 330, "Cuerpo", "end")
        etiqueta(360, 452, 330, 496, "Curva en U (arco)", "middle")
        etiqueta(444, 270, 480, 290, "Campana (pabellón)")
        etiqueta(180, 20, 190, 14, "Correa")
        etiqueta(296, 120, 330, 108, "Pulgar izquierdo (octava)")
        etiqueta(424, 350, 460, 380, "Anillo del pulgar derecho", "start")
    c.append('<circle cx="424" cy="350" r="8" fill="none" stroke="#3b2410" stroke-width="3"/>')
    c.append("</svg>")
    return "\n".join(c)


def svg_familia():
    """Los saxofones de la familia, a escala aproximada, con su tonalidad."""
    familia = [("Soprano", "Si♭", 80), ("Alto", "Mi♭", 120), ("Tenor", "Si♭", 170), ("Barítono", "Mi♭", 225)]
    c = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 620 360" width="620" height="360" role="img" aria-label="La familia del saxofón: soprano, alto, tenor y barítono, con su afinación" font-family="Segoe UI,Tahoma,sans-serif">',
         '<rect width="620" height="360" fill="#fffaf0"/>']
    for i, (nombre, afin, alto) in enumerate(familia):
        x = 60 + i * 140
        base = 310
        c.append(f'<rect x="{x}" y="{base-alto}" width="22" height="{alto}" rx="10" fill="#e8c868" stroke="#8a5a14" stroke-width="2"/>')
        c.append(f'<path d="M{x+22} {base-20} Q{x+54} {base+10} {x+70} {base-30} L{x+70} {base-60} L{x+52} {base-60} Z" fill="#c9962b" stroke="#8a5a14" stroke-width="2"/>')
        c.append(f'<path d="M{x+11} {base-alto} Q{x+11} {base-alto-26} {x-16} {base-alto-20}" fill="none" stroke="#3b2410" stroke-width="7" stroke-linecap="round"/>')
        resalta = nombre == "Alto"
        c.append(f'<text x="{x+30}" y="{base+30}" font-size="15" font-weight="700" fill="{"#c0392b" if resalta else "#3b2410"}" text-anchor="middle">{nombre}</text>')
        c.append(f'<text x="{x+30}" y="{base+48}" font-size="12" fill="#555" text-anchor="middle">en {afin}</text>')
    c.append('<text x="310" y="22" font-size="14" fill="#555" text-anchor="middle">Cuanto más grande, más grave. Este curso es del saxo alto (en rojo).</text>')
    c.append("</svg>")
    return "\n".join(c)
