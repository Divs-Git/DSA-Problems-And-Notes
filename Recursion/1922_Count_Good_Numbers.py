class Solution:
    MOD = 7 + 10**9

    def power(self,x,n):
        if n == 0:
            return 1
        
        help = self.power(x, n // 2)

        if n % 2 == 0:
            return (help * help) % self.MOD
        else:
            return (help * help * x) % self.MOD

    def countGoodNumbers(self, n: int) -> int:
        even_count = (n + 1) // 2
        odd_count = n // 2

        return self.power(5,even_count) * self.power(4,odd_count) % self.MOD
        