class Solution(object):
    def numMovesStones(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        
        # Logic 1: Sort the ranges to obtain possible consecutive
        a, b, c = sorted([a,b,c])
        moves = [0, 0]
        # Minimum should exist or be 1 or be 2 at the max
        if (b-a) == 1 and (c-b) == 1:
            moves[0] = 0
        elif (b-a) > 2 and (c-b) > 2:
            moves[0] = 2
        else:
            moves[0] = 1
        # Maximum must be total length and empty spots
        moves[1] = c - a - 2 # c - a is full range and minus 2 for c,a
        return moves
        
        """
        # Scribble
        moves = [0, 0]
        if abs(a-b) != 1 or abs(b-c) != 1:
            n = max([a,b,c])
            moves[0] = 1
            moves[1] = n-3
        return moves
        """
