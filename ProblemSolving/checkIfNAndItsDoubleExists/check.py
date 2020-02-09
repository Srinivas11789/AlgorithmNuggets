class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        
        # Logic 1: Naive Iteration
        for i in range(len(arr)):
            if 2*arr[i] in set(arr[:i]+arr[i+1:]):
                return True
        return False
    
        # Logic 2: Use Dictionary / Set to check existence and then check for all doubles

