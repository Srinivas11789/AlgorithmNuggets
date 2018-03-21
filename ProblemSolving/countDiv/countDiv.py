# Codility Problem - 100 percent - N logic was easy but there is a better formula [(largest_divisible) - (smallest_divisible) + 1] within range

def solution(A, B, K):
    # Required O(1) complexity
    # Within range find the smallest and largest divisible number and use the formula
    if A%K == 0 and B%K == 0:
        return ((B//K)-(A//K))+1
    else:
	# Lesson: Had a mistake in the while loop: "A%K == 0" which wont work rather not equal works, for while or if loop review the logic and condition properly 
        while A%K != 0:
            A = A + 1
        while B%K != 0:
            B = B - 1
        #print(A,B)
        return ((B//K)-(A//K))+1
    
    """
    # O(N): Correctness 100 percent, Performance 50 percent due to timeouts
    count = 0    
    for i in range(A,B+1):
        if i%K == 0:
            count += 1
    return count
    """
