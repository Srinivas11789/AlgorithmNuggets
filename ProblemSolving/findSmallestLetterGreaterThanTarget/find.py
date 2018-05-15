class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        
        # 
        if ord(target) == ord("z"):
            return letters[0]
        for char in letters:
            if ord(char) > ord(target):
                return char
        return letters[0]

        
                
                
        
