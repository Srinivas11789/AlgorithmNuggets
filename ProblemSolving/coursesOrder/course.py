# Courses Selection

### Given as input:
# all_courses = ['A','DS','NLP','CS']
# pre_req = [['CS','A'],['A','DS'],['CS','NLP']]

def coursePlan(all_courses, pre_req):
    
    # Create a dictionary of the pre-req relation
    prereq = {}
    for item in pre_req:
        if item[0] not in prereq:
           prereq[item[0]] = []
        prereq[item[0]].append(item[1])

    result = []
    for course in all_courses:
        if course in prereq:
                for d in prereq[course]:
                        if d not in all_courses:
                             return []
                        temp = d
                        k = 0
                        if d in prereq:
                           while k == 0:
                                 if course in prereq[temp]:
                                    return []
                                 for z in prereq[temp]:
                                    if z in prereq:
                                       if course in prereq[z]:
                                    	  return []
                                 
                	if d not in result:
				result.append(d)
        if course not in result:
        	result.append(course)

    return result

def main():

    # General usecase
    #all_courses = ['A','DS','NLP','CS']
    #pre_req = [['CS','A'],['A','DS'],['CS','NLP']]

    # Negative testcase when the courses cannot be selected
    #all_courses = ['A','DS','NLP','CS']
    #pre_req = [['CS','A'],['A','DS'],['CS','A2']]

    # Circular dependancy
    #all_courses = ['A','DS','NLP','CS']
    #pre_req = [['CS','A'],['A','CS'],['CS','NLP']]

    # Circular dependancy - round about
    all_courses = ['A','DS','NLP','CS']
    pre_req = [['CS','A'],['A','NLP'],['NLP','CS']]

    # Multiple dependancy testcase

    # Boundary cases - empty array cases

    # Single course with all the dependancy

    # 
    print coursePlan(all_courses, pre_req)

main()


