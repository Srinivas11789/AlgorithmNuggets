class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:

        # Logic 1: 2 O(len(words)) iteration with O(sum(words)) iteration to create substrings - 88% faster
        substrings = {}
        encoded = 0
        
        # Iteration 1 to store substrings
        for w in words:
            i = 1 # avoid adding full word for now
            while i < len(w):
                curr_subs = w[i:]
                substrings[w[i:]] = True
                i += 1
            
        # Iteration 2 to check intersection (substring)
        for w in words:
            if w not in substrings:
                encoded += len(w) + 1
                substrings[w] = True # update with full word
            
        return encoded
        
        
