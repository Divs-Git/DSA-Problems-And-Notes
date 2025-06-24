class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        s = 0
        e = len(arr)

        while s < e:
            mid = s + (e - s) // 2
            missing = arr[mid] - (mid + 1)

            if missing < k:
                s = mid + 1
            else:
                e = mid

        return s + k
                    
