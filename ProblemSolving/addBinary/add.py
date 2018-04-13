class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        
        # Input is in a binary string notation. Use int to convert it into binary with base 2
        a = int(a,2)
        b = int(b,2)
        # Addition operation
        c = a + b
        # Convert the int sum back to binary using bin function, exclude the prefix 0b
        return bin(c)[2:]
