
#N2 Logic    
def zeroCollect(a):
    for i in range(len(a)):
        if a[i] == 0:
            for j in range(0,i):
                if a[j] != 0:
                    a[i] = a[j]
                    a[j] = 0
                    break
    print a

#N Logic
def zeroCollect2(a):
    temp = 0
    for i in range(len(a)):
        if a[i] == 0:
           a[i] = a[temp]
           a[temp] = 0
           temp = temp + 1
	else:
           if temp == 0:
	   	temp = i 
    print a


zeroCollect([1,0,9,2,4,0,0,5,0])
zeroCollect2([1,0,9,2,4,0,0,5,0])

