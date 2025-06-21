class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        s = 0
        e = n - 1

        while s <= e: 
            mid = s + (e - s) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                e = mid - 1
            else:
                s = mid + 1
        
        return -1
        