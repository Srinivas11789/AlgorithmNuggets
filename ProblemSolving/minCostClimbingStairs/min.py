class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        
        # There are 2 ways to think this solution out
        # 1. At each step, the next step could be one or two steps ahead
        # 2. Looking from backwards, at each step the cost incurred for that location is the minimum(-1,-2)
        #    Iterting to calculate all the minimum cost progressively will give the last 2 elements of the array or the top stack of steps from where you can jump to the top of the stairs in one or 2 step
        
        
        # Starting at 2 because both 1 and 2 can be considered for jumping
        n = len(cost)
        for i in range(2,n):
            # Cost at that particular level is
            cost[i] += min(cost[i-1], cost[i-2])
        
        return min(cost[n-1], cost[n-2])
    
            
        
