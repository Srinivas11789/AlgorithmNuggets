class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        
        # Logic 1: naive iteration of matrix O(n*m) to contruct the transpose
        transpose = []
        
        for m in matrix:
            for i in range(len(m)):
                if i >= len(transpose):
                    transpose.append([])
                transpose[i].append(m[i])
                
        return transpose
