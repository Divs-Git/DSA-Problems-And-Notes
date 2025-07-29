package LC6_Linked_List;

public class LC143_Reorder_List {
    public ListNode rev(ListNode head) {
        ListNode curr = head;
        ListNode prev = null;

        while (curr != null) {
            ListNode nextNode = curr.next;
            curr.next = prev;
            prev = curr;
            curr = nextNode;
        }

        return prev;
    }

    // T: O(n), S: O(1)
    public void reorderList(ListNode head) {
        // middle
        ListNode slow = head;
        ListNode fast = head;

        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }

        // reverse second
        ListNode sec = slow.next;
        slow.next = null;
        ListNode second = rev(sec);

        // merge
        ListNode first = head;
        ListNode dummyHead = new ListNode(-1);
        ListNode curr = dummyHead;

        while (second != null) {
            curr.next = first;
            first = first.next;
            curr = curr.next;

            curr.next = second;
            second = second.next;
            curr = curr.next;
        }

        if (first != null) {
            curr.next = first;
        }
    }
}
