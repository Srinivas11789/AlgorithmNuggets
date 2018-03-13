# Bubble Sort - 
# Swap every pair as we traverse with 2 for loops
n = int(raw_input().strip())
a = map(int, raw_input().strip().split(' '))
temp = None
swaps = 0
for i in range(n):
    for j in range(n-1):
        if a[j] > a[j+1]:
            temp = a[j+1]
            a[j+1] = a[j]
            a[j] = temp
            swaps += 1
print "Array is sorted in "+str(swaps)+" swaps."
print "First Element: "+str(a[0])
print "Last Element: "+str(a[n-1])
            
