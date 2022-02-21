from xml.dom import minidom
from typing import Tuple
import xml.dom.minidom
from xml.dom.minidom import parse, parseString
from models.nodes import Node, graphList


def analyzeXML(filename) -> Tuple[Tuple[list]]:
    rows: int = 0
    columns: int = 0
    flip: float = 0
    swap: float = 0
    patterns: list = []

    doc = minidom.parse(filename)
    pisos = doc.getElementsByTagName("piso")
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
        print("============ PATRONES de Piso "+str(row)+'=======')
        patrones = piso.getElementsByTagName('patron')

        for i in range(len(patrones)):
            print("----------Patron"+str(rowPatterns)+'---------')
            print(patrones[i].getAttribute('codigo'))
            print(patrones[i].firstChild.data.replace(" ", "").replace("\n", "").replace("\t", ""))
            print(rowPatterns)





