class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        
        if not A and not B:
            return True
        
        for i in range(len(A)):
            if A[i:]+A[:i] == B:
                return True
        return False
