class Solution(object):
    def numSmallerByFrequency(self, queries, words):
        """
        :type queries: List[str]
        :type words: List[str]
        :rtype: List[int]
        """
        
        def strength_of_string(word):
            word = sorted(word)
            temp = word[0]
            strength = 1
            for char in word[1:]:
                if char == temp:
                    strength += 1
                else:
                    break
            return strength
        
        queries_strength = []
        for w in queries:
            queries_strength.append(strength_of_string(w))
            
        result = [0 for i in range(len(queries_strength))]
        for w in words:
            words_strength = strength_of_string(w)
            i = 0
            while i < len(queries_strength):
                if words_strength > queries_strength[i]:
                    result[i] += 1
                i += 1
        return result
                
        
