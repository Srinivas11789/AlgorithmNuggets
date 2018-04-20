class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        ##### One testcase fails, again not sure of lexicograph
        words = sorted(words)
        #print words
        result = []
        maxi = 0
        for i in range(len(words)-1,-1,-1):
            check = list("".join(words[:i]))
            #print check, words[i]
            count = 0
            for ch in words[i]:
                if ch in check:
                    del check[check.index(ch)]
                    count += 1
                else:
                    #print ch
                    break
            if count >= len(words[i])-1 and len(words[i]) >= maxi:
                #print words[i], len(words[i])-1, maxi
                #print words[i], maxi
                if maxi >= 0:
                    maxi = len(words[i])
                result.append(words[i])
        #print sorted(result)
        if result == []:
            return ""
        else:
            result = sorted(result)
            #print result
            for r in result:
                if len(r) == maxi:
                    return r
                
        
        """
        # Easy and simple try
        words = sorted(words)
        n = len(words)
        if words[n-2] in words[n-1]:
            return words[n-2]
        """
        
        """
        # Not working for a few cases
        w = "".join(list(set("".join(words))))
        print w
        for word in words:
            count = 0
            for i in w:
                if i in word:
                    count += 1
            if count == len(w):
                return word
        return ""
        """
            
            
        
        
