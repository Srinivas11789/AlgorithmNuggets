class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        # dont forget to strip as the case "a " with whitespace at end might cause problems. To remove white space at the end use strip 
        given = s.strip().split(" ")
        n = len(given)
        
        if n >= 1:
            return len(given[n-1])
        else:
            return 0
        
