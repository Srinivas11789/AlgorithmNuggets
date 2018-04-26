class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        
        # The binary watch <look at the example>, for each n, the number of ones in the hours or minutes or hours+minutes is n. Hence for each n, find the number of ones in the all the combinations
        
        result = []
        # hours is 0-11 => 12
        for i in range(12): 
            # minutes is 0-59 => 60
            for j in range(60):
                if (bin(i)+bin(j)).count("1") == num:
                    # construct the time such that two zeros appears after the colon
                    result.append("%d:%02d" % (i,j))
        return result
