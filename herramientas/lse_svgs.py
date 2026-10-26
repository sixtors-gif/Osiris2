"""Dibujos del curso de lengua de signos española (SVG)."""
import html

F = 'font-family="Segoe UI,Tahoma,sans-serif"'
VERDE, NARANJA, CLARO = "#0f766e", "#f97316", "#e6f4f2"


def _t(x, y, txt, size=13, color="#222", anchor="middle", peso=400):
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" text-anchor="{anchor}" font-weight="{peso}">{html.escape(txt)}</text>'


def _lin(x, y, txt, n=18, size=13, color="#222", peso=400, paso=16):
    l, cur = [], ""
    for p in txt.split(" "):
        if cur and len(cur) + 1 + len(p) > n:
            l.append(cur); cur = p
        else:
            cur = (cur + " " + p).strip()
    l.append(cur)
    return "".join(_t(x, y + i * paso, s, size, color, "middle", peso) for i, s in enumerate(l))


def parametros():
    cajas = [("1", "Configuración", "la forma de la mano", 60), ("2", "Orientación", "hacia dónde miran la palma y los dedos", 240),
             ("3", "Lugar", "dónde se hace: cara, pecho, espacio…", 420), ("4", "Movimiento", "cómo se mueven las manos", 600),
             ("5", "Componentes no manuales", "cara, mirada, cabeza y cuerpo", 780)]
    c = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 250" width="960" height="250" role="img" aria-label="Los cinco parámetros de un signo" {F}>',
         '<rect width="960" height="250" fill="#fff"/>',
         _t(480, 34, "Un signo = 5 parámetros a la vez", 20, VERDE, "middle", 700)]
    for n, t, d, x in cajas:
        c.append(f'<rect x="{x-50}" y="60" width="170" height="150" rx="14" fill="{CLARO}" stroke="{VERDE}" stroke-width="2"/>')
        c.append(f'<circle cx="{x+35}" cy="82" r="16" fill="{NARANJA}"/>' + _t(x + 35, 88, n, 16, "#fff", "middle", 700))
        c.append(_lin(x + 35, 122, t, 16, 14, VERDE, 700) + _lin(x + 35, 160 + (16 if len(t) > 16 else 0), d, 20, 12, "#333"))
    c.append("</svg>")
    return "".join(c)


def espacio_signado():
    c = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 420" width="760" height="420" role="img" aria-label="Esquema del espacio de signado" {F}>',
         '<rect width="760" height="420" fill="#fff"/>',
         f'<rect x="170" y="40" width="420" height="320" rx="40" fill="{CLARO}" stroke="{VERDE}" stroke-width="3" stroke-dasharray="8 6"/>',
         '<circle cx="380" cy="100" r="42" fill="#fde6c8" stroke="#555" stroke-width="2"/>',
         '<rect x="320" y="150" width="120" height="170" rx="30" fill="#cfd8dc" stroke="#555" stroke-width="2"/>',
         '<line x1="320" y1="170" x2="240" y2="260" stroke="#555" stroke-width="12" stroke-linecap="round"/>',
         '<line x1="440" y1="170" x2="520" y2="260" stroke="#555" stroke-width="12" stroke-linecap="round"/>',
         '<circle cx="366" cy="92" r="4" fill="#333"/><circle cx="394" cy="92" r="4" fill="#333"/><path d="M366 116 Q380 126 394 116" stroke="#333" fill="none" stroke-width="2"/>',
         _t(380, 24, "Zona de signado: de la cabeza a la cintura y de codo a codo", 15, VERDE, "middle", 700),
         _t(80, 100, "Cara", 14, "#333", "middle", 700), '<line x1="115" y1="96" x2="335" y2="96" stroke="#999" stroke-dasharray="3 3"/>',
         _t(80, 190, "Cuello y hombros", 13, "#333", "middle", 700), '<line x1="150" y1="186" x2="318" y2="180" stroke="#999" stroke-dasharray="3 3"/>',
         _t(80, 250, "Pecho", 14, "#333", "middle", 700), '<line x1="115" y1="246" x2="330" y2="236" stroke="#999" stroke-dasharray="3 3"/>',
         _t(80, 320, "Espacio neutro", 14, "#333", "middle", 700), _t(80, 338, "(delante del cuerpo)", 12), '<line x1="150" y1="316" x2="300" y2="300" stroke="#999" stroke-dasharray="3 3"/>',
         _t(680, 100, "Mirada y expresión", 13, NARANJA, "middle", 700), '<line x1="610" y1="96" x2="425" y2="96" stroke="#999" stroke-dasharray="3 3"/>',
         _t(680, 250, "Lados: pronombres", 13, NARANJA, "middle", 700), _t(680, 268, "y localización", 13, NARANJA, "middle", 700), '<line x1="620" y1="252" x2="525" y2="256" stroke="#999" stroke-dasharray="3 3"/>',
         "</svg>"]
    return "".join(c)


