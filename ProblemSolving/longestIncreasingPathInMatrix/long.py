# Logic 2: Backtrack with Memoization - 100 pass
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        def backtrack(current, visited):
            
            if self.cache[current[0]][current[1]] != 0:
                return self.cache[current[0]][current[1]]

            for i,j in [(0,1), (0,-1), (1,0), (-1,0)]:
                
                nxt = (current[0]+i, current[1]+j)
                
                if 0 <= nxt[0] < len(matrix) and 0 <= nxt[1] < len(matrix[0]):
                    
                    val = matrix[nxt[0]][nxt[1]]
                    if val <= matrix[current[0]][current[1]]:
                        continue
                    if nxt in visited:
                        continue
                    
                    self.cache[current[0]][current[1]] = max(self.cache[current[0]][current[1]], 1+backtrack(nxt, visited.union({nxt})))
                    
            return self.cache[current[0]][current[1]]
            
        self.mpath = 0
        self.cache = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                self.mpath = max(self.mpath, 1+backtrack((i,j), set()))
                #print(self.cache)
        return self.mpath


# Logic 1: Naive Backtrack - all pass but time limit exceeded
"""
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        def backtrack(current, visited, path):
            
            #print(current)
            if self.cache[current[0]][current[1]] != 0:
                return self.cache[current[0]][current[1]]
            
            if len(path) > self.mpath:
                self.mpath = len(path)
                
            for i,j in [(0,1), (0,-1), (1,0), (-1,0)]:
                nxt = (current[0]+i, current[1]+j)
                if 0 <= nxt[0] < len(matrix) and 0 <= nxt[1] < len(matrix[0]): 
                    val = matrix[nxt[0]][nxt[1]]
                    if val <= matrix[current[0]][current[1]]:
                        continue
                    if nxt in visited:
                        continue
                    self.cache[current[0]][current[1]] = max(self.cache[current[0]][current[1]],backtrack(nxt, visited.union({nxt}), path+[nxt]))
            return self.cache[current[0]][current[1]]
            
        self.mpath = 0
        self.cache = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                backtrack((i,j), set(), [(i,j)])
        return self.mpath
"""
