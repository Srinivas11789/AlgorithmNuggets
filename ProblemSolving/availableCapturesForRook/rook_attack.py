class Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        
        # 100 pass 99% faster
        # Revisit 1 -> O(N2) iteration to find rook and pawns, another iteration to attack condition
        # Logic: Find vertical, horizontal positions of pawns with respect to the rook and check if the path is empty!\
        
        # Variables to record positions of pawns & rook
        pawns = [] # pawns position -> [x, y] // # dict logic => row -> [col1, col2, col3....]
        rook = [0, 0] # rook position -> [x, y]
        others = [] # other pieces
        count = 0
        empty = []
        # 8x8 board of Chess - Iterate for positions
        for row in range(8):
            for column in range(8):
                if board[row][column] == "R": # white color rook
                    rook[0] = row
                    rook[1] = column
                elif board[row][column] == "p": # Black pawn, then potential attack possible
                    #if row not in pawns:
                    #    pawns[row] = []
                    #pawns[row].append(column)
                    pawns.append([row, column])
                elif board[row][column] != ".": # to check if something else is in between
                    others.append([row, column])
                elif board[row][column] == ".": # Empty block
                    empty.append([row, column])
        # Find things in between to satisfy the attack condition
        print rook, pawns, others
        for position in pawns:
            # Row check - Horizontal movement attack
            if position[0] == rook[0]:
                print "here", position[0], rook[0]
                block = 0
                if position[1] > rook[1]:
                    for i in range(rook[1]+1, position[1]):
                        if [position[0], i] in pawns or [position[0], i] in others:
                            block += 1
                        if block > 0:
                            break
                    if block == 0:
                        count += 1
                else:
                    block = 0
                    for i in range(position[1]+1, rook[1]):
                        if [position[0], i] in pawns or [position[0], i] in others:
                            block += 1
                        if block > 0:
                            break
                    if block == 0:
                        count += 1
            elif position[1] == rook[1]:
                print "there", position[0], rook[0]
                # Column check - Vertical movement attack
                if position[0] < rook[0]:
                    block = 0
                    for i in range(position[0]+1, rook[0]):
                        if [i, position[1]] in pawns or [i, position[1]] in others:
                            block += 1
                        if block > 0:
                            break
                    if block == 0:
                        count += 1
                else:
                    block = 0
                    for i in range(rook[0]+1, position[0]):
                        if [i, position[1]] in pawns or [i, position[1]] in others:
                            block += 1
                        if block > 0:
                            break
                    if block == 0:
                        count += 1
            print count
        return count
        
        # Logic2: Just traverse horizontal and vertical path of Rook until the first hit
        
        """
        # Old Logic: Pending...
        pawns = 0
        rook_position = -1
        first_pawn_down = 0
        first_pawn_up = 0
        
        for i in range(len(board)):
            # Rook Condition
            board[i] = "".join(board[i])
            if "R" in board[i]:
                rook_position = board[i].index("R")
                print board[i]
                if rook_position+1 < len(board[i]) and board[i][rook_position+1] == "p":
                    pawns += 1
                if rook_position-1 > len(board[i]) and board[i][rook_position-1] == "p":
                    pawns += 1
                j = i
                while j > 0:
                    if board[i][rook_position] == "p" and first_pawn_up == 0:
                        pawns += 1
                        first_pawn_up += 1
                        break
                    j -= 1
            if rook_position > -1:
                if board[i][rook_position] == "p" and first_pawn_down == 0:
                    pawns += 1
                    first_pawn_down += 1
                    
        return pawns
        """
        
        
