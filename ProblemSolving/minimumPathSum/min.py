class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        # Logic 3 - DP Iterative
        M = len(grid)
        N = len(grid[0])
        
        for i in range(M):
            if i > 0:
                grid[i][0] += grid[i-1][0]
            for j in range(1, N):
                if i > 0:
                    grid[i][j] += min(grid[i-1][j], grid[i][j-1])
                else:
                    grid[i][j] += grid[i][j-1]
        print grid
        return grid[-1][-1]
        
        # Logic 2 - DP - Recursive Memoization with an extra grid
        """
        self.row = len(grid)-1
        self.column = len(grid[0])-1
        self.grid = grid
        self.memo_grid = [[-1]*(self.column+1)]*(self.row+1)
        
        # Recurse and find all path like traversing a bst
        def recurse_all_paths(g_element, grid, memo):
            M = len(grid)
            N = len(grid[0])

            # Grid is a tuple with m x n
            m = g_element[0]
            n = g_element[1]
            
            print(m, n)
            
            if m == M or n == N:
                return float('inf')  
            elif memo[m][n] != -1:
                return memo[m][n]
            else:
                # Recurse down and right path at each point
                memo[m][n] = min(recurse_all_paths([m+1, n], grid, memo), recurse_all_paths([m, n+1], grid, memo)) + grid[m][n]
    
            return memo[m][n]

        self.memo_grid[self.row][self.column] = self.grid[self.row][self.column]
        return recurse_all_paths([0, 0], self.grid, self.memo_grid)
        """
        
        # Brute force - Only recursive through all the path - Time Limit Exceeded - (No memoization)
        """
        self.mini_path = float('inf')
        self.row = len(grid)-1
        self.column = len(grid[0])-1
        self.grid = grid
        
        # Recurse and find all path like traversing a bst
        def recurse_all_paths(g_element, path_sum):
            #print(g_element, path_sum)

            # Grid is a tuple with m x n
            m = g_element[0]
            n = g_element[1]
            
            # Path_sum is an integer record of all the values met
            # Update path sum as we iterate over each element
            path_sum += self.grid[m][n]
            
            # End Sum Calculation when length is reached
            if m == self.row and n == self.column:
                if path_sum < self.mini_path:
                    self.mini_path = path_sum
            else:
                # Recurse down and right path at each point
                if m < self.row and (path_sum+self.grid[m+1][n]) < self.mini_path:
                    recurse_all_paths([m+1, n], path_sum)
                if n < self.column and (path_sum+self.grid[m][n+1]) < self.mini_path:
                    recurse_all_paths([m, n+1], path_sum)
        
        recurse_all_paths([0, 0], 0)
        return self.mini_path
        """
