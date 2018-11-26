class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        # We use list operation: 
        # * append for push
        # * pop() to remove
        
        n = len(pushed)
        
        # Create a separate stack list to perform push, pop operation
        stack = []
        
        # Simulate stack operations 
        # * start by pushing elements as we iterate
        # * When the last element pushed is equal to the first element in the popped list, remove the element from both the lists
        # * Perform the above step until the lists are empty or the last elements is not equal
        i = 0
        while i < n:
            stack.append(pushed[i])
            while (stack and popped) and (stack[-1] == popped[0]):
                stack.pop()
                popped.pop(0)
            i += 1
            
        # If stack is empty the stack operation is a success
        if stack:
            return False
        else:
            return True
