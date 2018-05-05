class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        
        """
        # Simulating the sequence
        n = len(timeSeries)
        i = 1
        total = 0
        while i <= timeSeries[n-1]:
            if i in timeSeries:
                total = i + (duration-1)
                i = i + (duration-1)
            else:
                i += 1
            print total,i
        return total
        """
        
        # Just find if they are overlapping sets or not logic
        # Original Thought but confused Implementation - in reference with a dicussion solution
    
        # Length of the series
        n = len(timeSeries)
    
        # Length being 0
        if n == 0:
            return 0
    
        # Variable declaration
        
        # result
        result = 0
        
        # Calculate start and end for the first timeSeries entry
        
        # Start time
        start = timeSeries[0]
        # end time
        end = start + duration
        
        # Iterating through the series to find over lapping and non overlapping sets - 0 already done above so from 1
        for i in range(1,n):
            
            # Overlapped condition where the time occurs before the end, change the end alone to a new end from the overlap
            if timeSeries[i] <= end:
                end = timeSeries[i] + duration
            else:
                # If no overlap occurs, then the start and end BOTH have to be changed to new values, and update the result as well
                result += end - start
                start, end = timeSeries[i], timeSeries[i]+duration
            
        
        result += end - start
        
        return result
                
            
            
            
            
        
        
        
        
        
            
                
