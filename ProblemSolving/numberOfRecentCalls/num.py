class RecentCounter(object):

    def __init__(self):
        # Maintain a list of pings at time
        self.pings = []
        

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        # Add ping data
        current_index = len(self.pings)-1
        if current_index < 0:
            current_index = 0
            
        self.pings.append(t)
        
        current_time = t
        past_3000second = t - 3000
        
        """
        # Time Limit Exceeded
        count = 0
        for item in self.pings:
            if item >= past_3000second:
                count += 1
            if item == current_time:
                return count
        """
        
        for i in range(current_index+1):
            if self.pings[i] >= past_3000second:
                return len(self.pings[i:current_index+1])
                
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
