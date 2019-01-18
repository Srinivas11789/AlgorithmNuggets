class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        
        # 100 pass 976ms
        # * A bit lousy logic with a number of datastructure or memory
        
        # Euclidean distance: Recollecting math...
        # * Use Pythagoras Theorem (for a triangle - right angle) 
        #   * Right Angle Triangle has 3 sides --> slanting (diagnal) + horizontal + vertical
        #   * Diagnal^2 = horizontal_line^2 + vertival_line^2 
        #   * Diagnal = sqrt(horizontal_line^2 + vertival_line^2)
        #   * Diagnal = sqrt([x2-x1]^2 + [y2-y1]^2) 
        #     - x1,y1 and x2, y2 are the points connecting the diagnal
        
        import math # To calc square root
        
        # Initial point is always the origin (based on the question)
        first_point = [0,0]
        
        # Dictionary to manage the distance vs the points
        distances = {}
        
        # Iterate the next points from given list
        for second_point in points:
            # Get the x distance from origin
            x_dist = first_point[0]-second_point[0]
            # Y distance from origin
            y_dist = first_point[1]-second_point[1]
            # Euc distance calculation
            euc_dist = math.sqrt(x_dist**2 + y_dist**2)
            # Add relationship between second_point and respective euc_distances in dictionary
            if euc_dist not in distances:
                distances[euc_dist] = []
            # if More than one value having same euc_distance, so use list
            distances[euc_dist].append(second_point)
        
        # Result list
        result = []
        
        # Arrange distances to origin is ascending order
        closest_to_origin = sorted(distances.keys())
        
        # Iterate until we get K elements
        while len(result) < K:
            # Get first entry from sorted distances
            current_closest = closest_to_origin.pop(0)
            
            # Handle more than one second point having same euc distance
            # * Append second points until the result length is less than K
            while distances[current_closest] and len(result) < K:
                result.append(distances[current_closest].pop(0))

        return result
