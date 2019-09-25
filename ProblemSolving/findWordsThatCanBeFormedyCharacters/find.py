class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        
        # Logic 1: Using (Counter) Dictionary datastructure - 10% faster - 100 pass
        
        import collections
        result = 0
        dict_char = collections.Counter(chars)
        for word in words:
            dict_word = collections.Counter(word)
            ## If you use subtract method it adds the non existing chars which complicates so use '-'
            #dict_word.subtract(dict_char)
            #print(dict_word - dict_char)
            #if sorted(dict_word.values(), reverse=True)[0] <= 0:
            not_good_word = dict_word - dict_char
            if not not_good_word:
                result += len(word)
        return result
        
        
        # Logic 2: Naive iteration Using for loop for chars, for words and for char in word
        
