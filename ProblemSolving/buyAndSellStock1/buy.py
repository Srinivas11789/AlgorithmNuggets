class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        # Find the max from the right hand side and min from left hand side and subtract
        # Idea and approach was perfect to start from brute force and think of min max resolution
        # Channelize and think about what should be done? Starting with min max ideology dont move into finding max min in the optimal manner. Rather try what are you wanting to accomplish? for example in this problem, we have to think like plotting a graph to get the peaks, like, we have to find the minimum which occurs while traversing the list, the maximum to be selected only is decisive, hence we could use logic like voting problem -> with min set, moving through the array to get the maximum value to be returned applying the formula directly rather than waiting to find the maximum. Just like how you calculate implement it.!!
        n = len(prices)
        mini = 6000000000
        max_profit = 0
        for i in range(n):
            if prices[i] < mini:
                mini = prices[i]
            elif prices[i] - mini > max_profit:
                max_profit = prices[i] - mini
        return max_profit
        
        """
        # brute force
        # time limit exceeded
        n = len(prices)
        maxi = 0
        for i in range(n-1,-1,-1):
            for j in range(i-1,-1,-1):
                if prices[j] < prices[i]:
                    if prices[i]-prices[j] > maxi:
                        maxi = prices[i] - prices[j]
        return maxi
        """
        
