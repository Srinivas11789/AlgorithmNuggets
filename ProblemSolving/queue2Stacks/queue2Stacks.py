# A good explanation: https://stackoverflow.com/questions/69192/how-to-implement-a-queue-using-two-stacks

class MyQueue(object):
    def __init__(self):
        self.first = []
        self.second = []
    
    def peek(self):
        n = len(self.second)
        return self.second[n-1]
        
    def pop(self):
        # Logic 1 Fails 2 testcases 6 and 7:
        # * Reduce list lookbacks
        # * Reduce length calculation of list more than a time
        # * Splitting list and modifying them revisits elements and causes delay
        """
        n = len(self.second)
        self.second = self.second[:n-1]
        self.first = self.first[1:]
        """
        del self.second[-1]
        del self.first[0]
        return
        
    def put(self, value):
        self.first.append(value)
        # Using logic 4 and changing the logic of pop works - Tcs 6 and 7 pass Yay!
        self.second = [value] + self.second
        
        # Logic 4 ===> Just add the element to the list - timeout 2 testcases
        """
        self.second = [value] + self.second
        """
        
        # Logic3 ===> Easy method pythonic list reverse - Again causes timeout 2 testcases
        """
        self.second = self.first[::-1]
        """
        
        # Logic2 ===> Causes timeout to 2 testcases
        """
        n = len(self.second)
        if n == 0:
            self.second.append(value)
        else:
            self.second = [value] + self.second
        """ 
        
        # Logic1 ===> Causes timeout to bunch of testcases
        """
        self.second = []
        for i in range(len(self.first)-1,-1,-1):
            self.second.append(self.first[i])
        """
        #print self.first,self.second
            
queue = MyQueue()
t = int(raw_input())
for line in xrange(t):
    values = map(int, raw_input().split())
    
    if values[0] == 1:
        queue.put(values[1])        
    elif values[0] == 2:
        queue.pop()
    else:
        print queue.peek()
        

