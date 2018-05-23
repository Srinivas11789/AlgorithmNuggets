class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        # Memoization? - the modulo is checked against all the numbers from 2-> n everytime. Think of a reverse, if we instead multiple all the values within the range and store them in the list or memoize then access times reduce and the multiples that dont occur are prime numbers
        
        # To hold all the multiples we encountered when we traversed, initially set them to zero
        multiples = [0]*n
        
        # To hold the prime number occurences
        count = 0
        
        # Iterate through the range
        for i in range(2,n):
        
            # If the number is already a multiple <check for key in a dictionary>
            if multiples[i] == 0:
                count += 1
                j = 2
                while i*j < n:
                    multiples[i*j] = 1
                    j += 1
                    
        return count        
        
        """
        # Calculating square root to reduce the combination - Again Time Limit Exceeded!
        import math
        result = []
        for i in range(2,n):
            j = 1
            count = 0
            while j <= math.sqrt(i):
                if i%j == 0:
                    count += 1
                if count > 1:
                    break
                j += 1
            if count == 1:
                result.append(i)
        print result
        return len(result)
        """
        
        
        """
        # Calculating until half the size of the number
        # All pass - Time limit exceeded
        result = []
        for i in range(n):
            j = 1
            count = 0
            while j <= i//2:
                if i%j == 0:
                    count += 1
                j += 1
            if count == 1:
                result.append(i)
        return len(result)
        """
                    
