class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        # Logic 1: At each price, try to find max and subtract - Obviously time limit exceeded
        """
        profit = 0
        for p in range(len(prices)):
            if prices[p+1:]:
                current_profit = max(prices[p+1:]) - prices[p]
                if current_profit > profit:
                    profit = current_profit
        return profit
        """
    
        # Logic 2: Greedy --> Buy when the price decreases from previous day and sell when it increases next day
        """
        buy = None
        sell = None
        for p in range(len(prices)):
            if buy == None and (prices[p] < prices[p-1] or prices[p+1] > prices[p]):
                buy = p
            elif buy < sell and prices[p] < prices[buy]:
                buy = p
            elif sell == None and buy != None and prices[p] > prices[buy]:
                sell = p
            elif buy != None and sell != None and sell > buy and prices[p] > prices[sell]:
                sell = p
        print(buy, sell)
        if not buy or not sell:
            return 0
        return sell-buy
        """
        
        # Logic 3: 2 pointer method - does not work
        """
        n = len(prices)
        buy = 0
        sell = n-1
        profit = 0
        while buy < sell:
            profit = max(prices[sell] - prices[buy], profit)
            if prices[sell] < prices[buy]:
                buy += 1
            elif prices[buy] > prices[sell]:
                sell -= 1
        return prices[sell]-prices[buy]
        """
        
        # Logic 4: O(N) iterate and follow mini and profit
        mini = float('inf')
        n = len(prices)
        profit = 0
        for i in range(n):
            if prices[i] < mini:
                mini = prices[i]
            elif prices[i]-mini > profit:
                profit = prices[i]-mini
        return profit
