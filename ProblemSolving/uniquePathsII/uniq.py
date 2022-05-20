# Logic 1: Brute force --> correct but exceeds time limit
"""
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        def findWays(current, visited, path):
            #print(self.path_exists)
            if current in self.path_exists:
                self.count += 1
                return

            if current == (len(obstacleGrid)-1, len(obstacleGrid[0])-1):
                if obstacleGrid[current[0]][current[1]] != 1:
                    self.paths.append(path)
                    self.path_exists = self.path_exists.union(path)
                    self.count += 1
                return
            
            if current[1]+1 < len(obstacleGrid[0]):
                right = (current[0], current[1]+1)
                if right not in visited and obstacleGrid[right[0]][right[1]] != 1:
                    findWays(right, visited.union({right}), path+[right])
                
            if current[0]+1 < len(obstacleGrid):
                down = (current[0]+1, current[1])
                if down not in visited and obstacleGrid[down[0]][down[1]] != 1:
                    findWays(down, visited.union({down}), path+[down])
                    
            return
            
        self.paths = []
        self.count = 0
        self.path_exists = set()
        if obstacleGrid[0][0] == 1:
            return 0
        findWays((0,0), set(), [(0,0)])
        #print(self.paths)
        return self.count
"""

# Logic 2: dynamic prog with tabular values (memo every cell) --> 100 pass
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        # Tip: only down and right
        rows = len(obstacleGrid)
        columns = len(obstacleGrid[0])
        
        if obstacleGrid[0][0] == 1 or obstacleGrid[rows-1][columns-1] == 1:
            return 0
        
        obstacleGrid[0][0] = 1
         
        # 1st row
        for c in range(1, columns):
            if obstacleGrid[0][c] == 0 and obstacleGrid[0][c-1] == 1: # only if left cell is 1 we can move here
                obstacleGrid[0][c] = 1
            elif obstacleGrid[0][c] == 1:
                obstacleGrid[0][c] = 0
        
        # 1st column
        for r in range(1,rows):
            if obstacleGrid[r][0] == 0 and obstacleGrid[r-1][0] == 1:
                obstacleGrid[r][0] = 1
            elif obstacleGrid[r][0] == 1:
                obstacleGrid[r][0] = 0
                
        # All other cells
        for r in range(1, rows):
            for c in range(1, columns):
                if obstacleGrid[r][c] == 1:
                    obstacleGrid[r][c] = 0
                    continue
                obstacleGrid[r][c] = obstacleGrid[r-1][c] + obstacleGrid[r][c-1]
                    
        #print(obstacleGrid)
        
        return obstacleGrid[rows-1][columns-1]

