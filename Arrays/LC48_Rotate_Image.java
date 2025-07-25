package Arrays;

public class LC48_Rotate_Image {
    class Solution {
        public void rotate(int[][] matrix) {
            int m = matrix.length;
            int n = matrix[0].length;
            for (int i = 0; i < m; i++) {
                for (int j = 0; j < i; j++) {
                    int temp = matrix[i][j];
                    matrix[i][j] = matrix[j][i];
                    matrix[j][i] = temp;
                }
            }

            for (int i = 0; i < m; i++) {
                reverse(matrix[i]);
            }
        }

        public void reverse(int[] nums) {
            int s = 0;
            int e = nums.length - 1;

            while (s < e) {
                int temp = nums[s];
                nums[s] = nums[e];
                nums[e] = temp;
                s++;
                e--;
            }

        }
    }
}
