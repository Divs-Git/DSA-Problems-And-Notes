package Arrays;

public class LC189_Rotate_Array {
    public void rotate(int[] nums, int k) {
        int n = nums.length;
        int[] temp = new int[n];
        k = k % n;

        for (int i = 0; i < n; i++) {
            temp[(i + k) % n] = nums[i];
        }

        for (int i = 0; i < n; i++) {
            nums[i] = temp[i];
        }
    }
}
