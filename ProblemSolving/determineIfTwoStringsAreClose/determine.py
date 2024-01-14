class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:

        import collections

        if len(word1) != len(word2):
            return False

        # character count matching
        count1 = collections.Counter(word1)
        count2 = collections.Counter(word2)

        if count1 == count2:
            return True

        chars1 = set(count1.keys())
        for c in count2.keys():
            if c not in chars1:
                return False

        if sorted(count1.values()) == sorted(count2.values()):
            return True
