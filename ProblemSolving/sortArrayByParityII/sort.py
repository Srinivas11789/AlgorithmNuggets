class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        
        # O(N) complex and O(1) space
        # Using defined indexed within the array
        
        # First odd and even indexes
        even = 0
        odd = 1
        
        # Size of the array
        n = len(A)
        
        # contain the array to not exceed the limit
        while even < n and odd < n:
            # Donot track for both even and odd, tracking anyone either even or odd is enough here as the mismatch is mutual
            if A[even] % 2 != 0:
                A[even], A[odd] = A[odd], A[even]
                odd += 2
            else:
                # Iterate even to jump subsequent even as we traverse when A[even] == Even
                even += 2
        return A
            
        
        
        # Custom O(N), tried for O(1) space - setting the pointer to None doesnt work alter logic and using None in this logic makes it complex and doesnt help
        """
        n = len(A)
        even_mismatch = None
        odd_mismatch = None
        for i in range(n):
            if A[i] % 2 == 0 and i % 2 != 0:
                even_mismatch = i
            elif A[i] % 2 != 0 and i % 2 == 0:
                odd_mismatch = i
            if even_mismatch is not None and odd_mismatch is not None:
                A[even_mismatch], A[odd_mismatch] = A[odd_mismatch], A[even_mismatch]
                even_mismatch = None
                odd_mismatch = None
            print even_mismatch, odd_mismatch
        if even_mismatch is not None and odd_mismatch is not None:
                A[even_mismatch], A[odd_mismatch] = A[odd_mismatch], A[even_mismatch]
                even_mismatch = None
                odd_mismatch = None
        if even_mismatch is not None or odd_mismatch is not None:
            A[i], A[i-1] = A[i-1], A[i]
        return A
        """
                
        
