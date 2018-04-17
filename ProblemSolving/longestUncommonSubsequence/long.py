class Solution(object):
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        
        # Quesiton asked is about longest uncommon subsequence, which could be either the entire string which is the longest all the time. A string is wither exact match of other string else longest uncommon string. Hence checking for this condition should suffice.
        
        n1 = len(a)
        n2 = len(b)
        if n1 > n2:
            maxi = n1
        else:
            maxi = n2
            
        for i in range(maxi):
            if i < n1 and i < n2:
                if a[i] != b[i]:
                    return maxi
            else:
                return maxi
                
        return -1
    
    
        # Use a dictionary to check if count of characters are equal, but it corrupts the arrangement of the characters
        
        """
        # Fails some testcases, think about the optimal condition here
        maxi1 = maxi2 = 0
        subseq = 0
        
        for char in a:
            if subseq > maxi1:
                maxi1 = subseq
            if char not in b:
                subseq += 1
            else:
                subseq = 0
        
        for char in b:
            if subseq > maxi2:
                maxi2 = subseq
            if char not in b:
                subseq += 1
            else:
                subseq = 0
        
        maxi = 0
        if maxi1 > maxi2:
            maxi = maxi1
        else:
            maxi = maxi2
        
        if maxi == 0:
            return -1
        else:
            return maxi
        """        
        
                
        
