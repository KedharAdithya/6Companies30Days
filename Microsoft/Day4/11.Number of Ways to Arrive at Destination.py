class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v, w in roads:
            graph[u].append((v, w))
            graph[v].append((u, w))

        distances = [float("inf") for _ in range(n)]
        ways = [0 for _ in range(n)]
        distances[0] = 0
        ways[0] = 1

        heap = [(0, 0)]
        while heap:
            distance, u = heapq.heappop(heap)
            if distances[u] < distance:
                continue
            for v, w in graph[u]:
                new_distance = distance + w
                if new_distance < distances[v]:
                    distances[v] = new_distance
                    ways[v] = ways[u]
                    heapq.heappush(heap, (new_distance, v))
                elif new_distance == distances[v]:
                    ways[v] += ways[u]
        return ways[n-1] % ((10 ** 9) + 7)