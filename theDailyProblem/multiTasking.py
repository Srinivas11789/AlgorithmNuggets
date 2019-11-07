"""
We have a list of tasks to perform, with a cooldown period. We can do multiple of these at the same time, but we cannot run the same task simultaneously.

Given a list of tasks, find how long it will take to complete the tasks in the order they are input.
tasks = [1, 1, 2, 1]
cooldown = 2
output: 7 (order is 1 _ _ 1 2 _ 1)
def findTime(arr, cooldown):
  # Fill this in.

print findTime([1, 1, 2, 1], 2)
# 7
"""

def findTime(arr, cooldown):
  time = 0
  tasks = set()
  while arr:
    if arr[0] not in tasks:
      tasks.add(arr.pop(0))
    else:
      time += len(tasks) + abs(len(tasks)-1-cooldown)
      print(tasks, time)
      tasks = set()    
  return time+len(tasks)

print findTime([1, 1, 2, 1], 2)
