# ref: similar to sliding window tech --> https://leetcode.com/problems/jump-game-vi/solution/
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        
        window = [] # window to hold all previous jump positions
        scores = [0]*len(nums) # score at i from 0
        scores[0] = nums[0] # starting point at 0
        window.append(0)
        
        for i in range(1,len(nums)):
            
            # contain the window by removing indices where from where the jump cannot happen
            while window and window[0] < i-k:
                window.pop(0)
                
            # compute the current score
            scores[i] = scores[window[0]] + nums[i]
            
            # prune window with no max potential
            while window and scores[window[-1]] <= scores[i]:
                window.pop()
            
            # update the window
            window.append(i)
                
        return scores[-1]
                
            
            
            
