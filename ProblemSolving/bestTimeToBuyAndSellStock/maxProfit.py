class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        
        # Greedy algorithm
        
        # As we thought,
        # * Creating a reference for minimum and maximum values is a trick
        # * Be greedy to choose the minimum and execute transaction as soon as we get profit
        
        # Number of days
        n = len(prices)
        
        # Assume min
        minimum = prices[0]
        
        # Total Money 
        total = 0
        
        for i in range(n):
            # If we found a minimum along the way, update it
            if prices[i] < minimum:
                minimum = prices[i]
            # As soon as we get a profit execute transaction
            # * Calculate profit as something greater than minimum + fee (Done calculate sell fee here, as atmost 0 is also a profit)
            elif prices[i] > minimum + fee:
                total += prices[i] - minimum - fee
                # Calculate the new minimum now as the executed proces minus the fees (this would be the buy fee)
                minimum = prices[i] - fee
            #print total
        
        return total
    
        """
        # Literal Calculation
        
        # Number of days
        n = len(prices)
        mid = n//2
        
        # reference array instead of calculating max and min prices as we traverse
        #prices_range = sorted(prices)
        minimum = prices[0] 
        
        #
        total = 0
        bought = False
        
        # Iterate over the prices range
        # * Find the min max as we traverse, calculate the max delta and execute the trade
        for i in range(n):
            if bought == False and prices[i] <= minimum:
                total -= prices[i]
                total -= fee
                bought = True
            if bought == True and prices[i] > minimum+fee:
                total += prices[i]
                total -= fee
                minu
                bought = False
        
        return total
        """
                 
                
        
