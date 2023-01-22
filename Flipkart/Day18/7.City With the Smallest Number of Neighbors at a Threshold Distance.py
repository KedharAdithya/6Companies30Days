class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # Create an adjacency list to represent the graph
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        
        # Initialize the result and the minimum number of reachable cities
        result = 0
        min_reachable = float('inf')
        
        # Start the Dijkstra's algorithm from each city
        for i in range(n):
            # Create a priority queue of unvisited cities
            heap = [(0, i)]
            dist = [float('inf')] * n
            dist[i] = 0
            
            while heap:
                # Extract the city with the lowest priority
                d, u = heapq.heappop(heap)
                
                # Update the distances of the neighboring cities
                for v, w in graph[u]:
                    if dist[v] > d + w:
                        dist[v] = d + w
                        heapq.heappush(heap, (dist[v], v))
            
            # Count the number of cities that are reachable within the distance threshold
            reachable = sum(1 for d in dist if d <= distanceThreshold)
            
            # Update the result if the current city has the smallest number of reachable cities
            if reachable <= min_reachable:
                min_reachable = reachable
                result = i
        
        return result
