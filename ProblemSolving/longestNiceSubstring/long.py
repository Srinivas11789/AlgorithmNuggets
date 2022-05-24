class Solution(object):
    def longestNiceSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        def getNiceSubStr(substr):
            nice = {}
            for s in substr:
                if s not in nice:
                    nice[s] = 0
                nice[s] += 1
            return nice
                
        def isNice(substr):
            for k,v in substr.items():
                if k.islower() and k.upper() in substr:
                    continue
                elif k.isupper() and k.lower() in substr:
                    continue
                else:
                    return False
            return True
        
        # Logic 1: Sliding window
        for i in range(len(s), -1, -1):
            for j in range(len(s)):
                if i+j > len(s):
                    continue
                window = getNiceSubStr(s[j:j+i])
                #print(s[j:j+i], isNice(window))
                if isNice(window):
                    return s[j:j+i]

        return ""
   
        
