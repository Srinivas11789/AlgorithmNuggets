"""
# make Palindorme program - thought and tried around for 1 hours but later was able to solve in 5 mins
* Tips:
- Be ready to erase away the logic and try writing again instead of iterating over the same same logic or loop. Keep making random or greater changes to innovate new logic
- Have each structured steps of the problem in mind and solve each case
- Burn down the problem into the fundamentals and solve from there
- clearly implement the logic of each step as you proceed with the problem
- understand the problem, think clear, implement logic, change logic and iterate...
"""
#!/bin/python

import sys

def isPalin(s):
    if s == s[::-1]:
        return True
    else:
        return False

def theLoveLetterMystery(s):
    
    n = len(s)
    s = list(s)
    count = 0
    
    for i in range(n):
        
        while s[i] != s[-i-1]:
            
            if ord(s[i]) > ord(s[-i-1]):
                select = ord(s[i])
                ind = i
            else:
                select = ord(s[-i-1])
                ind = -i-1+n
            
            if select > 97:
                s[ind] = chr(ord(s[ind])-1)
                count += 1
                
    if isPalin(s):
        return count
    else:
        return -1

q = int(raw_input().strip())
for a0 in xrange(q):
    s = raw_input().strip()
    result = theLoveLetterMystery(s)
    print(result)


