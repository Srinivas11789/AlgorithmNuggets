# Codility Problem - EquiLeader

# * Even number of occurence of the leaders should be performed to get a equileader
# * Dictionary method
def solution(A):
    record = {}
    count = 0
    n = len(A)
    max = n//2
    for i in range(n):
        if A[i] not in record:
            record[A[i]] = [0,[]]
        record[A[i]][0] += 1
        if record[A[i]][0] > max:
            max = A[i]
        record[A[i]][1].append(i)
    #print(record)
    #for i in range(len(record[max][1])):
    #    length = 
    #    length1 =
    count = 0
    count2 = 0
    ans = 0
    array = record[max][1]
    for item in array:
        for i in range(item+1):
            if i in array:
                count += 1
        for i in range(item+1,n):
            if i in array:
                count2 += 1
        #print(count,count2)
        if len(A[:item+1])//2 < count and len(A[item+1:])//2 < count2:
            ans += 1
        count = 0
        count2 = 0
    return ans
            
        
        
        
        

        
