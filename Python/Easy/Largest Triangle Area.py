# TC = O(N^3)
# SC = O(1)
class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        def area(x1, y1, x2, y2, x3, y3):
            return abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) /2

        max_area = 0
        P = len(points)
        for i in range(P - 2):
            for j in range(i + 1, P - 1):
                for k in range(j + 1, P):
                    max_area = max(max_area, area(*points[i], *points[j], *points[k]))

        return max_area
