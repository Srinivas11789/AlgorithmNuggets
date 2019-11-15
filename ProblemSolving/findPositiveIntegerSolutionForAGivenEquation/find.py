"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""
class Solution(object):
    def findSolution(self, customfunction, z):
        """
        :type num: int
        :type z: int
        :rtype: List[List[int]]
        """
        
        i = 1
        j = 1
        result = []
        while customfunction.f(i,j) <= z:
            while customfunction.f(i,j) <= z:
                if customfunction.f(i,j) == z:
                    result.append([i, j])
                j += 1
            j = 1
            i += 1
        return result
            
        
        
        
