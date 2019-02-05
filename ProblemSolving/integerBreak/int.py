class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        # Hard code minumum value that would be a constant
        if n == 2:
            return 1
        
        # Memoization to maintain a record of max across numbers
        memo = [1]*(n+1)
        
        # Iterate to n+1 so n is calculated for sure
        for i in range(2, n+1):
            # Calculate the different from 1 to i
            for j in range(1, i):
                # Compare already existing value vs new difference
                calc_max = max(j*memo[i-j], j*(i-j))
                # Store the max difference
                memo[i] = max(memo[i], calc_max)
        return memo[n]

    
        """
        # Logic: Brute force
        # * Tried recursive strategy, stuck at places....pending on my own logic.
        # * subtract iteratively (as long as atleast 2 + are present) until 0 and record the maximum product
        self.memo = [1,1]
        
        def maxProd(k, current_max):
            print self.memo
            if k == 1:
                return 1
            elif k < len(self.memo):
                return self.memo[k]
            else:
                for i in range(1,k//2+1):
                    delta = k - i
                    product = i * maxProd(delta, 0) 
                    if product > current_max:
                        self.memo.append(product)
                return product
        
        maxProd(n,0)
        return self.memo[n] 
        """
