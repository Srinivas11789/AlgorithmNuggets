### Pending...

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        
        n = len(word1)
        m = len(word2)
        select1, select2 = 0,0
        if n and m:
            for i in range(n):
                for j in range(n,i,-1):
                    if word1[i:j] in word2:
                        if len(word1[i:j]) > select1:
                            select1 = len(word1[i:j])
                            one = n+m-(2*select1)
            for i in range(m):
                for j in range(m,i,-1):
                    if word2[i:j] in word1:
                        if len(word2[i:j]) > select2:
                            select2 = len(word2[i:j])
                            two = n+m-(2*select2)
            print one, two
            return min(one,two)
        elif n:
            return n
        elif m:
            return m
        return m+n
    
                
        
        
        """
        # Fails as order gets crapped in a dictionary
        import collections
        total = word1+word2
        dic = collections.Counter(total)
        result = 0
        for k,v in dic.items():
            if v == 1:
                result += 1
        return result
        """
        
        """
        word1 = list(word1)
        count = 0
        i = 0
        while i < len(word1):
            if prev+word1[i] not in word2:
                count += 1
                word1[i].pop(i)
            else:
                i += 1
                prev = word1[i]
        """ 
            
        
