# Codility Problem - Flags 

def solution(A):

    """
    # Attempt 1 - only 6 percen
    n = len(A)
    peaks = []
    heights = []
    flags = 0
    for i in range(1,n-1):
        if A[i] > A[i-1] and A[i] > A[i+1]:
            peaks.append(A[i])
            heights.append(i)
            if flags == 0:
                flags += 1
            else:
                if abs(heights[-1] - heights[-2]) >= flags:
                    flags += 1
    return flags-1
    """
            
