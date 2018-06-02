class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        if s.count("A") > 1:
            return  False
        
        count = 1
        for i in range(len(s)-1):
            if s[i] == "L" and s[i] == s[i+1]:
                count += 1
            else:
                count = 1
            if count > 2:
                return False
            
        return True
        
