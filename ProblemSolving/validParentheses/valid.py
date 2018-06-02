class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        brac = {"{":"}", "(":")", "[":"]"}
        
        s = list(s)
        
        i = 0
        while i < len(s):
            if s[i] in brac:
                i += 1
            else:
                if s[i-1] in brac and s[i] == brac[s[i-1]]:
                    s.pop(i-1)
                    s.pop(i-1)
                    i = i-1
                else:
                    return False
        if not s:
            return True
        else:
            return False
        
