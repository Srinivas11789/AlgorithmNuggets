class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        
        vowels = ['a','e','i','o','u']
        S = S.split(" ")
        n = len(S)
        for i in range(n):
            if S[i][0].lower() in vowels:
                S[i] = S[i]+"ma"
            else:
                S[i] = S[i][1:]+S[i][0]+"ma"
            S[i] = S[i]+"a"*(i+1)
        return " ".join(S)
        
