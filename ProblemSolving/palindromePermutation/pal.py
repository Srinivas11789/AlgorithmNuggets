class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        # Logic 1: Using the COUNTER test
        # * Even length string: palindrome exists only when all the char are divisible by 2
        # * Odd length string: palindrome exists only when there is one odd and other even chars
        import collections
        c = collections.Counter(s)
        n = len(s)
        even = 0
        odd = 0
        for a in c.keys():
            if c[a]%2 == 0:
                even += 1
            else:
                odd += 1
        if n%2 == 0 and odd == 0 and even >= 0:
            return True
        elif n%2 != 0 and odd == 1 and even >= 0:
            return True
        else:
            return False
