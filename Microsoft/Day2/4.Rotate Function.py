class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        max_value = float("-inf")
        curr_value = 0
        for i in range(len(nums)):
            curr_value += i * nums[i]
        sum_nums = sum(nums)
        for k in range(len(nums)):
            curr_value = curr_value + sum_nums - len(nums) * nums[-k-1]
            max_value = max(max_value, curr_value)
        return max_value
