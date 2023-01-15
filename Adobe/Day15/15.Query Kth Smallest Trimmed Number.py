class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        res = []
        for k, t in queries:
            trimmed_nums = [(num[-t:], i) for i, num in enumerate(nums)]
            trimmed_nums.sort()
            res.append(trimmed_nums[k-1][1])
        return res