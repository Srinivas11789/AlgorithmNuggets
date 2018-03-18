# Enter your code here. Read input from STDIN. Print output to STDOUT
class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        
    def __repr__(self):
        return self.__class__
        
    def comparator(a, b):
        if a.score < b.score:
            return 1
        elif a.score == b.score:
            if a.name > b.name:
                return 1
            else:
                return -1 
        else:
            return -1 
        
n = int(raw_input())
data = []
for i in range(n):
    name, score = raw_input().split()
    score = int(score)
    player = Player(name, score)
    data.append(player)
    
data = sorted(data, cmp=Player.comparator)
for i in data:
    print i.name, i.score
