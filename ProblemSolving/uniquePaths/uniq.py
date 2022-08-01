class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        grid = [[0 for i in range(n)] for i in range(m)]
        
        grid[0][0] = 1
        
        for i in range(m):
            for j in range(n):
                if i-1 >= 0:
                    grid[i][j] += grid[i-1][j]
                if j-1 >= 0:
                    grid[i][j] += grid[i][j-1]
        
        #print(grid)
        return grid[m-1][n-1]
