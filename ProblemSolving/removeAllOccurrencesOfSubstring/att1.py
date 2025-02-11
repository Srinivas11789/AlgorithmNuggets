class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        
        result = [s]

        while result:
            s = result.pop(0)
            remaining = ""
            i = 0
            while i < len(s):
                if len(s[i:]) < len(part):
                    remaining += s[i]
                    i += 1
                    continue
                if s[i:i+len(part)] != part:
                    remaining += s[i]
                    i += 1
                    continue
                print(s, remaining, s[i:i+len(part)], i)
                s = remaining + s[i+len(part):]
                remaining = ""
                i = 0
                
            if not result:
                result.append(remaining)
            else:
                result[0].append(remaining)
            
            if s == result[0]:
                return s
        
        return result
