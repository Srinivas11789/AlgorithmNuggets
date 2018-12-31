class Solution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        
        # Condition 1
        if len(A) < 3:
            return False
        
        # Condition 2
        # We have to go to the highest and then reverse to the lowest from there
        # A[0].<..A[max]..>.A[n]
        
        # 100 pass 64 ms faster
        # 2 pointer logic to meet at the peak
        n = len(A)
        left = 0
        right = n-1
        
        # Climbing mountain from left to obtain the peak
        while left < n-1 and A[left] < A[left+1]:
            left += 1
        
        # Climbing mountain from right to obtain peak 
        while right > 0 and A[right] < A[right-1]:
            right -= 1
        
        # Climbing both sides should have left us at the peak
        # Also peak should not be at the start of the end
        if left == right and left > 0 and left < n-1:
            return True
    
        return False
        
        
        """
        # 100 pass 64 ms faster
        # Break down logic of solving each condition separate
    
        # Find maximum peak
        peak = max(A)
        
        # There should be only one peak
        if A.count(peak) > 1:
            return False
        
        # Index of peak
        peak_index = A.index(peak)
        
        # Peak should not be present in the beginning or the end
        if peak_index == len(A)-1 or peak_index == 0:
            return False
        
        # Iterate upward to peak
        for i in range(0, peak_index):
            if A[i] >= A[i+1]:
                return False
        
        # Iterate downward from peak
        for i in range(peak_index+1, len(A)):
            if i+1 < len(A) and A[i] <= A[i+1]:
                return False
        
        return True
        """
        
        """
        # Not 100 pass
        # Just compare if both sides of the peak are sorted
        # This also fails when both the elements are equal occurring continuously, add check
        
        peak = max(A)
        if A.count(peak) > 1:
            return False
        peak_index = A.index(peak)

        
        if sorted(A[:peak_index+1]) == A[:peak_index+1] and sorted(A[peak_index:]) == A[peak_index:][::-1]:
            return True
        else:
            return False
        """
        
        """
        # Not 100 pass
        # Simple technique - There is should be only one time when the max fall takes place A[i] > A[i+1] else it is not a mountain
        # Con: this runs through the full loop though....
        #      - this also doesnt work when equal numbers exist
        peak = 0
        while A:
            current = A.pop()
            if A and current > A[-1]:
                print A, current
                peak += 1
        if peak != 1:
            return False
        else:
            return True
        """
        
        
        
        
        
