class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        # Logic 1: Sliding window using a dictionary/map - 24% faster
        freqs = {}
        maxi = 0
        i = 0
        
        while i < len(s):
            ch = s[i]
            
            if ch not in freqs:
                freqs[ch] = i
            else:
                dup = freqs[ch]
                for k,v in freqs.items():
                    if v <= dup:
                        del freqs[k]
                freqs[ch] = i
            
            if len(freqs) > maxi:
                maxi = len(freqs)
                
            i += 1
            
        return maxi
