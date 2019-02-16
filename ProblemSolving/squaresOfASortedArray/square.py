class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        
        # This works but we want the squares in the result
        #return sorted(A, key= lambda x: x**2)
        
        return sorted(map(lambda x: x**2, A))
