class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        
        # Make a dictionary of all the words
        import collections
        result = []
        occurenceDict = collections.Counter(A.split(" ")+B.split(" "))
        for k,v in occurenceDict.items():
            if v == 1:
                result.append(k)
        return result
            
        
