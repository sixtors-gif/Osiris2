#!/usr/bin/env python3
"""Inserta actividades de arrastrar y soltar en los cursos SCORM (posproceso, repetible).

Para cada curso de cursos/ que tenga un fichero herramientas/dragdrop/<curso>.json:
  - copia dragdrop.js a la raíz del curso y añade (o actualiza) los estilos al final de style.css;
  - inserta cada actividad en su página, justo antes del punto indicado, y carga dragdrop.js en esa página.
Puede ejecutarse varias veces: las actividades llevan marcas <!--dd:ID-->…<!--/dd:ID--> y se sustituyen.
Orden recomendado: generadores → este script → scorm_seguimiento.py (para que dragdrop.js entre en el manifiesto) → empaquetar.sh.

Formato del JSON de un curso: una lista de actividades
  {"id": "m3-escalas", "pagina": "modulo3.html", "antes_de": "summary" | "nav" | "quiz" | "<texto HTML literal>",
   "tipo": "emparejar" | "clasificar" | "ordenar" | "rellenar" | "etiquetar", "titulo": "...", "instruccion": "...", ...}
  emparejar : "pares": [["Pregunta", "Respuesta"], ...], "extra": ["distractor", ...]
  clasificar: "categorias": ["A", "B"], "items": [["texto", índice de categoría], ...]
  ordenar   : "items": ["paso 1", "paso 2", ...]  (en el orden correcto; se muestran mezclados)
  rellenar  : "texto": "Una frase con {0} y {1}.", "huecos": ["palabra0", "palabra1"], "extra": ["distractor"]
  etiquetar : "imagen": "img/x.svg", "alt": "...", "ancho": 720, "zonas": [{"x": %, "y": %, "respuesta": "Texto", "punto": [x%, y%], "ancho": px}], "extra": [...]

Uso: python3 herramientas/insertar_dragdrop.py [curso ...]      (sin argumentos: todos los cursos con JSON)
     python3 herramientas/insertar_dragdrop.py --validar fichero.json curso
"""
import html, json, os, re, shutil, sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.join(AQUI, "..", "cursos")
DD = os.path.join(AQUI, "dragdrop")
ANCLAS = {"summary": '<div class="summary-box"', "nav": '<div class="navigation"', "quiz": '<div class="quiz"'}
CSS_INI, CSS_FIN = "/* dd:inicio */", "/* dd:fin */"
TIPOS = {"emparejar", "clasificar", "ordenar", "rellenar", "etiquetar"}


def validar_actividad(a, d=None):
    """Devuelve una lista de errores (vacía si la actividad es correcta)."""
    e = []
    for k in ("id", "pagina", "tipo"):
        if not a.get(k):
            e.append(f"falta «{k}»")
    if e:
        return e
    if not re.fullmatch(r"[\w-]+", a["id"]):
        e.append(f"{a['id']}: id no válido (solo letras, números, - y _)")
    t = a["tipo"]
    if t not in TIPOS:
        e.append(f"{a['id']}: tipo desconocido «{t}»")
        return e
    def textos(xs):
        return all(isinstance(x, str) and x.strip() for x in xs)
    if t == "emparejar":
        p = a.get("pares", [])
        if not (2 <= len(p) <= 10) or not all(isinstance(x, list) and len(x) == 2 and textos(x) for x in p):
            e.append(f"{a['id']}: «pares» debe tener de 2 a 10 pares de textos")
        elif len({x[1] for x in p}) != len(p):
            e.append(f"{a['id']}: las respuestas de «pares» deben ser distintas entre sí")
    elif t == "clasificar":
        c, it = a.get("categorias", []), a.get("items", [])
        if not (2 <= len(c) <= 4) or not textos(c):
            e.append(f"{a['id']}: «categorias» debe tener de 2 a 4 textos")
        if not (4 <= len(it) <= 14) or not all(isinstance(x, list) and len(x) == 2 and isinstance(x[0], str) and isinstance(x[1], int) and 0 <= x[1] < max(len(c), 1) for x in it):
            e.append(f"{a['id']}: «items» debe tener de 4 a 14 pares [texto, categoría]")
        elif len({x[1] for x in it}) < len(c):
            e.append(f"{a['id']}: todas las categorías deben tener al menos un elemento")
    elif t == "ordenar":
        it = a.get("items", [])
        if not (3 <= len(it) <= 9) or not textos(it):
            e.append(f"{a['id']}: «items» debe tener de 3 a 9 textos")
    elif t == "rellenar":
        h, tx = a.get("huecos", []), a.get("texto", "")
        if not (1 <= len(h) <= 8) or not textos(h):
            e.append(f"{a['id']}: «huecos» debe tener de 1 a 8 textos")
        elif sorted(int(x) for x in re.findall(r"\{(\d+)\}", tx)) != list(range(len(h))):
            e.append(f"{a['id']}: «texto» debe contener {{0}}…{{{len(h)-1}}} una vez cada uno")
    elif t == "etiquetar":
        z = a.get("zonas", [])
        if not a.get("imagen") or not (2 <= len(z) <= 12):
            e.append(f"{a['id']}: «etiquetar» necesita «imagen» y de 2 a 12 «zonas»")
        else:
            for k in z:
                if not (isinstance(k.get("x"), (int, float)) and isinstance(k.get("y"), (int, float)) and isinstance(k.get("respuesta"), str)):
                    e.append(f"{a['id']}: cada zona necesita x, y y respuesta")
            if len({k.get("respuesta") for k in z}) != len(z):
                e.append(f"{a['id']}: las respuestas de las zonas deben ser distintas")
            if d and not os.path.exists(os.path.join(d, a["imagen"])):
                e.append(f"{a['id']}: no existe la imagen {a['imagen']}")
    if d:
        p = os.path.join(d, a["pagina"])
        if not os.path.exists(p):
            e.append(f"{a['id']}: no existe la página {a['pagina']}")
        else:
            s = open(p, encoding="utf-8").read()
            ancla = ANCLAS.get(a.get("antes_de", "nav"), a.get("antes_de", ""))
            if ancla not in re.sub(r"<!--dd:.*?<!--/dd:[\w-]+-->", "", s, flags=re.S):
                e.append(f"{a['id']}: no se encuentra el punto de inserción {ancla!r} en {a['pagina']}")
    return e


