# Clear your mind and look at all the possibilities of conditions that could occur.
# The code below shows you are already confused or brain fried
# Clear your mind take a deep breath and think about the problem then approach it
# Again, read the instructions clearly

# Enter your code here. Read input from STDIN. Print output to STDOUT
def getFine(rdate, edate):
    if rdate[2] < edate[2]:
        return 0
    elif rdate[1] < edate[1] and rdate[2] == edate[2]:
        #if rdate[1] < edate[1]: print "yay"
        return 0
    elif rdate[0] <= edate[0] and rdate[1] == edate[1] and rdate[2] == edate[2]:
        return 0
    elif rdate[2] > edate[2]:
        return 10000
    elif rdate[1] > edate[1] and rdate[2] == rdate[2]:
        #print int(rdate[1]) - int(edate[1])
        return 500 * (int(rdate[1]) - int(edate[1]))
    else:
        return 15 * (int(rdate[0]) - int(edate[0]))
                                             
returned_date = [int(i) for i in str(raw_input().strip()).split(" ")]
expected_date = [int(i) for i in str(raw_input().strip()).split(" ")]
print getFine(returned_date, expected_date )
"""
# Returned by valid date
#if returned_date[2] <= expected_date[2] or returned_date[1] <= expected_date[1] or returned_date[0] <= expected_date[0]:
#    print 0  
if tuple(returned_date) <= tuple(expected_date):
    print 0
# Number of years comparison
elif returned_date[2] > expected_date[2]:
    print 10000
elif returned_date[1] > expected_date[1]:
    print 500 * (int(returned_date[1])-int(expected_date[1]))
# Returned by number of days
else:# returned_date[0] > expected_date[0]:
    print 15 * (int(returned_date[0])-int(expected_date[0]))
"""
"""
# Returned by valid date
if returned_date <= expected_date:
    print 0
# Returned by number of days
rdays = returned_date[0]
edays = expected_date[0]
if returned_date[1:] == expected_date[1:]:
    print 15 * (int(rdays)-int(edays))
# Returned by number of months
rmonths = returned_date[1]
emonths = expected_date[1]
if returned_date[1:] != expected_date[1:]:
    print 500 * (int(rmonths)-int(emonths))
# Number of years comparison
if returned_date[2] != expected_date[2]:
    print 10000
"""
"""
value = 0
# DAYS LOGIC
if returned_date[2] == expected_date[2] and returned_date[1] == expected_date[1]:
    value = (int(returned_date[0])-int(expected_date[0]))
    if value < 0:
        value = 0
    else:
        value = value * 15
elif returned_date[2] == expected_date[2] and returned_date[1] != expected_date[1]:
    months = returned_date[1] - expected_date[1]
    if months < 0:
        value = 0
    else:
        value = 500 * months
else:
    value = 10000
print value
    
### Diff logic
days  = int(returned_date[0])-int(expected_date[0])
months = ((int(returned_date[1])-int(expected_date[1])))
years = ((int(returned_date[2])-int(expected_date[2])))*
days = days+months+years
value = days * 15
print value
"""

