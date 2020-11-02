class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        """
        :type sentence: str
        :type searchWord: str
        :rtype: int
        """
        
        # Logic 1: split sentence and compare searchWord length prefix for every word - 75% faster
        words = sentence.split(" ")
        m = len(searchWord)
        
        for i in range(len(words)):
            if searchWord == words[i][:m]:
                return i+1
        return -1
        
