# Naive add/sub with 2 pointers
  
def isEven(num):
    for i in list(str(num).strip()):
        if int(i)%2 != 0:
            return False
    return True

def uniqCalc(N):
    left = right = 0
    
    while not isEven(N-left) and not isEven(N+right):
        #print N+left, N+right, isEven(N+left), isEven(N+right)
        left += 1
        right += 1
    
    if isEven(N-left):
        return left
    else:
        return right

testcases = input()
for i in range(testcases):
    num = input()
    print "Case #"+str(i+1)+": "+str(uniqCalc(num))

