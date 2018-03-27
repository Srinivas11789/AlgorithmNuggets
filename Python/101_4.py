# Lesson learned:
### * split for a single space
### * raw_input in python 2 works for taking input in a while loop, input() doesnt function proper\
### and throws EOF error

# Enter your code here. Read input from STDIN. Print output to STDOUT
pb = {}
n = raw_input()
for i in range(int(n)):
    io = raw_input().strip().split(" ")
    pb[io[0]] = io[1]
while(1): 
    name = raw_input()
    if name in pb:
        print name+"="+pb[name]
    else:
        print "Not found"


