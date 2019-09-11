class Solution(object):
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        
        # Logic 1: 93 % faster
        # * Problem here is we have to
        #   - Iterate the array A 
        #   - Iterate the index 
        # * Logic with 2 for loops or one with dictionary to store all index elements would help but will be long logic
        # * Thinking to iterate all the strings within one loop 
        #   - Used unpack (*) of list to unpack the list to strings
        #   - Zip to iterate all the arguments by index together in one for loop 
        count = 0
        
        for i in zip(*A):
            if list(i) != sorted(i):
                count += 1
        
        return count

