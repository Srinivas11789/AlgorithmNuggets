# Courses Selection

### Problem:
# Given a list of courses and corresponding dependancies, print out the list of courses in order to be taken.
# If the courses cannot be ordered, return empty list []

### Given as input:
# all_courses = ['A','DS','NLP','CS']
# pre_req = [['CS','A'],['A','DS'],['CS','NLP']]

### Output:
# list of ordered courses or empty list

### Method 1 - Create a dependancies list and build a new results array from the dependancy list
# Function to order the courses
def coursePlan(all_courses, pre_req):
    
    # Create a dictionary of the pre-req relation - data structure to maintain relationship
    prereq = {}

    # Construct a data structure of relation between the pre-req and the courses
    for item in pre_req:
        if item[0] not in prereq:
           prereq[item[0]] = []
        prereq[item[0]].append(item[1])

    # Results or output array
    result = []
 
    # Courses addition into the result array with dependancies - each course at a time
    for course in all_courses:

	# Dependancies for courses
        if course in prereq:
                
	 	# All the dependancies of a course into a list, digs deeper iteratively to produce a list
                # temp to hold the variations for each course without data structure altering
                temp = prereq[course]

                # Loop decision params
                prev = 0
                new = len(temp)

                # each item in temp array holding all dependancies
                for item in temp:
                      
                      # loop control when no change in the array - exhaustion of dependancy
                      if new == prev: 
                         break
                      prev = len(temp)
                      
                      # Circular dependancy check 
                      if course in temp: 
                         return []
                      
		      # dependancies addition	
                      if item in prereq:
                         temp.extend(prereq[item])
                      new = len(temp)

                # Add courses into the result list
                for d in temp[::-1]:

                        # Dependancy not present at all
                        if d not in all_courses:
                             return []

		        # append the course after resolving dependancy or with no dependancy
                	if d not in result:
				result.append(d)
              
                # append the course to the array when not present already
                if course not in result:
                	result.append(course)

        # if the course has no dependancy append it to the list
        else:# 
                if course not in result:
        	   result.append(course)

    return result

### Method 2 - Perform a insertion sort kind of logic of shifting the array for each course addition

def main():

    # General usecase
    all_courses = ['A','DS','NLP','CS']
    pre_req = [['CS','A'],['A','DS'],['CS','NLP']]
    # Expecting = ['DS','A','NLP','CS']
    print "General or main use-case: "+str(coursePlan(all_courses, pre_req))

    # Negative testcase when the courses cannot be selected
    all_courses = ['A','DS','NLP','CS']
    pre_req = [['CS','A'],['A','DS'],['CS','A2']]
    # Expecting = []
    print "Negative use-case: "+str(coursePlan(all_courses, pre_req))

    # Circular dependancy - one level
    all_courses = ['A','DS','NLP','CS']
    pre_req = [['CS','A'],['A','CS'],['CS','NLP']]
    # Expecting = []
    print "One level use-case: "+str(coursePlan(all_courses, pre_req))

    # Circular dependancy - two level
    all_courses = ['A','DS','NLP','CS']
    pre_req = [['CS','A'],['A','NLP'],['NLP','CS']]
    # Expecting = []
    print "Third level: "+str(coursePlan(all_courses, pre_req))

    # Circular dependancy - third level
    all_courses = ['A','DS','NLP','CS','DF']
    pre_req = [['CS','A'],['A','NLP'],['NLP','DF'],['DF','CS']]
    # Expecting = []
    print "Third level: "+str(coursePlan(all_courses, pre_req))
 
    # Circular dependancy - more than 5 level
    all_courses = ['A','DS','NLP','CS','DF','AS','OS','IS']
    pre_req = [['CS','A'],['A','NLP'],['NLP','DF'],['DF','AS'],['OS','AS'],['IS','AS'],['AS','CS']]
    # Expecting = []
    print "Five level: "+str(coursePlan(all_courses, pre_req))

    # Multiple dependancy testcase
    all_courses = ['A','DS','NLP','CS','DF','AS','OS','IS']
    pre_req = [['CS','A'],['A','NLP'],['NLP','DF'],['DF','AS'],['OS','AS'],['IS','AS']]
    # Expecting - AS, DF, NLP, A, DS, CS, OS, IS
    print "Multiple dependancy testcase: "+str(coursePlan(all_courses, pre_req))

    # Boundary cases - empty array cases
    all_courses = []
    pre_req = [['CS','A']]
    # Expecting = []
    print "Boundary testcase1: "+str(coursePlan(all_courses, pre_req))
      
    all_courses = ['CS','A','NLP']
    pre_req = []
    # Expecting = CS, A, NLP
    print "Boundary testcase2: "+str(coursePlan(all_courses, pre_req))

    # Single course with all the dependancy
    all_courses = ['A','NLP','ML','A2','DS','AI','CS','AS']
    pre_req = [['ML','A2'],['ML','DS'],['ML','AI']]
    # Expecting = A, NLP, A2, DS, AI, ML, CS, AS
    print "Single course with dependancy at middle: "+str(coursePlan(all_courses, pre_req))
  
    # Single course with all dependancies occuring first in the list
    all_courses = ['A','NLP','A2','AI','ML']
    pre_req = [['ML','A'],['ML','NLP'],['ML','AI'],['ML','A2']]
    # Expecting = A, NLP, AI, A2, ML
    print "Single course with dependancy at last: "+str(coursePlan(all_courses, pre_req))
    
    # Single course with all dependancies occuring last in the list
    all_courses = ['ML','NLP','A2','AI','A']
    pre_req = [['ML','A'],['ML','NLP'],['ML','AI'],['ML','A2']]
    # Expecting = A, NLP, AI, A2, ML
    print "Single course with dependancy at first: "+str(coursePlan(all_courses, pre_req))
	
main()

"""
# Output:
Srinivass-MacBook-Pro:ProblemSolving darkknight$ python coursesOrder/course.py 
General or main use-case: ['DS', 'A', 'NLP', 'CS']
Negative use-case: []
One level use-case: []
Third level: []
Third level: []
Five level: []
Multiple dependancy testcase: ['AS', 'DF', 'NLP', 'A', 'DS', 'CS', 'OS', 'IS']
Boundary testcase1: []
Boundary testcase2: ['CS', 'A', 'NLP']
Single course with dependancy at middle: ['A', 'NLP', 'AI', 'DS', 'A2', 'ML', 'CS', 'AS']
Single course with dependancy at last: ['A', 'NLP', 'A2', 'AI', 'ML']
Single course with dependancy at first: ['A2', 'AI', 'NLP', 'A', 'ML']
"""
