class matrixNode:
    def __init__(self, color: str, posX: int, posY: int, flip: float, swap: float) -> None:
        self.color: str = color
        self.posX: int = posX
        self.posY: int = posY
        self.flip: float = flip
        self.swap: swap = swap
        self.next = None
        self.index = None
        self.up = None
        self.down = None
        self.prev = None
        self.block = False

class matrix:
    def __init__(self, rows: int , columns: int, code: str, counter: int ):
        self.head = None
        self.rows = rows
        self.columns = columns
        self.code: str = code
        self.counter: int = counter
        self.index = 0

        self.graphvizText = '''subgraph cluster_'''+str(self.counter)+''' {''''a' + str(self.counter) + ''' 
        [label=<
        <TABLE border="10" cellspacing="10" cellpadding="10" style="rounded" bgcolor="white" gradientangle="315">

                '''
    def writeGraph(self):
        n: matrixNode
        n = self.head
        while n != None:

            for i in range(int(self.rows)):
                self.graphvizText += '<TR>'
                for j in range(int(self.columns)):
                    if n.color.upper() == 'B':
                        self.graphvizText += '<TD border="3"  bgcolor="black">+'+ str(i) + str(j) + '</TD>'
                    elif n.color.upper() == 'W':
                        self.graphvizText += '<TD border="3"  bgcolor="white">'+ str(i) + str(j) +' </TD> \n'
                    n = n.next
                self.graphvizText += '</TR>'


    def returnGraphviz(self):
        #self.graphvizText += "}"
        self.graphvizText += ';</TABLE>>];  \n' + 'label = '+str(self.code) + '; }'
        return self.graphvizText


    def append(self, color, posX, posY, flip, swap) -> None:

        if self.head == None:
            firstPlate = matrixNode(color, posX, posY, flip, swap)
            print(color + str(posX) + str(posY) + '->', end='')
            self.head = firstPlate

        elif self.head != None:
            current = self.head
            row = current.posY
            while current.next != None:
                current = current.next
                current.prev = current
                row = current.posY
                line = current.posX
            newPlate = matrixNode(color, posX, posY, flip, swap)
            current.next = newPlate
            newPlate.prev = current

            if row != newPlate.posY:
                print(color + str(posX) + str(posY))
            else:
                print(color + str(posX) + str(posY) + '->', end='')

    def searchByPos(self, posY: int, posX: int):
        current_node = self.head
        while current_node is not None:
            if int(current_node.posY) == int(posY) and int(current_node.posX) == int(posX):
                return current_node
            current_node = current_node.next
        return None

    def orthogonalNodes(self, plate: matrixNode):
        upPlate = self.searchByPos(int(plate.posY) - 1, plate.posX)
        downPlate = self.searchByPos(int(plate.posY) + 1, plate.posX)
        leftPlate = self.searchByPos(int(plate.posY), plate.posX -1)
        rightPlate = self.searchByPos(int(plate.posY), plate.posX + 1)

        return upPlate, downPlate, leftPlate, rightPlate

    def appendWithIndex(self, color, posX, posY, flip, swap, index):
        if self.head == None:
            firstPlate = matrixNode(color, posX, posY, flip, swap)
            print(color + str(posX) + str(posY) + '->', end='')
            self.head = firstPlate
            firstPlate.index = index

        elif self.head != None:
            current = self.head
            row = current.posY
            while current.next != None:
                current = current.next
                current.prev = current
                row = current.posY
                line = current.posX
            newPlate = matrixNode(color, posX, posY, flip, swap)
            current.next = newPlate
            newPlate.prev = current
            newPlate.index = index

            if row != newPlate.posY:
                print(color + str(posX) + str(posY))
            else:
                print(color + str(posX) + str(posY) + '->', end='')

        pass

    def len(self):
        n = self.head
        while n != None:
            n = n.next
            self.index += 1

        return self.index



    def format(self):
        head = self.head
        while head.siguiente != None:
            print(head.index)
            head = head.siguiente


    def pop(self):
        if self.head is None:
            print("La lista no contiene Nodos para eliminar")
            return

        if self.head.next is None:
            self.head = None
            return
        pointer: matrixNode
        pointer = self.head
        while pointer.next is not None:
            pointer = pointer.next
        pointer.prev.next = None

    def delete(self, index):
        aux = self.head
        prev = None
        while aux and aux.index != index:
            prev = aux
            aux = aux.next
        if prev is None:
            self.head = aux.next
        elif aux:
            prev.next = aux.next
            aux.next = None



    def indexList(self):
        n: matrixNode
        n = self.head
        i = 0
        while n != None:
            n.index = i
            n = n.next
            i += 1


    def print(self):
        head = self.head
        while head != None:
            print(head.color, 'INDICE ', head.index)
            head = head.next



    def crearIndex(self):
        head = self.head
        i = 0
        while head != None:
            head.index = i
            head = head.siguiente
            i += 1

    def imprimirIndex(self):
        head = self.head
        while head != None:
            print(head.index)
            head = head.siguiente

    def changeColorByIndex(self, index: int, color: str):
        #Buscar Index
        head = self.head
        while head != None and head.index != index:
            head = head.next
        if head == None:
            print("No se encontro el nodo")
        else:
            head.color = color

    #Cambiar color del Index
    def swap(self, index1,color1,  index2, color2):
        print("Cambio Indice "+ str(index1) + ' Indice'+  str(index2))
        self.print()
        self.changeColorByIndex(index1, color1)
        self.print()
        self.changeColorByIndex(index2, color2)
        print("SWAP ENTRE " + str(index1) + ' y ' + str(index2))
        self.print()


    def flip(self, index, color):
        self.changeColorByIndex(index, color)















    def len(self):
        head = self.head
        len = 0
        while head != None:
            head = head.siguiente
            len += 1

        return len







def main():
    entrada = 'BWBWBWBWBWWWWWWBBBBB'
    print("Entrada Inicial: ")
    print(len(entrada))
    print("Cantidad de Columnas:")
    columns = 5
    print(str(columns))

    rows = len(entrada)/columns
    rows = int(rows)
    print("Cantidad de Filas: ")
    print(str(rows))
    nuevaMatriz: matrix
    nuevaMatriz = matrix(rows, columns, 'cod123')
    posX = 0
    posY = 0
    flip = 10.4
    swap = 10.4
    indx = 0
    for i in range(rows):
        posY += 1
        posX = 0
        for j in range(columns):
            indx +=1
            posX += 1
            nuevaMatriz.append(entrada[j], posX, posY, flip, swap, j)
    print("Matriz=Normal")
    nuevaMatriz.print()
    print("Matriz borrando el Nodo 4")
    nuevaMatriz.deleteByIndex(4)
    nuevaMatriz.print()
    print("Matriz with append al final")
    nuevaMatriz.appendWithIndex('B', 1, 1, 1)
    print("Test 1 ")
    nuevaMatriz.print()
    print("Matriz ")
    nuevaMatriz.bub


if __name__ == "__main__":
    main()
