class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        
        # Collections Counter method
        from collections import Counter
        result = ""
        last_temp = ""
        for word in d:
            temp = list((Counter(s) & Counter(word)).elements())
            print temp, result, word
            if len(temp) > len(last_temp):
                last_temp = temp
                result = word
            elif len(temp) == len(last_temp):
                if word < "".join(last_temp):
                    result = word
        
        return result
