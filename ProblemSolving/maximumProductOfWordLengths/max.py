# Pending...
class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        
        # Brute Force: Correct Logic - Time Limit Exceeded!
        def intersection(w1,w2):
            for char in w1:
                if char in w2:
                    return False
            return True
        
        n = len(words)
        maxi = 0 # default value
        for i in range(n):
            for j in range(i+1,n):
                if i != j and not set(words[i]).intersection(set(words[j])):#intersection(words[i], words[j]):
                    prod = len(words[i])*len(words[j])
                    maxi = max(prod, maxi)
        return maxi
    
        
                    
