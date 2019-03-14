class Solution(object):
    def clumsy(self, N):
        """
        :type N: int
        :rtype: int
        """
        
        # Logic 1: Using Eval() function to evaluate expression - 100 pass 25% faster
        
        # Operations
        operation = ["*", "/", "+", "-"]
        
        # Initial expression
        expression = str(N)
        
        # Control variables
        op = 0
        i = N-1
        
        # Loop to construct expression
        while i > 0:
            if op > 3:
                op = 0
            expression += operation[op] + str(i)
            op += 1
            i -= 1
        
        # Return evaluated expression
        return eval(expression)
