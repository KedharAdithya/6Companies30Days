class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        ls = list(range(1, n + 1))
        while len(ls) > 1:
            i = (k - 1) % len(ls)
            ls = ls[i + 1:] + ls[:i]
        return ls[0]
