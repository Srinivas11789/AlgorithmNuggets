class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        
        if len(s) == len(part) and s == part:
            return ""

        if len(part) > len(s):
            return s

        if part == "":
            return s
        
        if s == "":
            return s

        if len(s) == 1 and s[0] == part[0]:
            return ""

        stack = ""
        i = 0
        while i < len(s):
            if i+len(part) <= len(s) and s[i:i+len(part)] == part:
                s = stack + s[i+len(part):]
                stack = ""
                i = 0
                continue
            stack += s[i]
            i += 1

        return stack

