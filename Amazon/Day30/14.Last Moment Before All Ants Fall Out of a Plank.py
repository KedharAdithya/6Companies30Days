class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        left_max = max(left) if left else 0
        right_max = max(n-x for x in right) if right else 0
        return max(left_max, right_max)