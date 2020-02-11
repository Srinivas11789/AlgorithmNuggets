# Logic 1: Declare Board and Make Moves + Observe for winning criteria - 100 pass - 5% faster
# * This logic checks for winning criterion every time a move is made which is pretty lame, as it iterates on every move.
# * Instead we could hold the winning category on a placeholder or dict or list and eliminiate to find the winning criteria on point.
class TicTacToe(object):

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        
        # Initialize the Board
        self.n = n
        self.board = [["." for i in range(n)] for i in range(n)]

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        
        # Move of a player
        if player == 1: # X
            self.board[row][col] = "X"
        else: # O
            self.board[row][col] = "O"
            
        # Check winning condition
        # Row check
        if set(self.board[row]) == set("X"):
            return 1
        elif set(self.board[row]) == set("O"):
            return 2
        
        # Column check
        if set([self.board[i][col] for i in range(self.n)]) == set("X"):
            return 1
        elif set([self.board[i][col] for i in range(self.n)]) == set("O"):
            return 2
        
        # Diagnal check - forward diagnal
        if set([self.board[i][i] for i in range(self.n)]) == set("X"):
            return 1
        elif set([self.board[i][i] for i in range(self.n)]) == set("O"):
            return 2

        # Diagnal check - reverse diagnal
        i = 0
        j = self.n-1
        if set([self.board[i+o][j-o] for o in range(self.n)]) == set("X"):
            return 1
        elif set([self.board[i+o][j-o] for o in range(self.n)]) == set("O"):
            return 2
        
        #print(self.board)
        return 0 # No One Wins


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
