class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:

        points = sorted(points, key=lambda x: x[0])
        arrows = 0

        print(points)
        curr_point = []
        if len(points) > 0:
            curr_point = points.pop(0)
        while points:
            nxt = points.pop(0)
            if curr_point[0] <= nxt[0] <= curr_point[1] or curr_point[0] <= nxt[1] <= curr_point[1]:
                curr_point[0] = min(curr_point[0], nxt[0])
                curr_point[1] = min(curr_point[1], nxt[1])
            else:
                arrows += 1
                curr_point = nxt
            print(curr_point, nxt, arrows)
        if curr_point:
            arrows += 1
        return arrows
