class Solution:
    # Logic 1: 
    # 1. Iterate row wise
    # * iterate forward and reverse to get the distance with no mines
    # 2. Iterate column wise
    # * similar
    # During the last iteration you should get the answer
    def orderOfLargestPlusSign(self, N: int, mines: List[List[int]]) -> int:
        # 1. Create a 2d map and mark mines
        twod = [[0]*N for i in range(N)]
        mineLoc = set()
        for mine in mines:
            mineLoc.add(tuple(mine))
        big = 0
        # 2. The possibilities are only in the center except the corners. So we backtrack on every selection?
        
        # row-wise iterate
        for r in range(N):
            # Forward
            no_mine = 0
            for c in range(N):
                if (r, c) in mineLoc:
                    no_mine = 0
                else:
                    no_mine += 1
                    
                twod[r][c] = no_mine
            
            # reverse
            no_mine = 0
            for c in range(N-1, -1, -1):
                if (r, c) in mineLoc:
                    no_mine = 0
                else:
                    no_mine += 1
                    
                twod[r][c] = min(no_mine, twod[r][c])
                
        # column-wise iterate
        for c in range(N):
            # Forward
            no_mine = 0
            for r in range(N):
                if (r, c) in mineLoc:
                    no_mine = 0
                else:
                    no_mine += 1
                    
                twod[r][c] = min(no_mine, twod[r][c])
            
            # reverse
            no_mine = 0
            for r in range(N-1, -1, -1):
                if (r, c) in mineLoc:
                    no_mine = 0
                else:
                    no_mine += 1
                    
                twod[r][c] = min(no_mine, twod[r][c])
                big = max(big, twod[r][c])
        
        return big
