class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        
        # Classic Method using variables - 100 pass
        """
        f0 = 0
        f1 = 1
        fnext = f0+f1
        if N >= 2:
            for i in range(2, N+1):
                fnext = f0 + f1
                f0 = f1
                f1 = fnext
        if N == 0:
            return f0
        elif N == 1:
            return f1
        else:
            return fnext
        """
        
        # List Method - 100 pass
        """
        fiboN = [0,1]
        i = 2
        while i < N+1:
            fiboN.append(fiboN[i-1]+fiboN[i-2])
            i += 1
        return fiboN[N]
        """
        
        # Recursion Only Method - Slow - 100 pass
        """
        def fiboRecurse(N):
            if N == 0:
                return 0
            elif N == 1:
                return 1
            else:
                return fiboRecurse(N-1)+fiboRecurse(N-2)
        return fiboRecurse(N)
        """
    
        # Memoization + Recursion - Faster 100 pass
        memo = [0, 1]
        def fiboRecurseMemo(N):
            if N < len(memo):
                return memo[N]
            else:
                memo.append(fiboRecurseMemo(N-1)+fiboRecurseMemo(N-2))
                return memo[-1]
        return fiboRecurseMemo(N)
        
        
        
            
        
