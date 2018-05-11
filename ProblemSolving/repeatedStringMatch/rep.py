class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        
        count = 1
        temp = A
        while B not in A:
            count += 1
            A += temp
            if len(A) > 3*len(B) and B not in A:
                return -1
        return count
            
        
        
        
        
