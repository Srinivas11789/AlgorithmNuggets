class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        
        # (a, b) and (0, 0) ==> sqrt((a-0)^2 + (b-0)^2) ==> sqrt(a^2 + b^2)
        
        def euc_dist(point):
            import math
            return math.sqrt(point[0]**2 + point[1]**2)
        
        points = sorted(points, key=lambda x: euc_dist(x))
        return points[:K]
