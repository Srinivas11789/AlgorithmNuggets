class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        
        
        # Logic 1: 100 pass
        #return map(lambda x:x**2, sorted(A, key= lambda x: x**2))
        
        # Logic 2: 100 pass
        #return sorted(map(lambda x: x**2, A))
        
        # Logic 3 - Time limit exceeded
        # Naive iterative without built in functions
        """
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
        """
        
        # Logic 4 - 100 pass
        # 2 pointer technique
        
        left = 0
        right = len(A)-1
        i = len(A)-1
        result = [0]*len(A)
        while i >= 0:
            if abs(A[left]) > abs(A[right]):
                result[i] = A[left]**2
                left += 1
            else:
                result[i] = A[right]**2
                right -= 1 
            i -= 1
        return result
