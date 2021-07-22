class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        self.islands = []
        
        def findIsland(i, j , currIsland, grid):
            currIsland.add((i,j))
            for x in [-1,1]:
                if -1 < i+x < len(grid) and grid[i+x][j] == "1" and (i+x,j) not in currIsland:
                    currIsland.update(findIsland(i+x,j,currIsland,grid))
            for y in [-1,1]:
                if -1 < j+y < len(grid[0]) and grid[i][j+y] == "1" and (i,j+y) not in currIsland:
                    currIsland.update(findIsland(i,j+y,currIsland,grid))
            return currIsland
        
        def isAlreadyAnIsland(x, y):
            for island in self.islands:
                #print(x,y,island)
                if (x,y) in island:
                    return True
            return False
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and not isAlreadyAnIsland(i,j):
                    currIsland = findIsland(i,j,set(),grid)
                    #print(currIsland)
                    self.islands.append(currIsland)
        
        return len(self.islands)
