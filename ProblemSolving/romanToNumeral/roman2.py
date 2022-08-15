class Solution:
    def romanToInt(self, s: str) -> int:
        
        integer = 0
        
        roman = {
            "": 0,
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        while s:
            curr = s[0]
            if len(s) > 1 and roman[curr] < roman[s[1]]:
                integer += roman[s[1]]-roman[curr]
                s = s[2:]
            else:
                integer += roman[curr]
                s = s[1:]
            
        return integer
