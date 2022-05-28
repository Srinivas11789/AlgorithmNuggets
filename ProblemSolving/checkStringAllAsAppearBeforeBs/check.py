class Solution(object):
    def checkString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        # Logic 1: O(N) iteration with a flag variable - 95% faster
        end_b = False
        
        for i in range(len(s)-1, -1, -1):
            
            if s[i] == "a":
                end_b = True
            if s[i] == "b" and end_b:
                return False

        return True
        
        # Logic 2: O(N) iteration to find wrong order
        """
        for i in range(len(s)-1):
            if s[i]+s[i+1] == "ba":
                return False
        return True
        """

