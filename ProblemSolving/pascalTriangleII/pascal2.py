class Solution:
    def getCurrentRow(self, row: int, triangle) -> List[int]:   
        # Iterate Row
        r = []
        for j in range(row):
            # Base case
            if j == 0 or j == row-1:
                r.append(1)
            else:
                r.append(triangle[row-1][j-1] + triangle[row-1][j])
        return r
    
    def getRow(self, rowIndex: int) -> List[int]:
        triangle = []
        for i in range(rowIndex+2):
            triangle.append(self.getCurrentRow(i, triangle))
        print(triangle)
        return triangle[rowIndex+1]
            
