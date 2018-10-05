# A little weak with 2d and 3d stuff
# Reference: https://leetcode.com/problems/battleships-in-a-board/discuss/166582/simple-6-line-Python-solution-with-explanation%3A-one-pass-O(1)-space-no-modification
#
class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        boats = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "X" and (i-1 < 0 or board[i-1][j] == ".") and (j-1 < 0 or board[i][j-1] == "."):
                    boats +=1 
        return boats
