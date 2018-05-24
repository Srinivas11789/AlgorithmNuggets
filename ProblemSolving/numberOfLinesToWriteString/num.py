# 100 pass
class Solution(object):
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        
        # Alphabet maximum 
        ascii = 97
        
        # Iterate through the string for each character
        total = 0
        lines = 0
        last = 0
        i = 0
        while i < len(S):
                # Ord(a) is 97 - hence to obtain the indices of the array width from a-z --> subtract from 97 
                char_value = widths[abs(ascii-ord(S[i]))]
                total = total + char_value
                if total > 100:
                    total = 0
                    lines += 1
                elif i == len(S) - 1:
                    lines += 1
                    last = total
                    i += 1
                else:
                    i += 1
        return [lines, last]

        
                
        
