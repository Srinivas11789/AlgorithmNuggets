class Solution:
    def freqAlphabets(self, s: str) -> str:
        # Logic 1: O(N) --> one reverse pass to covert to char with ascii value
        # * We need to to find if the integer falls in which half
        # * Easy way to achieve this would be to iterate string chars in reverse to know single digit vs double digit alphabets to expect
        
        decode = ""
        i = len(s)-1
        asciiStart = 96
        while i >= 0:
            if s[i] == "#":
                decode = chr(int(s[i-2:i])+asciiStart) + decode # add to front as we reverse iterate
                i -= 3
            else:
                decode = chr(int(s[i])+asciiStart) + decode
                i -= 1
        return decode
