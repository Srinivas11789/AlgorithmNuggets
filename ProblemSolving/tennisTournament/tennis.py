# Codility Problem - tennisTournament - 100 percent

def solution(P, C):
    game = 0
    if P%2 == 0:
        game = P//2
    else:
        P = P-1
        game = P//2
    #print(game,C)
    if game == C or game < C:
        return game
    else:
        return C

        
    
