class Solution:

    def findMin(self, nums):
        n = len(nums)
        s = 0
        e = n - 1

        if nums[0] <= nums[n - 1]:
            return 0

        while s <= e:
            mid = s + (e - s) // 2
            prev = (mid - 1 + n) % n
            next = (mid + 1) % n

            if nums[mid] <= nums[prev] and nums[mid] <= nums[next]:
                return mid
            else:
                if nums[0] <= nums[mid]:
                    s = mid + 1
                else:
                    e = mid - 1

        return -1
        

    def bs(self,nums,s,e,target):
        while s <= e:
            mid = s + (e - s) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                e = mid - 1
            else:
                s = mid + 1

        return -1


    def search(self, nums: List[int], target: int) -> int:
        mini = self.findMin(nums)
        n = len(nums)

        if nums[mini] == target:
            return mini

        left = self.bs(nums,0,mini - 1,target)
        right = self.bs(nums,mini + 1,n - 1, target)

        return right if left == -1 else left

        