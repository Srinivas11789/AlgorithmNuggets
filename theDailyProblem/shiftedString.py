"""
You are given two strings, A and B. Return whether A can be shifted some number of times to get B.

Eg. A = abcde, B = cdeab should return true because A can be shifted 3 times to the right to get B. A = abc and B= acb should return false.

def is_shifted(a, b):
  # Fill this in.
  
print is_shifted('abcde', 'cdeab')
# True
"""

def is_shifted(a, b):
  for i in range(len(a)):
    shift = a[i:]+a[:i]
    #print(shift, i)
    if shift == b:
      return True
  return False

print is_shifted('abcde', 'cdeab')
# True
