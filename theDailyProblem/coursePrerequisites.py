"""
You are given a hash table where the key is a course code, and the value is a list of all the course codes that are prerequisites for the key. Return a valid ordering in which we can complete the courses. If no such ordering exists, return NULL.

Example:
{
  'CSC300': ['CSC100', 'CSC200'], 
  'CSC200': ['CSC100'], 
  'CSC100': []
}

This input should return the order that we need to take these courses:
 ['CSC100', 'CSC200', 'CSCS300']

Here's your starting point:

def courses_to_take(course_to_prereqs):
  # Fill this in.

courses = {
  'CSC300': ['CSC100', 'CSC200'], 
  'CSC200': ['CSC100'], 
  'CSC100': []
}
print courses_to_take(courses)
# ['CSC100', 'CSC200', 'CSC300']
"""

courses = {
  'CSC300': ['CSC100', 'CSC200'],
  'CSC200': ['CSC100'],
  'CSC100': []
}

# This is a recursive thing
# * Return when the course pre-req is empty
# * Recurse when the course pre-req is not empty
def order_of_courses_to_take(subject, order):
        if courses[subject]:
            for prereq in courses[subject]:
                order_of_courses_to_take(prereq, order)
        if subject not in order:
            order.append(subject)
        return

order = []
result = []
for key in courses:
     order_of_courses_to_take(key, order)
     if len(order) == len(courses.keys()):
        result = order
print(order)        
