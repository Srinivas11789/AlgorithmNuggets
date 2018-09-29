class MyCircularDeque(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        :type k: int
        """
        self.queue = []
        self.limit = k
        

    def insertFront(self, value):
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if len(self.queue) < self.limit:
            self.queue = [value]+self.queue
            return True
        return False

    def insertLast(self, value):
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if len(self.queue) < self.limit:
            self.queue = self.queue + [value]
            return True
        return False
        

    def deleteFront(self):
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if len(self.queue) > 0:
            self.queue = self.queue[1:]
            return True
        return False
        

    def deleteLast(self):
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if len(self.queue) > 0:
            self.queue = self.queue[:-1]
            return True
        return False
        

    def getFront(self):
        """
        Get the front item from the deque.
        :rtype: int
        """
        try:
            return self.queue[0]
        except:
            return -1
        
        

    def getRear(self):
        """
        Get the last item from the deque.
        :rtype: int
        """
        try:
            return self.queue[-1]
        except:
            return -1

    def isEmpty(self):
        """
        Checks whether the circular deque is empty or not.
        :rtype: bool
        """
        if len(self.queue) > 0:
            return False
        else:
            return True
        

    def isFull(self):
        """
        Checks whether the circular deque is full or not.
        :rtype: bool
        """
        if len(self.queue) == self.limit:
            return True
        else:
            return False
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
