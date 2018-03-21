# Codility Dominator -
# Lessons learnt: 
## Easy testcase failed - test for empty array!!!!!!!!

def solution(A):
    # Dictionary method
    n = len(A)
    count = {}
    max = 0
    if n == 0:
        return -1
    for i in range(n):
        if A[i] not in count:
            count[A[i]] = [0,[]]
        count[A[i]][0] += 1
        count[A[i]][1].append(i)
        if count[A[i]][0] > max:
            max = A[i]
    #print(count[max][0],n//2)
    if count[max][0] > n//2:
        return count[max][1][0]
    else:
        return -1
