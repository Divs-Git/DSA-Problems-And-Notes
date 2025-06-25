class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        store = {}
        if len(s) != len(t):
            return False

        for e in s:
            store[e] = store.get(e,0) + 1
        
        for e in t:
            if e in store and store[e] > 0:
                store[e] = store[e] - 1
            else:
                return False

        return True
