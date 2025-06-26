class Solution:
    def binarySearch(self,nums,target):
        s = 0
        e = len(nums) - 1

        while s <= e:
            mid = s + (e - s) // 2

            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                s = mid + 1
            else:
                e = mid - 1

        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        s = 0
        e = len(matrix) - 1
        rowIdx = -1

        while s <= e:

            mid = s + (e - s) // 2

            if matrix[mid][0] <= target and target <= matrix[mid][len(matrix[0])- 1]:
                rowIdx = mid
                break
            elif matrix[mid][0] < target :
                s = mid + 1
            else:
                e = mid - 1

        return self.binarySearch(matrix[rowIdx],target)