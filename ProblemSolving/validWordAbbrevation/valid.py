class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        
        # Logic 1: Iterate abbrevation with word - 100 pass - 94.25% faster
        i = j = 0
        delta = "0"
        while i < len(abbr):
            print(abbr[i])
            if abbr[i].isalpha():
                j += int(delta)
                delta = "0"
                if j < len(word) and abbr[i] == word[j]:
                    i += 1
                    j += 1
                else:
                    return False
            else:
                while i < len(abbr) and abbr[i].isdigit():
                    delta += abbr[i]
                    if delta == "00":
                        return False
                    i += 1
                if j + int(delta) > len(word):
                    return False
        j += int(delta)
        if j < len(word):
            return False
        return True
                
            
        
