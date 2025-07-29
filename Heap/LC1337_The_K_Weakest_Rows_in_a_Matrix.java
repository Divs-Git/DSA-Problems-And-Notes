import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class LC1337_The_K_Weakest_Rows_in_a_Matrix {
    class Solution {
        public int[] kWeakestRows(int[][] mat, int k) {
            int rows = mat.length, cols = mat[0].length;

            List<int[]> list = new ArrayList<>();

            for (int row = 0; row < rows; row++) {
                int sol = 1;

                for (int col = 0; col < cols; col++) {
                    if (mat[row][col] == 0) {
                        break;
                    }

                    sol += 1;
                }

                list.add(new int[] { sol, row });
            }

            Collections.sort(list, (e1, e2) -> {
                if (e1[0] == e2[0])
                    return e1[1] - e2[1];
                return e1[0] - e2[0];
            });

            int[] res = new int[k];

            for (int i = 0; i < k; i++) {
                res[i] = list.get(i)[1];
            }

            return res;
        }
    }
}
