class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        s = 0
        e = n - 1
        ans = n

        while s <= e:

            mid = s + (e - s) // 2

            if nums[mid] == target: 
                return mid
            elif nums[mid] < target:
                s = mid + 1
            else:
                ans = mid
                e = mid - 1

        return ans
                
        