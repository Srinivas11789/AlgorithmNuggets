"""
Input: "banana"
Output: "anana"

Input: "million"
Output: "illi"
class Solution: 
    def longestPalindrome(self, s):
      # Fill this in.
        
# Test program
s = "tracecars"
print(str(Solution().longestPalindrome(s)))
# racecar
"""

class Solution:
    def longestPalindrome(self, s):

        # Logic 2: left and right pointer testing all the possible substrings and exiting on the first match
        # * Going worst case by iterating the left for each right index
        left = 0
        right = len(s)
        while right > 0:
            left = 0
            while (right-left) > 1:
                #print(s[left:right])
                if s[left:right] == s[left:right][::-1]:
                    return s[left:right]
                left += 1
            right -= 1
        return ""
        
        # Logic 1: 2 pointer logic - use a left and right pointer to traverse all possible substrings 
        # * maintaining the order of the elements in the array
        # * return on the first substring palindrome hit 
	"""
	left = 0
        right = len(s)+1
        while left < right:
            if s[left:right] == s[left:right][::-1]:
                return s[left:right]
        """
	# Will this logic tackle a[1//2:] and a[:1//2] being a palindrome?    
        
        # Logic 0: Thoughts O(N) logic wont work as the palindrome would not be fixed on any index
   

def main():
    s = Solution()
    question = "banana"
    print( question, s.longestPalindrome(question))
    assert "anana", s.longestPalindrome(question)
    question = "million"
    print( question, s.longestPalindrome(question))
    assert "illi", s.longestPalindrome(question)
    question = "racecar"
    print( question, s.longestPalindrome(question))
    assert "racecar", s.longestPalindrome(question)

main()
