# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.nested = nestedList
        self.flatten = []
    
    def flattener(self):
        curr_nested = self.nested.pop(0)
        
        if curr_nested.isInteger():
            self.flatten.append(curr_nested.getInteger())
            return 
            
        if curr_nested.getList():
            self.nested = curr_nested.getList() + self.nested
            return self.flattener()
    
    def next(self) -> int:
        #print("ss", self.flatten)
        return self.flatten.pop(0)
        
    def hasNext(self) -> bool:
        #print(self.nested, self.nested == True)
        while self.nested:
            self.flattener()
        if self.nested or self.flatten:
            return True
        return False
            

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
