class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        
        # Modified version of the reference: Simple to understand and removed collections lib
        # Reference: https://leetcode.com/problems/sudoku-solver/discuss/140837/Python-very-simple-backtracking-solution-using-dictionaries-and-queue-~100-ms-beats-~90
        
        rows = {} # Track row elements
        columns = {} # Track column elements
        square = {} # Track the elements within a /3 square
        self.invisible_nodes = []
        
        # Iterate to fill in all the helper space data structures
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] != ".":
                    # Fill rows
                    if r not in rows:
                        rows[r] = set()
                    rows[r].add(board[r][c])
                    # Fill columns
                    if c not in columns:
                        columns[c] = set()
                    columns[c].add(board[r][c])
                    # Fill squares
                    key = (r//3, c//3)
                    if key not in square:
                        square[key] = set()
                    square[key].add(board[r][c])
                else:
                    self.invisible_nodes.append((r, c))
        
        #print(square)
        
        def backtrack():
            
            # True if everything is solved
            if not self.invisible_nodes:
                return True
            
            # Take the first position to solve
            r, c = self.invisible_nodes[0]
            key = (r//3, c//3)
            
            # Start guessing
            for guess in range(1, 10):
                
                guess = str(guess)
                
                # Check existence before continue
                if guess not in rows[r] and guess not in columns[c] and (key not in square or guess not in square[key]):
                    # update guess
                    board[r][c] = guess
                    # update row
                    rows[r].add(guess)
                    # update column
                    columns[c].add(guess)
                    # update square
                    if key in square:
                        square[key].add(guess)
                    else:
                        square[key] = set()
                        square[key].add(guess)
                    # Remove from invisible
                    self.invisible_nodes.pop(0)
                    
                    if backtrack(): # Backtrack with all other value succeeds
                        return True
                    else:  # Backtrack fails with this guess so revert everything
                        board[r][c] = "."
                        rows[r].discard(guess)
                        columns[c].discard(guess)
                        square[key].discard(guess)
                        self.invisible_nodes.insert(0, (r, c))
            return False
        
        backtrack()
                        
                
            
        
        
        
