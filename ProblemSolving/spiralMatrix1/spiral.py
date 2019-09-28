class Solution(object):
    def spiralOrder(self, matrix):
        
        # Logic 1: Naive Iteration into Spiral mode
        # Ref here: https://leetcode.com/problems/spiral-matrix/discuss/20599/Super-Simple-and-Easy-to-Understand-Solution nice logic
        
        if len(matrix) == 0:
            return []
        
        # Row start & end
        rowStart = 0
        rowEnd = len(matrix)-1
        
        # Column start & end
        columnStart = 0
        columnEnd = len(matrix[0])-1
        
        result = []
        
        while (rowStart <= rowEnd) and (columnStart <= columnEnd):
            
            # Traverse right columns 00 -> 0n
            for i in range(columnStart, columnEnd+1):
                result.append(matrix[rowStart][i])
            
            # Corner elements are visited twice handle them
            rowStart += 1
            
            # Traverse down rows 0n -> nn
            for i in range(rowStart, rowEnd+1):
                result.append(matrix[i][columnEnd])
            
            # Corner elements are visited twice handle them
            columnEnd -= 1
            
            if rowStart <= rowEnd:
                # Traverse left columns nn -> n0
                for i in range(columnEnd, columnStart-1, -1):
                    result.append(matrix[rowEnd][i])

            # Corner elements are visited twice handle them
            rowEnd -= 1
        
            if columnStart <= columnEnd:
                # Traverse up row n0 -> 00 (but 10)
                for i in range(rowEnd, rowStart-1, -1):
                    result.append(matrix[i][columnStart])
            
            # Corner elements are visited twice handle them
            columnStart += 1
            
        return result
        
