# Logic1
# * Recursion

def cut_rods(prices, n):
    if n <= 0:
        return 0
    
    maxi = float('-inf')

    for i in range(n):
        maxi = max(maxi, prices[i] + cut_rods(prices, n-i-1))
 
    return maxi

# Logic2
# * Memoization
def cut_rods2(prices, n):
    memo = [0]*(n+1)
    for i in range(1, n+1):
        maxi = float('-inf')
        for j in range(i):
            maxi = max(maxi, prices[j] + memo[i-j-1])
        memo[i] = maxi
    return memo[n]
    

# Logic3:
# * Memoization + Recursion?
def cut_rods3(prices, n, memo):
    maxi = float('-inf')
    for i in range(n, 1, -1):
        maxi = max(maxi, prices[i] + cut_rods3(prices, n-1, memo))
    print(memo)
    memo[i] = maxi

# Driver
def main():
    arr = [1, 5, 8, 9, 10, 17, 17, 20] 
    size = len(arr)
    print(cut_rods(arr, size))
    print(cut_rods2(arr, size))
    print(cut_rods3(arr, size, [0]*size))

main()
