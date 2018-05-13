class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.stack.append(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        n = len(self.stack)
        value = self.stack[n-1]
        del self.stack[n-1]
        return value
        

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        n = len(self.stack)
        return self.stack[n-1]
        

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        if self.stack:
            return False
        else:
            return True
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
