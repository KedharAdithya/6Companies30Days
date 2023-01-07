class Solution:
    def trailingZeroes(self, n: int) -> int:
        num_fives = 0
        num_twos = 0
        i = 5
        while n // i > 0:
            num_fives += n // i
            i *= 5
        i = 2
        while n // i > 0:
            num_twos += n // i
            i *= 2
        return min(num_fives, num_twos)