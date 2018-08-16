class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        count = 0
        
        # N+1 Logic
        while n != 1:
            if n%2 == 0:
                n = n//2
            elif n-1 == 2 or ((n-1)/2)%2 == 0:
                n -= 1
            elif ((n+1)/2)%2 == 0:
                n += 1
            count += 1
        return count
