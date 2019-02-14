class Solution(object):
    def addToArrayForm(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """

        # Cracky one line solution - Run @58% and Store @100 faster
        return [int(j) for j in str(eval("".join([str(i) for i in A])+"+"+str(K)))]
    
	"""
        # Pending...
        # Literal Addition - Iterate O(K) 
        # * Always positive number
        # * Only ADD operation
        # * Avoid list of string to integer type conversions...
        
        # Make K iterable
        K = str(K)[::-1]
        carry = 0
        n = len(A)-1
        for i in range(len(K)):
            if i <= n:
                A[n-i] = A[n-i] + int(K[i]) + carry
                if A[n-i] > 9:
                    carry = A[n-i]//10
                    A[n-i] = A[n-i]%10
                else:
                    carry = 0
            else:
                A = [int(K[i])] + A
                
        while n-i >= 0 and carry >= 0:
            i += 1
            if n-i == 0:
                A = [carry] + A
            else:
                carry = A[n-i]//10
                A[n-i] = A[n-i]%10
        return A
        """ 
        
