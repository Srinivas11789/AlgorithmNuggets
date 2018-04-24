class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        freq = {}
        for char in set(s):
            count = s.count(char)
            if count not in freq:
                freq[count] = []
            freq[count].append(char)
        result = []
        for count in sorted(freq.keys()):
            for char in freq[count]:
                result.append(char*count)
        return "".join(result[::-1])
    
            
            
        
