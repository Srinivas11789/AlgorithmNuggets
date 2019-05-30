class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        
        # Logic 1: O(4n)
	# * Execute the directions in order and check if origin is reached
        # * Increment the number of times to execute the instructions. Got pass in 4
        # * Reference: https://leetcode.com/problems/robot-bounded-in-circle/discuss/300372/python-4*instructions-O(n) 

        # Convert Instructions to some number of times until reaches the origin, this can be infinite or some even count
        instructions += instructions*3
            
        # Directions 
        # * based on the face -> L,R of each
        directions = {
            "N": ['W', 'E'],
            "S": ['E', 'W'],
            "E": ['N', 'S'],
            "W": ['S', 'N']
        }
        
        # Facing direction
        face = "N"
        
        # Current co-ordinate
        x, y = 0, 0
        
        # One Full Loop of the Instructions
        
        # Intructions iteration
        for ins in instructions:
            # Set face based on the directions
            if ins == "L":
                face = directions[face][0]
            elif ins == "R":
                face = directions[face][1]
            else:
                # G --> movement in the particular direction of face
                if face == "N":
                    y += 1
                elif face == "S":
                    y -= 1
                elif face == "E":
                    x += 1
                else:
                    x -= 1
        
        if x == 0 and y == 0:
            return True
        else:
            return False
        
        
                
                
        
                
        
    