# Esquemas de configuraciones de la mano: estado de pulgar, índice, corazón, anular y meñique.
# u = estirado, c = curvado, d = doblado (cerrado); el pulgar: u = hacia fuera, c = cruzado ante la palma, d = recogido.
CONFIG = [("Mano plana", "uuuuu", "dedos juntos y estirados"), ("Puño", "dddddd"[:5], "todos los dedos cerrados"),
          ("Índice", "duddd", "solo el índice estirado"), ("Mano en C", "ccccc", "dedos y pulgar curvados"),
          ("Pinza o círculo", "cccuu", "pulgar e índice se tocan"), ("Mano en V", "duudd", "índice y corazón separados"),
          ("Mano abierta", "uuuuu", "dedos separados"), ("Meñique", "ddddu", "solo el meñique"),
          ("Pulgar", "udddd", "solo el pulgar"), ("Cuerno", "duddu", "índice y meñique")]


def configuraciones():
    c = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 330" width="960" height="330" role="img" aria-label="Esquemas de configuraciones de la mano" {F}>',
         '<rect width="960" height="330" fill="#fff"/>',
         _t(480, 26, "Algunas configuraciones básicas de la mano (esquema simplificado)", 17, VERDE, "middle", 700)]
    for k, (nombre, st, desc) in enumerate(CONFIG):
        col, fila = k % 5, k // 5
        x0, y0 = 20 + col * 188, 50 + fila * 140
        c.append(f'<rect x="{x0}" y="{y0}" width="172" height="128" rx="12" fill="{CLARO}" stroke="{VERDE}"/>')
        c.append(f'<rect x="{x0+46}" y="{y0+62}" width="80" height="34" rx="8" fill="#fde6c8" stroke="#555"/>')
        sep = 18 if nombre == "Mano abierta" else 0
        for i, e in enumerate(st[1:]):
            fx = x0 + 52 + i * 19 + (i - 1.5) * sep / 3
            alto = {"u": 46, "c": 26, "d": 8}[e]
            c.append(f'<rect x="{fx}" y="{y0+62-alto}" width="14" height="{alto+6}" rx="6" fill="#fde6c8" stroke="#555"/>')
        e = st[0]
        if e == "u":
            c.append(f'<rect x="{x0+20}" y="{y0+66}" width="34" height="13" rx="6" fill="#fde6c8" stroke="#555" transform="rotate(-25 {x0+54} {y0+72})"/>')
        elif e == "c":
            c.append(f'<rect x="{x0+50}" y="{y0+72}" width="52" height="12" rx="6" fill="#fde6c8" stroke="#555"/>')
        else:
            c.append(f'<rect x="{x0+44}" y="{y0+74}" width="22" height="14" rx="6" fill="#fde6c8" stroke="#555"/>')
        c.append(_t(x0 + 86, y0 + 112, nombre, 13, VERDE, "middle", 700))
    c.append("</svg>")
    return "".join(c)


def linea_historia():
    ev = [(1550, "Ponce de León educa a sordos en Oña"), (1620, "Bonet publica el primer tratado en España"), (1760, "L'Épée abre en París la primera escuela pública"),
          (1805, "Colegio de Sordomudos en Madrid"), (1880, "Congreso de Milán: se prohíben los signos"), (1936, "Nace la CNSE"),
          (2006, "ONU: Convención de derechos"), (2007, "Ley 27/2007 reconoce la LSE")]
    c = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 340" width="960" height="340" role="img" aria-label="Línea de tiempo de la historia de la lengua de signos" {F}>',
         '<rect width="960" height="340" fill="#fff"/>', f'<line x1="30" y1="170" x2="930" y2="170" stroke="{VERDE}" stroke-width="5" stroke-linecap="round"/>']
    for i, (a, t) in enumerate(ev):
        x = 70 + i * 117
        arriba = i % 2 == 0
        c.append(f'<circle cx="{x}" cy="170" r="9" fill="{NARANJA}" stroke="#fff" stroke-width="2"/>')
        c.append(f'<line x1="{x}" y1="{161 if arriba else 179}" x2="{x}" y2="{125 if arriba else 215}" stroke="{VERDE}" stroke-width="2"/>')
        c.append(_t(x, 112 if arriba else 238, str(a), 17, VERDE, "middle", 700))
        c.append(_lin(x, 40 if arriba else 262, t, 15, 12, "#222", 400, 15))
    c.append("</svg>")
    return "".join(c)
