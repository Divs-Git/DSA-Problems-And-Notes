import java.util.PriorityQueue;

public class LC703_Kth_Largest_Element_in_a_Stream {
    class KthLargest {
        PriorityQueue<Integer> minHeap;
        int k = 0;

        public KthLargest(int k, int[] nums) {
            minHeap = new PriorityQueue<>();
            this.k = k;

            for (int num : nums) {
                minHeap.add(num);

                if (minHeap.size() > k) {
                    minHeap.poll();
                }
            }
        }

        public int add(int val) {
            if (minHeap.size() < k) {
                minHeap.add(val);
                return minHeap.peek();
            }

            minHeap.add(val);
            minHeap.poll();
            return minHeap.peek();
        }
    }

    /**
     * Your KthLargest object will be instantiated and called as such:
     * KthLargest obj = new KthLargest(k, nums);
     * int param_1 = obj.add(val);
     */
}
