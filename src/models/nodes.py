from colorama import *
class designNode:
    def __init__(self, name: str,  patron, code) -> None:
        self.name: str = name
        self.patron = patron
        self.code = code
        self.next = None


class designList:
    def __init__(self):
        self.head = None
        self.index = 0
    def append(self, patron, name: str, code: str) -> None:
        if self.head == None:
            firstPattern = designNode(name, patron, code)
            print(name  + '->', end='')
            self.head = firstPattern
        elif self.head != None:
            current = self.head
            while current.next != None:
                current = current.next
                current.prev = current
            newPlate = designNode(name, patron, code)
            current.next = newPlate
            print(name + '->', end='')

    def len(self):
        n = self.head
        while n != None:
            n = n.next
            self.index += 1
        return self.index

    def search(self, code):
        current_node: designNode
        current_node = self.head
        while current_node is not None:
            if current_node.code == code:
                return current_node
            current_node = current_node.next
        return False
    def print(self):
        head = self.head
        print(Back.LIGHTMAGENTA_EX)
        print(Fore.BLACK)
        while head != None:
            print(head.code, end='->')
            head = head.next
        print(Style.RESET_ALL)



