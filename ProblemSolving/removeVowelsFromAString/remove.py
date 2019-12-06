class Solution:
    def removeVowels(self, S: str) -> str:
        
        # Logic 1: Define vowels as set for O(1) check and iterate string to remove vowels
        # 1. we can remove the vowels --> 88% faster 
        """
        vowels = {'a', 'e', 'i', 'o', 'u'}
        i = 0
        while i < len(S):
            if S[i] in vowels:
                S = S[:i]+S[i+1:]
            else:
                i += 1
        return S
        """
        
        # 2. we can also create a new string if they are not vowels --> 95 % faster
        
        vowels = {'a', 'e', 'i', 'o', 'u'}
        result = ""
        i = 0
        while i < len(S):
            if S[i] not in vowels:
                result += S[i]
            i += 1
        return result
        
        
        # 3. we can use string replace or regex functions --> 95 % faster
        """
        import re
        return re.sub("a|e|i|o|u", "", S)
        """

        
