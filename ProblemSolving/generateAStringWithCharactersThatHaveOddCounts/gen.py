class Solution:
    def generateTheString(self, n: int) -> str:
        
        # Logic 1: choose alphas at random, you would need only 2 --> Odd with one and Even with 2 chars - 92 % faster
        """
        import string
        alphas = list(string.ascii_lowercase)
        if n%2 == 0:
            return alphas.pop(0)*(n-1)+alphas.pop(0)
        else:
            return alphas.pop(0)*n
        """
        
        # Logic 2: Bit more optmize by loosing all the char list - 98% faster
        first = "x"
        sec = "y"
        if n%2 == 0:
            return first*(n-1)+sec
        else:
            return sec*n
            
