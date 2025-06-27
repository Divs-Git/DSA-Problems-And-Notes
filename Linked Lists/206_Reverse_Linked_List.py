# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None

        if head is None or head.next is None:
            return head

        while curr is not None:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode

        return prev
    

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        returnedHead = self.reverseList(head.next)
        head.next.next = head
        head.next = None

        return returnedHead