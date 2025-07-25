package Arrays;

import java.util.HashMap;
import java.util.Map;

public class LC1_Two_Sum {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int comp = target - nums[i];
            if (map.containsKey(comp)) {
                return new int[] { i, map.get(comp) };
            }

            map.put(nums[i], i);
        }

        return new int[] { -1, -1 };
    }
}
