class Solution:
    def punishmentNumber(self, n: int) -> int:
        
        def findPunishNum(square, integer, result): 
            #print(square, integer, result)   
            tens = 0
            test = square
            while test >= 10:
                test = test//10
                tens += 1

            if square+result == integer:
                return True

            if tens == 0:
                if integer == square: # single digit multiplier case
                    return True
                if square+result == integer:
                    return True
            
            for m in range(1, tens+1):
                m = 10**m
                if findPunishNum(square//m, integer, result + square%m):
                    return True
            
            return False

        ans = 0
        for i in range(1, n+1):
            sq = i*i
            if findPunishNum(sq, i, 0):
                print(i)
                ans += sq
        #print(findPunishNum(25, 5, 0))

        return ans
