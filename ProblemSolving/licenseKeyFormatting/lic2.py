class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        
        S = S.upper()
        sub = S.split("-")
        result = ""
        
        while sub:
            nxt = sub.pop()
            while sub and len(nxt) < K:
                nxt = sub.pop() + nxt
            if nxt:
                if len(nxt) > K:
                    sub.append(nxt[:-K])
                    nxt = nxt[-K:]
                if result:
                    result = "-" + result
                result = nxt + result
        return result
