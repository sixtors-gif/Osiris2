"""Maquetación para el curso «Inteligencia artificial para jóvenes: aprende con Claude»."""
import html

from piano_explicaciones import caja, como, errores, lista, palabras, pasos, practica, tabla  # noqa: F401


def fig(img, alt, cap):
    return f'<div class="figure"><img src="img/{img}" alt="{html.escape(alt, quote=True)}"><div class="figure-caption">{cap}</div></div>'


def kp(items, ico):
    return '<ul class="key-points">' + "".join(f"<li>{ico} <span>{i}</span></li>" for i in items) + "</ul>"


def quiz(qid, q, opts, ok, why):
    b = "".join(f'<button class="option" onclick="checkAnswer(this,{str(j == ok).lower()},\'{qid}\')">{chr(65+j)}. {o}</button>' for j, o in enumerate(opts))
    return f'<div class="quiz"><h4>🧩 {q}</h4><div class="options">{b}</div><p class="feedback" id="fb-{qid}" data-ok="{html.escape(why, quote=True)}"></p></div>'


def actividad(t, txt, ph):
    return f'<div class="activity"><h3>✍️ {t}</h3><p>{txt}</p><textarea placeholder="{ph}"></textarea></div>'


def prompt(texto, titulo="Prompt para probar"):
    """Cuadro con un texto para copiar y pegar en Claude."""
    return (f'<div class="prompt"><div class="prompt-t">💬 {titulo}</div><pre>{html.escape(texto)}</pre>'
            '<button type="button" onclick="copiar(this)">📋 Copiar</button></div>')


def respuesta(texto, titulo="Ejemplo de respuesta (ilustrativo)"):
    """Ejemplo de respuesta escrito para el curso; no es una salida literal de Claude."""
    return f'<div class="respuesta"><div class="resp-t">🤖 {titulo}</div>{texto}</div>'


def hosteleria(texto):
    return f'<div class="hosteleria"><b>🍽️ En la hostelería:</b> {texto}</div>'


def cuidado(texto):
    return f'<div class="alert-box"><b>⚠️ Ojo:</b> {texto}</div>'
