class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        # Logic 1: Simple Iterative by swapping - 100 pass 90% faster
        """
        # Declare first three values
        T0 = 0
        T1 = 1
        T2 = 1
        
        # Iterate to find nth value and swap
        for i in range(3,n+1):
            Tn = T0 + T1 + T2
            T0 = T1
            T1 = T2
            T2 = Tn
            
        # Condition when n < 3
        if n == 0:
            Tn = T0
        elif n == 1:
            Tn = T1
        elif n == 2:
            Tn = T2
            
        return Tn
        """
    
        # Logic 2: Iterate using O(N) space - 70 percent faster
        
        """
        # Init array with initial values
        series = [0, 1, 1]
        
        # Iterate and extend series in the array
        for i in range(3, n+1):
            series.append(series[-1]+series[-2]+series[-3])
            
        return series[n]
        """
    
        # Logic 3: Recursive - Time limit exceeded obviously and it takes forever.
        """
        def recurse_series(n):
            # Return first few initial values 0, 1, 2
            if n == 0:
                return 0
            elif n == 1:
                return 1
            elif n == 2:
                return 1
            else:
                # Calculate and return other values
                return recurse_series(n-1) + recurse_series(n-2) + recurse_series(n-3)
        
        return recurse_series(n)
        """
        
        # Logic 4: Recursive with Memoization

        # Memo array with initial values
        memo = [0, 1, 1]
        def recurse_series(n):
            # Return memoized values
            if n < len(memo):
                return memo[n]
            else:
                # Calculate and return other values
                next_value = recurse_series(n-1) + recurse_series(n-2) + recurse_series(n-3)
                memo.append(next_value)
                return next_value
        
        return recurse_series(n)
