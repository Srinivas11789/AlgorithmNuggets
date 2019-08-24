class Node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


class MyCalendar(object):

    # Logic 1: expand ranges and use set property - Time limit exceeded
    """
    def __init__(self):
        
        # Data structure to store all the events
        
        # Logic 1
        # List with all the ranges in the expanded form
        self.events = []

    def book(self, start, end):
        
        # Overlapping intervals using SET()
        if set(self.events).intersection(range(start, end)):
            return False
        else:
            self.events.extend(range(start,end))
            return True
    """ 
        
    # Logic 2: range as tuples on a list and iterate o(N) - 100 pass 5% gaster
    
    def __init__(self):

        # Data structure to store all the events

        # Literally store all the range in list as tuples
        self.events = []
    def book(self, start, end):

        # Iterate O(N) over all the ranges
        for intervals in self.events:
            s = intervals[0]
            e = intervals[1]
            # Start, End within the intervals - directly overlapping sets
            if (s <= start <= e-1) or (s <= (end-1) <= e-1):
                #print(intervals, start, end)
                return False
            elif (start <= s <= end-1) or (start <= (e-1) <= end-1):
                # Indirect overlapping sets - wide start and end 
                return False
        self.events.append((start,end))
        self.events.sort()
        return True
    
    """    
    # Logic 3: use better datastructure and sort the ranges in order for better search
    
    
    # Dictionary with schema <start>, <end> to look up faster than list lookup
    #self.events = {}
    # Or use a bst
    
    #def __init__(self):
    #    self.root = Node(0)
    
    #def book(self, start, end):
    """
        
    
    
        

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
