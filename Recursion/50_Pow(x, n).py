class Solution:
    def powHelper(self, x, n):
        if n == 0:
            return 1

        half = self.powHelper(x, n // 2)

        if n % 2 == 0:
            return half * half
        else:
            return half * half * x

    def myPow(self, x: float, n: int) -> float:
        is_neg = False
        if n < 0:
            is_neg = True
            n = -n
        ans = self.powHelper(x, n)

        return 1 / ans if is_neg else ans
