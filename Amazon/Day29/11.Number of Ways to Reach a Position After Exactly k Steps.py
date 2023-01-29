from math import comb
class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        total_steps = k
        diff_right_left_steps = endPos - startPos
        right_steps = (total_steps + diff_right_left_steps) // 2
        if (total_steps + diff_right_left_steps) % 2 != 0 or right_steps < 0 or right_steps > total_steps:
            return 0
        return comb(total_steps, right_steps) % (10**9 + 7)