class Solution:
    def isLesser(self,nums,threshold,div):
        sum = 0
        for num in nums:
            num = math.ceil(num / div)
            sum += num

        return True if sum <= threshold else False
        

    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        s = 1
        e = max(nums)
        ans = -1

        while s <= e:
            mid = s + (e - s) // 2

            if self.isLesser(nums,threshold,mid):
                ans = mid
                e = mid - 1
            else:
                s = mid + 1
        
        return ans