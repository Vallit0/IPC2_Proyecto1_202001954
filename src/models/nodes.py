class designNode:
    def __init__(self, name: str,  patron) -> None:
        self.name: str = name
        self.patron = patron
        self.next = None


class designList:
    def __init__(self):
        self.head = None
        self.index = 0
    def append(self, patron, name: str) -> None:
        if self.head == None:
            firstPattern = designNode(name, patron)
            print(name  + '->', end='')
            self.head = firstPattern
        elif self.head != None:
            current = self.head
            while current.next != None:
                current = current.next
                current.prev = current
            newPlate = designNode(name, patron)
            current.next = newPlate
            print(name + '->', end='')

    def len(self):
        n = self.head
        while n != None:
            n = n.next
            self.index += 1
        return self.index

    def search(self, code):
        current_node = self.head
        while current_node is not None:
            if current_node.code == code:
                return current_node
            current_node = current_node.next
        return False

    def insert(self):
        pass

    def delete(self):
        pass

    def pop(self):
        pass

    def move(self):
        pass

