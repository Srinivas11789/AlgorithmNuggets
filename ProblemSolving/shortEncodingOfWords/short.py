class Solution(object):
    def minimumLengthEncoding(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        
        encoded_string = ""
        
        for word in sorted(words, key=lambda x: len(x), reverse=True):
            # One other thing to check is, if the substring is such that <substring># occurs rather than <substring>...# (which is not correct)!
            if word+"#" not in encoded_string:
                encoded_string += word + "#"

        return len(encoded_string)
    
        """
        # Logic to satisfy literally the indexes and encoded string, as the length is only required - no need to calculate the indexes
        encoded_string = ""
        indexes = []
        
        # Sort array with length in the decreasing order
        for word in sorted(words, key=lambda x: len(x), reverse=True):
            if word+"#" in encoded_string:
                indexes.append(encoded_string.index(word))
            else:
                encoded_string += word + "#"

        return len(encoded_string)
        """
