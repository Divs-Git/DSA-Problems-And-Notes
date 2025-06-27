# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        t1 = l1
        t2 = l2
        carry = 0

        dummyhead = ListNode(-1)
        curr = dummyhead

        while t1 is not None and t2 is not None:
            sum = t1.val + t2.val + carry
            digit = sum % 10
            carry = sum // 10

            node = ListNode(digit)
            curr.next = node
            curr = node

            t1 = t1.next
            t2 = t2.next
        
        while t1 is not None:
            sum = t1.val + carry
            digit = sum % 10
            carry = sum // 10

            node = ListNode(digit)
            curr.next = node
            curr = node

            t1 = t1.next

        while t2 is not None:
            sum = t2.val + carry
            digit = sum % 10
            carry = sum // 10

            node = ListNode(digit)
            curr.next = node
            curr = node

            t2 = t2.next

        if carry != 0:
            node = ListNode(carry)
            curr.next = node
            curr = node

        return dummyhead.next
        


