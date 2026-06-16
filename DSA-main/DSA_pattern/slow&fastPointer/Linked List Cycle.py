# Question: Given head, the head of a linked list, determine if the linked list has a cycle in it.
# Description: There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
# Return true if there is a cycle in the linked list. Otherwise, return false.
# Example 1:
# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where tail connects to the second node.
# Example 2:
# Input: head = [1,2], pos = 0
# Output: true
# Explanation: There is a cycle in the linked list, where tail connects to the first node.
# Example 3:    

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



def hasCycle(head):
    if not head:
        return False

    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False



# Create nodes for the linked list
node1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(-4)

# Connect the nodes to form a cycle
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2  # Creates a cycle

print(hasCycle(node1))  # Output: True

# Create nodes for another linked list
node5 = ListNode(1)
node6 = ListNode(2)

# Connect the nodes
node5.next = node6

print(hasCycle(node5))  # Output: True

# Create a single node linked list
node7 = ListNode(1)

print(hasCycle(node7))  # Output: False


# Explanation:
# We use two pointers, slow and fast. The slow pointer moves one step at a time, while the fast pointer moves two steps at a time.
# If there is a cycle, the fast pointer will eventually meet the slow pointer. If there is no cycle, the fast pointer will reach the end of the list.
# Time Complexity: O(n)
# Space Complexity: O(1)        

# Time and space complexity:    
# Time Complexity: O(n) where n is the number of nodes in the linked list. In the worst case, we may have to traverse the entire list to determine if there is a cycle.
# Space Complexity: O(1) because we are using only a constant amount of extra space for the slow and fast pointers.