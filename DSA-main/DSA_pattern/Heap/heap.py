class HeapNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


class MinHeap:
    def __init__(self):
        self.root = None


    def add(self,data):
        if not self.root:
            self.root = HeapNode(data)

    
    