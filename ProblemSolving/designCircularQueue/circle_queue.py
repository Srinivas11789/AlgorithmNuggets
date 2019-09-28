class MyCircularQueue(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        """
        
        # Let us take a queue to be a list
        # Construct queue
        self.queue = [] # we dont want to initialize 0 for i in range(k)
        self.size = k
        

    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if not self.isFull():
            self.queue.append(value)
            return True
        else:
            return False
        

    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        :rtype: bool
        """
        if self.isEmpty():
            return False
        else:
            self.queue.pop(0)
            return True
        

    def Front(self):
        """
        Get the front item from the queue.
        :rtype: int
        """
        if not self.queue:
            return -1
        else:
            return self.queue[0]
        

    def Rear(self):
        """
        Get the last item from the queue.
        :rtype: int
        """
        if not self.queue:
            return -1
        else:
            return self.queue[-1]
        

    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        :rtype: bool
        """
        if self.queue != []:
            return False
        else:
            return True

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """
        if len(self.queue) == self.size:
            return True
        else:
            return False
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
