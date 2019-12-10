class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        # Exploration: 
        # * Based on the problem of MINIMIZING number of coins, we go greedy to choose the highest coin value each time
        #   * Drawback on this would be, there might be one option which is not optimal which might succeed that wont be found if greedy approach is taken
        # * Recurse as we have to iterate every time for each value and reuse the code
        
        # Logic 1 --> Brute Force --> Obvious time limit exceeded
        """
        def coinChangeForValue(coins: List[int], amount: int, num_of_coins: int, selected: List[int]) -> int:
            if amount > 0:
                for change in coins:
                    if change <= amount:
                        coinChangeForValue(coins, amount-change, num_of_coins+1, selected+[change])
            else:
                #print(amount, num_of_coins, selected)
                if amount == 0:
                    #print(coins, amount, num_of_coins, selected)
                    if num_of_coins < self.optimal_choice:
                        self.optimal_choice = num_of_coins
            return
        
        self.optimal_choice = float('inf')
        coins = sorted(coins, reverse=True)
        coinChangeForValue(coins, amount, 0, [])
        if self.optimal_choice == float('inf'):
            return -1
        else:
            return self.optimal_choice
        """
        
        # Logic 2 --> Memoize the above - in progress
        """
        def coinChangeForValue(coins: List[int], amount: int, num_of_coins: int) -> int:
            print(amount, num_of_coins, self.memo)
            if amount in self.memo:
                coins = num_of_coins + self.memo[amount]
                if coins < self.optimal:
                    self.optimal = coins
            elif amount > 0:
                for change in coins:
                    if change <= amount:
                        current_target = amount-change
                        num_of_coins += 1
                        if current_target not in self.memo:
                            self.memo[current_target] = num_of_coins
                        coinChangeForValue(coins, current_target, num_of_coins)
            else:
                if amount == 0:
                    if num_of_coins < self.optimal:
                        self.optimal = num_if_coins
        
        self.memo = {}
        self.optimal = float('inf')
        coins = sorted(coins, reverse=True)
        coinChangeForValue(coins, amount, 0)
        if self.optimal == float('inf'):
            return -1
        return self.optimal
        """
        
        # Logic 3: Bottom Up Approach
        # * Calculate for all optimal subproblems
        
        # Create space for subproblems
        dp = [float('inf')]*(amount + 1) # Initialize
        
        # Initial 0 value
        dp[0] = 0
        
        # Iterate coins
        for change in coins:
            # For each coin, iterate value until amount
            for value in range(change, amount+1):
                # Track min value
                dp[value] = min(dp[value], dp[value-change]+1)
        
        #print(dp)
        return dp[-1] if dp[-1] != float('inf') else -1
        
