class Solution:

    def firstOcc(self, nums, target):
        n = len(nums)
        s = 0
        e = n - 1
        ans = -1

        while s <= e:
            mid = s + (e - s) // 2

            if nums[mid] == target:
                ans = mid
                e = mid - 1
            elif nums[mid] > target:
                e = mid - 1
            else: 
                s = mid + 1

        return ans



    def lastOcc(self, nums, target):
        n = len(nums)
        s = 0
        e = n - 1
        ans = -1

        while s <= e:
            mid = s + (e - s) // 2

            if nums[mid] == target:
                ans = mid
                s = mid + 1
            elif nums[mid] > target:
                e = mid - 1
            else: 
                s = mid + 1

        return ans


    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = self.firstOcc(nums,target)
        last = -1
        if first != -1:
            last = self.lastOcc(nums,target)
        
        return [first, last]
        