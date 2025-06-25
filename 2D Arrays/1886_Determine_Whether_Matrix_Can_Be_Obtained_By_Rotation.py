class Solution:
    def checkIfSame(self,mat,target):
        for i in range(len(mat)):
            for j in range(len(target)):
                if mat[i][j] != target[i][j]:
                    return False

        return True

    def swap(self,nums):
        s = 0
        e = len(nums) - 1

        while s < e:
            nums[s],nums[e] = nums[e],nums[s]
            s += 1
            e -= 1

    def rotate(self,mat):
        for i in range(len(mat)):
            for j in range(i+1):
                mat[i][j],mat[j][i] = mat[j][i],mat[i][j]

        
        for i in range(len(mat)):
            self.swap(mat[i])

    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:

        for i in range(4):
            if self.checkIfSame(mat,target):
                return True
            else:
                self.rotate(mat)

        return False
        