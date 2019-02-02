class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        
        # Logic 1: Graph method would be feasible to solve this problem
        # * Also, recusive approach first
		# * (No extra space other than the recurse stack)
        
        def enter_all_rooms(room_num):
            
            # To maintain a visited list of rooms, conver the entry of visited rooms to 0
            if rooms[room_num] != 0:
                current = rooms[room_num]
                rooms[room_num] = 0
        
                # Take the keys in each room and open other rooms
                for key in current:
                    enter_all_rooms(key)
        
        # Room 0 is free to enter
        enter_all_rooms(0)

        # If all the rooms are 0 then they are all visited else false
        if rooms.count(0) == len(rooms):
            return True
        else:
            return False
