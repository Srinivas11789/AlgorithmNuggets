# Build custom DS and implement

class ListNode:
    
    def __init__(self, val):
        self.value = val
        self.next = None
        

class PeekingIterator:

    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        
        self.pointer = None
        self.listDS = None
        self.start = None
        
        while iterator.hasNext():
            i = iterator.next()
            current = ListNode(i)
            if self.listDS == None:
                self.listDS = current
                self.pointer = current
            else:
                self.listDS.next = current
                self.listDS = self.listDS.next  

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        
        if self.start == None:
            return self.pointer.value
        
        if self.pointer.next:
            return self.pointer.next.value
        else:
            return None

    def next(self):
        """
        :rtype: int
        """
        
        if self.start == None:
            self.start = True
            return self.pointer.value
        
        if self.pointer.next:
            self.pointer = self.pointer.next
            return self.pointer.value
        else:
            return None

    def hasNext(self):
        """
        :rtype: bool
        """
        
        if self.start == None:
            return True
        
        if self.pointer.next:
            return True
        else:
            return False
        

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].
