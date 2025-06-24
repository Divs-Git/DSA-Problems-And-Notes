class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        store = {}
        res = []

        for num in nums1:
            store[num] = store.get(num,0) + 1
        
        for num in nums2:
            if num in store:
                res.append(num)
                del store[num]
        
        return res