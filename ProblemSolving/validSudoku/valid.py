class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        # Logic 1: Math way
        visited_dict = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != ".":
                    for x in [(i, board[i][j]), (board[i][j], j), (board[i][j], i//3, j//3)]:
                        if x in visited_dict:
                            return False
                        visited_dict.add(x)
        return True
        
        
        # Logic 2: Utilizing String key way --> Dictionary Key Value Way
        """
        visited_dict = {}
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != ".":
                    row_key = board[i][j] + " in row " + str(i)
                    column_key = board[i][j] + " in column " + str(j)
                    box_key = board[i][j] + " in box " + str(i//3) + str(j//3)
                    if row_key in visited_dict or column_key in visited_dict or box_key in visited_dict:
                        return False
                    visited_dict[row_key] = []
                    visited_dict[column_key] = []
                    visited_dict[box_key] = []
        return True
        """
        
