class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        def distance(p1, p2):
            x1, y1 = p1
            x2, y2 = p2
            return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

        count = 0
        for i in range(len(points)):
            distances = {}
            for j in range(len(points)):
                if i == j:
                    continue
                d = distance(points[i], points[j])
                if d in distances:
                    distances[d] += 1
                else:
                    distances[d] = 1
            for d in distances:
                count += distances[d] * (distances[d] - 1)
        return count
