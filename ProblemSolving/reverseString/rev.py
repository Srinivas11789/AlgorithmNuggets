class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        # pythonic solution
        #return s[::-1]
    
        # Swap logic
        s = list(s)
        n = len(s)
        i = 0
        j = n-1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        return "".join(s)
        
        """
        # Naive solution
        # time limit exceeded
        result = ""
        n=len(s)
        for i in range(n-1,-1,-1):
            result += s[i]
        return result
        """
        
        # Todo in golang
