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

    def recursive_add(self,node,data):
        if not node.left:
            node.left = HeapNode(data)
            return
        if not node.right:
            node.right = HeapNode(data)
            return
        
        if node.left.data < node.right.data:
            self.recursive_add(node.left,data)
        else:
            self.recursive_add(node.right,data)

    def recursive_remove(self,node,data):
        if not node:
            return None
        if node.data == data:
            if not node.left and not node.right:
                return None
            if not node.left:
                return node.right
            if not node.right:
                return node.left
            
            
                
    
    