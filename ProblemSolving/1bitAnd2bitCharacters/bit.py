class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """

        # Iterate to remove all the two bit and one bit characters until the array is with only one element
        i = 0
        while i < len(bits):
            if bits[i] == 1:
                bits.pop(i)
                bits.pop(i)
            else:
                if len(bits) > 1:
                    bits.pop(i)
                else:
                    i += 1
        
        # Debug
        print bits
        
        # Last Character Check
        if len(bits) == 1 and bits[0] == 0:
            return True
        else:
            return False
        
        
                
        
        
        
