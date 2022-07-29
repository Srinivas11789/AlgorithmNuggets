class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        
        patt = {}
        for p in range(len(pattern)):
            if pattern[p] not in patt:
                patt[pattern[p]] = []
            patt[pattern[p]].append(p)
        
        def matchPattern(src):
            if len(src) != len(pattern):
                return False
            visited = set()
            visited_char = set()
            for i in range(len(src)):
                if i in visited:
                    continue
                visited.add(i)
                if src[i] in visited_char:
                    return False
                for p in patt[pattern[i]]:
                    if src[p] != src[i]:
                        return False
                    visited.add(p)
                visited_char.add(src[i])
            return True
        
        result = []
        for word in words:
            if matchPattern(word):
                result.append(word)
        return result
                    
                
