class Solution:
    def clearDigits(self, s: str) -> str:
        
        result = ""
        for i in s:
            if i.isdigit() and result:
                result = result[:-1]
            else:
                result += i
        return result
