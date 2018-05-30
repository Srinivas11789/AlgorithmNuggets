class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # Proper Dynamic Programming Solution - pending 
        
        
        # Hacky Solution
        # Reference from discussions -> yangshun
        
        def maximizeScore(points):
            current = past = 0
            for point in points:
                past, current = current, max(point+past, current)
            return current
    
        # Array holding points of all the input, index --> points relationship
        points = [0]*10001
        for num in nums:
            points[num] += num
        return maximizeScore(points)
        
        
        
        
        

    
    
        
        
