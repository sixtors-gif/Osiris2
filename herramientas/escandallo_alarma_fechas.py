#!/usr/bin/env python3
"""Crea Alarma_fechas_practica.ods para el curso de Escandallo.

Hoja «Ficha»: cabecera de una ficha de receta (A1:B3) con la alarma de antigüedad en B2.
Hoja «Pruebas»: tres fechas relativas a hoy (10, 40 y 75 días) para ver los tres estados.

La alarma usa dos estilos de celda y un formato condicional con DOS condiciones, en este orden:
  1. El valor de la celda es <= AHORA()-60  → estilo «Precio caducado» (rojo)
  2. El valor de la celda es <= AHORA()-30  → estilo «Precio antiguo»  (naranja)
El orden importa: Calc aplica la PRIMERA condición que se cumple, y una fecha de hace
70 días también es <= AHORA()-30.

Uso: python3 herramientas/escandallo_alarma_fechas.py cursos/Curso_Escandallo_Catering_SCORM/Alarma_fechas_practica.ods
Requiere LibreOffice (soffice) y su módulo de Python «uno».
"""
import datetime, os, subprocess, sys, time

import uno
from com.sun.star.beans import PropertyValue

RUTA = os.path.abspath(sys.argv[1])
ESTILOS = {  # nombre: (fondo, color de letra)
    "Precio caducado": (0xF4B6B6, 0x9C0006),
    "Precio antiguo": (0xFFD8A8, 0x7A4100),
}
CONDICIONES = [("NOW()-60", "Precio caducado"), ("NOW()-30", "Precio antiguo")]


def prop(nombre, valor):
    p = PropertyValue(); p.Name = nombre; p.Value = valor
    return p


proc = subprocess.Popen(["soffice", "--headless", "--invisible", "--norestore", "-env:UserInstallation=file:///tmp/lo_perfil_escandallo",
                         "--accept=socket,host=127.0.0.1,port=2083;urp;"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
desktop = None
try:
    local = uno.getComponentContext()
    resolver = local.ServiceManager.createInstanceWithContext("com.sun.star.bridge.UnoUrlResolver", local)
    for _ in range(60):
        try:
            ctx = resolver.resolve("uno:socket,host=127.0.0.1,port=2083;urp;StarOffice.ComponentContext"); break
        except Exception:
            time.sleep(0.5)
    desktop = ctx.ServiceManager.createInstanceWithContext("com.sun.star.frame.Desktop", ctx)
    doc = desktop.loadComponentFromURL("private:factory/scalc", "_blank", 0, (prop("Hidden", True),))
    es = uno.createUnoStruct("com.sun.star.lang.Locale"); es.Language, es.Country = "es", "ES"
    doc.CharLocale = es  # documento en español (España)

    # Código de formato en notación inglesa (YYYY); Calc lo muestra igual en español (AAAA)
    en = uno.createUnoStruct("com.sun.star.lang.Locale"); en.Language, en.Country = "en", "US"
    fmt = doc.NumberFormats.queryKey("DD/MM/YYYY", en, False)
    if fmt < 0:
        fmt = doc.NumberFormats.addNew("DD/MM/YYYY", en)

    # 1) Estilos de celda
    familia = doc.StyleFamilies.getByName("CellStyles")
    for nombre, (fondo, letra) in ESTILOS.items():
        est = doc.createInstance("com.sun.star.style.CellStyle")
        familia.insertByName(nombre, est)
        est.CellBackColor = fondo
        est.CharColor = letra
        est.CharWeight = 150.0      # negrita
        est.NumberFormat = fmt      # la fecha se sigue viendo como fecha

    # Estilo base para las fechas (sin alarma): así todas se ven como DD/MM/AAAA
    base = doc.createInstance("com.sun.star.style.CellStyle")
    familia.insertByName("Fecha", base)
    base.NumberFormat = fmt
    base.HoriJustify = uno.Enum("com.sun.star.table.CellHoriJustify", "RIGHT")

    LESS_EQUAL = uno.Enum("com.sun.star.sheet.ConditionOperator", "LESS_EQUAL")

    def alarma(celda):
        entradas = celda.ConditionalFormat
        entradas.clear()
        for formula, estilo in CONDICIONES:       # 60 días PRIMERO
            entradas.addNew((prop("Operator", LESS_EQUAL), prop("Formula1", formula), prop("StyleName", estilo)))
        celda.ConditionalFormat = entradas

    # 2) Hoja «Ficha»
    hojas = doc.Sheets
    ficha = hojas.getByIndex(0); ficha.Name = "Ficha"
    for ref, valor in (("A1", "Nombre:"), ("A2", "Fecha:"), ("A3", "Raciones:"), ("B1", "Porra Archidonesa")):
        ficha.getCellRangeByName(ref).String = valor
    ficha.getCellRangeByName("B3").Value = 10
    ficha.getCellRangeByName("A1:A3").CharWeight = 150.0
    b2 = ficha.getCellRangeByName("B2")
    b2.Value = (datetime.date(2025, 1, 10) - datetime.date(1899, 12, 30)).days  # número de serie de Calc
    b2.CellStyle = "Fecha"
    b2.NumberFormat = fmt
    alarma(b2)
    ficha.getCellRangeByName("A5").String = "Cambia la fecha de B2 por la de hoy y la alarma desaparece."
    ficha.getCellRangeByName("A6").String = "En la hoja «Pruebas» verás los tres estados."
    ficha.Columns.getByIndex(0).Width = 2600
    ficha.Columns.getByIndex(1).Width = 4200

    # 3) Hoja «Pruebas»: fechas relativas a hoy
    hojas.insertNewByName("Pruebas", 1)
    pr = hojas.getByName("Pruebas")
    pr.getCellRangeByName("A1").String = "Precios revisados…"
    pr.getCellRangeByName("B1").String = "Fecha"
    pr.getCellRangeByName("C1").String = "Qué debe verse"
    pr.getCellRangeByName("A1:C1").CharWeight = 150.0
    for fila, (dias, txt) in enumerate(((10, "Sin color: precios recientes"), (40, "Naranja: más de 30 días"), (75, "Rojo: más de 60 días")), start=2):
        pr.getCellRangeByName(f"A{fila}").String = f"hace {dias} días"
        c = pr.getCellRangeByName(f"B{fila}")
        # Primero el formato y después la fórmula: si la celda ya tiene formato,
        # Calc no le aplica su formato de fecha automático (que depende del idioma)
        c.CellStyle = "Fecha"
        c.NumberFormat = fmt
        c.Formula = f"=TODAY()-{dias}"
        alarma(c)
        pr.getCellRangeByName(f"C{fila}").String = txt
    for i, w in enumerate((3600, 3200, 6200)):
        pr.Columns.getByIndex(i).Width = w

    # Comprobación: condiciones leídas de vuelta
    for c in (b2, pr.getCellRangeByName("B4")):
        cf = c.ConditionalFormat
        print([(cf.getByIndex(i).Formula1, cf.getByIndex(i).StyleName) for i in range(cf.Count)])

    doc.storeToURL(uno.systemPathToFileUrl(RUTA), (prop("FilterName", "calc8"),))
    doc.close(True)
finally:
    try:
        if desktop:
            desktop.terminate()
    except Exception:
        pass
    time.sleep(1)
    proc.terminate()
print("Creado:", RUTA)
