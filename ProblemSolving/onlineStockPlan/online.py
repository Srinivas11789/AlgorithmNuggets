# Pending...
class StockSpanner(object):

    # Logic to literally follow the question and build solution (no specific technique)
    
    def __init__(self):

        # Just initialize with a data structure
        self.prices = []
        self.span = []

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        
        self.prices.append(price)
        
        # Iterate the days to obtain max consecutive days
        n = len(self.prices)
        
        # Track count - account to track max to work for large num of days
        max_consecutive = 0
        count_progress = 0
        
        # Iteration from the current day backwards
        i = n-1
        while i >= 0:
            if self.prices[i] <= price:
                count_progress += 1
            else:
                break
                
            # Maximum condition
            #if count_progress > max_consecutive:
            #    max_consecutive = count_progress
            
            i -= 1
        
        self.span.append(count_progress)
        
        return count_progress


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
