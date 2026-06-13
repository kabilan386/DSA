# class HeapNode:
#     def __init__(self,data):
#         self.data = data
#         self.left = None
#         self.right = None


# class MinHeap:
#     def __init__(self):
#         self.root = None


#     def add(self,data):
#         if not self.root:
#             self.root = HeapNode(data)

#     def recursive_add(self,node,data):
#         if not node.left:
#             node.left = HeapNode(data)
#             return
#         if not node.right:
#             node.right = HeapNode(data)
#             return
        
#         if node.left.data < node.right.data:
#             self.recursive_add(node.left,data)
#         else:
#             self.recursive_add(node.right,data)

#     def recursive_remove(self,node,data):
#         if not node:
#             return None
#         if node.data == data:
#             if not node.left and not node.right:
#                 return None
#             if not node.left:
#                 return node.right
#             if not node.right:
#                 return node.left
            


import heapq

arr = [1,2,17,4,23,6,19,8,9,10]

heapq.heapify(arr)

print(arr)

# output : [1, 2, 6, 4, 10, 17, 19, 8, 9, 23]

# Explanation :
# 1 is the root
# 2 and 6 are the children of 1
# 4 and 10 are the children of 2
# 17 and 19 are the children of 6
# 8 and 9 are the children of 4
# 23 is the child of 10

# calculate parent and child index
# parent of index i is (i-1)//2
# left child of index i is 2*i + 1
# right child of index i is 2*i + 2

# for index 0 : parent is (0-1)//2 = -1
# left child of index 0 is 2*0 + 1 = 1
# right child of index 0 is 2*0 + 2 = 2




            
                
    
    