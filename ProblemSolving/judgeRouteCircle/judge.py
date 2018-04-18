### Nice thinking :- Implement algorithm in relation to how you understand and how your brain thinks!!!!!!!
### So you want to start at a reference point say (0,0) and then use 2d co-ordinate system to travel up, down, left, right with (+1 -1) logic 
class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        pos = [0,0]
        for move in moves:
            if move == "U":
                pos[1] += 1
            elif move == "D":
                pos[1] -= 1
            elif move == "L":
                pos[0] -= 1
            elif move == "R":
                pos[0] += 1
        
        if pos[0] == 0 and pos[1] == 0:
            return True
        else:
            return False
        
        
