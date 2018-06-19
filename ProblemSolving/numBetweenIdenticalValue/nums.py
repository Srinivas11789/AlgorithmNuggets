
# Remove digits between identical pairs 
"""
# Logic 1 - Pythonic Logic with split

a = [1,2,3,4,2,4,3,5,3]

for i in range(len(a)):
    a[i] = str(a[i])
b = "".join(a)

result = []

for item in set(a):
    if a.count(item) > 1:
       c = b.split(item)
       d = []
       print item, c
       for i in range(1, len(c)-1):
           d.extend(c[i])
       result.extend(d)

print result
"""

# Logic 2 - Dictionary logic

a = [1,2,3,4,2,4,3,5,3]
print a

import collections
c = collections.Counter(a)

result = []

for k,v in c.items():
    if v > 1:
       first = a.index(k)
       count = v
       while count > 0:
             second = a[first+1:].index(k)
             result.extend(a[first+1:second+first+1])
             print a[first+1:second+first+1], count, first, second
       	     count -= 1
             first = second

print result
