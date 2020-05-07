# Logic 1: Naive logic with iterations --> 20% faster
class CustomStack(object):

    def __init__(self, maxSize):
        """
        :type maxSize: int
        """
        
        self.stack = []
        self.max = maxSize

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if self.max == len(self.stack):
            return
        self.stack = [x] + self.stack
        

    def pop(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack.pop(0)
        return -1
        

    def increment(self, k, val):
        """
        :type k: int
        :type val: int
        :rtype: None
        """
        n = len(self.stack)-1
        i = 0
        while k and i <= n:
            self.stack[n-i] += val
            k -= 1
            i += 1

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
