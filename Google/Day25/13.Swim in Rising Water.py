# approach 1
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        heap = [(grid[0][0], 0, 0)]  # Starting point with time 0
        seen = {(0, 0)}  # Keep track of seen points
        while heap:
            time, x, y = heapq.heappop(heap)
            if x == N - 1 and y == N - 1:
                return time
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < N and (nx, ny) not in seen:
                    seen.add((nx, ny))
                    heapq.heappush(heap, (max(time, grid[nx][ny]), nx, ny))


#approach 2
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        if len(grid) == 1 and len(grid[0]) == 1:
            return 0
        n = len(grid)
        left, right = grid[0][0], n * n
        while left < right:
            mid = (left + right) // 2
            visited = set()
            queue = deque([(0, 0)])
            visited.add((0, 0))
            while queue:
                x, y = queue.popleft()
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nx, ny = x + dx, y + dy
                    if nx < 0 or nx >= n or ny < 0 or ny >= n or grid[nx][ny] > mid or (nx, ny) in visited:
                        continue
                    if nx == n - 1 and ny == n - 1:
                        right = mid
                        break
                    queue.append((nx, ny))
                    visited.add((nx, ny))
            if right != mid:
                left = mid + 1
        return left
