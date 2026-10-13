#!/usr/bin/env python3
"""Genera las ilustraciones SVG del curso «Informática básica para jóvenes».

Uso: python3 herramientas/generar_informatica_basica_imagenes.py cursos/Curso_Informatica_Basica_Jovenes_SCORM
"""
import os, sys

OUT = os.path.join(sys.argv[1], "img")
os.makedirs(OUT, exist_ok=True)

NAVY, TEAL, GREEN, CORAL, YELLOW, GREY, LIGHT = "#1e3c72", "#4ecdc4", "#44a08d", "#ff6b6b", "#ffd166", "#6b7280", "#f4f7fb"
FONT = "font-family=\"Segoe UI,Tahoma,Verdana,sans-serif\""


def svg(name, w, h, title, body):
    s = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="{title}" {FONT}>\n'
         f'<title>{title}</title>\n<rect width="{w}" height="{h}" rx="18" fill="#ffffff"/>\n{body}\n</svg>\n')
    open(os.path.join(OUT, name), "w", encoding="utf-8").write(s)


def text(x, y, t, size=15, fill=NAVY, weight="600", anchor="middle"):
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" font-weight="{weight}" text-anchor="{anchor}">{t}</text>'


def label(x, y, t, tx, ty, anchor="start"):
    """Etiqueta con línea guía desde (x,y) hasta el texto en (tx,ty)."""
    return (f'<line x1="{x}" y1="{y}" x2="{tx}" y2="{ty-5}" stroke="{GREY}" stroke-width="1.5"/>'
            f'<circle cx="{x}" cy="{y}" r="4" fill="{CORAL}"/>' + text(tx + (4 if anchor == "start" else -4), ty, t, 14, NAVY, "700", anchor))


def arrow(x1, y1, x2, y2, color=TEAL):
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="5" stroke-linecap="round" marker-end="url(#flecha)"/>')


DEFS = f'<defs><marker id="flecha" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="4" markerHeight="4" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="{TEAL}"/></marker></defs>'

# Iconos reutilizables ---------------------------------------------------------

def monitor(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="0" y="0" width="120" height="80" rx="8" fill="{NAVY}"/>'
            f'<rect x="8" y="8" width="104" height="60" rx="4" fill="#bfefff"/><rect x="50" y="80" width="20" height="16" fill="{GREY}"/>'
            f'<rect x="30" y="96" width="60" height="8" rx="4" fill="{GREY}"/></g>')


def keyboard(x, y, s=1.0):
    keys = "".join(f'<rect x="{8+c*14}" y="{8+r*12}" width="11" height="9" rx="2" fill="#ffffff"/>' for r in range(3) for c in range(9))
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="0" y="0" width="136" height="50" rx="8" fill="{GREY}"/>{keys}</g>')


def mouse(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="0" y="0" width="34" height="52" rx="17" fill="{GREY}"/>'
            f'<line x1="17" y1="0" x2="17" y2="20" stroke="#ffffff" stroke-width="2"/></g>')


def chip(x, y, s=1.0, t="CPU"):
    pins = "".join(f'<rect x="{10+i*14}" y="-8" width="5" height="8" fill="{GREY}"/><rect x="{10+i*14}" y="70" width="5" height="8" fill="{GREY}"/>'
                   f'<rect x="-8" y="{10+i*14}" width="8" height="5" fill="{GREY}"/><rect x="70" y="{10+i*14}" width="8" height="5" fill="{GREY}"/>' for i in range(4))
    return (f'<g transform="translate({x},{y}) scale({s})">{pins}<rect x="0" y="0" width="70" height="70" rx="8" fill="{NAVY}"/>'
            f'<rect x="14" y="14" width="42" height="42" rx="4" fill="{TEAL}"/>' + text(35, 41, t, 14, "#ffffff", "700") + '</g>')


def disk(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="0" y="0" width="90" height="64" rx="8" fill="{GREY}"/>'
            f'<circle cx="38" cy="32" r="24" fill="#d9dee7"/><circle cx="38" cy="32" r="5" fill="{GREY}"/>'
            f'<line x1="70" y1="10" x2="44" y2="30" stroke="{NAVY}" stroke-width="4" stroke-linecap="round"/></g>')


def phone(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="0" y="0" width="50" height="92" rx="10" fill="{NAVY}"/>'
            f'<rect x="5" y="10" width="40" height="68" rx="3" fill="#bfefff"/><circle cx="25" cy="85" r="3" fill="#ffffff"/></g>')


