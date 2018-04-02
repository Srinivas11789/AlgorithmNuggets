#!/bin/python

import sys

def counterGame(n):

    # Simple bit manipulation hacker rank solution - from discussions
    # Count the number of ones in the value n-1 and reduce the value to 0 or 1 based on the count
    
    # Debug
    # print bin(n-1).count("1"), n, bin(n-1).count("1")%2
    
    players = "Richard", "Louise"
    # Based on awesome solution from AbhishekVermaIIT
    return (players[bin(n-1).count("1")%2])
    
    """
    # Type 2
    # Debug 
    print bin(n-1)[2:]
    test = sum(b=='1' for b in bin(input()-1)[2:])
    print test
    for i in range(n):
        value = sum(bit=='1' for bit in bin(n-1)[2:])
    if value&1:
        print "Louise"
    else:
        print "Richard"
    """

    """
    # Runtime Error
    # Power of two function
    def powerOf2(n):    
        count = 0
        while n%2 == 0:
            n = n//2
            count += 1
        if n == 1:
            return ["True", count]
        else:
            return ["False", 0]
    
    # Game function
    def game(n):
        if powerOf2(n)[0] == "True":
            return n//2
        else:
            # Memory error when large numbers occur hence fails. 
            # 5
            # 1560834904
            # 1768820483
            # 1533726144
            # 1620434450
            # 1463674015
            
            for i in range(n,1,-1):
                result = powerOf2(i)
                if result[0] == "True":
                    return result[1]

    # Turns
    i = 0
    while n > 1:
        i = i + 1
        #print n
        n = game(n)
    
    if i%2 == 0:
        return "Richard"
    else:
        return "Louise"
    
    """

if __name__ == "__main__":
    t = int(raw_input().strip())
    for a0 in xrange(t):
        n = long(raw_input().strip())
        result = counterGame(n)
        print result


