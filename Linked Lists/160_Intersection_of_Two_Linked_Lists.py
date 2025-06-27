# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        currA = headA
        currB = headB

        lenA = 0
        lenB = 0

        while currA is not None:
            lenA += 1
            currA = currA.next

        while currB is not None:
            lenB += 1
            currB = currB.next

        diff = abs(lenA - lenB)
        
        currA = headA
        currB = headB

        if lenA > lenB:
            while diff != 0:
                currA = currA.next
                diff -= 1
        else:
            while diff != 0:
                currB = currB.next
                diff -= 1

        while currB is not None:
            if currA == currB:
                return currA
            currA = currA.next
            currB = currB.next

        return None

            