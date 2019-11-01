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

"""
class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        
        # Naive Rotate and Check
        A = list(A)
        B = list(B)
        if A == B:
            return True
        for i in range(len(A)):
            A.insert(len(A)-1, A.pop(0))
            print(A, B)
            if A == B:
                return True
        return False
"""
