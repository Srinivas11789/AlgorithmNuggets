# Time Limit Exceeded...
class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
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
        
        #for i in range(3, len(A)+1):
        #    for comb in itertools.combinations(A, r=i):
        for i in range(len(A)):
            for j in range(i+1, len(A)+1):
                if len(A[i:j]) >= 3:
                    if isArithmetic(A[i:j], delta):
                        #print A[i:j]
                        count += 1
        return count
