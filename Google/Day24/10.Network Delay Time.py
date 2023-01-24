class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        
        dist = [float('inf')] * (n+1)
        dist[k] = 0
        
        pq = [(0, k)]
        while pq:
            d, node = heapq.heappop(pq)
            if dist[node] < d:
                continue
            for nei, d2 in graph[node]:
                if dist[nei] > dist[node] + d2:
                    dist[nei] = dist[node] + d2
                    heapq.heappush(pq, (dist[nei], nei))
        
        max_time = max(dist[1:])
        if max_time == float('inf'):
            return -1
        return max_time
