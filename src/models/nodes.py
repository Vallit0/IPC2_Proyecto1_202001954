class Node:
    def __init__(self, data, next, prev, nodeList):
        self.data = data
        self.next = None
        self.prev = None
        self.nodeList = None


class graphList:
    def __init__(self):
        self.head = None
        self.graphvizText = '''
            digraph Example{

        '''

    def add(self, data):
        if self.head is None:
            nuevo_nodo = Node(data, None, None)
            self.head = nuevo_nodo
        else:
            current = self.head
            while current.next:
                current = current.next
                current.prev = current
            current.next = Node(data, None, None)

    def print_list(self):
        n = self.head
        while n != None:
            self.graphvizText += str(n.data)
            print(n.data, end="->")
            n = n.next
            if n != None:
                self.graphvizText += "->"

    def returnGraphviz(self):
        self.graphvizText += "}"
        return self.graphvizText

    def invertir(self):
        if self.head and self.head.next != None:
            curr = self.head
            while curr.next != None:
                curr = curr.next
            back = curr
            newcurr = self.head

