class Solution(object):
    def fixedPoint(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        
        
        # Logic 1: Naive O(N) Iteration of the list - 10.5 % faster
        """
        for i in range(len(A)):
            if A[i] == i:
                return i
        return -1
        """
        
        # Logic 2: Binary Search Iteration - 99% faster
        
        # From the question,
        """
        Remember the order is already sorted,
        * A[i] - i < 0 as we want to find a condition A[i] == i then the element lesser than this index wont apply too
        """
        
        left = 0
        right = len(A)-1
        # Binary search
        while left < right:
            mid = left + (right-left)//2 # mid point
            if A[mid] - mid < 0:
                left = mid+1
            else:
                right = mid
        if A[left] == left:
            return left
        else:
            return -1
            
