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
        m = len(popped)
        stack = []
        
        i = 0
        while i < n:
            stack.append(pushed[i])
            while (stack and popped) and (stack[-1] == popped[0]):
                stack.pop()
                popped.pop(0)
            i += 1
            
        if stack:
            return False
        else:
            return True
            