def laptop(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="14" y="0" width="132" height="86" rx="8" fill="{NAVY}"/>'
            f'<rect x="22" y="8" width="116" height="70" rx="4" fill="#bfefff"/><path d="M0,90 h160 l-10,12 h-140 z" fill="{GREY}"/></g>')


def printer(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="20" y="0" width="60" height="22" fill="#ffffff" stroke="{GREY}" stroke-width="2"/>'
            f'<rect x="0" y="20" width="100" height="44" rx="8" fill="{GREY}"/><rect x="20" y="52" width="60" height="30" fill="#ffffff" stroke="{GREY}" stroke-width="2"/>'
            f'<line x1="28" y1="62" x2="72" y2="62" stroke="{TEAL}" stroke-width="3"/><line x1="28" y1="71" x2="62" y2="71" stroke="{TEAL}" stroke-width="3"/></g>')


# 1. Portada -------------------------------------------------------------------
svg("portada.svg", 640, 260, "Ilustración de un portátil, una torre y un móvil conectados",
    DEFS + f'<rect x="0" y="0" width="640" height="260" rx="18" fill="{LIGHT}"/>'
    + laptop(40, 70, 1.15) + phone(250, 90, 1.0)
    + f'<rect x="330" y="40" width="90" height="170" rx="10" fill="{NAVY}"/><circle cx="375" cy="70" r="8" fill="{TEAL}"/>'
    + ''.join(f'<rect x="345" y="{100+i*18}" width="60" height="8" rx="4" fill="#2d4d8a"/>' for i in range(5))
    + text(530, 110, "Informática", 30, NAVY, "800") + text(530, 145, "básica", 30, GREEN, "800")
    + text(530, 180, "hardware · software · redes", 14, GREY, "600"))

# 2. Entrada - proceso - salida ------------------------------------------------
svg("entrada_proceso_salida.svg", 720, 330, "Esquema entrada, proceso, salida y almacenamiento de un ordenador",
    DEFS
    + f'<rect x="20" y="30" width="190" height="180" rx="16" fill="{LIGHT}" stroke="{TEAL}" stroke-width="3"/>'
    + keyboard(47, 70, 1.0) + mouse(95, 135, 1.0) + text(115, 200, "ENTRADA", 18, NAVY, "800")
    + arrow(215, 120, 258, 120)
    + f'<rect x="265" y="30" width="190" height="180" rx="16" fill="{LIGHT}" stroke="{TEAL}" stroke-width="3"/>'
    + chip(325, 70, 1.0) + text(360, 200, "PROCESO", 18, NAVY, "800")
    + arrow(460, 120, 503, 120)
    + f'<rect x="510" y="30" width="190" height="180" rx="16" fill="{LIGHT}" stroke="{TEAL}" stroke-width="3"/>'
    + monitor(545, 55, 1.0) + text(605, 200, "SALIDA", 18, NAVY, "800")
    + f'<line x1="360" y1="215" x2="360" y2="245" stroke="{GREEN}" stroke-width="5" stroke-dasharray="6 5"/>'
    + f'<rect x="225" y="248" width="270" height="70" rx="14" fill="#e8f5e8" stroke="{GREEN}" stroke-width="3"/>'
    + disk(237, 251, 1.0) + text(410, 290, "ALMACENAMIENTO", 14, "#2e7d32", "800"))

