def solve_maze(grid, lydia_movement):
    path = (0,0)
    lydia = [(0,0)]
    me = "E" if lydia_movement[0] == "S" else "S" 
    for direction in lydia_movement[1:]:
        if direction == "E":
            lydia.append((lydia[-1][0]+1, lydia[-1][1]))
            me += "S"
        else:
            lydia.append((lydia[-1][0], lydia[-1][1]+1))
            me += "E"
    return me

tcs = input()
for i in range(int(tcs)):
    grid = input()
    lydia_movement = raw_input()
    print "Case #"+str(i+1)+": "+solve_maze(grid, lydia_movement)