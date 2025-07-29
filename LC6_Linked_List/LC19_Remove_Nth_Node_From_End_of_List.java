package LC6_Linked_List;

public class LC19_Remove_Nth_Node_From_End_of_List {

    // T: O(n), S: O(1)
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode fast = head;
        ListNode slow = head;

        while (n > 0 && fast != null) {
            fast = fast.next;
            n--;
        }

        if (fast == null)
            return head.next;

        while (fast.next != null) {
            slow = slow.next;
            fast = fast.next;
        }

        slow.next = slow.next.next;
        return head;
    }
}
