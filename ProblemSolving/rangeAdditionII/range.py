class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        
        # Logic 2: 98% faster logic and 100% space
        
        # * Obviously we dont need to go through every element again and again
        # * We need to find the intersection of the range ( max intersection ), or the elements that will be included in most of the ranges
        # * Question claims all the opertion ranges starts with 0 -> a or 0->b
        # --> To find the maximum:
        # * That means the common index for all ranges would for sure be 0,0 which will be the maximum element incurring changes on each operation
        # * The value of 0,0 will be the number of operation or length of operation
        
        # Scribble To find the maximum:
        """
        # If no operation is performed all elements are max which is 0
        if not ops:
            return m*n
        # If operation is performed, (0,0) will incur changes on all operation and be the max value
        return len(ops)
        """
        
        # We need to find how much element has this max --> Find all the intersections and leave the rest
        # * If no operation is performed all elements are max which is 0
        # * The most minimum range is the one that went through all other ranges that were greater than itself so that is the answer
        # * Using sorted only looks at x in x,y
        
        if not ops:
            return m*n
        row = m
        column = n
        for op in ops:
            row = min(row, op[0])
            column = min(column, op[1])
        return row*column
            
        # Logic 1: Very Naive Method with for loops - Literally following counter logic without any shortcuts or property usage
        """
        count = m*n
        if not ops:
            return count
        matrix = [[0 for i in range(n)] for j in range(m)]
        maxi = -float('inf')
        for op in ops:
            for i in range(op[0]):
                for j in range(op[1]):
                    matrix[i][j] += 1
                    if matrix[i][j] > maxi:
                        maxi = matrix[i][j]
                        count = 1
                    elif matrix[i][j] == maxi:
                        count += 1
        return count
        """
        
