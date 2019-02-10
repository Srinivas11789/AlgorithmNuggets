class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        
        # Logic: Using the start and end indexed
        # - Solve by just checking if the ranges bisect
        # Steps:
        # * Sort the ranges (on start or end)
        # * Find if they intersect
        
        # Sort ranges with the end index so every subset range fall in line
        points = sorted(points, key = lambda x: x[1])
        # Control variables
        arrow = 0
        previous_range_end = -float("inf") # negative infinity to satify first iteration
        # Iterate ranges in points, if start of current range exceeds end of last range then they dont intersect...
        for start, end in points:
            if start > previous_range_end:
                arrow += 1
                # Update end only when the range intersection does not exist
                previous_range_end = end

        return arrow
        
        """
        # Logic1: All scenarios work except for scale case ==> memory limit exceeded (why? this expands the full range which we do not need for this problem, only the arrow count is required...)
        # Using set intersection assuming the input is list
        ## set(a).intersection(set(b)) or
        ## set(a) & set(b) or
        ## set(a).intersection(b)
        # * this might have a o(N2) complexity
        
        if len(points) == 1:
            return 1
        
        minimum_arrows = None
        count = 0
        
        points = sorted(points)
        
        for ranges in points:
            if minimum_arrows:
                minimum_arrows = set(minimum_arrows).intersection(range(ranges[0], ranges[1]+1))
                if not minimum_arrows:
                    count += 1
                    minimum_arrows = range(ranges[0], ranges[1]+1)
                    
            else:
                minimum_arrows = range(ranges[0], ranges[1]+1)
        
        if minimum_arrows:
            count += 1
        
        return count
        
        # Other attempts:
        # * iteration with enumerate
        # * using dictionary to check
        """
