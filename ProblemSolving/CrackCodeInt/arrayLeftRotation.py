def array_left_rotation(a, n, k):
    answer = ["" for i in range(n)]
    for i in range(n):
        j = i - k
        answer[j] = str(a[i])
    return answer
        
  

n, k = map(int, raw_input().strip().split(' '))
a = map(int, raw_input().strip().split(' '))
answer = array_left_rotation(a, n, k);
print ' '.join(map(str,answer))
