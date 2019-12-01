# Count the boxes with box names having 2 repeating and 3 repeating letters
# * multiply them to obtain the checksum 

# Fetch input from url
import requests, sys
# Sent the cookie set through the environment variable to get this
input = requests.get("https://adventofcode.com/2018/day/2/input")

# Hard Coded inputs
input = open("21.input","r").read()
input = input.split("\n")

"""
# Set logic complicates by giving unique and unordered elements
# * use multiset to preseve repeating elements which is only found in the bag implementation
# * Or use collection.Counter to do this kind of task

# Logic
"""
"""
>>> a = {"s", "r", "i"}
>>> b = {"s", "r", "n"}
>>> a.difference(b)
set(['i'])
""" 
"""
result  = []
# Do worst case brute force to crack this soon
# Set alters the positions and deletes repeated elements, becareful
for i in range(len(input)):
    for j in range(i+1, len(input)):

"""
"""
        one = set(input[i])
        two = set(input[j])
        #inter1 = len(one.intersection(two))
        #inter2 = len(two.intersection(one))
        #if (inter1 == len(input[i])-1) and (inter2 == len(input[j])-1):
        if len(one.difference(two)) == 1 and len(two.difference(one)) == 1:
           index = input[i].index(one.difference(two).pop())
           index2 = input[j].index(two.difference(one).pop())
           #print index, index2, one, two
           if index == index2:
              print input[i], input[j]
              result.append(input[i][:index]+input[i][index+1:])
print set(result)
"""

# Logic 2 revamping with comparison logic 

print input
result = []
n = len(input)
for i in range(n):
    for j in range(i+1, n):
        print i, j, input[i],input[j]
        one = list(input[i])
        two = list(input[j]) 
        count = 0
        if len(one) == len(two):
              for k in range(len(one)):
                     if one[k] == two[k]:
                        pass
                     else:
  		        count += 1
                        index = k
              if count == 1:
		 result.append(input[i][:index]+input[i][index+1:])
print result

# Better logic: identify the same prefix between two strings and quantify the postfix equality after the irregularity (different character)           
