class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        # Hacky
        x = str(x)
        if '-' in x:
            value =  int('-'+x[1:][::-1])
        else:
            value = int(x[::-1])
        
        # Max 32 bit integer value 2147483647
        if value > 2147483647 or value < -2147483647:
            return 0
        else:
            return value
        
