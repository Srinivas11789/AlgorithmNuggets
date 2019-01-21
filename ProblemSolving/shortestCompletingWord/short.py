class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        
        # Logic 3:  
        # * Dictionary compare
        
        import collections
        
        license = collections.Counter([str(i.lower()) for i in licensePlate if not i.isdigit() and i != " "])
        result = ""
        
        for word in words:
            word_count = collections.Counter(word.lower())
            decide = 0
            for character in license.keys():
                if character not in word_count or license[character] > word_count[character]:
                    decide = 1
                #print character, license[character], word_count[character], decide
            if decide == 0:
                if result == "":
                    result = word
                else:
                    if len(word) < len(result):
                        result = word
        return result
                
        # Logic 2: Sorted Match Logic: But fails when the characters not present in one of the string sort becomes wrong
        """
        # Sanitize licensePlate
        # * Lowercase
        # * not digit
        # * sorted order to match
        license = str("".join(sorted([str(char.lower()) for char in licensePlate if not char.isdigit() and char != " "])))
        
        result = ""
        
        # iterate through words for a substring match
        for word in words:
            current = str("".join(sorted(word.lower())))
            if license in current:
                if result == "":
                    result = word
                else:
                    if len(word) < len(result):
                        result = word
        return result
        """
        
        # Logic1: O(NM) - to iterate on both licenseplate and words
        # * One full iteration of the array to find the minimum length that contains all the letters
        #### CRAP............
        """
        result = []
        result_mini = ""
        
        # Iterate the words
        for word in words:
            
            # Lowercase the word as per instructons
            current = list(word.lower())
            temp = list(licensePlate.lower())
            
            # Iterate licensePlate to match all characters of the word
            for i in range(len(temp)):
                for j in range(len(current)):
                    if not temp[i].isdigit() and temp[i] == current[j]:
                        if (i, j) not in result:
                            result.append((i,j))
                    
            # LicensePlate match
            if not temp:
                if result_mini == "":
                    result_mini = len(current)
                else:
                    result_mini = min(result_mini, len(current))
                    
        return result_mini
        """
        
        
        
