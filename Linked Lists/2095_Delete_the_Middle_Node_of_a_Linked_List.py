# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        slowPrev = None

        if head == None or head.next == None:
            return None

        while fast is not None and fast.next is not None:
            slowPrev = slow
            slow = slow.next
            fast = fast.next.next

        
        slowPrev.next = slow.next

        return head
        
