class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        res = 0
        max_neg = float('-inf')
        min_pos = float('inf')
        count_neg = 0
        
        for i in range(n):
            for j in range(n):
                res += abs(matrix[i][j])
                
                if matrix[i][j] <= 0:
                    count_neg += 1
                    max_neg = max(max_neg, matrix[i][j])
                else:
                    min_pos = min(min_pos, matrix[i][j])
        
        if count_neg % 2 == 0:
            max_neg = 0
        
        return max(res + 2 * max_neg, res - 2 * min_pos)
