class Solution(object):
    def indexPairs(self, text, words):
        """
        :type text: str
        :type words: List[str]
        :rtype: List[List[int]]
        """
        
        # Logic 1: O(N) iteration on all the words and corresponding iteration on text everytime - 100 pass 95% faster
        result = []
        for word in words:
            n = len(word)
            for i in range(len(text)):
                if text[i:i+n] == word:
                    result.append([i, i+n-1])
        return sorted(result)
