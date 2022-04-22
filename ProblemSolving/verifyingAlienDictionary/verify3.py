class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        i = 0
        
        ref = {}
        for j, o in enumerate(order):
            if o not in ref:
                ref[o] = j
        
        while words and i < float('inf'):
            
            position_chars = []
            
            for w, word in enumerate(words):
                if i >= len(word):
                    if position_chars:
                        return False
                    continue

                print(i, word, position_chars)
                
                if position_chars and ref[word[i]] < ref[position_chars[-1]]:
                    #print(word[i], ref[word[i]], position_chars[-1], ref[position_chars[-1]])
                    return False
                elif position_chars and ref[word[i]] > ref[position_chars[-1]]:
                    words.pop(w)
                else:
                    pass
                    
                position_chars.append(word[i])
            
            if position_chars == []:
                return True
            
            i += 1
