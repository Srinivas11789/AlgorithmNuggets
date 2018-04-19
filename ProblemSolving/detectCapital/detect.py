class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        capitals = 0
        for ch in word:
            if ch == ch.upper():
                capitals += 1
        
        if capitals == len(word):
            return True
        elif capitals == 0:
            return True
        elif capitals == 1 and len(word) > 1 and word[0] == word[0].upper():
            return True
        else:
            return False
        
