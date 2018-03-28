# Davis recursion staircase, outline of the problem is, we have stairs which could be climbed at 1, 2 or 3 steps a time. Number of ways to climb the stairs given the height of the stair case.

# Think about the possible scenarios with all 1s, 2s and 3s and combinations of the same further. Possibly factorial of something?.....
# A better thought and hint from the question would be to use recursion as well as memoizing using a dictionary
# * Recursing the values upto 0 and memoization would help
# * perform recursion with n-1 + n-2 + n-3 to arrive at the final result

way = {}
def ways(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    elif n in way:
        return way[n]
    else:
        result = ways(n-1) + ways(n-2) + ways(n-3)
        way[n] = result
        return result

s = int(raw_input().strip())
for a0 in xrange(s):
    n = int(raw_input().strip())
    print ways(n)
    
    
    

