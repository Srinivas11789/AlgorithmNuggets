class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        
        # Logic 1: All passed except for scale testcase leading to time limit exceeded --> Fix below 
        # * Follow all the adjacent paths through the matrix should work
        # * Disadvantage is when 2 or more possible path exists --> Solution is to recurse
        """
        def recurse_and_match(current, remaining, board, path):
            
            print(current, len(remaining))
            
            # Match has occurred
            if remaining == "":
                self.match = True
                return
            
            # Possible start of match
            if current == None:
                for r in range(len(board)):
                    for c in range(len(board[0])):
                        if board[r][c] == remaining[0]:
                            recurse_and_match((r,c), remaining[1:], board, [(r,c)])
                return
            else:
                # Progressive match as we proceed
                r, c = current
                for x,y in [ (1,0), (-1,0), (0,1), (0,-1) ]:
                    #print(r+x, c+y, remaining[0], path)
                    if 0 <= r+x < len(board) and 0 <= c+y < len(board[0]) and (r+x, c+y) not in path and remaining[0] == board[r+x][c+y]:
                        recurse_and_match((r+x, c+y), remaining[1:], board, path + [(r+x, c+y)])    
                return
        
        self.match = False
        recurse_and_match(None, word, board, [])
        return self.match
        """
        
        # Segregate, Recurse and Return --> Use a visited memory to track instead of a list to traverse extra (path above)
        def recurse_and_match(r, c, remaining, board):
            
            # Match has occurred
            if remaining == "":
                return True

            # Progressive match as we proceed
            self.visited[r][c] = 1
            for x,y in [ (r+1,c), (r-1,c), (r,c+1), (r,c-1) ]:
                if 0 <= x < len(board) and 0 <= y < len(board[0]) and self.visited[x][y] == 0 and remaining[0] == board[x][y]:
                    if recurse_and_match(x, y, remaining[1:], board):
                        return True
            self.visited[r][c] = 0
            return False
        
        # Possible start of match
        self.visited = [[0]*len(board[0]) for _ in range(len(board))]
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0] and recurse_and_match(r, c, word[1:], board):
                    return True
        return False
        
