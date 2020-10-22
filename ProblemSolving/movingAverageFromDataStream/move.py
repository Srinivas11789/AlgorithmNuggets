# Logic 1: Naive queue type method --> 100 pass 21% faster --> O(N)
"""
class MovingAverage:

    def __init__(self, size: int):
        self.sliding_window = []
        self.size = size
        

    def next(self, val: int) -> float:
        # Maintian window size
        n = len(self.sliding_window)
        if len(self.sliding_window) == self.size:
            self.sliding_window = self.sliding_window[1:]
        self.sliding_window.append(val)
        # calculate the average
        return float(sum(self.sliding_window)/len(self.sliding_window)) # This causes it to be O(N)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
"""
   
# Logic 2: Queue with head/tail + window sum tracking - 98% faster ( ref from solutions in lt )
class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.sliding_window = [0]*size
        self.size = size
        
        self.head = 0
        self.window_sum = 0
        self.stream_length = 0
        

    def next(self, val: int) -> float:
        # Update the current window length
        self.stream_length += 1
        
        # Set the tail properly
        tail = (self.head + 1) % self.size
        
        # Calculate the moving window sum
        self.window_sum = self.window_sum - self.sliding_window[tail] + val
        
        # update head and values
        self.head = (self.head + 1) % self.size
        self.sliding_window[self.head] = val
        
        # calculate avg
        return self.window_sum/min(self.stream_length, self.size)
    
# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)


