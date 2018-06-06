def zeroCollect(num):
    
    # Easy solution
    #return sorted(num)

    nonzp = 0
   
    for i in range(len(num)):
        if num[i] == 0:
            num[i] = num[nonzp]
            num[nonzp] = 0
            nonzp += 1
        else:
            if nonzp == 0:
            	nonzp = i
           

    return num

print zeroCollect([1,0,9,2,4,0,0,5,0])
