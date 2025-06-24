# O(n ^ 3)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        maxi = nums[0]

        for i in range(n):
            for j in range(i,n):
                sum = 0
                for k in range(i,j + 1):
                    sum += nums[k]

                maxi = max(sum,maxi)

        return maxi
    
# Kadane's algorithm O(n)    
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = float('-inf')
        sum = 0

        for num in nums:
            sum += num
            maxi = max(sum,maxi)
            
            if sum < 0:
                sum = 0

        return maxi