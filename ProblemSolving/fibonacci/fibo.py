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


def fibonacci_iterative(n):
    fibo = [0,1]
    for i in range(1,n):
        fibo.append(fibo[-1]+fibo[-2])
    return fibo[-1]

def fibonacci_iterative_2(n):
    a = 0
    b = 1
    for i in range(1,n):
	fibo = a+b
        a = b
        b = fibo
    return fibo

n = int(raw_input())
print(fibonacci(n))
print(fibonacci_iterative(n))
print(fibonacci_iterative_2(n))

