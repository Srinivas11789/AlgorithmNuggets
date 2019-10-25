# Naive add/sub with 2 pointers
  
def isEven0(num):
    if num%2 == 0:
        for i in list(str(num).strip()):
            if int(i)%2 != 0:
                return False
        return True
    else:
        return False

def uniqCalc(N):
    step = 0
    
    if N%2 != 0:
        step += 1
    
    while not isEven0(N-step) and not isEven0(N+step):
        #print N+left, N+right, isEven(N+left), isEven(N+right)
        step += 2
    
    return step

testcases = input()
for i in range(testcases):
    num = input()
    print "Case #"+str(i+1)+": "+str(uniqCalc(num))

