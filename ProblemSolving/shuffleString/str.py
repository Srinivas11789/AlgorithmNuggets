# Logic 1: convert indices::char to dictionary and iterate once --> 100 pass 20% faster
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        
        mapIndexToChar = {}
        x = 0
        n = len(indices)
        result = ""
        
        while x < n:
            mapIndexToChar[indices[x]] = s[x]
            x += 1
        
        x = 0
        while x < n:
            #print(x, mapIndexToChar[x])
            result += mapIndexToChar[x]
            x += 1
            
        return result
