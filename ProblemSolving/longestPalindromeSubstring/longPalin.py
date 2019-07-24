class Solution(object):
    def longestPalindrome(self, s):
            """
            :type s: str
            :rtype: str
            """
            
            # Logic 1: 2 pointer method - Moving from right towards the left or vice versa - Failure
            # * Solves some testcases but not everything
            """
            left = 0
            right = len(s)
            if right == 0:
                return ""
            elif len(set(s)) == 1:
                return s
            elif right <= 2:
                return s[0]
            while right > 0:
                left = 0
                while (right-left) > 1:
                    #print(s[left:right])
                    if s[left:right] == s[left:right][::-1]:
                        return s[left:right]
                    left += 1
                right -= 1
            return ""
            """
            
            # Logic 2: 100 pass 87% - Same 2 pointer expanding from an index outward. Gist obtained from the logic at https://leetcode.com/problems/longest-palindromic-substring/discuss/2954/Python-easy-to-understand-solution-with-comments-(from-middle-to-two-ends).
            # * Start from the middle and expand for every index
            # * Iterate O(N) and at every current index expand for a longest palindrome match
            
            def expand_window(string, left, right):
                # Boundary of palindrome is when the characters at the end are equal
                # left equal to 0 while right should be lesser than length of string always
                while left >= 0 and right < len(string) and string[left] == string[right]:
                    left -= 1
                    right += 1
                return string[left+1:right]
            
            # Palindrome can be 2 types
            # * Odd length palindrome has a center character different like abcba
            # * Even length palindrome is symmetric abba
            result= ""
            for i in range(len(s)):
                # Odd length palindrome - expand from the same index
                palindrome_substring = expand_window(s, i, i)
                if len(palindrome_substring) > len(result):
                    result = palindrome_substring
                # Even length palindrome - expand from next index so we can find the equal internal elem
                palindrome_substring = expand_window(s, i, i+1)
                if len(palindrome_substring) > len(result):
                    result = palindrome_substring
            return result

        
