class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        
        """
        # Time limit exceed for -1,1
        
        # mimic return a+b without using + or -
        
        # Solution reference from geekofgeeks
        
        # Iterate till there is no carry
        while b != 0:
            
            # carry contains common set of bits of both a and b 
            carry = a & b
            
            # sum of bits of a, b with bits that are different or not set
            a = a ^ b
            
            # carry is shifted by 1, so that adding this gives the sum
            b = carry << 1
        
        return a
        """
        """
        # Above solution in a recursive manner - timeout
        def Add(a,b):
            # Recursive approach
            if b == 0:
                return a
            else:
                return Add(a^b, (a&b) << 1)
            
        return Add(a,b)
        """
        
        """
        # Hacky Solution - Pythonic
        return sum([a,b])
        """
        
        # 32 bits integer max
        MAX = 0x7FFFFFFF
        # 32 bits integer min
        MIN = 0x80000000
        # mask to get last 32 bits
        mask = 0xFFFFFFFF
        
        while b != 0:
            a,b = (a^b) & mask, ((a&b) << 1) & mask
        return a if a <= MAX else ~(a^mask)
        
            
        
        
        
