class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        
        if len(s) == 0:
            return True

        sq = 0
        for i in range(len(t)):
            if sq < len(s):
                if s[sq] == t[i]:
                    sq += 1 

        return sq == len(s)

