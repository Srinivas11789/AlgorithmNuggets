class Solution:
    # Logic 1: O(N) + O(M) + O(NM) iterations to fix the row and col indexes and then do restricted search with breaks
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        
        rid = 0
        cid = 0
        
        for i in range(len(matrix)):
            if matrix[i][0] <= target:
                rid += 1
        
        for j in range(len(matrix[0])):
            if matrix[0][j] <= target:
                cid += 1
        
        if rid == 0 and cid == 0 and matrix[0][0] == target:
            return True
        if not matrix:
            return False
        
        for r in range(rid):
            for c in range(cid):
                print(r,c,matrix[r][c])
                if matrix[r][c] == target:
                    return True
                elif matrix[r][c] > target:
                    break
                else:
                    continue
        
        return False
