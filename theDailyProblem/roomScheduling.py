"""
You are given an array of tuples (start, end) representing time intervals for lectures. The intervals may be overlapping. Return the number of rooms that are required.

For example. [(30, 75), (0, 50), (60, 150)] should return 2.
"""

# Recon
# * When overlap occurs we need another room, else we use the same room

def rooms(schedule):
    
    # Logic 1: Naive method
    # * Sort the schedule with start times as reference
    # * Maintain a rooms dictionary to know what class is going on that room
    # * Iterate tuples and see if there is a overlap, if overlap occurs create a room in rooms dictionary and add current class

    # Room dictionary 
    rooms = {}

    # Sort the schedule with respect to the start time
    schedule.sort()

    # First room allocated
    rooms[1] = schedule[0]

    # Iterate other rooms 
    for i in range(1, len(schedule)):
        # current Start and End time
        start = schedule[i][0]
        end = schedule[i][1]
        # Sentinel for identifying if room is allocated
        got_room = False
        # Iterate the rooms dictionary to find free slots
        for room in rooms.keys():
            # If there is a conflict move to next room
            if start < rooms[room][1]:
                pass
            else:
                # If there is no conflict get the room and leave
                rooms[room] = (start, end)
                got_room = True
                break
        # If we dont get any room yet ( conflicts ), create a new room
        if not got_room:
            rooms[len(rooms.keys())+1] = (start, end)
        #print(rooms)
    return len(rooms.keys())


def main():
    schedule = [(30, 75), (0, 50), (60, 150)]
    print(rooms(schedule))

main()