# 3. Ordenador por dentro ------------------------------------------------------
svg("ordenador_por_dentro.svg", 720, 420, "Torre de ordenador abierta con sus componentes señalados",
    f'<rect x="200" y="20" width="300" height="380" rx="14" fill="#2b2f3a"/>'
    f'<rect x="215" y="35" width="270" height="350" rx="8" fill="#3a4050"/>'
    # placa base
    f'<rect x="230" y="50" width="200" height="240" rx="6" fill="#2e7d5b"/>'
    + ''.join(f'<line x1="{240+i*18}" y1="60" x2="{240+i*18}" y2="280" stroke="#3f9d76" stroke-width="1"/>' for i in range(11))
    # CPU + disipador
    + f'<rect x="250" y="70" width="80" height="80" rx="6" fill="#b0b7c3"/>'
    + ''.join(f'<rect x="254" y="{76+i*9}" width="72" height="5" fill="#8a93a3"/>' for i in range(8))
    # RAM
    + ''.join(f'<rect x="{350+i*14}" y="62" width="9" height="110" rx="2" fill="{YELLOW}" stroke="#c9a227"/>' for i in range(4))
    # GPU
    + f'<rect x="240" y="190" width="180" height="40" rx="5" fill="#111827"/><circle cx="290" cy="210" r="14" fill="#374151"/><circle cx="360" cy="210" r="14" fill="#374151"/>'
    # SSD M.2
    + f'<rect x="250" y="250" width="70" height="16" rx="3" fill="#1f2937" stroke="{TEAL}" stroke-width="2"/>'
    # fuente
    + f'<rect x="230" y="305" width="150" height="70" rx="6" fill="#111827"/><circle cx="270" cy="340" r="24" fill="#374151"/><circle cx="270" cy="340" r="4" fill="#9ca3af"/>'
    # disco 3.5
    + f'<rect x="395" y="305" width="80" height="70" rx="6" fill="#9ca3af"/><circle cx="425" cy="340" r="20" fill="#d1d5db"/>'
    # ventilador trasero
    + f'<circle cx="460" cy="90" r="26" fill="#111827"/><circle cx="460" cy="90" r="6" fill="#9ca3af"/>'
    + label(290, 110, "Procesador (CPU)", 190, 60, "end")
    + label(370, 120, "Memoria RAM", 530, 60)
    + label(330, 210, "Tarjeta gráfica (GPU)", 190, 200, "end")
    + label(285, 258, "Disco SSD", 190, 262, "end")
    + label(330, 160, "Placa base", 530, 165)
    + label(270, 340, "Fuente de alimentación", 190, 345, "end")
    + label(435, 340, "Disco duro (HDD)", 530, 345)
    + label(460, 90, "Ventilador", 530, 110))

# 4. Periféricos ---------------------------------------------------------------
svg("perifericos.svg", 720, 300, "Periféricos de entrada, de salida y mixtos",
    ''.join(f'<rect x="{20+i*235}" y="20" width="210" height="260" rx="16" fill="{c}" />' for i, c in enumerate(["#eafffb", "#fff5e6", "#eef2fb"]))
    + text(125, 52, "ENTRADA", 18, GREEN, "800") + text(360, 52, "SALIDA", 18, "#e67e22", "800") + text(595, 52, "MIXTOS", 18, NAVY, "800")
    + keyboard(57, 75, 1.0) + mouse(108, 140, 0.9)
    + f'<g transform="translate(70,205)"><rect x="0" y="0" width="22" height="40" rx="11" fill="{NAVY}"/><rect x="8" y="40" width="6" height="16" fill="{GREY}"/></g>'
    + f'<g transform="translate(120,210)"><rect x="0" y="0" width="70" height="44" rx="6" fill="{GREY}"/><circle cx="35" cy="22" r="13" fill="#1f2937"/><circle cx="35" cy="22" r="6" fill="{TEAL}"/></g>'
    + monitor(300, 70, 1.0) + printer(310, 190, 0.85)
    + f'<g transform="translate(275,215)"><path d="M0,10 h10 l14,-10 v40 l-14,-10 h-10 z" fill="{GREY}"/></g>'
    + f'<g transform="translate(535,75)"><rect x="0" y="0" width="120" height="80" rx="8" fill="{NAVY}"/><rect x="8" y="8" width="104" height="64" rx="4" fill="#bfefff"/>'
      f'<circle cx="70" cy="45" r="9" fill="{CORAL}" opacity=".8"/></g>'
    + f'<g transform="translate(545,180)"><path d="M10,40 a30,30 0 0 1 60,0" fill="none" stroke="{NAVY}" stroke-width="7"/><rect x="0" y="36" width="18" height="30" rx="6" fill="{NAVY}"/><rect x="62" y="36" width="18" height="30" rx="6" fill="{NAVY}"/></g>'
    + f'<g transform="translate(640,195)"><rect x="0" y="0" width="22" height="40" rx="4" fill="{GREY}"/><rect x="5" y="-10" width="12" height="10" fill="#9ca3af"/></g>'
    + text(125, 272, "teclado · ratón · micro · cámara", 12, GREY, "600")
    + text(360, 272, "monitor · altavoz · impresora", 12, GREY, "600")
    + text(595, 272, "pantalla táctil · cascos · USB", 12, GREY, "600"))

