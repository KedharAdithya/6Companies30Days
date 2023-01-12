class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        dp = [[[0.0 for _ in range(n)] for _ in range(n)] for _ in range(k+1)]
        dp[0][row][column] = 1.0
        for moves in range(1, k+1):
            for r in range(n):
                for c in range(n):
                    for dr, dc in [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]:
                        if 0 <= r + dr < n and 0 <= c + dc < n:
                            dp[moves][r][c] += dp[moves-1][r+dr][c+dc] / 8
        return sum(dp[k][i][j] for i in range(n) for j in range(n))