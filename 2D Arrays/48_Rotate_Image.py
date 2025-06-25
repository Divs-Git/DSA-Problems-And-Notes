class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # transpose
        for i in range(len(matrix)):
            for j in range(i + 1):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]

        # reverse each row
        for i in range(len(matrix)):
            self.swap(matrix[i])

    def swap(self,nums):
        s = 0
        e = len(nums) - 1

        while s <= e:

            nums[s],nums[e] = nums[e],nums[s]
            s += 1
            e -= 1
    
        