# Reference: https://leetcode.com/problems/01-matrix/discuss/142584/Python-simple-and-readable-solution-beats-100
class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        
        # 2 x O(mn) logic
        # 1. Iteration 1 from left to right updated with min distance
        # 2. Iteration 2 from right to left updated with min distance
        
        m = len(matrix)
        n = len(matrix[0])
        
        # 1
        for i in range(m):
            for j in range(n):
                if matrix[i][j] != 0:
                    matrix[i][j] = float('inf')
                    if i > 0 and matrix[i-1][j] +1 < matrix[i][j]:
                        matrix[i][j] = matrix[i-1][j] + 1 
                    if j > 0 and matrix[i][j-1] +1 < matrix[i][j]:
                        matrix[i][j] = matrix[i][j-1] + 1
        
        # 2
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if matrix[i][j] != 0:
                    if i < m-1 and matrix[i+1][j] +1 < matrix[i][j]:
                        matrix[i][j] = matrix[i+1][j] + 1 
                    if j < n-1 and matrix[i][j+1] +1 < matrix[i][j]:
                        matrix[i][j] = matrix[i][j+1] + 1
        
        return matrix
        
                        
                
                
                
