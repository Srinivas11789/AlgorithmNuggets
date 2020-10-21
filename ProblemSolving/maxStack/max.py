# Logic 1: Naive iteration for popMax otherwise array ops --> 100 pass
class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.max = -float('inf')
        self.max_level = 0

    def push(self, x: int) -> None:
        if x >= self.max:
            self.max = x
            n = len(self.stack)
            self.max_level = -len(self.stack)-1
        self.stack = [x] + self.stack

    def pop(self) -> int:
        popped = self.stack[0]
        if popped == self.max:
            return self.popMax()
        self.stack = self.stack[1:]
        return popped

    def top(self) -> int:
        return self.stack[0]

    def peekMax(self) -> int:
        return self.max

    def popMax(self) -> int:
        n = len(self.stack)
        m = n+self.max_level
        self.stack = self.stack[:m] + self.stack[m+1:]
        prev_max = self.max
        self.max = -float('inf')
        for i in range(len(self.stack)):
            if self.stack[i] > self.max:
                self.max = self.stack[i]
                self.max_level = -(len(self.stack)-i)
        return prev_max


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
