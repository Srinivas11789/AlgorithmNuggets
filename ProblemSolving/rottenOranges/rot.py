class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        rotten = 0
        minute = 0
        old_rotten = 1
        
        while old_rotten != rotten:
            for i in range(3):
                for j in range(3):
                    old_rotten = rotten
                    if grid[i][j] == 2:
                        if i-1 > 0 and grid[i-1][j] != 2:
                            grid[i-1][j] = 2
                            rotten += 1
                        if i+1 < 3 and grid[i+1][j] != 2:
                            grid[i+1][j] = 2 
                            rotten += 1
                        if j-1 > 0 and grid[i][j-1] != 2:
                            grid[i][j-1] = 2
                            rotten += 1
                        if j+1 < 3 and grid[i][j+1] != 2:
                            grid[i][j+1] = 2
                            rotten += 1
                    print i, j
                    if rotten != old_rotten:
                        minute += 1
        return minute
        
        
