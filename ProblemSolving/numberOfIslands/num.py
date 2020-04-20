class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        # Logic 1 -> Naive Iteration and using sets --> Fails for scale cases ( has some pass rate )
        # * Visit islands and perform set union for every set intersection
        # * Count the number of such sets
        """
        # Set of all the islands in the format ij
        islands = []
        
        # 2D array iteration
        for i in range(len(grid)): # Rows
            for j in range(len(grid[0])): # Columns
                #print(i,j)
                land = set()
                if grid[i][j] == "1": # Ignore if water, focus on land
                    land.add(str(i)+str(j))
                    # Row top and bottom
                    if i-1 >= 0 and grid[i-1][j] == "1":
                        land.add(str(i-1)+str(j))
                    if i+1 < len(grid) and grid[i+1][j] == "1":
                        land.add(str(i+1)+str(j))
                    # Column left and right
                    if j-1 >= 0 and grid[i][j-1] == "1":
                        land.add(str(i)+str(j-1))
                    if j+1 < len(grid[0]) and grid[i][j+1] == "1":
                        land.add(str(i)+str(j+1))
                    #print(land, islands)
                    k = 0
                    while k < len(islands):
                        if len(land.intersection(islands[k])) > 0:
                            land = land.union(islands.pop(k))
                        else:
                            k += 1
                    if land:
                        islands.append(land)
        return len(islands)
        """
        
        # Logic 2 -> Recursive - 100 pass
        # * visit all 1s change then to visited "$" or "0" and backtrack to find more linked near to it
        
        def track_islands(r, c):
            #print(r, c)
            if r < len(grid) and c < len(grid[0]) and r >= 0 and c >= 0 and  grid[r][c] == "1":
                grid[r][c] = "$"
                track_islands(r-1, c)
                track_islands(r+1, c)
                track_islands(r, c+1)
                track_islands(r, c-1)
                return 1
            return 0
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    count += track_islands(i, j)
        
        return count
        
                            
