# Factorial

# Recursive
def factorial(n):
    if n == 0:
       return 1
    return n*factorial(n-1)

# Iterative
def factorial(n):
    fact = 0
    for i in range(n,0,-1):
      fact *= i
    return fact

def main():
    n = 3
    print factorial(n)

main()
