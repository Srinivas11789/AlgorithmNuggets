class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        
        # Clean GIST
        if n == 0:
            return 1
        other_half = 1
        N = abs(n)
        if N%2 != 0:
            other_half *= x
        half_power = self.myPow(x, N//2)
        answer = half_power * half_power * other_half
        if n < 0:
            answer = 1/answer
        return answer
        
        # Logical
        ## THE GIST
        # Like merge sort, reduce by 2 as we calculate
        # If odd change to the nearest even with -1
        """
        self.memo = [1]
        def power(x,n):
            print(x, n)
            if n <= 1:
                return 1
            else:
                half_pow = power(x, n/2.0)
                

        
        # Nearest even power
        odd = False
        if n%2 != 0:
            odd = True
            n -= 1
        # Reduce to half and build from there
        n = n//2
        result = power(x, n)
        if odd:
            result = x*result
        return result
        """
            
        # Iterative - Time Limit Exceeded
        """
        result = 1
        if n < 0:
            x = 1/x
            n = abs(n)
        while n:
            result *= x
            n -= 1
        return result
        """
