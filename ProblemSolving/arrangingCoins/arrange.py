class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        """
        # Memory Error - Sum
        count = 0
        total = n
        for i in range(1,n):
            total -= i
            if total < i:
                return count
            else:
                #print i, total
                count += 1
        """     
        
        """
        # Memory Error - Subtract
        total = 0
        count = 0
        for i in range(1,n):
            total += i
            if total > n:
                return count
            else:
                count += 1
        """
        
        """
        # 100 pass - Hacks + Tweaks + A more control While Loop 
        total = 1
        i = 1
        if n == 1:
            return 1
        if n == 0:
            return 0
        while total < n:
            i += 1
            total += i
            if total > n:
                i -= 1
        return i
        """
    
        # 100 pass - Clean logic with less space and complexity
        i = 1
        while n>=i:
            n -= i
            i += 1
        return i-1
        
        
