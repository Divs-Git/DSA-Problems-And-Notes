import java.util.Collections;
import java.util.PriorityQueue;

public class LC1046_Last_Stone_Weight {
    class Solution {
        public int lastStoneWeight(int[] stones) {
            PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());

            // O(n.logn)
            for (int stone : stones) {
                maxHeap.add(stone);
            }

            // O(logn)
            while (maxHeap.size() > 1) {
                int lStone = maxHeap.poll();
                int sStone = maxHeap.poll();

                int diff = lStone - sStone;
                maxHeap.add(diff);
            }

            return maxHeap.peek();
        }
    }
}
