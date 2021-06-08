class Solution:
    # Reference the solution in leetcode which is elaboarate: https://leetcode.com/problems/min-cost-climbing-stairs/solution/
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        # Dynamic Programming
        
        # 1. tabular
        """
        step_cost = [0]*(len(cost)+1)
        for i in range(2, len(step_cost)):
            one_down = step_cost[i-1]+cost[i-1]
            two_down = step_cost[i-2]+cost[i-2]
            step_cost[i] = min(one_down, two_down)
        return step_cost[-1]
        """
        
        # 2. recursive with memo
        """
        def min_cost(step):
            if step <= 1:
                return 0
            
            if step in memo:
                return memo[step]
            
            down_one = cost[step-1]+min_cost(step-1)
            down_two = cost[step-2]+min_cost(step-2)
            memo[step] = min(down_one, down_two)
            return memo[step]
        memo={}
        return min_cost(len(cost))
        """
        
        # 3. constant space
        down_one = down_two = 0
        for i in range(2, len(cost)+1):
            temp = down_one
            down_one = min(down_one + cost[i-1], down_two+cost[i-2])
            down_two = temp
        return down_one
