class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        
        goat = []
        onemiss = []

        matchesPerPlayer = {}
        resultsPerPlayer = {}

        for match in matches:
            winner = match[0]
            loser = match[1]
            
            for player in [winner, loser]:
                if player not in matchesPerPlayer:
                    matchesPerPlayer[player] = 0
                if player not in resultsPerPlayer:
                    resultsPerPlayer[player] = 0

                matchesPerPlayer[player] += 1

            resultsPerPlayer[winner] += 1
            resultsPerPlayer[loser] -= 1

        for p in sorted(matchesPerPlayer.keys()):
            #print(p, matchesPerPlayer[p], resultsPerPlayer[p])
            if matchesPerPlayer[p] == resultsPerPlayer[p]:
                goat.append(p)
            if (matchesPerPlayer[p] - resultsPerPlayer[p]) == 2:
                onemiss.append(p)

        return [goat, onemiss]
