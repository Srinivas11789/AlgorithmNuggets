# Codility Problem - Count Triangles

# Calculate the condition as we iterate and get to know i and j, reduce the combination for k by sorting the array and setting value correspondingly

def solution(A):

    n = len(A)
    count = 0
    A.sort()
    for i in range(n-2):
        for j in range(i+1,n-1):
            value = A[i]+A[j]
            k = j+1
            # CodeSays suggestion
            while k < n and A[k] < value:
               k += 1
            count += k -j -1
            
    return count
                
            
            
    """
    ## Still takes O(N3)
    n = len(A)
    count = 0
    A.sort()
    for i in range(n-2):
        for j in range(i+1,n-1):
            value = A[i]+A[j]
            k = j+1
            while k < n and A[k] < value:
                count += 1
                k += 1
    return count
    """         
    """
    # 100 percent correct but 63 percent in performance - O(N3)
    n = len(A)
    count = 0
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if A[i]+A[j] > A[k] and A[j]+A[k] > A[i] and A[k]+A[i] > A[j]:
                    count += 1
    return count
    """
