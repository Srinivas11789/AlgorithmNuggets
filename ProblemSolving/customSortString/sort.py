# Pending...
# Tc fail - duplicate character occurence

class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
    
        # Logic 1 - Any combination - so add the array S in the same order with others
        result = []
        match = []
        for char in T:
            if char not in S:
                result.append(char)
            else:
                match.append(char)
                
        print match
        
        i = 0
        S = list(S)
        while i < len(S):
            if S[i] not in match:
                del S[i]
            else:
                i += 1
        
        return "".join(result)+"".join(S)
        
        """
        # One Logic of iteration 
        result = []
        for char in T:
            if char in S:
                for char in result:
        
            else:    
                result.append(char) 
        """
