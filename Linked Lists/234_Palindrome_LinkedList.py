# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self,head):
        if head is None or head.next is None:
            return head

        p = self.reverse(head.next)

        head.next.next = head
        head.next = None

        return p

    
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # middle of LL
        slow = head
        fast = head

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

        # reverse the second
        secHead = self.reverse(slow)
        firstHead = head

        # compare the two LL
        curr1 = firstHead
        curr2 = secHead
        while curr2 != None:
            if curr1.val != curr2.val:
                return False
            
            curr1 = curr1.next
            curr2 = curr2.next

        return True

    