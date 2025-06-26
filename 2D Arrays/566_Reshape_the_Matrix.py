class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])

        res = [[0 for _ in range(c)] for _ in range(r)]

        if r * c != m * n:
            return mat
        
        for i in range(r * c):
            res[i // c][i % c] = mat[i // n][i % n]

        return res
            