def number_needed(a, b):
    char_del = []
    temp1 = a
    temp2 = b
    """
    for i in range(len(b)):#char in b:
        if b[i] not in temp1:
            char_del.append(b[i])
        else:
            temp1 = temp1[:i]+temp1[i+1:]
       # print temp1
    for i in range(len(a)):
        #print temp2
        if a[i] not in temp2:
            char_del.append(a[i])
        else:
            temp2 = temp2[:i]+temp2[i+1:]
        #print temp2
    return len(char_del)
    """
    """
    for i in range(len(b)):
        if b[i] not in temp1:
            char_del.append(b[i])
        else:
            temp1 = temp1[:i]+"*"+temp1[i+1:]
        print temp1
    for i in range(len(a)):
        if a[i] not in temp2:
            char_del.append(a[i])
        else:
            temp2 = temp2[:i]+"*"+temp2[i+1:]
    return len(char_del)
    """
    for i in range(len(b)):
        if b[i] in temp1:
            index = temp1.index(b[i])
            temp1 = temp1[:index]+"*"+temp1[index+1:]
        else:
            char_del.append(b[i])
    for i in range(len(a)):
        if a[i] in temp2:
            index = temp2.index(a[i])
            temp2 = temp2[:index]+"*"+temp2[index+1:]
        else:
            char_del.append(a[i])
    return len(char_del)
    
a = raw_input().strip()
b = raw_input().strip()

print number_needed(a, b)

