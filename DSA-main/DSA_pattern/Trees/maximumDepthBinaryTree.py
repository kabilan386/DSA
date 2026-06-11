# Question : Maximum Depth of Binary Tree
# Description : Maximum depth of a binary tree is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Example : 
#     A
#    / \
#   B   C
#  / \   \
# D   E   F
# Maximum depth of the tree is 3

graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["F"],
    "F": []
}

def maxDepth(graph, node):
    if node is None:
        return 0
    
    leftDepth = maxDepth(graph, graph[node][0])
    rightDepth = maxDepth(graph, graph[node][1])
    
    return max(leftDepth, rightDepth) + 1


print(maxDepth(graph, "A"))


# Time and space complexity
# Time complexity : O(n)
# Space complexity : O(n)

# 