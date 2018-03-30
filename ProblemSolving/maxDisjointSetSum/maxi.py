### Only 12 percent evaluation percent, check for any other testcases
# Given
# A = Array of trees with no of apples
# K = number of consec trees Alice can pick
# L = number of consec trees Bob can pick
# Choose:  disjoint set and consecutive trees

# Logic1: For K and L, choose the greatest pair that would work. Use them. 
# * Initially choose the greatest pair for alice, eliminate it and then greates pair for bob

def solution(A, K, L):
    # Given data
    n = len(A)
    
    # Initial condition - Possibility of disjoint sets
    total = K + L
    if n < total:
        return -1
        
    # Alice condition - All possible sum value of Alice
    alice = {}
    for i in range(n-(K-1)):
        value = 0
        key = ""
        j = i
        count = 0
        while count < K:
            value += A[j]
            key += str(j)
            j += 1
            count += 1
        alice.update({key:value})
    #print(alice)
    
    # Bob condition - All possible sum value of Bob
    bob = {}
    for i in range(n-(L-1)):
        value = 0
        key = ""
        j = i
        count = 0
        while count < L:
            value += A[j]
            key += str(j)
            j += 1
            count += 1
        bob.update({key:value})
    #print(bob)
    
    # maximum disjoint
    maxi = -600000
    for k,v in alice.items():
        for k1,v1 in bob.items():
            result = v + v1
            if result > maxi and k not in k1:
                maxi = result
    
    return maxi
            
        
