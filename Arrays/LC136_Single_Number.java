package Arrays;

import java.util.HashMap;
import java.util.Map;

public class LC136_Single_Number {

    public int singleNumber(int[] nums) {
        Map<Integer, Integer> map = new HashMap<>();

        for (int num : nums) {
            map.put(num, map.getOrDefault(num, 0) + 1);
        }

        for (int num : nums) {
            if (map.get(num) == 1) {
                return num;
            }
        }

        return -1;
    }

    // Optimized
    public int singleNumber1(int[] nums) {
        int ans = 0;

        for (int num : nums) {
            ans = ans ^ num;
        }

        return ans;
    }
}
