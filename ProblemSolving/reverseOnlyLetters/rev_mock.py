class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        
        # Logic 1: 
        reverse = list(S[::-1])
        result = ""
        for i in range(len(S)):
            #print(result, S, reverse)
            if S[i].isalpha():
                while reverse and not reverse[0].isalpha():
                    reverse.pop(0)
                result += reverse.pop(0)
            else:
                result += S[i]
        return result
        
        # Just Reverse
        #return S[::-1]
        
        # Reverse the substring alone
        """
        for i in range(len(S)):
            if not S[i].isalpha():
                S = S[:i][::-1]+S[i:]
                i += 1
        return S
        """
