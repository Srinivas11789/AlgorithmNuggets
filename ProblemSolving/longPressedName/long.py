class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        
        # Logic 2: 
        # * Start from name and then scan type
        while name and typed:
            # Check the first element of both list, delete if they are same
            if name[0] == typed[0]:
                name = name[1:]
                typed = typed[1:]
            else:
                # Delete mistyped letter by they dont match
                if typed:
                    typed = typed[1:]
                
        # Name should be empty after the scan
        if name:
            return False
        else:
            return True
        
        
        """
        # Logic 1: Fail - Set(typed) maintaining the index of occurence to match the name 
        # * multiple occurence of char in name fails
        result = []
        for char in typed:
            if char not in result:
                result.append(char)
                
        if name == "".join(result):
            return True
        else:
            return False
        """
        
