class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        
        """
        #loop
        if num == 0:
            return False
        
        while num%4 == 0:
            num = num//4
        
        if num == 1:
            return True
        else:
            return False
        """
        
        """
        # Take some high power of 4
        for i in range(40):
            print 4**i
        """
        
        #1
        import re
        # Power of 4 binary comparison
        return bool(re.match('^0b1(00)*$',bin(num))) 
    
        #2 
        return num > 0 and num & (num-1) == 0 and len(bin(num)[3:])%2 == 0
    
