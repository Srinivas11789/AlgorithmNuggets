class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        
        # Logic 1: Naive iteration - 100 pass 5% faster - O(N)
        # * First fine whether it is increasing or decreasing
        # * Second iterate to check whether they are monotonic
        
        
        # First figure out Monotonic Increasing or Decreasing
        i = 0
        n = len(A)
        
        # Single element array handle
        if n == 1:
            return True
        
        # Logic of same element array
        # all Equal elements bypass
        if len(set(A)) == 1:
            return True
        
        # while elements are equal incremenrt
        while i+1 < len(A) and A[i] == A[i+1]:
            i += 1
        #if i == len(A)-1:
        #    return True

        # monotonic 
        if A[i] <= A[i+1]:
            i += 1
            for i in range(i, n-1):
                if A[i] > A[i+1]:
                    return False
        elif A[i] >= A[i+1]:
            i += 1
            for i in range(i, n-1):
                if A[i] < A[i+1]:
                    return False
        return True
        
        
        # Logic 2: Use inbuilt sorted method to easily achieve this - 100 pass 5 percent faster - assuming sorted function uses merge sort internally n*log(n)
        """
        sorted_array = sorted(A)
        if A == sorted_array or A == sorted_array[::-1]:
            return True
        else:
            return False
        """

# Other Thoughts:
# * dictionary logic?
# * Sorted or any arrangement
# * 2 pointer method
# * Tree Building?
# * Diff logic

