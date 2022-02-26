from os import system, startfile
from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename
from models.matrixNode import matrix
from tkinter import filedialog as fd
from analyzer import analyzeXML
from models.piso import Piso, listaPisos
from models.nodes import designList, designNode
global option
option = True
def graph(name: str, listPisos: listaPisos):
    designsList: designList
    designsList = listPisos.search(name).patrones
    #Iterate throughout design list and create graphviz
    #for i in range(int(designsList.len())):
        #designsList
        #pass
    head: designNode
    head = designsList.head
    text = '''
                    digraph Example{
                      fontname="Helvetica,Arial,sans-serif"
                      node [fontname="Helvetica,Arial,sans-serif"]
                      edge [fontname="Helvetica,Arial,sans-serif"]
                      
            '''

    text += 'label = ' + name + ';'
    filename = name
    filename += '.dot'
    outputFileName = name + '.png'
    while head != None:
        #filename: str = head.patron.code
        #outputFileName = filename
        #filename += '.dot'
        #outputFileName += '.svg'

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




    pass



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
            #Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
            #filename = fd.askopenfilename(title="Select file", filetypes=(("PNG Files", "*.png"), ("All", "*.txt")))
            #print(filename)
            #file = open(filename,encoding="utf8" )
            #pisos = listaPisos()
            #analyzeXML(file)
            #First

            # process_file(tokens, errs)
        elif op == '2':
            print("===Cargar Instrucciones====")
            filename = askopenfilename()
            filereader = ''
            filereader = open(filename, 'r+', encoding='utf-8')
            current_file = filereader.read()
            #tokens, errs = automata(current_file)
            # images = analizador(tokens)
            # for img in images:
            # lst_images.append(img)

        elif op == '3':
            print("===Analizar====")
            contador: int = 0





        elif op == '5':
            print("==================================")
            print("| Gracias por usar el Analizador |")
            print("==================================")
            break