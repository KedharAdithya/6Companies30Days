class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        def rev(x):
            return int(str(x)[::-1])
        
        counts = defaultdict(int)
        for i in range(len(nums)):
            counts[nums[i]-rev(nums[i])] +=1
        return sum(counts[key]*(counts[key]-1)//2 for key in counts.keys() )% (10**9 + 7)