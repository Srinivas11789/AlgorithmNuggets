class Solution:
    def countOdds(self, low: int, high: int) -> int:
        # Logic 1: Math way - 100 pass 94%
        odds = 0
        if (low%2 != 0): # if low is odd
            odds += 1
        if (high%2 != 0): # is high is odd
            odds += 1
        if odds == 0 or odds < 2: # anyone or none are odd we do diff//2
            odds += (high - low)//2
        elif odds == 2: # both low,high are odds then we take diff-1//2
            odds += (high - low - 1)//2
        return odds
