# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution(object):
    def depthSum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        
        # Logic 1: Iterative and expand the lists by each level until exhaustion
        """
        total = 0
        level = 1
        while nestedList:
            i = 0
            while i < len(nestedList):
                if not nestedList[i].isInteger():
                    temp = nestedList[i].getList()
                    nestedList = nestedList[:i] + temp + nestedList[i+1:]
                    i += len(temp)
                else:
                    total += level*(nestedList[i].getInteger())
                    nestedList.pop(i)
                #print(nestedList)
            level += 1
            #print(total)
        return total
        """

        # Logic 2: Recursive Logic - 86 % faster
        def recurse_nested_list(array, level):
            while array:
                current = array.pop(0)
                if current.isInteger():
                    self.sum += current.getInteger()*level
                else:
                    recurse_nested_list(current.getList(), level+1)
                #print(self.sum, level)
        self.sum = 0
        recurse_nested_list(nestedList, 1)
        return self.sum
        
        
        """
        # Other logics that dont work...
        
        # same logic - The comment was misleading claiming not to speculate the interface code. So the below logic assumes naive list of list with integers.
        
        total = 0
        while nestedList:
            i = 0
            while i < len(nestedList):
                if isinstance(nestedList[i], (list)):
                    nestedList = nestedList[:i] + nestedList[i] + nestedList[i+1:]
                    i += len(nestedList[i])
                else:
                    total += level*nestedList[i]
                    nestedList.pop(i)
            level += 1
        return total
        """
        
            
