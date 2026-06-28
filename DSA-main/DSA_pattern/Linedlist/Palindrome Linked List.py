from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next


        prev = None
        while slow:
            nextNode=slow.next
            slow.next = prev
            prev = slow
            slow = nextNode

        left = head
        right = prev

        while right is not None:
            if left.val != right.val:
                return False
            
            left = left.next
            right = right.next

        return True

        

            

        
       
        
        
       
        





head = ListNode(1,ListNode(2,ListNode(3,ListNode(3,ListNode(2,ListNode(1))))))

print(Solution().isPalindrome(head))