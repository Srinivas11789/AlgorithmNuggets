
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
        if numRows == 0:
            return []
        
        pascal_triangle = [[1], [1,1]] # Constant values which are common for any pascal triangle
        
        row = 2
        while row < numRows:
            previous = pascal_triangle[-1]
            current = []
            for i in range(len(previous)+1):
                if i-1 < 0 or i+1 > len(previous):
                    current.append(1)
                else:
                    current.append(previous[i]+previous[i-1])
            pascal_triangle.append(current)
            row += 1
        
        return pascal_triangle[:numRows]
