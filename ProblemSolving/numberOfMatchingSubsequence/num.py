class Solution:

    # Logic 1: store string by index and iterate words for subsequence checks
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        
        full = {}
        for i in range(len(s)):
            if s[i] not in full:
                full[s[i]] = []
            full[s[i]].append(i)
        
        result = []
        
        for word in words:
            visited = set()
            prev = -1
            isSub = True
            for w in range(len(word)):
                if word[w] not in full:
                    isSub = False
                    break
                    
                curr = None
                for r in full[word[w]]:
                    key = word[w]+str(r)
                    if r > prev and key not in visited:
                        curr = r
                        visited.add(key)
                        break 
                
                if curr == None:
                    isSub = False
                    break
                
                if prev == -1:
                    prev = curr
                elif curr < prev:
                    isSub = False
                    break
                else:  
                    prev = curr
                    
            #print(word, visited)
            if isSub and len(visited) == len(word):
                result.append(word)
                
        print(result)
        return len(result)
                
            
