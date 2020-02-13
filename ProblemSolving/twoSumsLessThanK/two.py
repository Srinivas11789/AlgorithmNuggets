class Solution(object):
    def twoSumLessThanK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        
        # Logic 1: Naive Iteration - 27 % faster
        """
        maxi = -1
        for i in range(len(A)):
            for j in range(i+1, len(A)):
                target = A[i] + A[j]
                if target > maxi and target < K:
                    maxi = target
                #print(A[i],A[j], maxi)
        return maxi
        """
        
        # Logic 2: 2 pointer technique - 78 % faster
        # * Yes the truth is to follow i < j and not alter the arragement
        # * But in addition i + j == j + i so it wont matter
        A = sorted(A)
        maxi = -1
        left = 0
        right = len(A)-1
        while left < right:
            target = A[left] + A[right]
            if target < K:
                maxi = max(maxi, target)
                left += 1
            else:
                right -= 1
        return maxi
            
        
        
    
        
        
