
class Piso:
         #Nombre, R, C, F, S, PATRONES (Sera una lista de listas)
    def __init__(self, name: str, rows: int, columns: int,flip: float, swap: float, patrones, counter: int, next, prev) -> None:
        self.name:  str = name
        self.rows: float = rows
        self.columns: int = columns
        self.flip: float = flip
        self.swap: swap = swap
        self.patrones = patrones
        self.counter: int = counter
        self.next = next
        self.prev = prev

class listaPisos:
    def __init__(self, head=None) -> None:
        self.head = head
        self.tail = None

    def append(self, name, rows, columns, flip, swap, patrones, counter):
        if self.head == None:
            firstNode = Piso(name, rows, columns, flip, swap, patrones, counter, None, None)
            print(name + '->', end='')
            self.head = firstNode
        elif self.head != None:
            copiaHead = self.head
            while copiaHead.next != None:
                copiaHead = copiaHead.next
                copiaHead.prev = copiaHead
            newNode = Piso(name, rows, columns, flip, swap, patrones, counter, None, copiaHead)
            copiaHead.next = newNode
            print(name + '->', end='')
        pass
    def pop(self):
        pass
    #position
    def delete(self):
        pass
    def search(self, name):
        current_node = self.head
        while current_node is not None:
            if current_node.name == name:
                return current_node
            current_node = current_node.next_node
        return False
        pass
    def isIn(self,name) -> bool:
        current_node = self.head
        while current_node is not None:
            if current_node.name == name:
                return True
            current_node = current_node.next_node
        return False



