# space O(n)
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []

        curr = head

        while curr is not None:
            arr.append(curr.val)
            curr = curr.next

        arr.sort()
        newHead = None
        prev = None

        for i in range(len(arr)):
            node = ListNode(arr[i])
            if i == 0:
                newHead = node
                prev = node
            else:
                prev.next = node
                prev = node
          

        return newHead
            
# space -> O(1)
class Solution:

    def findMiddle(self,head):
        if head is None:
            return head

        slow = head
        fast = head.next

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        return slow

    def merge(self,leftHead,rightHead):
        curr1 = leftHead
        curr2 = rightHead

        dummyhead = ListNode(-1)
        temp = dummyhead

        while curr1 is not None and curr2 is not None:
            if curr1.val <= curr2.val:
                temp.next = curr1
                temp = curr1
                curr1 = curr1.next
            else:
                temp.next = curr2
                temp = curr2
                curr2 = curr2.next

        if curr1:
            temp.next = curr1
        
        if curr2:
            temp.next = curr2

        return dummyhead.next

    def mergeSort(self,head):
        if head is None or head.next is None:
            return head

        middle = self.findMiddle(head)

        leftHead = head
        rightHead = middle.next

        middle.next = None

        leftHead = self.mergeSort(leftHead)
        rightHead = self.mergeSort(rightHead)

        return self.merge(leftHead,rightHead)

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.mergeSort(head)

    
