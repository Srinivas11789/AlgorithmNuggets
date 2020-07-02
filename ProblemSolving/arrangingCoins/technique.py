class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        # Logic 1: Construct formula and solve the equation until <= satisfied
        # * the stairs are added with respect to kth step 1, 2, 3 which is basically sum of all steps == n
        # * sum of n natural nums --> k(k+1)//2 = n --> k**2 + k = 2n
        
        N = 2*n
        result = 0
        for i in range(1, n+1):
            sumOfK = i**2 + i
            if sumOfK > N:
                return result
            result = i
        return result
