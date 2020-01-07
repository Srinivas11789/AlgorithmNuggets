class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        
        # Logic 1: Sort + Dictionary to store schedule - 100 pass - 95% faster 
        def meeting_rooms(meetings):
            schedule = {}
            meetings.sort()
            for meet in meetings:
                    if schedule:
                        room = 1
                        while room in schedule and schedule[room][1] > meet[0]:
                            room += 1
                        schedule[room] = meet
                    else:
                        schedule[1] = meet
            return len(schedule.keys())
        return meeting_rooms(intervals)
        
        # Optimize can you do without sorting...?
