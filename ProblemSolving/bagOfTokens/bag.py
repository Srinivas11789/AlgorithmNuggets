class Solution:
    
    # Logic 1: Make subproblems independent with sorting and solve greedily (ref: sol)
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:

        tokens.sort() # sorting converts it to greedy removing choice dependency
        
        score = 0
        result = 0
        
        while tokens and (power >= tokens[0] or score > 0):
            
            while tokens and tokens[0] <= power: # maximize the score with while to be greedy
                curr_card = tokens.pop(0)
                power -= curr_card
                score += 1
            
            result = max(result, score) # calc max score as we play
                
            if tokens and score > 0: # maximize the power by choosing last element to be greedy
                curr_card = tokens.pop()
                score -= 1
                power += curr_card
       
        return result
