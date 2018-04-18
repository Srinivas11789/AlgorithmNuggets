class Solution(object):
    
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        
        # toeplitz rule and example
        """
        A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same element.
        Now given an M x N matrix, return True if and only if the matrix is Toeplitz.
        
        Input: matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
        Output: True
        Explanation:
        1234
        5123
        9512

        In the above grid, the diagonals are "[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]", and in each diagonal all elements are the same, so the answer is True.
        """
        
        # neglect the single element occuring at the beginning and the last
        # Diagnals with size 2, 3... are to be considered
        # Based on n x n make the checks, get the last list and for each number go back to the previous list and previous element to check the diagnal
        
        n = len(matrix)
        select = matrix[n-1]
        s = len(select)
        curr = n-1
        i = 1
        if s <= 1:
            return True
        while i > 0:
            element = matrix[curr][i]
            j = i-1
            k = curr-1
            if k < 0:
                i = -1
            while j >= 0 and k >= 0:
                #print j, k
                #print  matrix[k][j], element
                if matrix[k][j] != element:
                    return False
                k -= 1
                j -= 1
            i += 1
            if i == s:
                i = s-1
                #j = i-1
                curr = curr - 1
                #k = curr-1
                #element = matrix[k][i]
        
        """
        for i in range(1,s):
            element = select[i]
            j = i-1
            k = n-2
            while j >= 0 and k >= 0:
                print  matrix[k][j], element
                if matrix[k][j] != element:
                    return False
                k -= 1
                j -= 1
        """
            
        return True
            
                
                
        
        
        
