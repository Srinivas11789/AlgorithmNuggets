# Revision
# Regex library regexsearch string with both the pattern and the variable containing the string
# The variable returned contains only the instance, .group(0) contains the full match and .group(1) contains scrapped string
#!/bin/python

import sys,re

names = []
N = int(raw_input().strip())
for a0 in xrange(N):
    firstName,emailID = raw_input().strip().split(' ')
    firstName,emailID = [str(firstName),str(emailID)]
    gmail = re.search("([a-zA-Z0-9]+)@gmail\.com",emailID)
    if gmail:
        name = gmail.group(1)
        names.append(firstName)
# Bubble Sort Names for alphabetical order
for i in range(len(names)):
    for j in range(len(names)-1):
        temp = None
        if names[j] > names[j+1]:
            temp = names[j+1]
            names[j+1] = names[j]
            names[j] = temp

for item in names:
    print item
            
                    
                    
        




