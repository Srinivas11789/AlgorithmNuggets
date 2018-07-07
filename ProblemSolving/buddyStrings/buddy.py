class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        
        if A == B:
            if len(set(A)) == 1:
                return True
            else:
                import collections
                c = collections.Counter(A)
                count = 0
                for k,v in c.items():
                    if v > 1:
                        count += 1
                if count >= 2: 
                    return True
                else:
                    return False
        elif A == "" or B == "":
            return False
        elif len(A) != len(B):
            return False
        else:
            n = len(A)
            A = list(A)
            B = list(B)
            first = None
            second = None
            for i in range(n):
                if A[i] != B[i]:
                    if first == None:
                        first = i
                    else:
                        second = i
            A[first],A[second] = A[second],A[first]
            if A == B:
                return True
            else:
                return False
                    
        
