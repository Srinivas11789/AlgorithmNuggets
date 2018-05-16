# Pendig....
class Solution(object):
    def maxRotateFunction(self, A):

        :type A: List[int]
        :rtype: int
        """
        
        """
        # Time Limit Exceeded
        # Rotate Array
        def rotate(A):
            n = len(A)
            if n == 1:
                return [A[0]]
            else:
                return [A[n-1]]+A[:n-1]
        
        # Result Calculation
        def result_calc(A):
            n = len(A)
            ans = 0
            for i in range(n):
                ans += i*A[i]
            return ans
        
        # Maximum value tracking
        maxi = -60000000000000
        n = len(A)
        if n == 0:
            return 0
        for i in range(n):
            A = rotate(A)
            value = result_calc(A)
            if value > maxi:
                maxi = value
        return maxi
        """
            
        
