class matrixNode:
    def __init__(self, color: str, posX: int, posY: int, flip: float, swap: float, next) -> None:
        self.color: str = color
        self.posX: int = posX
        self.posY: int = posY
        self.flip: float = flip
        self.swap: swap = swap
        self.next = next

class matrix:
    def __init__(self, rows: int , columns: int, code: str, counter: int ):
        self.head = None
        self.rows = rows
        self.columns = columns
        self.code: str = code
        self.counter: int = counter
        #self.graphvizText = '''
                    #digraph Example{
                      #fontname="Helvetica,Arial,sans-serif"
                      #node [fontname="Helvetica,Arial,sans-serif"]
                     # edge [fontname="Helvetica,Arial,sans-serif"]
                      #
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
            firstPlate = matrixNode(color, posX, posY, flip, swap, None)
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
            newPlate = matrixNode(color, posX, posY, flip, swap, None )
            current.next = newPlate

            if row != newPlate.posY:
                print(color + str(posX) + str(posY))
            else:
                print(color + str(posX) + str(posY) + '->', end='')

    def insert(self):
        pass
    def delete(self):
        pass
    def pop(self):
        pass
    def move(self):
        pass

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
    nuevaMatriz = matrix()
    posX = 0
    posY = 0
    flip = 10.4
    swap = 10.4
    for i in range(rows):
        posY += 1
        posX = 0
        for j in range(columns):
            posX += 1
            nuevaMatriz.append(entrada[j], posX, posY, flip, swap)


if __name__ == "__main__":
    main()
