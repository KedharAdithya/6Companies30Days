class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        def dfs(nums, target, used, todo, lookup):
            if lookup[used] is None:
                targ = (todo-1)%target + 1
                lookup[used] = any(dfs(nums, target, used | (1<<i), todo-num, lookup) \
                                   for i, num in enumerate(nums) \
                                   if ((used>>i) & 1) == 0 and num <= targ)
            return lookup[used]

        total = sum(nums)
        if total%k or max(nums) > total//k:
            return False
        lookup = [None] * (1 << len(nums))
        lookup[-1] = True
        return dfs(nums, total//k, 0, total, lookup)
