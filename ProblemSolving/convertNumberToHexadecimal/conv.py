class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        
        """
        # 100 pass
        # Logic 1: Maximum value of 32 bit unsigned integer
        # Either create a dictionary of alphabets for hex from a-f or create such a list
        hexi = ["a","b","c","d","e","f"]
        
        if num == 0:
            return "0"
        
        if num<0:
            num = num+4294967296 # maximum value for a 32-bit unsigned integer in computing (wiki)
                                 # value can be got by -1 & 0xffffffff  
        
        result = []
        while num:
                value = num%16
                if value > 9:
                    value = hexi[int(str(value)[-1])]
                result.append(str(value))
                num = num//16

        return "".join(result[::-1])
        """
    
        # Logic 3: Using numpy to convert to unsigned 32 bitinteger - 100pass
        import numpy
        hexi = ["a","b","c","d","e","f"]
        
        if num == 0:
            return "0"
        
        if num<0:
            num = numpy.uint32(num)
            
        result = []
        while num:
                value = num%16
                if value > 9:
                    value = hexi[int(str(value)[-1])]
                result.append(str(value))
                num = num//16

        return "".join(result[::-1])
        
           
        
