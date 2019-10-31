class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        result = 0
        neg = False
        if x < 0:
            x = abs(x)
            neg = True
        maxi = 2**31
        while x > 0:
            result = result*10 + x%10
            x = x/10
            if result > maxi or result < -maxi:
                return 0
        if neg:
            result = -(result)
        return result
