class Solution(object):
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        
        # Logic2: 100 pass only 5%faster.. better one yet?
        # * Iterate through row and columsn (i,j)
        # * For each column, the previous possible combinations are i-1, j-1 and i-1, j and i-1, j+1
        # * Get the minimum of those combinations and add as we iterate to the last row
        # * Return the minimum possible from the last row sums.
        # * Reference: https://leetcode.com/problems/minimum-falling-path-sum/discuss/186843/Python-easy-4-liner
        
        for i in range(1, len(A)): # Row iteration
            for j in range(len(A)): # Column iteration
                A[i][j] += min(A[i-1][j-1] if j-1 >= 0 else float("inf"), A[i-1][j], A[i-1][j+1] if j+1 < len(A) else float("inf"))
        print A[-1]
        return min(A[-1])
        
        """
        # Logic 1: Wrong
        # * This takes into account the paths that cannot be traversed in a square like 1,4,9
        min_path = float('inf')
        import itertools
        for path in itertools.product(*A):
            min_path = min(sum(path), min_path)
        return min_path
        """
        
        
