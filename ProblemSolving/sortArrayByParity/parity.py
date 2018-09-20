"""
New Leetcode UI: <results below>
Runtime: 60 ms, faster than 96.24% of Python online submissions for Sort Array By Parity.
"""

class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        
        # O(N) time and space logic
        n = len(A)
        odd_loc = None
        for i in range(n):
            if A[i] % 2 == 0:
                # Even condition, swap with the previous odd instance
                if odd_loc is not None:
                    A[i], A[odd_loc] = A[odd_loc], A[i]
                    # Update the odd location to next
                    # By this time of the logic the odd instances are next items
                    odd_loc += 1
            else:
                # Odd condition, record first odd instance
                if odd_loc is None:
                    odd_loc = i
        return A
        
