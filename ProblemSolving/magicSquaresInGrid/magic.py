class Solution(object):
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        def is_magic_square(matrix):
            
            #print(matrix)
            # For a 3x3 grid
            
            # continue only if 3x3 grid
            if len(matrix[0]) != 3 and len(matrix) != 3:
                return False
            
            # distinct number check
            distinct = set()
            for r in matrix:
                distinct = distinct.union(set(r))
            #print(distinct)
            if len(distinct) != 9:
                return False
            
            # Check all the sum 
            check = sum(matrix[0])
            
            # row sum
            for r in range(1, len(matrix)):
                if check != sum(matrix[r]):
                    return False
            
            # column and diagnal sum
            for c in range(len(matrix[0])):
                
                # column sum
                col_sum = 0
                for r in range(len(matrix)):
                    # Distinct digits from 1 to 9 only rule
                    if matrix[r][c] < 1 or matrix[r][c] > 9:
                        return False
                    col_sum += matrix[r][c]
                if col_sum != check:
                    return False
                
                # forward diagnal sum
                diag_sum = 0
                row = 0
                column = c
                while row < 3 and column < 3:
                    diag_sum += matrix[row][column]
                    #print(matrix[row][column], row, column)
                    row += 1
                    column += 1
                if row == 3 and column == 3 and diag_sum != check:
                    return False
                
                # backward diagnal sum
                diag_sum = 0
                row = 0
                column = c
                while row < 3 and column >= 0:
                    diag_sum += matrix[row][column]
                    #print(matrix[row][column], row, column)
                    row += 1
                    column -= 1
                #print(diag_sum, row, column)
                if row == 3 and column == -1 and diag_sum != check:
                    return False
                
            return True
        
        count = 0
        r = 0
        while r < len(grid):
            for c in range(len(grid[0])):
                #print(r, c, r+2, c+2)
                if r+2 < len(grid) and c+2 < len(grid[0]):
                    new_matrix = []
                    for row in range(r, r+3):
                        new_matrix.append(grid[row][c:c+3])
                    if is_magic_square(new_matrix):
                            count += 1
            r += 1
        return count
    
        # Note: [[10,3,5],[1,6,11],[7,9,2]] was a correct magic square but violates the question of 1 to 9 distinct digits so the answer is False, this was very confusing to me as it was a magic square already with all sum equalities
    
        
