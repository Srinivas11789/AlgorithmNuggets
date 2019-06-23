# Dynamic Programming
## * Problem solved by dividing into sub-problems which are dependent and reused to create the solution

# Example: Fibonacci - sum of last 2 digits form the third digit

# Recursion Method
## * Essence of divide and conquer a problem with subproblems to obtain the solution

def fibonacci(n):
    if n == 0:
       return 0
    elif n == 1:
       return 1
    else:
       return fibonacci(n-1) + fibonacci(n-2)

# Top Down Approach - Memoization
## * Create a table to store sub-problem solutions that can be reused
## * On-demand storing of sub-problem that only need to be reused
## * First lookup the table for sub-problem solution then calculate

memo = [0, 1]
def fibonacci_top(n):
   
    if n < len(memo):
       return memo[n]
    else:
       memo.append(fibonacci(n-1) + fibonacci(n-2))
       return memo[-1]

# Bottom Up Approach - Mandatory tabulation to find the answer ( build from ground to answer )
def fibonacci_bottom(n):
    
    table = [0,1]

    for i in range(2, n+1):
        table.append(table[i-1]+table[i-2])
   
    return table[-1]

print fibonacci(4)
print fibonacci_top(4)
print fibonacci_bottom(4)
