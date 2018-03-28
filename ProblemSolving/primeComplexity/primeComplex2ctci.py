# Works fine, but last last few cases with wrong and runtime errors - Optimized with break as soon as count increases
# * Check the question for ranges supported? only positive ranges of n, try large numbers which would increase runtime
# * Lesson:  check for possible anamolies, instead of worrying about the larger number, check for a smaller number with discrepancies like 1 or 2 - provide range(1<=n<=2 power n)
#
import math
p = int(raw_input().strip())
for _ in xrange(p):
    n = int(raw_input().strip())
    count = 0
    # Last digit check to optimize further
    #print str(n)[-1]
    if n > 9 and str(n)[-1] not in ["1","3","7","9"]:
        print "Not prime"
    elif n == 2:
        print "Prime"
    elif n == 1:
        print "Not prime"
    # One testcase was dependant on this condition wherein some multiple of 3 fail above condition
    elif n%2 == 0 or n%3 == 0:
        print "Not prime"
    else:
        # Eliminating all even numbers list as no even number is prime except 2
        # Taking till the square root of a number will pass the case, sqrt +1 to include the resp sqrt number as well. Convert to int explicit
        for i in range(3,int(math.sqrt(n)+1),2):
            if n%i == 0:
                count += 1
                if count > 0:
                    print "Not prime" 
                    break
        if count == 0:
            print "Prime"

