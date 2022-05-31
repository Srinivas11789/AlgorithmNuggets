class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        
        # Logic 1: naive iteration (O(N)*2) with comparison -> 29% faster
        
        def hasIntersection(d1, d2):
            for k,v in d1.items():
                if k != "length" and k in d2:
                    return True
            return False
        
        def makeDict(word):
            d = {}
            for w in range(len(word)):
                if word[w] not in d:
                    d[word[w]] = 0
                d[word[w]] += 1
            d["length"] = len(word)
            return d
        
        maps = []
        max_l = 0
        
        for i in range(len(words)):
            d = makeDict(words[i])
            for another_d in maps:
                #print(d, another_d)
                if hasIntersection(d, another_d):
                    continue
                l = d["length"]*another_d["length"]
                if l > max_l:
                    max_l = l
            maps.append(d)
        
        return max_l
        
