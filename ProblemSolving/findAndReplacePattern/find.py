class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        
        # Analyse pattern
        # convert the pattern to numbers
        def analyse(string):
            # Order and pattern of 0123... matters which is easier to compare
            # Dictionary to maintain the id of the characters already visited
            charId = {}
            # Id tracking
            i = -1
            # Pattern string
            pattern = ""
            # Iterate through each character
            # 1. If the character has already been visited, fetch the value from the dict and update pattern
            # 2. Else, update the id and create an entry in the dictionary, also update the pattern
            for char in string:
                if char in charId:
                    pattern += charId[char]
                else:
                    i += 1
                    charId[char] = str(i)
                    pattern += str(i)
            return pattern
        
        # Iterate the pattern match for each word
        original = analyse(pattern)
        print original
        result = []
        for word in words:
            print analyse(word)
            if analyse(word) == original:
                result.append(word)
        return result
    
        """
        # Thoughts:
            # Logic 1: Fails because char can occur at different places 'xyx'
            pattern = ""
            prev = ""
            num = 0
            for char in string:
                if prev == char:
                    pattern += str(num)
                else:
                    pattern += str(num+1)
                    prev = char
            return pattern
            
            # Logic 2: Sort the characters and create a pattern
            # Logic 3: Index the occurrences and create a pattern
        """
        
        
