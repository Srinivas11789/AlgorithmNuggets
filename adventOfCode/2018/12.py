# Calculate the End Frequency Changes from the Freq changes list
# * Start from 0
# * Condition: When first repeating freq result occurs, start from beginning

# Fetch input from url
import requests, sys
# Sent the cookie set through the environment variable to get this
input = requests.get("https://adventofcode.com/2018/day/1/input")

# Hard Coded inputs
input = open("12.input","r").read()
input = input.split("\n")

# freqs list to track the frequency
exp = "0"
freqs = []
count = 0
while exp:
  for i in input:
       if i != "":
         exp = str(eval(exp+i))
         if exp in freqs:
            print exp
            sys.exit()
         else:
            freqs.append(exp)
  #print exp
  count += 1
  print count
  #sys.exit()

