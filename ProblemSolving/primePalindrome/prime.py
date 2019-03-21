# LT Hard --> Pending...
# Time limit exceeded...
class Solution(object):
    def primePalindrome(self, N):
        """
        :type N: int
        :rtype: int
        """
        
        def isPrime(num):
            import math
            count = 0
            if num == 1:
                return False
            for i in range(3, int(math.ceil(math.sqrt(num)+1)), 2):
                if num%i == 0:
                    count += 1
                if count > 0:
                    return False
            return True
        
        def isPalindrome(num):
            if str(num) == str(num)[::-1]:
                return True
            else:
                return False
        
        while 1:
            if (N > 2 and N%2 != 0) or N <= 2:
                if isPalindrome(N):
                    if isPrime(N):
                        return N
            if N < 2 or N%2 == 0:
                N += 1
            else:
                N += 2
        
        
