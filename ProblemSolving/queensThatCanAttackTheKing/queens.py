class Solution(object):
    def queensAttacktheKing(self, queens, king):
        """
        :type queens: List[List[int]]
        :type king: List[int]
        :rtype: List[List[int]]
        """
        
        # Logic 1: 6% Faster - 100 pass
        # * Naive iteration on a chess board of 8x8 - vertical, horizontal, diagnal
        xk = king[0]
        yk = king[1]
        attack = []
        
        for queen in queens:
            xq = queen[0]
            yq = queen[1]
            attacks = False
            # Vertical Attack
            y = yq
            while not attacks and y < 8:
                if [xq, y] != [xq, yq]:
                    if [xq,y] in queens:
                        break
                    elif [xq, y] == king:
                        attacks = True
                        attack.append(queen)
                y += 1
            y = yq
            while not attacks and y >= 0:
                if [xq, y] != [xq, yq]:
                    if [xq,y] in queens:
                        break
                    elif [xq, y] == king:
                        attacks = True
                        attack.append(queen)
                y -= 1
            # Horizontal Attack
            x = xq
            while not attacks and x < 8:
                if [x, yq] != [xq, yq]:
                    if [x,yq] in queens:
                        break
                    elif [x, yq] == king:
                        attacks = True
                        attack.append(queen)
                x += 1
            x = xq
            while not attacks and x >= 0:
                if [x, yq] != [xq, yq]:
                    if [x,yq] in queens:
                        break
                    elif [x, yq] == king:
                        attacks = True
                        attack.append(queen)
                x -= 1
            # Diagnal Attack
            x = xq
            y = yq
            while not attacks and x < 8 and y < 8:
                if [x, y] != [xq, yq]:
                    if [x,y] in queens:
                        break
                    elif [x, y] == king:
                        attacks = True
                        attack.append(queen)
                x += 1
                y += 1
            x = xq
            y = yq
            while not attacks and x >= 0 and y >= 0:
                if [x, y] != [xq, yq]:
                    if [x,y] in queens:
                        break
                    elif [x, y] == king:
                        attacks = True
                        attack.append(queen)
                x -= 1
                y -= 1
            x = xq
            y = yq
            while not attacks and x >= 0 and y < 8:
                if [x, y] != [xq, yq]:
                    if [x,y] in queens:
                        break
                    elif [x, y] == king:
                        attacks = True
                        attack.append(queen)
                x -= 1
                y += 1
            x = xq
            y = yq
            while not attacks and x < 8 and y >= 0:
                if [x, y] != [xq, yq]:
                    if [x,y] in queens:
                        break
                    elif [x, y] == king:
                        attacks = True
                        attack.append(queen)
                x += 1
                y -= 1
        return attack
