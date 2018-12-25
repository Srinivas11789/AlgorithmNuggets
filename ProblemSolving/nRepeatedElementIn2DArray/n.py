class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        
        # Create record of counts of all letters
        import collections
        letter_count = collections.Counter(A)
        #print letter_count
        
        n = len(A)
        result = n//2
        
        for letter, count in letter_count.items():
            #print count, letter, result
            if count == result:
                return letter
        return None
        
        
