class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        # Simple O(N) iteration over the binary representation
        # 100 pass 79
        n_bin = bin(n)[2:]
        for i in range(len(n_bin)-1):
            if n_bin[i] != n_bin[i+1]:
                pass
            else:
                return False
        return True
