class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        # Logic without using min
        self.min = float('inf')

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if x < self.min:
            self.min = x
        

    def pop(self):
        """
        :rtype: void
        """
        n = len(self.stack)
        element = self.stack[n-1]
        if element == self.min:
            del self.stack[n-1]
            self.min = float('inf')
            for item in self.stack:
                if item < self.min:
                    self.min = item
        else:
            del self.stack[n-1]
        return element

    def top(self):
        """
        :rtype: int
        """
        n = len(self.stack)
        element = self.stack[n-1]
        return element
        

    def getMin(self):
        """
        :rtype: int
        """
        #return min(self.stack)
        return self.min
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
