class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        n = len(letters)
        ans = letters[0]
        s = 0
        e = n - 1

        while s <= e:
            mid = s + (e - s) // 2

            if letters[mid] > target:
                ans = letters[mid]
                e = mid - 1
            else:
                s = mid + 1

        return ans