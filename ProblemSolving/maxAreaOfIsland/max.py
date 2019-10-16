class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        """
        result = [set()]
        maxi = -float('inf')
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    # create new island
                    if not result[-1]:
                        result[-1].add((i, j))
                    # column
                    if i-1 >= 0 and grid[i-1][j] == 1:
                        result[-1].add((i-1, j))
                    if i+1 < len(grid) and grid[i+1][j] == 1:
                        result[-1].add((i+1, j))
                    # row
                    if j-1 >= 0 and grid[i][j-1] == 1:
                        result[-1].add((i, j-1))
                    if j+1 < len(grid[0]) and grid[i][j+1] == 1:
                        result[-1].add((i, j+1))
                    
                    if len(result[-1]) > maxi:
                        maxi = len(result[-1])
                
                    next_island = True
                    for x,y in result[-1]:
                        print(x,y)
                        if (x+1 < len(grid) and grid[x+1][y] != 0) and (y+1 < len(grid[0]) and grid[x][y+1] != 0):
                            next_island = False
                    
                    if next_island:
                        result.append(set())
                    print(result)

        return maxi
        """
    
        # Recursive Logic
        def sizeOfIsland(grid, i, j):
            if i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0]) and grid[i][j] == 1:
                grid[i][j] = 0
                return 1 + sizeOfIsland(grid, i-1, j) + sizeOfIsland(grid, i+1, j) + sizeOfIsland(grid, i, j+1) + sizeOfIsland(grid, i, j-1)
            return 0
            
        maxSize = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    maxSize = max(maxSize, sizeOfIsland(grid, i, j))
                print(grid)
        return maxSize
                    
