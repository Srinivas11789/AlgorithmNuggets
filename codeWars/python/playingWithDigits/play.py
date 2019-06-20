def dig_pow(n, p):
    answer = 0
    temp = list(str(n))
    while temp:
        answer += int(temp.pop(0))**p
        p += 1
    print(n, p, answer)
    if answer % n == 0:
        return answer//n
    else:
        return -1
        
