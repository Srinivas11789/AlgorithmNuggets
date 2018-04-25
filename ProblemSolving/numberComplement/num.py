class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        
        
        # 100 pass - Int (number) ==> Binary representation ==> flip bits ==> to Int again!!
        binary = bin(num)[2:]
        result = []
        for bit in binary:
            if bit == "1":
                result.append("0")
            else:
                result.append("1")
        return int("".join(result),2)
        
        
