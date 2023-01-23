class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        n = len(nums)
        ans = 0
        flag = []
        for element in nums:
            if element % p == 0:
                flag.append(1)
            else:
                flag.append(0)
        
        added = set()
        prefix_sum = [0]
        start = 0
        for element in flag:
            start += element
            prefix_sum.append(start)
        
        for i in range(1, len(nums)+1):
            for j in range(i, len(nums)+1):
                target = prefix_sum[j] - prefix_sum[i-1]
                arr = tuple(nums[i-1:j])
                if target <= k and tuple(arr) not in added:
                    added.add(tuple(arr))
        
        return len(added)
