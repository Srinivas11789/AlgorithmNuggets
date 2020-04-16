class Solution(object):
    def stringShift(self, s, shift):
        """
        :type s: str
        :type shift: List[List[int]]
        :rtype: str
        """
        
        n = len(s)
        
        for [direc, sft] in shift:
            # shifts that matter
            while sft > n: # because >= n shift would be the same string
                sft = n
            
            if direc == 1:
                for i in range(sft):
                    s = s[-1] + s[:-1]
                    #print(s)
            else:
                for i in range(sft):
                    s = s[1:] + s[0]
                    #print(s)
                        
            print(direc, sft, s)
            
        return s
