from os import system, startfile
from models.piso import Piso, listaPisos
from models.nodes import designList, designNode
from models.matrixNode import matrix
from functions import graph
global option
option = True

def submenu(nombrePiso, pisos: listaPisos):

    while option == True:

        print("============= Analisis de Piso "+ nombrePiso + " =================================")
        print("| Dimensiones (Filas X Columnas) >>>" + 'data')
        print("|  1. Visualizar Opciones                                             |")
        print("|  2. Analizar Costo de Cambio                                        |")
        print("|  3. Salir                                                           |")
        print('=======================================================================')

        op = input('Ingresa una opción: ')
        if op == '1':
            print("===Ha visualizar opciones====")
            graph(nombrePiso, pisos)
        elif op == '2':
            inputMatrix: matrix
            outputMatrix: matrix
            print("===Analizar Costo de Cambio====")
            print("Por favor Ingrese el piso incial>>: ")
            inputPattern = str(input())
            print("Por favor Ingrese el piso final>>: ")
            outputPattern = str(input())
            print("Esta seguro que desea seguir? [Y/N]")
            designsList: designList
            designsList = pisos.search(nombrePiso).patrones
            inputMatrix = designsList.search(inputPattern).patron
            outputMatrix = designsList.search(outputPattern).patron

            #compare(inputMatrix, outputMatrix)
            print("Desea Realizar Cambio? [S/N] (S para Si, N para No)")

        elif op == '3':
            print("===Salir====")
            option = False





        elif op == '5':
            print("==================================")
            print("| Gracias por usar el Analizador |")
            print("==================================")
            break