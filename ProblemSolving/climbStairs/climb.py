#### Analysis further required - ****
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        # 4 Line solution from discussions - 100 pass
        
        x = y = 1
        for i in range(n):
            x, y = y, x+y
        return x
        
        
        """
        # 100 pass
        # with reference from solution - recursive solution works best + memoization
        # dynamic programming problem as well
        # 0 1 2 3 5 8 13 
        
        def recurse_stairs(n):
            
            if n == 0:
                return 0
            if n == 1:
                return 1
            if n == 2:
                return 2
            if len(values)>n:
                return values[n]
            
            value = recurse_stairs(n-1) + recurse_stairs(n-2)
            values.append(value)
            return value
        
        # memoize
        values = [0,1,2]
        return recurse_stairs(n)
        """
        
        """
        # Attempt became more complex hence stopped
        
        # every time you climb only 1 or 2 steps 
        # Create i for i in range(n) => with only 2s or with only 1s or with both
        
        # All ones scenario - by default include 1 everytime
        count = 1
        
        # All 2s scenario
        if n%2 == 0:
            count += n//2
        
        # Both ones and twos combination
        if n%2 == 0:
            # 14 => 7 2s => 6,1 - 5,2 - 4,3 - 3,4 - 2,5 - 1,6 => 7*6
        """ 
        
        
        
