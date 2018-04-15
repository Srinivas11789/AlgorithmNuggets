class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        alp_rows = [['qwertyuiop'],['asdfghjkl'],['zxcvbnm']]
        final = []
        for word in words:
            result = []
            for ch in word.lower():
                for i in range(len(alp_rows)):
                    if ch in "".join(alp_rows[i]):
                        if i not in result:
                            result.append(i)
            if len(result) == 1:
                final.append(word)
        return final
                        
        
