# Logic 1: Naive logic with WHILE loop blocking for threads --> 5% Faster 
class BoundedBlockingQueue(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.queue = []
        self.max = capacity
        

    def enqueue(self, element):
        """
        :type element: int
        :rtype: void
        """
        while len(self.queue) == self.max:
            pass
        self.queue = [element] + self.queue

    def dequeue(self):
        """
        :rtype: int
        """
        while len(self.queue) == 0:
            pass
        return self.queue.pop()

    def size(self):
        """
        :rtype: int
        """
        return len(self.queue)
        
