class Solution(object):
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        
        # Logic2: 
        # * Have a direction logic - to decide on facing direction
        # * Obstacle detecting logic
        
        # Initial origin where the robot would start from
        x = 0 
        y = 0
        
        # Direction logic
        # Facing +y direction initially (Initial direction along the +y axis)
        facing_direction = "y"
        
        # Go through each command 
        for com in commands:
            # Direction logic
            # Move only when it is not left or right turn else update last turn
            if com == -1 or com == -2:
                if facing_direction == "y":
                    if com == -1:
                        facing_direction = "x"
                    elif com == -2:
                        facing_direction = "-x"
                elif facing_direction == "-y":
                    if com == -1:
                        facing_direction = "-x"
                    elif com == -2:
                        facing_direction = "x"
                elif facing_direction == "x":
                    if com == -1:
                        facing_direction = "-y"
                    elif com == -2:
                        facing_direction = "y"
                else:
                    if com == -1:
                        facing_direction = "y"
                    elif com == -2:
                        facing_direction = "-y"       
            else:
                # Robot starts moving in particular direction from last turn
                for i in range(com):
                    # Increment movement
                    if "x" in facing_direction:
                        if "-" in facing_direction:
                            x -= 1
                        else:
                            x += 1
                    else:
                        if "-" in facing_direction:
                            y -= 1
                        else:
                            y += 1
                
                    # While the robot is moving check for obstacles on the way
                    if [x, y] in obstacles:
                        if "x" in facing_direction:
                            if "-" in facing_direction:
                                x += 1
                            else:
                                x -= 1
                        else:
                            if "-" in facing_direction:
                                y += 1
                            else:
                                y -= 1
                        break
            print x,y            
        return x**2 + y**2
        
        # Logic1: Image a x-y axis graph with 4 quadrants, start at 0,0 (maintain x and y as we proceed), stop at obstacle and continue with the next step
        """
        # Initial origin where the robot would start from
        x = 0 
        y = 0
        
        # This logic fails when all the quadrants are exercised, changing
        # direction keys as a dictionary for reference (given data from question)
        # x,y|-x,-y|x,-y|-x,y ==> select x,y
        direction = {
            -1:x, # right --> x
            -2:y, # left --> y
        }

        # Track the last direction turn made
        last_turn = -2
        
        # Go through each command 
        for com in commands:
            # Move only when it is not left or right turn else update last turn
            if com in direction.keys():
                last_turn = com
            else:
                # Robot starts moving in particular direction from last turn
                for i in range(com):
                    direction[last_turn] += 1
                    # While the robot is moving check for obstacles on the way
                    if [direction[-1], direction[-2]] in obstacles:
                        direction[last_turn] -= 1
                        break
                print direction[-1], direction[-2]
        return direction[-1]**2 + direction[-2]**2
        """
