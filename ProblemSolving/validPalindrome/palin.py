# 100 pass
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        # Ignore cases - convert everything to lower case
        s = s.lower()
        
        # Strip all the special characters - Allow only alphanumeric
        s = "".join([i for i in s if (ord(i) > 96 and ord(i) < 123) or (ord(i) > 47 and ord(i) < 58)])
        
        # Check palindrome
        if s == s[::-1]:
            return True
        else:
            return False
        
        

        
