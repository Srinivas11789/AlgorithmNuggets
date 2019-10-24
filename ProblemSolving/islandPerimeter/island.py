class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        # Logic 1:
        # * We are assured to have one island with no lakes
        # * We just need to find the 1s and if this could be a border. 
        # * If it is a border it has 0 on that side.
        
        n = len(grid)
        m = len(grid[0])
        
        perimeter = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    for side in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                        if side[0] < 0 or side[1] < 0:
                            perimeter += 1
                        elif side[0] >= n or side[1] >= m:
                            perimeter += 1
                        elif grid[side[0]][side[1]] == 0:
                            perimeter +=1
        return perimeter
        
