# Codility Problem - SemiPrimes


### Logic 1 - Correctness 100 percent - Performance Failes to 40 --- large values timeout
def solution(N, P, Q):
    n = len(P)
    ans = []
    # Memoize
    primes = []
    for i in range(n):
        lower = P[i]
        higher = Q[i]
        #primes = []
        count = 0
        for j in range(1,higher):
            num = 1
            if j not in primes:
            	while num < j:
                	if j%num == 0:
                    		count += 1
                	num += 1
            	if count == 1:
                	if j == 1:
                    		pass
                	else:
                    		primes.append(j)
            count = 0
        #print(primes)
        c = 0
        for p in range(len(primes)):
            for q in range(p,len(primes)):
                if primes[p]*primes[q] <= higher and primes[p]*primes[q] >=lower:
                    #ans.append(p*q)
                    #print(primes[p],primes[q])
                    c +=1
        #print(c)
        ans.append(c)
    #print(ans)
    return ans
                    
    """ 
	# Possible method to divide by prime number and check
        c = 0
        for k in range(higher):
            if k not in primes:
                for p in primes:
                    res = k//p
                    if res in primes:
                        c += 1
        ans.append(c)
    """        
        
            
            
