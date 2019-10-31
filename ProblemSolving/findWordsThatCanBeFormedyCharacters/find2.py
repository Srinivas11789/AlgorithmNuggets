class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        
        # Logic: Dictionary to store all characters count
        import collections
        c_count = collections.Counter(chars)
        lengths = 0
        for word in words:
            w_count = collections.Counter(word)
            diff = w_count - c_count
            if not diff:
                lengths += len(word)
        return lengths
