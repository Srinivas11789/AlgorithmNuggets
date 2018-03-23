# Codility Problem - MinPerimeterOfRectangle
# 
def solution(N):

    current = 1
    # One testcase for a 9 digit prime number kept failing again and again, the mini to be set high passed the case.
    # Set the mini or max to as high as possible to escape corner cases
    mini = 60000000000
    sumi = 0

    #### Test for simple testcases: 60 to 80 percent pass
    #### * Test for N=1, which is a simple one that failed
    #### * Test for N=36, which is a square number to be checked
    #### Corner cases were sqaure numbers obviously and small numbers
    ## N=1 throws 1200000 which is wrong, correct it
    ## while loop should inclide square numbers "="

    # Setting the while condition to <= N passes both the above scenarios    
   #if N==1:
   #     return 2*(1+1) 

    ### Last testcase fails are for large prime numbers 

    while current * current <= N:
         if N%current == 0:
             #print(current)
             if current * current == N:
                 sumi = current*2
             else:
                 sumi = current + N//current
         if sumi < mini:
            mini = sumi
         current += 1
    return mini*2

# diffreernce between 2 factors should be less
