from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        
        current = head

        while current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        
        return head

 
head = ListNode(1,ListNode(1,ListNode(2)))

sorted_list =  Solution().deleteDuplicates(head)

current = sorted_list
while current:
    print(current.val, end=" -> ")
    current = current.next