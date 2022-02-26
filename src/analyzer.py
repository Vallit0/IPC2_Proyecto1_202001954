from xml.dom import minidom
from models.piso import Piso, listaPisos
from models.nodes import designNode, designList
from models.matrixNode import matrixNode, matrix
from typing import Tuple
import xml.dom.minidom
from xml.dom.minidom import parse, parseString

def fillMatrix(rows, columns, color, matrix, flip, swap) -> None:
    posX = 0
    posY = 0
    for i in range(rows):
        posY += 1
        posX = 0
        for j in range(columns):
            posX += 1
            matrix.append(color[j], posX, posY, flip, swap)

def analyzeXML(filename, listaPisos):
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
        print("")
        print("----------PISO " + str(row) + '--------')
        print('Nombre Piso', nombrePiso)
        name = nombrePiso
        print("Rows ->", rows.firstChild.data)
        rowN  = rows.firstChild.data
        print("Columns ->", columns.firstChild.data)
        column = columns.firstChild.data
        print("FlipPrice ->", flipPrice.firstChild.data)
        flipPRICE = flipPrice.firstChild.data
        print("Swap Price ->", swapPrice.firstChild.data)
        swapPRICE = swapPrice.firstChild.data
        print("============ PATRONES de Piso "+str(row)+'=======')
        patrones = piso.getElementsByTagName('patron')

        #Crear un piso y anadirlo a la lista proporcionada
        #Patrones sera la lista de matrices
        designs = designList()

        for i in range(len(patrones)):
            #Crear una matriz
            print("")
            print("----------Patron"+str(rowPatterns)+'---------')
            print("Codigo >>" + patrones[i].getAttribute('codigo'))
            print("Patron >>" + patrones[i].firstChild.data.replace(" ", "").replace("\n", "").replace("\t", ""))
            rowPatterns += 1
            print("======MATRIX=====")
            newMatrix = matrix(rowN, column,patrones[i].getAttribute('codigo'))
            fillMatrix(int(rows.firstChild.data), int(columns.firstChild.data), patrones[i].firstChild.data.replace(" ", "").replace("\n", "").replace("\t", ""),newMatrix, float(flipPRICE), float(swapPRICE))
            #Anadir matriz a lista de matrices
            print("")
            designs.append(newMatrix, nombrePiso)

        print('')
        listaPisos.append(name, rowN, column, flipPRICE, swapPRICE, designs, row)

    return listaPisos



