class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        import collections
        consistent = 0
        allowd = collections.Counter(allowed)
        for w in words:
            consist = True
            for c in w:
                if c not in allowd:
                    consist = False
                    break
            if consist:
                consistent += 1
        return consistent
