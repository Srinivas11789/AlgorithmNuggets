'''
Design a Tic-Tac-Toe game played between two players on an n x n grid. A move is guaranteed to be valid, and a valid move is one placed on an empty block in the grid. A player who succeeds in placing n of their marks in a horizontal, diagonal, or vertical row wins the game. Once a winning condition is reached, the game ends and no more moves are allowed. Below is an example game which ends in a winning condition:

Given n = 3, assume that player 1 is "X" and player 2 is "O" 
board = TicTacToe(3);

board.move(0, 0, 1); -> Returns 0 (no one wins)
|X| | |
| | | |    // Player 1 makes a move at (0, 0).
| | | |

board.move(0, 2, 2); -> Returns 0 (no one wins)
|X| |O|
| | | |    // Player 2 makes a move at (0, 2).
| | | |

board.move(2, 2, 1); -> Returns 0 (no one wins)
|X| |O|
| | | |    // Player 1 makes a move at (2, 2).
| | |X|

board.move(1, 1, 2); -> Returns 0 (no one wins)
|X| |O|
| |O| |    // Player 2 makes a move at (1, 1).
| | |X|

board.move(2, 0, 1); -> Returns 0 (no one wins)
|X| |O|
| |O| |    // Player 1 makes a move at (2, 0).
|X| |X|

board.move(1, 0, 2); -> Returns 0 (no one wins)
|X| |O|
|O|O| |    // Player 2 makes a move at (1, 0).
|X| |X|

board.move(2, 1, 1); -> Returns 1 (player 1 wins)
|X| |O|
|O|O| |    // Player 1 makes a move at (2, 1).
|X|X|X|

Here's a starting point:

class TicTacToe(object):
  def __init__(self, n):
    # Fill this in.

  def move(self, row, col, player):
    # Fill this in.

board = TicTacToe(3)
board.move(0, 0, 1)
board.move(0, 2, 2)
board.move(2, 2, 1)
board.move(1, 1, 2)
board.move(2, 0, 1)
board.move(1, 0, 2)
print(board.move(2, 1, 1))
'''

class TicTacToe(object):
  def __init__(self, n):
    # Initialize nxn with all 0s
    self.n = n
    self.grid = [[0 for i in range(n)] for i in range(n)]

  def move(self, row, col, player):
    # * Ensuring move is always valid we dont need to check
    # * Using player ids instead of X0
    self.grid[row][col] = player
    # Check winning row
    for rw in range(self.n):
        rwCheck = set(self.grid[rw])
        if len(rwCheck) == 1:
          return "1" + "(player " + str(rwCheck) + " wins)"
    # Check winning col
    for col in range(self.n):
        colCheck = set(self.grid[col])
        if len(colCheck) == 1:
          return "1" + "(player " + str(colCheck) + " wins)"
    # Check winning diagnal
    diag = set()
    for i in range(0, self.n):
      diag.add(self.grid[i][i])
      if len(diag) > 1:
        break
    if len(diag) == 1:
      return "1" + "(player " + str(diag) + " wins)"
    return "0"

board = TicTacToe(3)
board.move(0, 0, 1)
board.move(0, 2, 2)
board.move(2, 2, 1)
board.move(1, 1, 2)
board.move(2, 0, 1)
board.move(1, 0, 2)
print(board.move(2, 1, 1))
     
        
