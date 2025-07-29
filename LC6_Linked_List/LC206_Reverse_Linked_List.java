package LC6_Linked_List;

public class LC206_Reverse_Linked_List {

    // T: O(n), S: O(1)
    public ListNode reverseList(ListNode head) {
        if (head == null || head.next == null)
            return head;

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

    // T: O(n), S: O(n)
    public ListNode rev(ListNode node) {
        if (node.next == null)
            return node;

        ListNode p = rev(node.next);
        node.next.next = node;
        node.next = null;
        return p;
    }

    public ListNode reverseList(ListNode head) {
        if (head == null)
            return null;

        return rev(head);
    }

}
