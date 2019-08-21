class Solution(object):
    def largestSumAfterKNegations(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        
        # Logic 1 - 70% faster
        # We need to maximize the sum 
        # * This means for any minimum number we can convert it to negative
        # * This also means for any maximum number we can convert it to positive (by negation)
        # Also, these
        # * For even number of times of negation in all positive integer array - do not negate
        
        A.sort()
        i = 0
        left = 0
        right = len(A)
        while left < right:
            if A[left] < 0:
                A[left] = -(A[left])
                i += 1
            if i == K:
                break
            left += 1
        sumi = sum(A)
        #print(sumi, i, A)
        if i < K and (K-i)%2 != 0:
            sumi -= min(A)*2
        return sumi
            
                    
        
        
        
        
