# https://leetcode.com/problems/palindrome-partitioning/description/
class Solution:
    def partition(self, s: str) -> List[List[str]]:

        self.allPalins = []

        def isPalindrome(test):
            if not test:
                return False
            if len(test) == 1:
                return True
            left = 0
            right = len(test)-1
            while left < right and test[left] == test[right]:
                left += 1
                right -= 1
            if right - left > 0:
                return False
            return True

        def backtrackPalin(remaining, palins):
            
            if len(remaining) == 0:
                self.allPalins.append(palins)
                return
            
            for r in range(1, len(remaining)+1):
                if isPalindrome(remaining[:r]):
                    backtrackPalin(remaining[r:], palins + [remaining[:r]])
            return
        
        backtrackPalin(s, [])
        return self.allPalins
