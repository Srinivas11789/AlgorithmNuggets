class Solution:
    def reorganizeString(self, s: str) -> str:
        
        # Logic 1: counting the num of chars, contructing a non overlap string from highest frequency
        
        freqs = {}
        for i in range(len(s)):
            if s[i] not in freqs:
                freqs[s[i]] = 0
            freqs[s[i]] += 1
        
        result = ""
        i = 0
        order = sorted(freqs.keys(), key=lambda x: freqs[x], reverse=True)
        
        while i < len(order) and len(order) > 1:
            prev = order
            o = order[i]
            if o not in freqs:
                i += 1
                continue
            if not result:
                result += o
                freqs[o] -= 1
                i += 1
            elif result[-1] != o:
                result += o
                freqs[o] -= 1
                i = 0
            else:
                print(i, o, result)
                i += 1
            if freqs[o] == 0:
                del freqs[o]
                order.pop(i)
                i = 0
            order = sorted(freqs.keys(), key=lambda x: freqs[x], reverse=True)
            if prev[i] != order[i]:
                i = 0
            
        if freqs and len(freqs) != 1:
            return ""
        if freqs and len(freqs) == 1:
            for k,v in freqs.items():
                if v == 1:
                    if result and k != result[-1]:
                        return result+k
                    else:
                        return k
                else:
                    return ""
        
        return result
