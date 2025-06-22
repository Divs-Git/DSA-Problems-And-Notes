class Solution:
    def isCreated(self,bloomDay,m,k,num):
        count = 0
        adjDays = 0

        for day in bloomDay:
            if day <= num:
                count += 1
            else:
                adjDays += count // k
                count = 0
        
        adjDays += count // k

        return True if adjDays >= m else False

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        s = min(bloomDay)
        e = max(bloomDay)
        ans = -1

        while s <= e:
            mid = s + (e - s) // 2

            if self.isCreated(bloomDay,m,k,mid):
                ans = mid
                e = mid - 1
            else:
                s = mid + 1
        
        return ans
        