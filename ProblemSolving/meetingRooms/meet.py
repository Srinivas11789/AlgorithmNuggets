class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # Logic 1: Sort by start times and O(N) iteration over intrevals to find if they overlap --> 68.84% faster
        """
        meetings = sorted(intervals, key= lambda x: x[0]) # sort by start times
        for i in range(1, len(meetings)):
            previous = meetings[i-1]
            if meetings[i][0] < previous[1]: # meeting starts while the previous meeting ongoing
                return False
        return True
        """
    
        # Logic 2: Bruteforce to find the overlap O(N2)
