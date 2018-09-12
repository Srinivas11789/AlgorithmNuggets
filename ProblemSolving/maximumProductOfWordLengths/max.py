class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        
        # Dictionary solves with the similar logic below
        dictionary = {}
        for w in words:
            dictionary[w] = set(w)
        
        n = len(words)
        maxi = 0
        
        for i in range(n):
            for j in range(i+1,n):
                if not dictionary[words[i]].intersection(dictionary[words[j]]):
                    maxi = max(maxi, len(words[i])*len(words[j]))
        return maxi 
        
        
        """
        # Naive method - Time limit exceeded
        def commonCheck(str1, str2):
            if set(str1).intersection(set(str2)):
                return False
            else:
                return True
            
        
        n = len(words)
        maxi = -6000000
        for i in range(n):
            for j in range(i+1,n):
                if commonCheck(words[i], words[j]):
                    prod = len(words[i])*len(words[j])
                    if prod > maxi:
                        maxi = prod
        if maxi == -6000000:
            maxi = 0
        return maxi
        """
                    
