class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)

        s = 1
        e = n - 2
        ans = -1

        if n == 1:
            return 0
        if nums[0] > nums[1]:
            return 0
        if nums[n - 1] > nums[n - 2]:
            return n - 1

        while s <= e:
            mid = s + (e - s) // 2

            if nums[mid] > nums[mid + 1]:
                ans = mid
                e = mid - 1
            else:
                s = mid + 1

        return ans

        


        