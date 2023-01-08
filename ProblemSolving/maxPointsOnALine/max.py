class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:

        # ref: https://leetcode.com/problems/max-points-on-a-line/solutions/2910679/max-points-on-a-line/comments/1747602
        # Use https://math.stackexchange.com/questions/701862/how-to-find-if-the-points-fall-in-a-straight-line-or-not
        def calcSlope(p1, p2):

            if p1[0] == p2[0]:
                return float('inf') # y2-y1 / x2-x1 is infinity
            if p1[1] == p2[1]:
                return 0
            return (p2[1]-p1[1]) / (p2[0]-p1[0])

        max_points = 0

        for p in range(len(points)):
            slopes = {}
            for other in range(p+1, len(points)):
                curr_slope = calcSlope(points[p], points[other])
                if curr_slope not in slopes:
                    slopes[curr_slope] = 1
                else:
                    slopes[curr_slope] += 1
                max_points = max(max_points, slopes[curr_slope])

        return max_points+1
