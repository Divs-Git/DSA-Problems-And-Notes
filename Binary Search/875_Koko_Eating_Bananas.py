class Solution:
    def hasEatenAll(self,piles,num,h):
        totalTime = 0

        for pile in piles:
            totalTime += math.ceil(pile/num)
        
        return True if totalTime <= h else False

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        s = 1
        e = max(piles)
        ans = 0

        while s <= e:

            mid = s + (e - s) // 2

            if self.hasEatenAll(piles,mid,h):
                ans = mid
                e = mid - 1
            else:
                s = mid + 1

        return ans