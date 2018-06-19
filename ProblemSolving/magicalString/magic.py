class Solution(object):
    def magicalString(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        # Initial Sequence
        seq = [1,2,2]
        # Count of consecutive will be --> 1, 2, (next count should be 2)*(value should be 1 if 2 else 1) 
        
        count = 2 # The last element visited
        
        while len(seq) < n+1:
            
            # below can also be worked out as 3-s[-1] in one line
            if seq[-1] == 1:
                value = 2
            else:
                value = 1
                
            seq.extend([value]*seq[count])
            
            # Count is always going to be the next element as we progress through the array as each element counts
            count += 1
        
        #print seq
        return seq[:n].count(1)
