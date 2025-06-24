class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        carry = 0
        sum = 0
        for i in range(n-1,-1,-1):
            if i == n - 1:
                sum = digits[i] + 1 + carry
            else:
                sum = digits[i] + carry
            digits[i] = sum % 10
            carry = sum // 10
        
        if carry != 0:
            digits.insert(0,carry)

        return digits