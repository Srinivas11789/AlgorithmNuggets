# Pending...
class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        # Maximizing the Total Score
        # Known facts:
        # * no player can skip turns
        # * once a player takes a score no one else can take it
        # * taking is only possible from beginning or the end...
        # * Consider the next score to play and make a decision
        
        def gameOn(scores, p1, p2):
            
            # The decision when all the scores has expired
            if not scores:
                if p1 > p2:
                    return True
                else:
                    return False
              
            """
            # Player 1s choice
            # * Even condition of array: try to maximize the score
            if len(scores)%2 == 0:
            next_chance_0 = 
            next_chance_final = 
            
            else:
                # Odd condition when there is no choice: If there is no possibility of maximum in the next turn choose the current maximum
                if scores[0] > scores[-1]:
                    p1 += scores[0]
                    scores = scores[1:]
                else:
                    p1 += scores[-1]
                    scores = scores[:-1]
    
            print scores
                
            # Player 2nd choice can go both ways...
            if scores:
                return (gameOn(scores[:][1:], p1, p2+scores[:][0])) or (gameOn(scores[:][:-1], p1, p2+scores[:][-1]))
            else:
                return gameOn(scores, p1, p2)
            """
            """
            if scores:
                # Both taking from the beginning of the array
                # Both taking from the end of the array
                # One takes beginning and one at the end
                print scores
                if len(scores)%2 != 0:
                    return (gameOn(scores[:][2:], p1+scores[:][0], p2+scores[:][1])) or (gameOn(scores[:][:-2]+scores[:][-1], p1, p2+scores[:][-2])) 
                elif len(scores) == 1:
                    if len(nums)%2 == 0:
                        return gameOn([], p1, p2+scores[0])
                    else:
                        return gameOn([], p1+scores[0], p2)
                else:
                    return (gameOn(scores[:][1:-1], p1+scores[:][0], p2+scores[:][-1])) or (gameOn(scores[:][1:-1], p1+scores[:][-1], p2+scores[:][0]))
            else:
                return gameOn(scores, p1, p2)
        
        # Start with initial scores
        return gameOn(nums, 0, 0)
        """
        
        """
        # Greedy for the max score in each step (0 or -1) will not work as the player work to maximize their total score. We need to consider the total score, a player might take lower score in current turn to anticipate to snatch a better score next turn -- implement this....
        
        # Logic: Player 1 is Greedy always!
        # * Lets assume player 1 always greedy and goes for the maximum element either at the start or the end
        # * For player 2, lets assume he is also greedy always
        
        # Conditions Faced:
        # * when there are even number of scores, having player 1 and player 2 play back to back with recursive works
        # * when there is odd number of scores, it doesnt. think of something!
        
        def gameOn(scores, p1, p2):
            
            # The decision when all the scores has expired
            if not scores:
                if p1 > p2:
                    return True
                else:
                    return False
              
            # Player 1s choice
            if scores[0] > scores[-1]:
                p1 += scores[0]
                scores = scores[1:]
            else:
                p1 += scores[-1]
                scores = scores[:-1]
    
            print scores
                
            # Player 2nd choice
            if scores:
                if scores[0] > scores[-1]:
                    return gameOn(scores[:][1:], p1, p2+scores[:][0])
                else:
                    return gameOn(scores[:][:-1], p1, p2+scores[:][-1])
            else:
                return gameOn(scores, p1, p2)
        
        # Start with initial scores
        return gameOn(nums, 0, 0)
        """
        
