class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        
        # InBuilt method python - 100 pass
        # return str.lower()
    
        # Ordinance Method - HEX to ASCII resolver
        lowerStr = ""
        for char in str:
            if ord(char) >= 65 and ord(char) <= 90:
                lowerStr += chr(ord(char)+32)
            else:
                lowerStr += char
        return lowerStr
