class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        dp = [1] * len(nums)
        maxLen = 0
        maxIdx = 0
        for j in range(1, len(nums)):
            for i in range(j - 1, -1, -1):
                if nums[j] % nums[i] == 0:
                    dp[j] = max(dp[j], 1 + dp[i])
                    if dp[j] > maxLen:
                        maxLen = dp[j]
                        maxIdx = j
        result = [nums[maxIdx]]
        for i in range(maxIdx - 1, -1, -1):
            if dp[i] == maxLen - 1 and nums[maxIdx] % nums[i] == 0:
                result.append(nums[i])
                maxLen -= 1
                maxIdx = i
        return result[::-1]