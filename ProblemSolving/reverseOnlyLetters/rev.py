class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        
        # Logic: 100 pass 40 ms
        # * Remove characters which are not alphabets from the string
        # * Reverse the string 
        # * Place respective non-alphabet characters were they were before
        
        # result string
        result = ""
        
        # Lets use isalpha to check for alphabets
        only_letters = [i for i in S if i.isalpha()][::-1]
        
        # Run through the original name to find non alphabets and place them
        for char in S:
            if not char.isalpha():
                result += char
            else:
                result += only_letters.pop(0)
        
        return result
        