def cfg_de(a):
    cfg = {k: v for k, v in a.items() if k not in ("id", "pagina", "antes_de")}
    return cfg


def bloque(a):
    cfg = html.escape(json.dumps(cfg_de(a), ensure_ascii=False, separators=(",", ":")), quote=True)
    return (f'<!--dd:{a["id"]}--><div class="dd" id="dd-{a["id"]}" data-config="{cfg}">'
            f'<noscript>Esta actividad necesita JavaScript.</noscript></div><!--/dd:{a["id"]}-->\n')


def procesar(nombre):
    d = os.path.join(RAIZ, nombre)
    f = os.path.join(DD, nombre + ".json")
    if not os.path.isfile(f) or not os.path.isdir(d):
        return None
    acts = json.load(open(f, encoding="utf-8"))
    errores = [m for a in acts for m in validar_actividad(a, d)]
    ids = [a["id"] for a in acts]
    if len(set(ids)) != len(ids):
        errores.append("hay ids repetidos")
    if errores:
        raise SystemExit(f"{nombre}:\n  " + "\n  ".join(errores))
    shutil.copy(os.path.join(DD, "dragdrop.js"), os.path.join(d, "dragdrop.js"))
    css = open(os.path.join(d, "style.css"), encoding="utf-8").read()
    css = re.sub(re.escape(CSS_INI) + r".*?" + re.escape(CSS_FIN) + r"\n?", "", css, flags=re.S)
    css += "\n" + CSS_INI + "\n" + open(os.path.join(DD, "dragdrop.css"), encoding="utf-8").read() + CSS_FIN + "\n"
    open(os.path.join(d, "style.css"), "w", encoding="utf-8").write(css)
    por_pagina = {}
    for a in acts:
        por_pagina.setdefault(a["pagina"], []).append(a)
    for pagina, lista in por_pagina.items():
        p = os.path.join(d, pagina)
        s = open(p, encoding="utf-8").read()
        s = re.sub(r"<!--dd:[\w-]+-->.*?<!--/dd:[\w-]+-->\n?", "", s, flags=re.S)   # quita las anteriores
        for a in lista:
            ancla = ANCLAS.get(a.get("antes_de", "nav"), a.get("antes_de", ""))
            i = s.index(ancla)
            s = s[:i] + bloque(a) + s[i:]
        if 'src="dragdrop.js"' not in s:
            s = s.replace('<script src="scorm.js"></script>', '<script src="dragdrop.js"></script>\n<script src="scorm.js"></script>', 1)
        assert 'src="dragdrop.js"' in s, pagina
        open(p, "w", encoding="utf-8").write(s)
    return len(acts), len(por_pagina)


if __name__ == "__main__":
    args = sys.argv[1:]
    if args and args[0] == "--validar":
        acts = json.load(open(args[1], encoding="utf-8"))
        d = os.path.join(RAIZ, args[2]) if len(args) > 2 else None
        err = [m for a in acts for m in validar_actividad(a, d)]
        ids = [a["id"] for a in acts]
        if len(set(ids)) != len(ids):
            err.append("hay ids repetidos")
        print("\n".join(err) if err else f"OK: {len(acts)} actividades válidas")
        sys.exit(1 if err else 0)
    cursos = args or sorted(os.listdir(RAIZ))
    for n in cursos:
        r = procesar(n)
        if r:
            print(f"{n}: {r[0]} actividades en {r[1]} páginas")
