package Arrays;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class LC350_Intersection_of_Two_Arrays_II {
    // T: O(m + n), S: O(m)
    public int[] intersect(int[] nums1, int[] nums2) {

        Map<Integer, Integer> map = new HashMap<>();

        for (int num : nums1) {
            map.put(num, map.getOrDefault(num, 0) + 1);
        }

        int[] res = new int[nums1.length];
        int k = 0;

        for (int num : nums2) {
            int count = map.getOrDefault(num, 0);

            if (count == 0) {
                continue;
            } else {
                res[k] = num;
                k++;
                map.put(num, map.get(num) - 1);
            }
        }

        return Arrays.copyOfRange(res, 0, k);
    }

    // T: O(mlogm + nlogn), S: O(1)
    public int[] intersect1(int[] nums1, int[] nums2) {
        Arrays.sort(nums1);
        Arrays.sort(nums2);

        int[] res = new int[nums1.length];

        int i = 0;
        int j = 0;
        int k = 0;

        while (i < nums1.length && j < nums2.length) {
            if (nums1[i] == nums2[j]) {
                res[k] = nums1[i];
                k++;
                i++;
                j++;
            } else if (nums1[i] > nums2[j]) {
                j++;
            } else {
                i++;
            }
        }

        return Arrays.copyOfRange(res, 0, k);
    }
}
