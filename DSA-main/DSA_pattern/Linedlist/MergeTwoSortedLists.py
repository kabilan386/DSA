from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1 is not None:
            tail.next = list1
        
        if list2 is not None:
            tail.next = list2
    
        return dummy.next
    

List1 = ListNode(1, ListNode(2, ListNode(4)))
List2 = ListNode(1, ListNode(3, ListNode(4)))
solution = Solution()
merged_list = solution.mergeTwoLists(List1, List2)
# Print the merged linked list
current = merged_list
while current:
    print(current.val, end=" -> ")
    current = current.next