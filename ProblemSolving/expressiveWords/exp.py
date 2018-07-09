# Pending...
class Solution(object):
    def expressiveWords(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        
        # Logic 1
        # Missed some important information - A letter is extended only when its length is 3 or more else they belong to the word
        n = len(S)
        first = None
        unique = []
        count = 0
        i = 0
        while i < n:
            if first == None:
                first = i
                count += 1
                i += 1
            elif S[first] == S[i]:
                count += 1
                i += 1
            elif S[first] != S[i]:
                #print count, first, S[i]
                if count >= 3:
                    unique.append(S[first])
                else:
                    unique.extend([S[first]]*count)
                first = None
                count = 0
                
            if i == n-1 and first != None and S[first] == S[i]:
                count += 1
                if count >= 3:
                    unique.append(S[first])
                else:
                    unique.extend([S[first]]*count)
               
        result = 0
        count = 0
        for word in words:
            word = list(word)
            for char in unique:
                if len(word) > 0 and char == word[0]:
                    word.pop(0)
                    count += 1
        
            if len(word) == 0 and count == len(unique):
                result += 1
                
        return result
      
        """
        # Dictionary Method
        import collections
        counts = collections.Counter(S)
        result = 0
        for word in words:
            count = 0
            wcount = collections.Counter(word)
            for k,v in wcount.items():
                counts[k] -= 1
                if counts[k] < 0:
                    break
        return result
        """
            
        
            
            
