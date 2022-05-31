class Solution(object):
    def hasAllCodes(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        
        # Logic 1: compute total combinations of k binary codes, check if number of visited substrings match the total computed before (assuming substring is contiguous)
        
        total_sizek_codes = 2**k
        
        substrings = {}
        
        for i in range(len(s)):
            end = i+k
            if end > len(s):
                continue
            subs = s[i:end]
            if subs not in substrings:
                substrings[subs] = 0
            substrings[subs] += 1
            
        #print(substrings)
        
        if len(substrings) == total_sizek_codes:
            return True
        
        return False
