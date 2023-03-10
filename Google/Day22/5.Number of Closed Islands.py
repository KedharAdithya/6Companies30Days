class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        def dfs(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                return False
            if grid[i][j] == 1:
                return True
            grid[i][j] = 1
            up = dfs(i-1, j)
            down = dfs(i+1, j)
            left = dfs(i, j-1)
            right = dfs(i, j+1)
            return up and down and left and right

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    if dfs(i, j):
                        count += 1
        return count