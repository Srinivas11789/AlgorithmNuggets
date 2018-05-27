class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        # A 1
        # AA 27
        # AZ 52
        # BA 53
        # AAA 
        
        # reverse the string for calculation
        s = s[::-1]
        
        if len(s) == 1:
            return ord(s)-65+1
        else:
            total = 0
            # 26*(65-ord(s[0]))
            for i in range(len(s)):
                    total += (26**i)*(ord(s[i])-65+1)
            return total
                    
        """
            #first = s[0]
            #fvalue = 26 + ord(first)
            total = 0
            total = 26*(len(s)-1)+(65-ord(s[len(s)-1])+1)
            return total
        """
            

        
