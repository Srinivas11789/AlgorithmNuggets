class Solution:
    def detectCapitalUse(self, word: str) -> bool:

        def isCaptial(charac):
            if 65 <= ord(charac) <= 90:
                return True
            return False

        if len(word) == 0:
            return False

        lastIsCapital = isCaptial(word[0])

        index = 1
        for char in word[1:]:
            if isCaptial(char):
                if not lastIsCapital:
                    return False
                lastIsCapital = True
            else:
                if lastIsCapital and index != 1:
                    return False
                lastIsCapital = False
            index += 1

        # Implied: if not captialExists or captialExists
        return True
