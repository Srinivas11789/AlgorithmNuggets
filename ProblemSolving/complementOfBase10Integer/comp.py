class Solution(object):
    def bitwiseComplement(self, N):
        """
        :type N: int
        :rtype: int
        """
        
        # Logic1: With String Replacement (Hacky String Trick)
        # --> 28ms (100%) faster and 100% less memory
        binary = bin(N)[2:]
        binary = binary.replace("0", "Z")
        binary = binary.replace("1", "0")
        binary = binary.replace("Z", "1")
        return int(binary, 2)
        
        # Logic2: Update pending...
