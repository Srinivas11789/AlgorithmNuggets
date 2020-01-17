class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        
        # Logic 1: If a line is going to be straight. All the DIFF/DISTANCE between every points should be equal - DIST does not work use SLOPE
        
        # Distance between 2 points
        def distance(p1, p2):
            import math
            return math.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)
        
        # Logic 2: Upgrading the same logic with SLOPE formula - 100 pass 50%faster
        # Ref: https://www.urbanpro.com/gre/how-to-determine-if-points-are-collinear

        def slope(p1, p2):
            # Using exception handler when x is 0 or undefined slope is encountered
            try:
                return (p2[1]-p1[1])//(p2[0]-p1[0])
            except:
                return 0
        
        # Iterate each pair of points
        dist = None
        coordinates.sort()
        for p in range(1, len(coordinates)):
            d = slope(coordinates[p], coordinates[p-1])
            #print(d, coordinates[p])
            if not dist:
                dist = d
            else:
                if d != dist:
                    return False
        return True
