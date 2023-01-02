class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        area = 0
        corner_points = set()

        for x, y, a, b in rectangles:
            area += (a - x) * (b - y)
            for point in [(x, y), (x, b), (a, y), (a, b)]:
                if point in corner_points:
                    corner_points.remove(point)
                else:
                    corner_points.add(point)

        if len(corner_points) != 4:
            return False

        corner_points = sorted(list(corner_points), key=lambda x: (x[0], x[1]))
        return area == ((corner_points[-1][0] - corner_points[0][0]) * (corner_points[-1][1] - corner_points[0][1]))