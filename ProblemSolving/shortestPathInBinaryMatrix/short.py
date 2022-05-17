class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        
        def backtrack(current, path, visited):
            #print(path)
            
            i, j = current
            
            if self.min != float('inf') and path > self.min:
                return
            
            if i == self.max_row-1 and j == self.max_col-1:
                if self.min > path:
                    self.min = path
                return
                
            for m in self.dirs:
                for n in self.dirs:
                    a = i+m
                    b = j+n
                    if (m==0 and n==0):
                        continue
                    if a >= self.max_row or a < 0:
                        continue
                    if b >= self.max_col or b < 0:
                        continue
                    if grid[a][b] == 0 and (a,b) not in visited:
                         backtrack((a,b), path+1, visited.union({(a,b)}))
            return
        
        
        if grid[0][0] != 0 or grid[-1][-1] != 0:
            return -1
        
        self.min = float('inf')
        self.max_row = len(grid)
        self.max_col = len(grid[0])
        self.dirs = [-1, 0, 1]
        #backtrack((0,0), [(0,0)], set((0,0)))
        backtrack((0,0), 1, set((0,0)))
        if self.min == float('inf'):
            return -1
        return self.min
