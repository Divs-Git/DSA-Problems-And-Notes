class Solution:
    def mySqrt(self, x: int) -> int:
        s = 0
        e = x
        ans = 0

        while s <= e:
            mid = s + (e - s) // 2

            if mid == 0 or mid <= x // mid:
                ans = mid
                s = mid + 1
            else:
                e = mid - 1

        return ans
        