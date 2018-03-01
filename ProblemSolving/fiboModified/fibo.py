def fibo(n):
    arr = []
    if n == 0:
        arr.append(0)
 	return 0
    if n == 1:
        arr.append(1)
 	return  1
    if n < len(arr) and arr[n]:
        return arr[n]
    return fibo(n-2) + (fibo(n-1))**2

def main():
    n = input("Enter the number:")
    print fibo(n)

main()
