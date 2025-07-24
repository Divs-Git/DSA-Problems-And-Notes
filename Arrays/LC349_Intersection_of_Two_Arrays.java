package Arrays;

import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

public class LC349_Intersection_of_Two_Arrays {

    // TC: O(m + n), SC: O(m + n)
    public int[] intersection(int[] nums1, int[] nums2) {
        Set<Integer> s1 = new HashSet<>();
        Set<Integer> s2 = new HashSet<>();

        for (int num : nums1) {
            s1.add(num);
        }

        for (int num : nums2) {
            s2.add(num);
        }

        int[] res = new int[s1.size()];

        int k = 0;

        for (int num : s1) {
            if (s2.contains(num)) {
                res[k] = num;
                k++;
            }
        }

        return Arrays.copyOfRange(res, 0, k);
    }
}
