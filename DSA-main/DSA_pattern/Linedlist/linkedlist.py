class Node:
    def __init__ (self, data):
        self.data = data
        self.next = None

class linkedlist:
    def __init__ (self):
        self.head = None

    def push(self, data):
        newnode = Node(data)
        newnode.next = self.head
        self.head = newnode
    
    def pop(self):
        if self.head is None:
            return
        self.head = self.head.next

    def print(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

linkedlist = linkedlist()
linkedlist.push(1)
linkedlist.push(2)
linkedlist.push(3)
linkedlist.print()