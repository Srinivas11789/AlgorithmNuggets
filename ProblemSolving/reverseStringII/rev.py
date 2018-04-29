class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        
        n = len(s)
        if n < k:
            return s[::-1]
        elif n > k and n < 2*k:
            return s[:k][::-1]+s[k:]
        else:
            poss = []
            for i in range(0,n,2*k):
                temp = s[i:(i+2*k)]
                temp = temp[:k][::-1]+temp[k:]
                poss.append(temp)
            return "".join(poss)
            
                
