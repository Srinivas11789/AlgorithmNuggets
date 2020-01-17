class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        
        # Logic 1: If a line is going to be straight. All the DIFF/DISTANCE between every points should be equal - DIST does not work
        
        # Distance between 2 points
        def distance(p1, p2):
            import math
            return math.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)
        
        # Iterate each pair of points
        dist = None
        coordinates.sort()
        for p in range(1, len(coordinates)):
            d = distance(coordinates[p], coordinates[p-1])
            print(d, coordinates[p])
            if not dist:
                dist = d
            else:
                if d != dist:
                    return False
        return True
            
            
        
