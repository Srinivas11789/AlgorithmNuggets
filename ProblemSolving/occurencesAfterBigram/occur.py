class Solution(object):
    def findOcurrences(self, text, first, second):
        """
        :type text: str
        :type first: str
        :type second: str
        :rtype: List[str]
        """
        
        # Logic: Iterate and return the third elements - O(N) == 100% faster
        result = [] # Result variable
        text = text.split(" ") # Split text into words
        i = 0
        while i < len(text):
            if text[i] == first and (i+1 < len(text) and text[i+1] == second):
                if i+2 < len(text):
                    result.append(text[i+2])
                    i = i+1
            i += 1
        return result
                
        
        
        
