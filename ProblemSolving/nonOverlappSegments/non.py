# Codility Problem - Greedy Non overlapping sets
  
def solution(A, B):
    # some reference to codesays logic
    n = len(A)
    # Lesser length check
    if n < 2:
        return n
    # Track the end array indices and compare with the A array start
    # initial setup
    count = 1
    last = B[0]
    ind = 1
    while ind < n:
        while ind < n and A[ind] <= last:
            ind += 1
        if ind == n:
            break
        count += 1
        last = B[ind]
    #print(count)
    return count