# 5. Unidades de información ---------------------------------------------------
steps = [("bit", "0 o 1"), ("Byte", "8 bits · una letra"), ("KB", "un texto · corto"), ("MB", "una foto · o canción"), ("GB", "una película"), ("TB", "miles de · películas")]
body = DEFS
for i, (u, ej) in enumerate(steps):
    x, y = 20 + i * 117, 230 - i * 36
    body += f'<rect x="{x}" y="{y}" width="105" height="{70 + i*36}" rx="10" fill="{[TEAL, GREEN, NAVY, "#2a5298", CORAL, "#e67e22"][i]}"/>'
    body += text(x + 52, y + 32, u, 22, "#ffffff", "800")
    for k, parte in enumerate(ej.split(" · ")):
        body += text(x + 52, y + 54 + k * 15, parte, 11, "#ffffff", "600")
    if i:
        body += text(x - 6, y - 8, "×1024" if i > 1 else "×8", 13, GREY, "700")
svg("unidades_informacion.svg", 720, 320, "Escalera de unidades de información: bit, byte, kilobyte, megabyte, gigabyte y terabyte", body)

# 6. Tipos de almacenamiento ---------------------------------------------------
svg("tipos_almacenamiento.svg", 720, 300, "Tipos de almacenamiento: disco duro, SSD, memoria USB, tarjeta SD y nube",
    disk(30, 60, 1.3) + text(88, 175, "HDD", 18, NAVY, "800") + text(88, 195, "barato · lento", 12, GREY)
    + f'<g transform="translate(175,62)"><rect x="0" y="0" width="110" height="80" rx="8" fill="#1f2937"/>'
      + ''.join(f'<rect x="{10+i*33}" y="18" width="24" height="44" rx="3" fill="#374151" stroke="{TEAL}"/>' for i in range(3)) + '</g>'
    + text(230, 175, "SSD", 18, NAVY, "800") + text(230, 195, "rápido · sin piezas móviles", 12, GREY)
    + f'<g transform="translate(330,70)"><rect x="0" y="20" width="70" height="40" rx="8" fill="{CORAL}"/><rect x="70" y="28" width="26" height="24" fill="#9ca3af"/>'
      f'<rect x="78" y="33" width="5" height="5" fill="#ffffff"/><rect x="87" y="33" width="5" height="5" fill="#ffffff"/></g>'
    + text(375, 175, "USB", 18, NAVY, "800") + text(375, 195, "para llevar", 12, GREY)
    + f'<g transform="translate(455,62)"><path d="M0,0 h48 l16,16 v64 h-64 z" fill="{NAVY}"/>'
      + ''.join(f'<rect x="{8+i*12}" y="6" width="7" height="16" fill="{YELLOW}"/>' for i in range(4)) + '</g>'
    + text(487, 175, "Tarjeta SD", 18, NAVY, "800") + text(487, 195, "móviles y cámaras", 12, GREY)
    + f'<g transform="translate(570,70)"><circle cx="40" cy="45" r="28" fill="#bfefff"/><circle cx="75" cy="35" r="34" fill="#bfefff"/>'
      f'<circle cx="110" cy="50" r="24" fill="#bfefff"/><rect x="40" y="45" width="70" height="29" fill="#bfefff"/></g>'
    + text(645, 175, "Nube", 18, NAVY, "800") + text(645, 195, "necesita Internet", 12, GREY)
    + f'<rect x="40" y="230" width="640" height="10" rx="5" fill="#e5e7eb"/><rect x="40" y="230" width="640" height="10" rx="5" fill="url(#g)"/>'
    + '<defs><linearGradient id="g"><stop offset="0" stop-color="#ff6b6b"/><stop offset="1" stop-color="#44a08d"/></linearGradient></defs>'
    + text(40, 265, "más lento", 13, GREY, "600", "start") + text(680, 265, "más rápido", 13, GREY, "600", "end")
    + text(360, 265, "velocidad aproximada (depende del modelo y de la conexión)", 12, GREY, "500"))

# 7. Capas del software --------------------------------------------------------
layers = [("👤 Tú (usuario)", "#ffffff", NAVY), ("Aplicaciones: navegador, editor de texto, juegos…", TEAL, "#ffffff"),
          ("Sistema operativo: Windows, macOS, Linux, Android, iOS", "#2a5298", "#ffffff"),
          ("Hardware: procesador, memoria, disco, pantalla…", "#374151", "#ffffff")]
