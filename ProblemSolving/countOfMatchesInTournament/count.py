"""
# Logic 1: Naive iteration backwards from n with even/odd logic --> 82% faster
class Solution:
    def numberOfMatches(self, n: int) -> int:
        match = 0
        advance = 0
        while n+advance != 1:
            print(n, match, advance)
            n += advance
            advance = 0
            if n%2 != 0:
                advance += 1
                n -= 1
            n -= n//2
            match += n
        return match
"""
# Logic 2: use modulo and division to make the loop simpler --> 95 % faster
class Solution:
    def numberOfMatches(self, n: int) -> int:
        matches = 0
        advance = 0
        while n+advance != 1:
            #print(n, matches, advance)
            n += advance
            advance = n%2
            n = n//2
            matches += n
        return matches
