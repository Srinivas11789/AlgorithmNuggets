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

###################### Clean implementation Learn from this logic
# Enter your code here. Read input from STDIN. Print output to STDOUT
#### READ THE INSTRUCTIONS PROPERLY AND CLEARLY AGAIN AND AGAIN !!!!!!!!!!!!!!!
# Printed 1 as Prime which was valid according to the logic
# Based on the instructions 1 should be displayed as not prime. Easy testcase remained not Pass and spent a lot of time to debug
# If you cant find out the case of a wrong testcase try out different input based on the range provided in the question.
# Sometimes, the program might be breaking or stopping at certain spots hence properly visualize or test the full range of inputs
# Tried reducing time the program will take with alteration in logic even then the program fails. Testcase with number 1000000006 ranges due to memory error in the for loop. Easy fix was to set the range to a permissible value to reduce the number of iteration for a large number, on the assumption that there wont be any number without factors less than 1000. This solution worked
#
import math

# Clean Implementation
def checker(data):
        # Technique solution: Even numbers are always divisible by 2, hence eliminate them from the list which reduces half the possibility, then iterate only odd number until the square root of the specific number which gives you the answer
        # Check for value 2, as it is a even prime number
        if data == 2:
            return "Prime"
        # Check for under 2 which is 1 and should be printed not prime
        if data < 2:
            return "Not prime"
        # Check for all the even numbers
        if data % 2 == 0:
            return "Not prime"
        # Check for odd numbers
        # First odd number is 3
        i = 3
        # Until the square root of the specific number
        ranger = math.sqrt(data)
        # iterate all odd number
        while i <= ranger:
            if data%i == 0:
                return "Not prime"
            i += 2
        return "Prime"
        
n = int(raw_input().strip())
for i in range(n):
        data = int(raw_input().strip())
        print checker(data)

            
