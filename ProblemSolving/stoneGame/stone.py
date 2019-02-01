class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        # lt medium 100 pass
        # Logic: Recursive method of alex choosing the winning option
        # * Go both ways of how lee will respond 
        def recurse_for_all_options(piles, alex, lee):
            
            # Null check - Game over condition for alex to win
            if not piles:
                if alex > lee:
                    return True
                else:
                    return False
            
            # Alex turn - Assume alex always takes maximum to win
            # * Max pile in the front of the list
            if piles[0] > piles[-1]:
                piles = piles[1:]
                alex += piles[0]
            elif piles[0] == piles[-1]:
                # when both the front and end are equal, check the next option to maximize
                if len(piles) >= 4 and piles[1] > piles[-2]:
                    alex += piles[-1]
                    piles = piles[:-1]
                else:
                    alex += piles[0] 
                    piles = piles[1:]    
            else:
                # Max pile in the end of the list
                alex += piles[-1]
                piles = piles[:-1]
            
            # Lee's turn - Assume lee takes anything first or last so recurse both the option he takes
            # * Or condition to check if Alex wins atleast once
            return recurse_for_all_options(piles[:][1:], alex, lee+piles[:][0]) or recurse_for_all_options(piles[:][:-1], alex, lee+piles[:][-1])
        
        return recurse_for_all_options(piles, 0, 0)
