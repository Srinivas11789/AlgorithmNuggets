class Solution(object):
    def largestPalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        high = int("9"*n)
        low = int("1"+"0"*(n-1))

        print low, high
        max_palindrome = -float('inf')
        if n == 1:
            return 9
        for i in range(high, high-100, -1):
            for j in range(high, high-1000, -1):
                value = i*j
                if str(value) == str(value)[::-1] and value > max_palindrome:
                    max_palindrome = value
        return max_palindrome%1337
        
        """
        # BruteForce
        high = int("9"*n)
        low = int("1"+"0"*(n-1))
        print high, low
        i = j = high
        while i >= low:
            while j >= low:
                value = i*j
                if str(value) == str(value)[::-1]:
                    return int(value)%1337
                j -= 1
            i -= 1
        """
        
