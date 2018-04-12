class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        
        numeral = 0
        for i in range(len(s)):
            if i+1<len(s) and roman[s[i]] < roman[s[i+1]]:
                    numeral -= roman[s[i]]
            else:
                    numeral += roman[s[i]]
            #print s[i], numeral
        
        return numeral
            
            
        
