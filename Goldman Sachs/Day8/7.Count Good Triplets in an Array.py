class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        res = 0
        index_map = {}
        q = []
        for i, num in enumerate(nums2):
            index_map[num] = i
        for p1, num1 in enumerate(nums1):
            p2 = index_map[num1] 
            idx = bisect.bisect(q, p2) 
            q.insert(idx, p2)
            before = idx
            after = n-1 - p1 - p2 + before 
            res += before * after
        return res
