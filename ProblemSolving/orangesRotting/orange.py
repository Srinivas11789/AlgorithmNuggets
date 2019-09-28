class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        # Logic 1: Use a datastructure to help ( dict or stack ) - lets use stack of rotten to start with
        # 1st find the rotten orange
        # 2nd recurse or add the adjacent oranges to a bucket
        # Continue until no rotten oranges are found
        
        # Build stack of rotten oranges
        stack = [[]]
        count_oranges = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # Finding the rotten orange
                if grid[i][j] == 2:
                    stack[0].append((i, j))
                if grid[i][j] > 0:
                    count_oranges += 1
        
        minute = 0
        rotten_orange = len(stack[0])
        #print(stack, rotten_orange)
        while stack:
            current_stack = stack.pop(0)
            new_stack = []
            while current_stack:
                current_rotten = current_stack.pop(0)
                x = current_rotten[0]
                y = current_rotten[1]
                # build adjacents and check
                if x-1 >= 0 and grid[x-1][y] == 1:
                    grid[x-1][y] += 1
                    new_stack.append((x-1,y))
                    rotten_orange += 1
                if x+1 < len(grid) and grid[x+1][y] == 1:
                    grid[x+1][y] += 1
                    new_stack.append((x+1,y))
                    rotten_orange += 1
                if y-1 >= 0 and grid[x][y-1] == 1:
                    grid[x][y-1] += 1
                    new_stack.append((x,y-1))
                    rotten_orange += 1
                if y+1 < len(grid[0]) and grid[x][y+1] == 1:
                    grid[x][y+1] += 1
                    rotten_orange += 1
                    new_stack.append((x,y+1))
            if new_stack:
                stack.append(new_stack)
                minute += 1
            #print(stack)
        #print(rotten_orange, count_oranges)
        if rotten_orange != count_oranges:
            return -1
        return minute
                
                
            
                    
        
