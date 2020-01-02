class Solution(object):
    def sumOfDigits(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        
        # Logic 1: Using in-built min and sum()/eval() --> 44% faster
        """
        mini = min(A)
        target = eval("+".join((list(str(mini)))))
        print(mini, target)
        if target%2 == 0:
            return 1
        else:
            return 0
        """
        
        # Logic 2: [without in-built] Naive O(N) iterate for minimum + Integer digit addition for sum - 92% faster
        mini = float('inf')
        for i in range(len(A)):
            if A[i] < mini:
                mini = A[i]
        target = 0
        while mini:
            #print(target, mini)
            target += mini%10
            mini = mini//10
        return int(target%2 == 0)
