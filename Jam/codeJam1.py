def give_check(amount):
    other = ""
    for i in str(amount):
        if i == "4":
            other += "1"
        else:
            other += i
    return other, str(int(amount)-int(other))
        

tcs = input()
for i in range(int(tcs)):
    one, two = give_check(input())
    print "Case #"+str(i+1)+": "+one+" "+two