class Solution:

    def isValid(self,weights,days,allowedWeight):
        sum = 0
        countDays = 0

        for weight in weights:
            if sum + weight <= allowedWeight:
                sum += weight
            else:
                countDays += 1
                sum = weight
        
        countDays += 1
        
        return True if countDays <= days else False

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        s = max(weights)
        e = sum(weights)
        ans = -1

        while s <= e:
            mid = s + (e - s) // 2

            if self.isValid(weights,days,mid):
                ans = mid
                e = mid - 1
            else:
                s = mid + 1

        return ans