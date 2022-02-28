from os import system, startfile
from models.piso import Piso, listaPisos
from models.matrixNode import matrix, matrixNode
from models.nodes import designList, designNode
def searchByPos(actualNode: matrixNode, matrix: matrix):
    pass

global option
option = True
def graph(name: str, listPisos: listaPisos):
    designsList: designList
    designsList = listPisos.search(name).patrones
    head: designNode
    head = designsList.head
    text = '''digraph Example{
        fontname="Helvetica,Arial,sans-serif"
        node [fontname="Helvetica,Arial,sans-serif"]
        edge [fontname="Helvetica,Arial,sans-serif"]'''
    text += '\n label = ' + name + ';'
    filename = name
    filename += '.dot'
    outputFileName = name + '.png'
    while head != None:
        head.patron.writeGraph()
        text += head.patron.returnGraphviz()
        head = head.next


    text += '}'
    text = text.replace("+", '')
    print(text)
    file = open(filename, 'w')
    file.write(str(text))
    file.close()

    system('dot -Tpng '+ filename + ' > '+ outputFileName)
    system('cd .')
    startfile(outputFileName)

def compare(inputMatrix: matrix, outputMatrix: matrix):
    proofMatrix: matrix
    head: matrixNode
    headInput: matrixNode
    headOutput: matrixNode
    headInput = inputMatrix.head
    headOutput = outputMatrix.head

    while headInput != None:

        if headInput.color != headOutput.color:
        #First, the robot need to watch the perifericals
            up, down, left, right = inputMatrix.orthogonalNodes(headInput)
        #Compare the Perifericals with headOutPut


        headOutput = headOutput.next
        headInput = headInput.next
    pass

