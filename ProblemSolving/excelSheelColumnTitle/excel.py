class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """

        # If n is a alphabet
        if n < 27:
            return chr(64+n)
        else:
            string = ""
            # Total combination is 26 power n
            while n > 0:
                print n
                n -= 1
                string += chr(65+n%26)
                n = n//26
            return string[::-1]
        
            
            
