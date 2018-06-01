class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        """
        # Loop Method
        if n == 0:
            return False
        
        while n%3 == 0:
            n = n//3
        
        if n == 1:
            return True
        else:
            return False
        """
        
        # Math onliner - n > 0 is obvious and 1162261467 is the highest power of 3, using that to check divisibility
        return n > 0 and 1162261467%n == 0
        
