from xml.dom import minidom
import xml.dom.minidom
from xml.dom.minidom import parse, parseString
from models.nodes import Node, graphList


def analyzeXML(filename):
    patterns: list = []
    rows: int = 0
    columns: int = 0
    flip: float = 0
    swap: float = 0

    #domtree = xml.dom.minidom.parse(filename)
    #pisosArtesanales = domtree.documentElement

    #pisos = pisosArtesanales.getElementsByTagName('piso')
    #for piso in pisos:
       # print('========PISO=================')
        #if piso.hasAttribute('nombre'):
            #print('NOMBRE: {} '.format(piso.getAttribute('nombre')))



    doc = minidom.parse(filename)

    #We know that there is just one pisosArtesanales Tag
    pisosArtesanales = doc.getElementsByTagName("pisosArtesanales")


    pisos = doc.getElementsByTagName("piso")
    #print(pisos.data)
    row = 0
    rowPatterns = 0
    for piso in pisos:
        row += 1
        nombrePiso = piso.getAttribute("nombre")
        rows = piso.getElementsByTagName("R")[0]
        columns = piso.getElementsByTagName("C")[0]
        flipPrice = piso.getElementsByTagName("F")[0]
        swapPrice = piso.getElementsByTagName("S")[0]
        print("----------PISO " + str(row) + '--------')
        print('Nombre Piso', nombrePiso)
        print("Rows ->", rows.firstChild.data)
        print("Columns ->", columns.firstChild.data)
        print("FlipPrice ->", flipPrice.firstChild.data)
        print("Swap Price ->", swapPrice.firstChild.data)

        patrones = doc.getElementsByTagName("patron")
        print("============ PATRONES de Piso "+str(row)+'=======')
        for patron in patrones:
            code = patron.getAttribute("codigo")
            pattern = piso.getElementsByTagName("patron")[0]
            print("Codigo", code)
            patternAux = pattern.firstChild.data
            patternAux = patternAux.replace(" ", "")
            print('Patron',patternAux )



