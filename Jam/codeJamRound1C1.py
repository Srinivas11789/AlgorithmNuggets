# Rock, Paper, Scissors Game
# * Make the Robot win against all the oponents
#   - R Wins S losses P
#   - P Wins R losses S
#   - S Wins P losses R
# No Matter How the Numbers are assigned? Means you should win all the oponents individually!!!!

# In order to win what you require
win = {
    "S": "R",
    "P": "S",
    "R": "P"
}

def match(o1, o2):
    for i, j in zip(o1, o2):
        if i == j:
            continue
        else:
            if win[j] == i:
                return o1
            else:
                return o2

# Function to create the winning program
def win_match(program, winner):
    # Find all the winning combinations...
    if program in each_win:
        return winner

    # the first win move
    #each_win[program].append(win[program[0]])
    
    # Other possibilities
    if len(each_win.keys()) == 0:
        each_win[program] = []
        n = len(program)
        for i in range(n+1):
            if i < n:
                possible = program[:i] + win[program[i]]
                each_win[program].append(possible)
            else:
                possible = program[:i] + win[program[0]]
                each_win[program].append(possible)
    
    if winner == "":
        return each_win[program]
    else:
        if type(winner) == list:
            for winp in each_win:
                for w in each_win[winp]:
                    #print w, program
                    if match(w, program) == w:
                            return w
        else:
            if len(winner) >= len(program) and match(winner, program) != winner:
                return None
            elif len(winner) < len(program):
                return winner+win[program[len(winner)]]
            else:
                return winner

# Test cases handle
tcs = raw_input()
for i in range(int(tcs)):
    Oponents = int(raw_input())
    winning_combination = ""
    fail = 0
    # Record win program of each oponent program
    each_win = {}
    for j in range(Oponents):
        Program = raw_input()
        if fail == 0:
            winning_combination = win_match(Program, winning_combination)
            if not winning_combination:
                fail = 1
    #print winning_combination, each_win
    if fail == 1:
        print "Case #"+str(i+1)+": "+"IMPOSSIBLE"
    else:
        if type(winning_combination) == list:
            winning_combination = winning_combination[0]
        print "Case #"+str(i+1)+": "+winning_combination
 


