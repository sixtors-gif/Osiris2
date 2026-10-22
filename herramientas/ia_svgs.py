"""Dibujos del curso de IA (SVG)."""
import html

F = 'font-family="Segoe UI,Tahoma,sans-serif"'
MORADO, ACENTO, CLARO = "#4b3a8f", "#f59e0b", "#f3effc"


def _t(x, y, txt, size=13, color="#222", anchor="middle", peso=400):
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" text-anchor="{anchor}" font-weight="{peso}">{html.escape(txt)}</text>'


def _lineas(txt, n=17):
    l, cur = [], ""
    for p in txt.split(" "):
        if cur and len(cur) + 1 + len(p) > n:
            l.append(cur); cur = p
        else:
            cur = (cur + " " + p).strip()
    l.append(cur)
    return l


def linea_tiempo():
    ev = [(1950, "Turing: ¿pueden pensar las máquinas?"), (1956, "Dartmouth: nace el término «IA»"), (1966, "ELIZA, el primer chatbot"),
          (1997, "Deep Blue gana a Kasparov"), (2012, "Deep learning: AlexNet gana ImageNet"), (2016, "AlphaGo gana a Lee Sedol"),
          (2017, "Transformers: «Attention is all you need»"), (2022, "ChatGPT llega al gran público"), (2023, "Primer Claude, de Anthropic")]
    paso, x0, y = 100, 70, 170
    c = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 340" width="960" height="340" role="img" aria-label="Línea de tiempo de la inteligencia artificial de 1950 a 2023" {F}>',
         '<rect width="960" height="340" fill="#fff"/>',
         f'<line x1="30" y1="{y}" x2="930" y2="{y}" stroke="{MORADO}" stroke-width="5" stroke-linecap="round"/>']
    for k, (a, txt) in enumerate(ev):
        x = x0 + k * paso
        arriba = k % 2 == 0
        c.append(f'<line x1="{x}" y1="{y}" x2="{x}" y2="{y-48 if arriba else y+48}" stroke="#b9afd6" stroke-width="1.5"/>')
        c.append(f'<circle cx="{x}" cy="{y}" r="9" fill="{ACENTO}" stroke="#fff" stroke-width="2"/>')
        base = y - 100 if arriba else y + 70
        c.append(_t(x, base - 8 if arriba else base, str(a), 15, MORADO, peso=700))
        for n, linea in enumerate(_lineas(txt)):
            c.append(_t(x, (base + 8 + n * 14) if arriba else (base + 16 + n * 14), linea, 11.5, "#333"))
    c.append(f'<rect x="{x0+2*paso+20}" y="{y+82+0}" width="0" height="0"/>')
    c.append(f'<rect x="{x0+2*paso+30}" y="{y-8}" width="{paso-60}" height="16" rx="8" fill="#9fb4d6" opacity=".85"/>')
    c.append(_t(x0 + 2 * paso + 30 + (paso - 60) / 2, y + 28, "«inviernos de la IA»", 10.5, "#3b5b8f"))
    c.append(_t(480, 322, "Los años no están a escala: entre 1966 y 1997 pasaron décadas de altibajos; entre 2012 y 2023, solo once años.", 11, "#777"))
    c.append("</svg>")
    return "\n".join(c)


def red_neuronal():
    capas = [("Entrada", 4), ("Capas ocultas", 5), ("Capas ocultas", 5), ("Salida", 2)]
    c = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 300" width="640" height="300" role="img" aria-label="Esquema de una red neuronal con capa de entrada, capas ocultas y capa de salida" {F}>',
         '<rect width="640" height="300" fill="#fff"/>']
    pos = []
    for i, (nombre, n) in enumerate(capas):
        x = 90 + i * 150
        col = [(150 - (n - 1) * 24 + j * 48) for j in range(n)]
        pos.append([(x, yy) for yy in col])
    for i in range(len(pos) - 1):
        for a in pos[i]:
            for b in pos[i + 1]:
                c.append(f'<line x1="{a[0]}" y1="{a[1]}" x2="{b[0]}" y2="{b[1]}" stroke="#c5bde0" stroke-width="1"/>')
    for i, (nombre, n) in enumerate(capas):
        for (x, yy) in pos[i]:
            col = {0: "#f59e0b", 3: "#16a34a"}.get(i, MORADO)
            c.append(f'<circle cx="{x}" cy="{yy}" r="13" fill="{col}" stroke="#fff" stroke-width="2"/>')
        c.append(_t(90 + i * 150, 286, nombre, 12, "#555", peso=700))
    c.append(_t(90, 16, "Datos", 12, "#b45309", peso=700)); c.append(_t(540, 16, "Resultado", 12, "#15803d", peso=700))
    c.append("</svg>")
    return "\n".join(c)


def flujo_llm():
    cajas = [("1. Tu mensaje", "«Escribe una reseña…»", "#f59e0b"), ("2. Tokens", "trozos de palabra", "#a78bfa"),
             ("3. El modelo", "calcula probabilidades", MORADO), ("4. Siguiente token", "elige uno y lo añade", "#16a34a")]
    c = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 220" width="900" height="220" role="img" aria-label="Cómo genera texto un modelo de lenguaje: mensaje, tokens, modelo y siguiente token, en bucle" {F}>',
         '<rect width="900" height="220" fill="#fff"/>',
         '<defs><marker id="fl" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#555"/></marker></defs>']
    for i, (t, s, col) in enumerate(cajas):
        x = 20 + i * 220
        c.append(f'<rect x="{x}" y="50" width="180" height="80" rx="14" fill="{col}"/>')
        c.append(_t(x + 90, 85, t, 15, "#fff", peso=700)); c.append(_t(x + 90, 108, s, 12, "#fff"))
        if i < 3:
            c.append(f'<line x1="{x+184}" y1="90" x2="{x+216}" y2="90" stroke="#555" stroke-width="2.5" marker-end="url(#fl)"/>')
    c.append('<path d="M770 132 Q770 190 440 190 Q110 190 110 132" fill="none" stroke="#555" stroke-width="2.5" stroke-dasharray="7 5" marker-end="url(#fl)"/>')
    c.append(_t(440, 182, "…y se repite palabra a palabra hasta terminar la respuesta", 13, "#555"))
    c.append("</svg>")
    return "\n".join(c)


def tipos_ia():
    c = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 360" width="640" height="360" role="img" aria-label="Rectángulos anidados: inteligencia artificial, aprendizaje automático, aprendizaje profundo e IA generativa" {F}>',
         '<rect width="640" height="360" fill="#fff"/>']
    cap = [("Inteligencia artificial", "máquinas que hacen tareas que requieren inteligencia", "#ede9fe"),
           ("Aprendizaje automático", "aprende de ejemplos, no de reglas escritas a mano", "#ddd6fe"),
           ("Aprendizaje profundo", "redes neuronales con muchas capas", "#c4b5fd"),
           ("IA generativa", "crea texto, imágenes… (Claude)", "#a78bfa")]
    for i, (nombre, sub, col) in enumerate(cap):
        x, y, w, h = 20 + 40 * i, 12 + 46 * i, 600 - 80 * i, 336 - 46 * i - 12
        c.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="20" fill="{col}" stroke="#6d5bb5" stroke-width="1.5"/>')
        c.append(_t(320, y + 25, nombre, 15, "#2e1f6b", peso=700)); c.append(_t(320, y + 42, sub, 11.5, "#4a3a7a"))
    c.append("</svg>")
    return "\n".join(c)
