"""Funciones de maquetación compartidas por los módulos del curso de saxofón alto."""
import html

from piano_explicaciones import caja, como, errores, lista, palabras, pasos, practica, tabla  # noqa: F401
from saxo_partituras import PIEZAS


def fig(img, alt, cap):
    return f'<div class="figure"><img src="img/{img}" alt="{html.escape(alt, quote=True)}"><div class="figure-caption">{cap}</div></div>'


def kp(items, ico):
    return '<ul class="key-points">' + "".join(f"<li>{ico} <span>{i}</span></li>" for i in items) + "</ul>"


def quiz(qid, q, opts, ok, why):
    b = "".join(f'<button class="option" onclick="checkAnswer(this,{str(j == ok).lower()},\'{qid}\')">{chr(65+j)}. {o}</button>' for j, o in enumerate(opts))
    return f'<div class="quiz"><h4>🧩 {q}</h4><div class="options">{b}</div><p class="feedback" id="fb-{qid}" data-ok="{html.escape(why, quote=True)}"></p></div>'


def actividad(t, txt, ph):
    return f'<div class="activity"><h3>🎷 {t}</h3><p>{txt}</p><textarea placeholder="{ph}"></textarea></div>'


def partitura(clave):
    p = PIEZAS[clave]
    modo = ""
    if p["acomp"]:
        modo = (f'<label>Sonido <select id="s-{clave}"><option value="todo" selected>Saxo + acompañamiento</option>'
                f'<option value="saxo">Solo saxo</option><option value="acomp">Solo acompañamiento (toca tú)</option></select></label>')
    return (f'<div class="score-box"><h4>🎼 {p["titulo"]}</h4><div class="score" id="p-{clave}"></div>'
            f'<div class="score-tools"><button onclick="tocar(\'{clave}\')">▶ Escuchar</button><button class="stop" onclick="parar()">■ Parar</button>'
            f'<label>Velocidad <select id="v-{clave}"><option value="0.5">50 %</option><option value="0.75">75 %</option><option value="1" selected>100 %</option></select></label>'
            + modo + f'<span class="score-msg" id="m-{clave}"></span></div>'
            + (f'<p class="score-note">{p["nota"]}</p>' if p["nota"] else "") + "</div>")


def digitacion(img, alt, cap):
    """Figura con digitaciones (SVG generado por el programa)."""
    return fig(img, alt, cap)
