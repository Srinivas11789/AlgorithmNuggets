# Codility Problem - count Chocolates

def solution(N, M):
    
    # Find the GCD and use the LCM to find the result, Codesays solution
    # 
    def gcd(n,m):
        if n%m == 0:
            return m
        else:
            return gcd(m,n%m)
    
    lcm = N*M//gcd(N,M)
    return lcm//M
        
    """
    # LCM of N,M and divide by M - by Jeane
    if N > M:
       z = N
    else:
       z = M

    while(True):
       if((z % N == 0) and (z % M == 0)):
           lcm = z
           break
       z += 1
    
    return lcm//M
    """
        
    # O(N+M) timeout error - 100% correct / score 50
    """
    next = 0
    chocolates = []
    if N  == 0:
        return 0
    while next not in chocolates:
        chocolates.append(next)
        next = (next+M)%N
    return len(chocolates)
    """ 
    """
    for i in range(N):
        next = (i+M)%N
        if next in chocolates:
            return len(chocolates)
        else:
            chocolates.append(next)
        print(chocolates)
    return len(chocolates)
    """
