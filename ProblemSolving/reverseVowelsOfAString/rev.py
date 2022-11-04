class Solution:
    def reverseVowels(self, s: str) -> str:

        vowels = { "a", "e", "i", "o", "u" }

        vs = []

        for i in range(len(s)):
            if s[i].lower() in vowels:
                vs.append(i)

        while len(vs) > 1:
            left = vs.pop(0)
            right = vs.pop()
            s = s[:left] + s[right] + s[left+1:right] + s[left] + s[right+1:]
        
        return s
