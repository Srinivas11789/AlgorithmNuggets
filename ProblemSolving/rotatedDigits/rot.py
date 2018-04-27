class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        # Rotate to themself
        # 0,1,8
        # Rotate to Each other
        # 2,5 
        # 6,9
        # Others do not rotate to valid numbers at all
        
        result = []
        for n in range(N+1):
            new = ""
            for char in str(n):
                if char in ["0","1","8"]:
                    new += char
                elif char == "6":
                    new += "9"
                elif char == "9":
                    new += "6"
                elif char == "2":
                    new += "5"
                elif char == "5":
                    new += "2"
                else:
                    break
            if str(n) != new and len(str(n)) ==len(new):
                result.append(n)
        return len(result)
        
        
