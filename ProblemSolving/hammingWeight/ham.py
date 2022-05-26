class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        # Logic 1: convert to binary and operate
        #return bin(n).count("1")
        import collections
        b = list(bin(n))
        counts = collections.Counter(b)
        return counts["1"]
        
        # Logic 2: Binary and removes the last signficant one for AND operation. 010 --> 011 --> 100
        ones = 0
        while n:
            n = n & (n-1)
            ones += 1
        return ones
