class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        def expand_window(string, left, right):
            while left >= 0 and right <= len(s)-1 and string[left] == string[right]:
                left -= 1
                right += 1
            return string[left+1:right]
        
        maxi = ""
        for i in range(len(s)):
            odd_palindrome = expand_window(s, i, i)
            if len(maxi) < len(odd_palindrome):
                maxi = odd_palindrome
            even_palindrome = expand_window(s, i, i+1)
            if len(maxi) < len(even_palindrome):
                maxi = even_palindrome
        return maxi