body = ""
for i, (t, bg, fg) in enumerate(layers):
    w = 420 + i * 70
    x = (720 - w) / 2
    body += f'<rect x="{x}" y="{25+i*68}" width="{w}" height="56" rx="12" fill="{bg}" stroke="{NAVY}" stroke-width="2"/>' + text(360, 59 + i * 68, t, 16, fg, "700")
svg("capas_software.svg", 720, 310, "Capas: usuario, aplicaciones, sistema operativo y hardware", body)

# 8. Árbol de carpetas ---------------------------------------------------------
def folder(x, y, t, c=YELLOW):
    return (f'<path d="M{x},{y+6} h18 l6,-6 h26 v34 h-50 z" fill="{c}" stroke="#c9a227" stroke-width="1.5"/>' + text(x + 60, y + 24, t, 15, NAVY, "700", "start"))


def filei(x, y, t, ext, c):
    return (f'<path d="M{x},{y} h26 l10,10 v30 h-36 z" fill="#ffffff" stroke="{c}" stroke-width="2"/>'
            f'<rect x="{x+2}" y="{y+22}" width="32" height="12" rx="2" fill="{c}"/>' + text(x + 18, y + 32, ext, 9, "#ffffff", "800")
            + text(x + 48, y + 26, t, 15, NAVY, "600", "start"))


line = lambda x1, y1, x2, y2: f'<path d="M{x1},{y1} V{y2} H{x2}" fill="none" stroke="{GREY}" stroke-width="2"/>'
svg("arbol_carpetas.svg", 720, 380, "Árbol de carpetas de ejemplo con la ruta de un archivo",
    folder(30, 20, "Documentos")
    + line(55, 55, 90, 85) + folder(95, 70, "Instituto")
    + line(120, 105, 155, 135) + folder(160, 120, "Matemáticas")
    + line(185, 155, 220, 185) + filei(225, 165, "tarea_fracciones.odt", "ODT", "#2a5298")
    + line(120, 105, 155, 235) + folder(160, 220, "Inglés")
    + line(185, 255, 220, 285) + filei(225, 265, "presentacion_viaje.pdf", "PDF", CORAL)
    + f'<path d="M196,37 H550 V68" fill="none" stroke="{GREY}" stroke-width="2"/>' + folder(525, 70, "Fotos")
    + line(550, 105, 585, 135) + filei(590, 115, "playa.jpg", "JPG", GREEN)
    + f'<rect x="20" y="320" width="680" height="44" rx="10" fill="{LIGHT}" stroke="{TEAL}" stroke-width="2"/>'
    + text(36, 348, "Ruta:  Documentos › Instituto › Matemáticas › tarea_fracciones.odt", 15, NAVY, "700", "start"))

# 9. Red doméstica -------------------------------------------------------------
waves = lambda x, y: ''.join(f'<path d="M{x-r},{y} a{r},{r} 0 0 1 {2*r},0" fill="none" stroke="{TEAL}" stroke-width="4" stroke-linecap="round"/>' for r in (14, 26, 38))
svg("red_domestica.svg", 720, 360, "Red doméstica: Internet, router, dispositivos por cable y por wifi",
    f'<g transform="translate(270,10)"><circle cx="50" cy="50" r="34" fill="#bfefff"/><circle cx="95" cy="38" r="42" fill="#bfefff"/>'
    f'<circle cx="140" cy="55" r="30" fill="#bfefff"/><rect x="50" y="50" width="90" height="35" fill="#bfefff"/></g>'
    + text(365, 75, "INTERNET", 20, NAVY, "800")
    + f'<line x1="365" y1="100" x2="365" y2="150" stroke="{GREY}" stroke-width="5"/>' + text(352, 130, "fibra / ADSL / 5G", 13, GREY, "600", "end")
    + f'<rect x="300" y="150" width="130" height="50" rx="10" fill="{NAVY}"/>' + text(365, 181, "ROUTER", 16, "#ffffff", "800")
    + ''.join(f'<circle cx="{325+i*20}" cy="192" r="3" fill="{TEAL}"/>' for i in range(5))
    + waves(455, 165)
    + f'<line x1="300" y1="190" x2="130" y2="255" stroke="{GREY}" stroke-width="5"/>' + text(185, 210, "cable", 13, GREY, "700")
    + monitor(70, 250, 0.9)
    + f'<line x1="380" y1="200" x2="380" y2="245" stroke="{TEAL}" stroke-width="3" stroke-dasharray="5 5"/>'
    + f'<line x1="420" y1="195" x2="560" y2="250" stroke="{TEAL}" stroke-width="3" stroke-dasharray="5 5"/>' + text(510, 210, "wifi", 13, TEAL, "800")
    + phone(355, 250, 0.9) + laptop(510, 255, 0.85)
    + text(130, 352, "PC", 13, NAVY, "700") + text(378, 352, "Móvil", 13, NAVY, "700") + text(578, 352, "Portátil", 13, NAVY, "700"))

