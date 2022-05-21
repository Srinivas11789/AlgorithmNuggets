class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        
        # Logic 1: Naive iteration - 100 & 5% faster
        result = ""
        
        while s:
            temp = k
            while temp and s:
                current = s[-1].upper()
                s = s[:-1]
                if current == "-":
                    continue
                result = current + result
                temp -= 1
            while s and s[0] == "-":
                s = s[1:]
            if temp == 0 and s:
                result = "-" + result
            #print(result, s)
        return result

"""
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        # Logic 2: 
        
        result = ""
        sgroup = s.upper()#.replace("-","")
        while sgroup:
            temp = k
            while sgroup and temp:
                current = sgroup[-1]
                if current == "-":
                    sgroup = sgroup[:-1]
                    continue
                sgroup = sgroup[:-1]
                result = current + result
                temp -= 1
            while sgroup and sgroup[-1] == "-":
                sgroup = sgroup[:-1]
            if sgroup:
                result = "-" + result
        return result
"""
