class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        """
        # Snap - can reversing the string and comparing work??
        if s == s[::-1]:
            return True
        else:
            return False
        """
        
        # Logic similar to the one in the discussion
        
        # Handling empty condition
        if not s:
            return False
            
        # String doubling and eliminating the first and the last character which would be the first and last character of a substring in a full string with substrings. 
        double = (s + s)[1:-1]
        
        # Debug
        #print double
        #print double.find(s)
        
        # Checking if the full string exists after doubling the string and removing first and last character proves if the full string is made of substrings
        return double.find(s) != -1
        
        
        
        """
        # 1 - Find the next start of the string and check if sub string exists
        start = s[0]
        n = len(s)
        sequence_end = s[n-1]
        if len(s) > 1:
            try:
                nxt = s[1:].index(sequence_end)
            except:
                return False
            size = nxt + 1
            print size, s[(n-size):], s[:size]
            if s[(n-size):] == s[:size]:
                return True
            else:
                return False
        else:
            return False
           """ 
        
        """
        # 2 - Iterating from substrings of 1 - n --> find existence of each in the string existence*char == length -- solution looks promising
        # Time limit exceeded with this logic
        n = len(s)
        for i in range(1,n//2+1):
            if s.count(s[:i])*i == n:
                return True
        return False
        """
        
        """
        # Fails some testcases - find multiple copies of substring that can be made again as the string
        for i in range(len(s)):
            if s[:i+2] in s[i+2:]:
                return True
        return False
        """
