# Cracking coding interview - 
# Memoize
fibos = [0,1]
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n < len(fibos):
        return fibos[n]
    else:
        return fibonacci(n-1) + fibonacci(n-2)
n = int(raw_input())
print(fibonacci(n))

