class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        reverse = ""
        limit = 2**31
        if x < 0:
            reverse += "-"
        x = abs(x)
        reverse += "0"
        while x:
            reverse += str(x%10)
            x = x/10
            if int(reverse) > limit-1 or int(reverse) < -(limit):
                return 0
        return int(reverse)
