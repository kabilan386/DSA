from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        t1 = headA
        t2 = headB
        while t1 != t2:
            t1 = t1.next
            t2 = t2.next

            if t1 == t2:
                return t1

            if t1 == None:
                t1 = headB
            if t2 == None:
                t2 = headA
        
        return t1
common = ListNode(8)
common.next = ListNode(4)
common.next.next = ListNode(5)

headA = ListNode(4)
headA.next = ListNode(1)
headA.next.next = common

headB = ListNode(5)
headB.next = ListNode(0)
headB.next.next = ListNode(1)
headB.next.next.next = common

print(Solution().getIntersectionNode(headA, headB).val)
print(Solution().getIntersectionNode(
    ListNode(4, 
            ListNode(1, 
                ListNode(8, 
                    ListNode(4, 
                        ListNode(5)
                    )
                )
            )
    ), 
    ListNode(5, 
        ListNode(0, 
            ListNode(1, 
                ListNode(8, 
                    ListNode(4, 
                        ListNode(5)
                    )
                )
            )
        )
    )
    )
)