# 10. Ergonomía ----------------------------------------------------------------
svg("ergonomia.svg", 720, 380, "Postura correcta frente al ordenador",
    f'<rect x="380" y="230" width="300" height="14" rx="4" fill="#8d6e63"/><rect x="400" y="244" width="12" height="120" fill="#8d6e63"/><rect x="650" y="244" width="12" height="120" fill="#8d6e63"/>'
    + monitor(540, 108, 1.05) + keyboard(420, 205, 0.7)
    # silla
    + f'<rect x="180" y="250" width="130" height="16" rx="6" fill="{GREY}"/><rect x="175" y="130" width="18" height="135" rx="6" fill="{GREY}"/><rect x="236" y="266" width="10" height="70" fill="{GREY}"/>'
    + f'<rect x="200" y="336" width="90" height="8" rx="4" fill="{GREY}"/>'
    # persona
    + f'<circle cx="235" cy="95" r="26" fill="#f2c7a5"/><path d="M212,88 q23,-35 46,0" fill="#5d4037"/>'
    + f'<path d="M210,125 q25,-8 40,0 l10,125 h-55 z" fill="{TEAL}"/>'
    + f'<path d="M250,140 q40,40 165,70" fill="none" stroke="{TEAL}" stroke-width="16" stroke-linecap="round"/>'
    + f'<path d="M215,250 h120 v90" fill="none" stroke="{NAVY}" stroke-width="20" stroke-linejoin="round"/>'
    + f'<rect x="320" y="338" width="40" height="10" rx="4" fill="#1f2937"/>'
    # guías
    + f'<line x1="258" y1="92" x2="545" y2="135" stroke="{CORAL}" stroke-width="2" stroke-dasharray="6 5"/>'
    + text(300, 86, "ojos a la altura del borde superior", 13, CORAL, "700", "start")
    + f'<line x1="270" y1="65" x2="540" y2="65" stroke="{GREEN}" stroke-width="2" marker-end="url(#flecha)"/>' + DEFS
    + text(405, 55, "50–70 cm (un brazo)", 13, GREEN, "700")
    + text(120, 200, "espalda", 13, NAVY, "700", "end") + text(120, 216, "apoyada", 13, NAVY, "700", "end")
    + text(420, 300, "codos a 90°", 13, NAVY, "700", "start") + text(230, 372, "pies apoyados en el suelo", 13, NAVY, "700"))

# 11. Ficha técnica ------------------------------------------------------------
rows = [("Procesador", "8 núcleos, hasta 4,4 GHz", "cerebro: rapidez al trabajar"),
        ("Memoria RAM", "16 GB", "cuántas cosas abiertas a la vez"),
        ("Almacenamiento", "SSD 512 GB", "espacio para archivos y velocidad"),
        ("Gráfica", "integrada", "suficiente para clase y vídeo"),
        ("Pantalla", '15,6" Full HD (1920×1080)', "tamaño y nitidez"),
        ("Batería", "hasta 10 h (según fabricante)", "autonomía real: suele ser menor"),
        ("Sistema operativo", "preinstalado o sin SO", "comprueba si viene incluido")]
body = f'<rect x="20" y="16" width="680" height="44" rx="10" fill="{NAVY}"/>' + text(360, 45, "Portátil de ejemplo · Ficha técnica", 18, "#ffffff", "800")
for i, (k, v, h) in enumerate(rows):
    y = 72 + i * 42
    body += f'<rect x="20" y="{y}" width="680" height="36" rx="8" fill="{LIGHT if i % 2 else "#ffffff"}" stroke="#e5e7eb"/>'
    body += text(36, y + 24, k, 14, NAVY, "800", "start") + text(220, y + 24, v, 14, "#111827", "600", "start") + text(684, y + 24, "← " + h, 12, GREEN, "700", "end")
svg("ficha_tecnica.svg", 720, 380, "Ficha técnica de un portátil de ejemplo con la explicación de cada dato", body)

print("imágenes:", sorted(os.listdir(OUT)))
