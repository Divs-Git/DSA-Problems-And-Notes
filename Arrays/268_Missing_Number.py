class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum = 0
        tSum = 0
        n = len(nums)

        for i in range(1,n+1):
            sum += i

        for i in range(n):
            tSum += nums[i]

        return sum - tSum