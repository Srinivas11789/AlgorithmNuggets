class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        
        """
        # Logic 1 - 100 pass
        n = len(A)
        if n >= 3:
            return A.index(max(A))
        """
        
        # Logic 2 - 100 pass
        n = len(A)
        if n >= 3:
            for i in range(n):
                if A[i] > A[i-1] and A[i] > A[i+1]:
                    return i
        
        
