class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        # Logic 2:
        memo = [0]*n
        count = 0
        if n > 2:
            count += 1
        for i in range(3, n, 2):
            if memo[i] == 0:
                count += 1
                j = 3
                while i*j < n:
                    memo[i*j] = 1
                    j += 1
        return count
    
        # Logic 1:
        """
        def is_prime(a):
                import math
                for i in range(3, int(math.sqrt(a))+1, 2):
                    if a%i == 0:
                        return False
                return True
        
        count = 0
        if n <= 2:
            return 0
        elif n < 3:
            return 1
        count = 1
        for i in range(3, n, 2):
            if is_prime(i):
                count += 1
        return count
        """
