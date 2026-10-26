"""Digitaciones del saxo alto (tono escrito) y dibujos SVG del curso.

FING[nota] = dict(oct=bool, lh=[dedos de la mano izquierda], rh=[dedos de la mano derecha],
                  lp='G♯'|'C♯'|'B'|'B♭'|None (meñique izquierdo), rp='E♭'|'C'|None (meñique derecho))
Las notas se nombran con el sistema español y número de octava científica (Do4 = Do central).
El registro agudo (Re5-Do♯6) repite la digitación del grave con la llave de octava.
"""
import html

import saxo_dibujos as sd

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
    return sd.diagrama(x, nombre, f, con_nombre)


def svg_digitaciones(nombres, titulo, con_nombre=True):
    """Un dibujo con varias digitaciones, una junto a otra."""
    cuerpo, x = [], 0
    for n in nombres:
        d, w = _diagrama(x, n, FING[n], con_nombre)
        cuerpo.append(d); x += w
    ancho = x + 6
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {ancho} 316" width="{ancho}" height="316" role="img" aria-label="{html.escape(titulo, quote=True)}" '
            f'font-family="Segoe UI,Tahoma,sans-serif">' + sd.DEFS + f'<rect width="{ancho}" height="316" fill="#fffaf0"/>' + "".join(cuerpo) + "</svg>")


def svg_diagrama_digitacion_js():
    """JSON con las digitaciones para el entrenador de digitaciones."""
    import json
    return json.dumps({k: FING[k] for k in REGISTRO_GRAVE + REGISTRO_AGUDO}, ensure_ascii=False)


def svg_partes(etiquetas=True, puntos=False):
    """Saxo alto con sus partes (dibujo realista de saxo_dibujos.py)."""
    return sd.svg_partes(etiquetas, puntos)


def svg_familia():
    """Los saxofones de la familia, a escala aproximada, con su tonalidad."""
    return sd.svg_familia()
