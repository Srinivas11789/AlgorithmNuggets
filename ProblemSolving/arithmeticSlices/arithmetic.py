class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        
        # Logic 3: Nice interpolation --> every nth digit after 3 digits adds n more possib
        # * https://leetcode.com/problems/arithmetic-slices/discuss/242396/Python-short-solution-with-explanation
    
        total_sequences = 0
        current_sequences = 0
        
        if len(A) < 3:
            return 0
        
        for i in range(2, len(A)):
            if A[i] - A[i-1] == A[i-1] - A[i-2]:
                current_sequences += 1
                total_sequences += current_sequences
            else:
                current_sequences = 0
        
        return total_sequences
        
        # Logic 2: 2 pointer method
        # * https://leetcode.com/problems/arithmetic-slices/discuss/257940/Two-pointers-O(N)-O(1)-Solution-(No-Math-No-DP)
        """
        n = len(A)
        
        if n < 3:
            return 0
        
        left = 0
        delta = A[1]-A[0]
        count = 0
        
        for right in range(2, len(A)):
            diff = A[right]-A[right-1]
            if diff == delta:
                length = right-left+1
                if length >= 3:
                    count += length-2
            else:
                delta = diff
                left = right - 1
                
        return count
        """
    
        # Logic 1: BruteForce Login: Time Limit Exceeded 
        
        """
        def isArithmetic(array, delta):
            n = len(array)
            for i in range(1, n):
                diff = array[i] - array[i-1]
                if diff != delta:
                    return False
            return True
        
        count = 0

        if len(A) < 3:
            return count
        
        delta = A[1]-A[0]
        
        # Itertools dont work as we want consecutive 
        # import itertools
        #for i in range(3, len(A)+1):
        #    for comb in itertools.combinations(A, r=i):
        
        for i in range(len(A)):
            for j in range(i+1, len(A)+1):
                if len(A[i:j]) >= 3:
                    if isArithmetic(A[i:j], delta):
                        #print A[i:j]
                        count += 1
        return count
        """
