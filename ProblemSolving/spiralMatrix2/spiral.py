class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        
        # Logic 1: Create a nxn matrix and use the same logic to traverse as in the spiral matrix 1
        
        # create a nxn matrix
        matrix = [[0 for i in range(n)] for j in range(n)]
        
        # Row start & end
        rowStart = 0
        rowEnd = len(matrix)-1
        
        # Column start & end
        columnStart = 0
        columnEnd = len(matrix[0])-1
        count = 0
        
        while (rowStart <= rowEnd) and (columnStart <= columnEnd):
            
            # Traverse right columns 00 -> 0n
            for i in range(columnStart, columnEnd+1):
                count += 1
                matrix[rowStart][i] = count
            
            # Corner elements are visited twice handle them
            rowStart += 1
            
            # Traverse down rows 0n -> nn
            for i in range(rowStart, rowEnd+1):
                count += 1
                matrix[i][columnEnd] = count
            
            # Corner elements are visited twice handle them
            columnEnd -= 1
            
            if rowStart <= rowEnd:
                # Traverse left columns nn -> n0
                for i in range(columnEnd, columnStart-1, -1):
                    count += 1
                    matrix[rowEnd][i] = count

            # Corner elements are visited twice handle them
            rowEnd -= 1
        
            if columnStart <= columnEnd:
                # Traverse up row n0 -> 00 (but 10)
                for i in range(rowEnd, rowStart-1, -1):
                    count += 1
                    matrix[i][columnStart] = count
            
            # Corner elements are visited twice handle them
            columnStart += 1
            
        return matrix
"""
# My Old contest logic that did not work
        grid = [[0 for i in range(n)] for i in range(n)]
        
        # 0,0 -> 0,1 -> 0,2 -> 1,2 -> 2,2 -> 2,1 -> 2,0  
        
        i = j = 0
        
        # I's turn is True and J's turn is False
        turn = False
        
        # to control loop
        count = 0
        value = 0
        grid[0][0] = value
        time = 1
        
        while count < n**2:
            
            print(i,j,time)
            if time%2 != 0:
                for x in range(j, n):
                    if grid[i][x] == 0:
                        value += 1
                        print(i,x, value)
                        grid[i][x] = value
                        count += 1
                    else:
                        j = x
                        break
                
                if j == 0:
                    j = n-1
                i += 1

                for y in range(i, n):
                    if grid[y][j] == 0:
                        value += 1
                        print(y, j, value)
                        grid[y][j] = value
                        count += 1
                    else:
                        i = y
                        break
                if i == 0:
                    print("adsada")
                    i = n-1
                j -= 1
            else:
                print("hi", i, j )
                for x in range(j, -1, -1):
                    if grid[i][x] == 0:
                        value += 1
                        print(i, x, value)
                        grid[i][x] = value
                        count += 1
                    else:
                        j = x
                        break
                i -= 1
                for y in range(i, -1, -1):
                    if grid[y][j] == 0:
                        value += 1
                        print(y, j, value)
                        grid[y][j]= value
                        count += 1
                    else:
                        i = y
                        break
            time += 1
            print(grid)
            
            """
            if j == n-1 and i == n-1:
                turn = False
            elif j == n-1:
                turn = True
            elif j == 0:
                turn = True
            else:
                turn = False
                
            if turn == False:
                if i == n-1:
                    j -= 1
                else:
                    j += 1
            else:
                if j == 0:
                    i -= 1
                else:
                    i += 1
            
            value += 1
            print(i,j, value)
            grid[i][j] = value -1
            
            count += 1
            """
        
        return grid
            
        
"""
