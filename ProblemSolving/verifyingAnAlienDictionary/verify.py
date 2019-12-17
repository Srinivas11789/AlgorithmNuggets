class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        
        # 1. Store the indexes of each letter in dictionary for easy access
        alp_order = {}
        alp_order[""] = -1
        for ch in range(len(order)):
            alp_order[order[ch]] = ch
        
        # 2. Compare function to compare 2 strings
        def compare_words(w1, w2):
            n = max(len(w1), len(w2))
            for c in range(n):
                # Character is null if index is greater than the string
                if c < len(w1):
                    char1 = w1[c]
                else:
                    char1 = ""
                if c < len(w2):
                    char2 = w2[c]
                else:
                    char2 = ""
                    
                # Sort when characters are set
                if alp_order[char1] < alp_order[char2]: # Lesser
                    return -1 
                elif alp_order[char2] < alp_order[char1]: # Greater
                    return 1
                
            return 0 # equal condition
        
        # 2. Sort based on the index of order and check
        print(sorted(words, cmp=compare_words))
        if words == sorted(words, cmp=compare_words):
            return True
        else:
            return False
        
        
        
