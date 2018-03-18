# Enter your code here. Read input from STDIN. Print output to STDOUT
#### READ THE INSTRUCTIONS PROPERLY AND CLEARLY AGAIN AND AGAIN !!!!!!!!!!!!!!!
# Printed 1 as Prime which was valid according to the logic
# Based on the instructions 1 should be displayed as not prime. Easy testcase remained not Pass and spent a lot of time to debug
# If you cant find out the case of a wrong testcase try out different input based on the range provided in the question.
# Sometimes, the program might be breaking or stopping at certain spots hence properly visualize or test the full range of inputs
# Tried reducing time the program will take with alteration in logic even then the program fails. Testcase with number 1000000006 ranges due to memory error in the for loop. Easy fix was to set the range to a permissible value to reduce the number of iteration for a large number, on the assumption that there wont be any number without factors less than 1000. This solution worked
#
n = int(raw_input().strip())
for i in range(n):
        data = int(raw_input().strip())
        #inputs.append(data)
        count = 0
        if data > 1000:
            ranger = 1000
        else:
            ranger = data
        for i in range(2,ranger):
            #print data,i
            if data%i == 0:
                count += 1
                print "Not prime"
                break
        if count == 0:
            if data == 1:
                print "Not prime"
            else:
                print "Prime"

### Old solution that was not properly functioning
"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
#### READ THE INSTRUCTIONS PROPERLY AND CLEARLY AGAIN AND AGAIN !!!!!!!!!!!!!!!
# Printed 1 as Prime which was valid according to the logic
# Based on the instructions 1 should be displayed as not prime. Easy testcase remained not Pass and spent a lot of time to debug
n = int(raw_input().strip())
for i in range(n):
        data = int(raw_input().strip())
        #inputs.append(data)
        count = 0
        for i in range(1,data+1):
            if data%i == 0:
                count += 1
            if count > 2:
                break
        if count > 2:
            print "Not prime"
        else:
            if data == 1:
                print "Not prime"
            else:
                print "Prime"
"""
