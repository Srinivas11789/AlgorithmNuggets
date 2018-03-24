# Codility Problem - TieRopes Greedy Algo - 100

def solution(K, A):
   n = len(A)
   if n < 1:
       return 0
   count = 0
   ind = 0
   length = 0
   l = []
   while ind < n:
        while ind < n and A[ind] < K:
           length = length + A[ind]
           if length >= K:
               l.append(length)
               length = 0
               ind += 1
           else:
               ind += 1
        if ind == n:
            break
        l.append(A[ind])
        length = 0
        ind += 1
   return len(l)
        
               
