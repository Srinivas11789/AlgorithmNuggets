class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        s = "".join(s.split(" "))
        left = 0
        right = len(s)-1
        while left < right:
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
            else:
                if s[left].lower() != s[right].lower():
                    print(s, s[left], s[right], left, right)
                    return False
                left += 1
                right -= 1
        return True
        
