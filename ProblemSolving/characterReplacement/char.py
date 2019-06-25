class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
        # Logic 1: Pending work.... No magic, just follow the steps in the problem literally.
        

        n = len(s)
        select = None
        result = 0
        i = 0
        while i < n:
            print i, select, result
            if select == None:
                select = i
                tempk = k
                tempi = None
            else:
                if s[i] != s[select]:
                    if tempk <= 0 or i == n-1:
                        if len(s[select:i]) > result:
                            result = len(s[select:i])
                        if i == n-1:
                            result += 1
                        select = None
                        if tempi > 0:
                            i = tempi-1
                    else:
                        if tempi == None:
                            tempi = i
                        tempk -= 1
            i += 1
        return result
    
        
        # Logic 2: 100 pass
        # * Reference: https://leetcode.com/problems/longest-repeating-character-replacement/discuss/91272/consise-python-sliding-window
        # * Using formal sliding window technique from the above thread
        
        # Array/List logic 
        # Initialize a alphabet space to use
        counts = [0]*26
        
        start = max_count = max_length = 0
        
        # Iterate end to move the window
        for end in range(len(s)):
            index = ord(s[end])-ord('A')
            # Increase count for the character
            counts[index] += 1
            # Set max_count as we proceed
            max_count = max(max_count, counts[index])
            # Move window
            while end - start + 1 - max_count > k:
                counts[ord(s[start])-ord('A')] -= 1
                start += 1
            max_length = max(max_length, end-start+1)
        return max_length
    
        # Dictionary logic: Replace array/list with dictionary for the above logic
                
            
            
        
