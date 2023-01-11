class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        small = second_small = float('inf')
        for num in nums:
            if num <= small:
                small = num
            elif num <= second_small:
                second_small = num
            else:
                return True
        return False