class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rs = 0
        cs = 0
        re = len(matrix) - 1
        ce = len(matrix[0]) - 1

        res = []

        count = len(matrix) * len(matrix[0])

        while count > 0:

            for i in range(cs,ce + 1):
                res.append(matrix[rs][i])
                count -= 1

            if count == 0:
                return res
            rs += 1

            for i in range(rs,re + 1):
                res.append(matrix[i][ce])
                count -= 1
            
            if count == 0:
                return res
            ce -= 1

            for i in range(ce,cs - 1,-1):
                res.append(matrix[re][i])
                count -= 1

            if count == 0:
                return res
            re -= 1

            for i in range(re,rs - 1,-1):
                res.append(matrix[i][cs])
                count -= 1
            
            if count == 0:
                return res
            cs += 1

        return res
