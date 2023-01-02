class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        words = s.split(" ")
        pattern_ref = {}
        value_ref = set()

        # build pattern for reference
        for i in list(pattern):
            if i not in pattern_ref:
                pattern_ref[i] = ""

        if len(words) != len(pattern):
            return False

        # check the words
        for w in range(len(words)):
            word = words[w]
            if pattern_ref[pattern[w]] == "" and word in value_ref:
                return False
            elif pattern_ref[pattern[w]] == "":
                pattern_ref[pattern[w]] = word
                value_ref.add(word)
            elif pattern_ref[pattern[w]] == word:
                continue
            else:
                return False
        return True
