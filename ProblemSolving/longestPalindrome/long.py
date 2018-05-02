class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        # Unique characters in string should be removed while repeated characters could be kept
        
        unique = set()
        for char in s:
            if char in unique:
                unique.remove(char)
            else:
                unique.add(char)
        if len(unique) > 0:
            return len(s) - len(unique) + 1 # One is added based on the consideration that there could be one unique element
        else:
            return len(s)
