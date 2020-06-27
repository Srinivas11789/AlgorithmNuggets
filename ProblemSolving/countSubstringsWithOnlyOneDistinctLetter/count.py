# Logic 1: Find the number of substring with ( sum of N ) for each disinct substrings - 100 pass - 7% pass 
class Solution:
    def sumOfN(self, n):
        return (n*(n+1))//2
            
    def countLetters(self, S: str) -> int:
        distinct = 0
        substring = []
        for i in range(len(S)):
            if len(set(substring+[S[i]])) > 1:
                n = len(substring)
                distinct += self.sumOfN(n)
                substring = []
            substring.append(S[i])
        if substring:
            n = len(substring)
            distinct += self.sumOfN(n)
        return distinct
