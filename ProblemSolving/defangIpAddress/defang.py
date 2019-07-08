class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        
        # Easy inbuilt solution -- 100 pass 100%
        ## return address.replace(".","[.]")
        
        # Another easy method -- 100 pass 100%
        return "[.]".join(address.split("."))
    
        # Manual replacements -- 100 pass 100%
        """
        address = list(address)
        for c in range(len(address)):
            if address[c] == ".":
                address[c] = "[.]"
        return "".join(address)
        """
        
