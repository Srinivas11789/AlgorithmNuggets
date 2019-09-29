class Solution(object): # mock
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        
        # Hacky
        """
        if sorted(words, key=lambda x: sorted(x, key=lambda y: order.index(y)) and len(x)) != words:
            return False
        return True
        """
        
        # build dictionary
        position = {}
        for w in range(len(order)):
            position[order[w]] = w
        
        for i in range(len(words)-1):
            word1 = list(words[i])
            word2 = list(words[i+1])
            while word1 and word2:
                print(word1, word2)
                char1 = word1.pop(0)
                char2 = word2.pop(0)
                if position[char1] > position[char2]:
                    return False
                elif position[char1] < position[char2]:
                    break
                else:
                    if word1 and not word2:
                        return False
            #if word1 and not word2:
            #    return False
        return True
