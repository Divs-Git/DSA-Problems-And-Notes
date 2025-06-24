class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        if numRows == 0:
            return result

        result.append([1])

        if numRows == 1:
            return result

        for i in range(1,numRows):
            row = []
            prevRow = result[i - 1]
            row.append(1)

            for j in range(0,i - 1):
                row.append(prevRow[j] + prevRow[j + 1])
            
            row.append(1)

            result.append(row)

        return result
                