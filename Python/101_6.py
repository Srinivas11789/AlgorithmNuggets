# Lets Review Challenge 101

### * Print the even and odd characters in a string
### * Getting input from hackerrank, use exception handler

data = []
while(1):
    try: 
        data.append(str(raw_input()))
    except EOFError:
        break
for i in range(1,len(data)):
    evenstring = ""
    oddstring = ""
    for j in range(len(data[i])):
        if j % 2 == 0:
            evenstring += data[i][j]
        else:
            oddstring += data[i][j]
    print evenstring+" "+oddstring
