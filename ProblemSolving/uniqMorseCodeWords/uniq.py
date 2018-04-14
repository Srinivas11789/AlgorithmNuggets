class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        
        # Mapping of the morse code and alphabets
        value = 96
        alp = []
        for i in range(26):
            value += 1
            alp.append(chr(value))
            
        # Morse code dictionary/list for easy fetching back results with key as the resulting morse code
        morse = []
        for word in words:
            result = ""
            for ch in word:
                result += morse_code[alp.index(ch)]
            
            if result not in morse:
                morse.append(result)
        
        return len(morse)
                
            
            

        
            
