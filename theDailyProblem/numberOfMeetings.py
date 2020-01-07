"""
Given a list of meetings that will happen during a day, find the minimum number of meeting rooms that can fit all meetings.

Each meeting will be represented by a tuple of (start_time, end_time), where both start_time and end_time will be represented by an integer to indicate the time. start_time will be inclusive, and end_time will be exclusive, meaning a meeting of (0, 10) and (10, 20) will only require 1 meeting room.

Here's some examples and some starting code:

def meeting_rooms(meetings):
  # Fill this in.

# print 1
print(meeting_rooms([(0, 10), (10, 20)]))
# 1

print(meeting_rooms([(20, 30), (10, 21), (0, 50)]))
# 3 (all meetings overlap at time 20)
"""

# Logic 2:
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

"""
# Logic 1: Naive try works for the cases below but fails in leetcode. So new logic above
def meeting_rooms(meetings):
  schedule = {}
  rooms = 0
  for meet in meetings:
      booked = False
      if rooms:
        for room in range(1, rooms+1):
          last_meeting = schedule[room]
          if last_meeting[1] > meet[0]:
            rooms += 1
            schedule[rooms] = meet
            booked = True
          else:
            schedule[rooms] = meet
            booked = True
          if booked:
            break
      else:
        rooms += 1
        schedule[rooms] = meet
      print(schedule)
  return rooms
"""

# print 1
print(meeting_rooms([(0, 10), (10, 20)]))
# 1

print(meeting_rooms([(20, 30), (10, 21), (0, 50)]))
# 3 (all meetings overlap at time 20)
