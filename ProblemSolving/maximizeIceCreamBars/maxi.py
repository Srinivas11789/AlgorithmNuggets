class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:

        # buy in any order and maximize
        costs.sort()
        icecream_bars = 0

        # iterate to maximize no of icecream_bars
        while costs and coins >= costs[0]:
            coins -= costs.pop(0)
            icecream_bars += 1
        
        return icecream_bars
