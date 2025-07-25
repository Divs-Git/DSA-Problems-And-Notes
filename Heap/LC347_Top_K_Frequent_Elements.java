import java.util.HashMap;
import java.util.Map;
import java.util.PriorityQueue;

public class LC347_Top_K_Frequent_Elements {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> map = new HashMap<>();

        for (int num : nums) {
            map.put(num, map.getOrDefault(num, 0) + 1);
        }

        PriorityQueue<Integer> heap = new PriorityQueue<>((e1, e2) -> map.get(e1) - map.get(e2));

        for (int ele : map.keySet()) {
            heap.add(ele);

            if (heap.size() > k) {
                heap.poll();
            }
        }

        int[] res = new int[k];
        int i = 0;
        while (!heap.isEmpty()) {
            res[i] = heap.poll();
            i++;
        }

        return res;
    }
}
