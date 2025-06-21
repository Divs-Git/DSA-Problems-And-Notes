class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        s = 0
        e = n - 1

        if nums[0] <= nums[n - 1]:
            return nums[0]

        while s <= e:
            mid = s + (e - s) // 2
            prev = (mid - 1 + n) % n
            next = (mid + 1) % n

            if nums[mid] <= nums[prev] and nums[mid] <= nums[next]:
                return nums[mid]
            else:
                if nums[0] <= nums[mid]:
                    s = mid + 1
                else:
                    e = mid - 1

        return -1
        