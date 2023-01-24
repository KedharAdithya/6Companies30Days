# approach 1
class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        for i1 in range(m):
            for i2 in range(1, n):
                mat[i1][i2] += mat[i1][i2 - 1]
        for i1 in range(1, m):
            for i2 in range(n):
                mat[i1][i2] += mat[i1 - 1][i2]
        output = []
        for i1 in range(m):
            cur = []
            for i2 in range(n):
                sums = 0
                sums += mat[min(i1 + k, m - 1)][min(i2 + k, n - 1)]
                if i1 - k > 0:
                    sums -= mat[i1 - k -1][min(i2 + k, n - 1)]
                if i2 - k > 0:
                    sums -= mat[min(i1 + k, m - 1)][i2 - k - 1]
                if i1 - k > 0 and i2 - k > 0:
                    sums += mat[i1 - k -1][i2 - k - 1]
                cur.append(sums)
            output.append(cur)
        return output

# approach 2
class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        preSum = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                preSum[i][j] = mat[i - 1][j - 1] + preSum[i - 1][j] + preSum[i][j - 1] - preSum[i - 1][j - 1]

        ans = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                r1, c1, r2, c2 = max(0, i - k), max(0, j - k), min(m - 1, i + k), min(n - 1, j + k)
                ans[i][j] = preSum[r2 + 1][c2 + 1] - preSum[r2 + 1][c1] - preSum[r1][c2 + 1] + preSum[r1][c1]

        return ans