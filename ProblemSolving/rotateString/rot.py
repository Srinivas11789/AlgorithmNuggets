class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        
        if len(B) == len(A) and B in A + A:
            return True
        else:
            return False

        
        """
        # Finding the full string brute force
        A = A+A
        if B in A:
            if A[A.index(B)] == B[0] and B[len(B)-1] == A[A.index(B)+len(B)]:
                return True
            else:
                return False
        else:
            return False
            """
        
        """
        # Fails some testcases
        if len(B) == 0 and len(A) == 0:
            return True
        
        try:
            start = B[0]
            index = A.index(start)
        except:
            return False
        
        if A[index:]+A[:index] == B:
            return True
        else:
            return False
        """
        
