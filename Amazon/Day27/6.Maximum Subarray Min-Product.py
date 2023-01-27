class Solution(object):
    def maxSumMinProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        stack, max_min_product = [], 0
        nums.append(0)
        for num in nums:
            subarray_sum = 0
            while len(stack) > 0 and num <= stack[-1][0]:
                (popped_val, popped_sum) = stack.pop()
                max_min_product = max(max_min_product, popped_val * (popped_sum + subarray_sum))
                subarray_sum += popped_sum
            stack.append((num, subarray_sum + num))
        return max_min_product % (10**9 + 7)