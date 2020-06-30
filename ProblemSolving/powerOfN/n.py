# Logic 1: Recurse by reducing one by one --> Leads to recursion depth reached as it reduced by one
"""
class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Tail recursion
        print(x, n)
        
        # Calculator power recursively ( handle negative power )
        if n < -1: 
            return self.myPow(x, n+1)*1/x
        elif n > 1:
            return self.myPow(x, n-1)*x
        
        # Condition to return when n == 1
        if n < 0:
            return 1/x
        elif n > 0:
            return x
        else:
            return 1
"""

# Logic 2: Use different technique to speed up and reduce number of recursion
class Solution:
    def fastPow(self, x: float, n:int) -> float:
        # Return 1 when n is 0
        if n == 0:
            return 1
        # Recurse
        half = self.fastPow(x, n//2)
        # Handle even odd nums
        if n%2 == 0:
            return half*half
        else:
            return half*half*x
        
    def myPow(self, x: float, n: int) -> float:
        # Handle negative power case
        if n < 0:
            x = 1/x
            n = -n
        # Recurse
        return self.fastPow(x, n)
