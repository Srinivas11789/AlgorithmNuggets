class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        # Logic 1: O(N) iterate and slice --> 100% faster 
        left = 0
        right = 0
        result = []
        i = 0
        while i < len(s):
            if s and s[i] == "L":
                left += 1
                i += 1
            elif s:
                right += 1
                i += 1
            if left != 0 and left == right:
                result.append(s[:i])
                s = s[i:]
                left = right = 0
                i = 0
        return len(result)
                
                
        # Logic 2: Use a stack --> this would require balance check on the stack every time
        
