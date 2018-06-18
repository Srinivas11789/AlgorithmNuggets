class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        
        # Using Stack and Iterating
        
        # Handle case of k being greater than the length of the array
        if k >= len(num):
            return "0"
        
        # Control variable declaration
        stack = []
        deleted = 0
        
        # Iteration across the num
        for i in range(len(num)):
            # Clear the stack if the last element inserted is greater than the current element
            while len(stack) > 0 and stack[-1] > num[i] and deleted < k:
                deleted += 1
                stack.pop()
            stack.append(num[i])
            
        # If deleted is not equal to k, delete until k elements have been removed
        while len(stack) > 0 and deleted < k:
            deleted += 1
            stack.pop()
        
        return str(int("".join(stack)))
            
        
        """
        # Works for all the cases -- Time Limit Exceeded
        import itertools
        mini = float('inf')
        nums = list(num)
        repeat = len(nums)-k
        if repeat == 0:
            return "0"
        for comb in itertools.combinations(nums, r=repeat):
            if int("".join(comb)) < mini:
                mini = int("".join(comb))
        return str(mini)
        """
