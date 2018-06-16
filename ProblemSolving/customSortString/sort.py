class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        
        # Use a differernt/custom key for the sorted function with reference to the given array S
        # 100 pass
        def keys(char):
            if char in S:
                return S.index(char)
            else:
                # Return anything higher will suggest the sorted function to place at the end - 1000, or len(T) or 26
                return len(T)
        
        return "".join(sorted(T, key=keys))
        
        
        
        """
        # Construct a sorted alp with Only lower case characters then solve
        key = ["a"]
        for i in range(25):
            key.append(chr(ord(key[-1])+1))
        start = key.index(S[0])
        key = key[start:]+key[:start]
          
        return sorted(T,key=key)
        """    
        
        """
        # Logic 1 - Any combination - so add the array S in the same order with others
        result = []
        match = []
        for char in T:
            if char not in S:
                result.append(char)
            else:
                match.append(char)
        
        i = 0
        S = list(S)
        while i < len(S):
            if S[i] not in match:
                del S[i]
            elif match.count(S[i]) > 1:
                S = S[:i]+[S[i]]*(match.count(S[i])-1)+S[i:]
                i += match.count(S[i])-1
            else:
                i += 1
        
        return "".join(result)+"".join(S)
        """
        
        """
        # One Logic of iteration 
        result = []
        for char in T:
            if char in S:
                for char in result:
        
            else:    
                result.append(char) 
        """
