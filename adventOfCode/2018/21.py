# Count the boxes with box names having 2 repeating and 3 repeating letters
# * multiply them to obtain the checksum 

# Fetch input from url
import requests, sys
# Sent the cookie set through the environment variable to get this
input = requests.get("https://adventofcode.com/2018/day/2/input")

# Hard Coded inputs
input = open("21.input","r").read()
input = input.split("\n")

# Iterate and count frequency of 2 and 3
# function to return dictionary of freqs
def freq(input):
    import collections
    return collections.Counter(input)

twos = 0
threes = 0
for i in input:
    fq = freq(i)
    # Count for exactly 2 or 3 times
    t = 0
    th = 0
    for k,v in fq.items():
        if v == 2 and t == 0:
           twos += 1
           t += 1
        if v == 3 and th == 0: 
           threes += 1
           th += 1

# checksum
print twos * threes
    
