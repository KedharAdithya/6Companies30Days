class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = n - 1
        while left < n - 1 and nums[left] <= nums[left + 1]:
            left += 1
        while right > 0 and nums[right] >= nums[right - 1]:
            right -= 1
        if left >= right:
            return 0
        min_val = float('inf')
        max_val = float('-inf')
        for i in range(left, right + 1):
            min_val = min(min_val, nums[i])
            max_val = max(max_val, nums[i])
        while left > 0 and nums[left - 1] > min_val:
            left -= 1
        while right < n - 1 and nums[right + 1] < max_val:
            right += 1
        return right - left + 1