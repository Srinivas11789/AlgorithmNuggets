class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        
        count = {}
        n = len(candies)
        divide = n//2
        
        for candy in candies:
            if candy not in count:
                count[candy] = 0
            count[candy] += 1
        
        if len(count.keys()) >= divide:
            return divide
        else:
            return len(count.keys())
        
            
