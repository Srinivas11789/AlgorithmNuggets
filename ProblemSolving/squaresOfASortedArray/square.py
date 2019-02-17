class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        
        # This works but we want the squares in the result
        #return sorted(A, key= lambda x: x**2)
        
        # Logic 1: 100 pass
        #return sorted(map(lambda x: x**2, A))
        
        # Logic 2
        # Naive iterative without built in functions
        result = []
        for i in range(len(A)):
            square = A[i]**2
            n = len(result)
            if n == 0:
                result.append(square)
            else:
                j = 0
                while j < n:
                    if result[j] > square:
                        result = result[:j] + [square] + result[j:]
                        break
                    j += 1
                #print j, result, A[i], square
                if j == n and len(result) == n:
                    result.append(square)
        return result
