class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

	# Easy solution without math library - from discussion forum leetcode
        r = x
        while r*r > x:
            r = (r + x/r) / 2
        return r
        
	# Easy pythonic solution
        """
        # using math lib
        import math
        return int(math.sqrt(x))
        """      
        
        
