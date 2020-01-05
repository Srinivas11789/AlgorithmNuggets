"""
Given a string, determine if you can remove any character to create a palindrome.

Here's some examples and some starter code:

def create_palindrome(s):
  # Fill this in.

print(create_palindrome("abcdcbea"))
# True
print(create_palindrome("abccba"))
# False
print(create_palindrome("abccaa"))
# False
"""

def create_palindrome(A):
  
  # Logic 1: 2 pointer method - 100 pass 
  left = 0
  right = len(A)-1
  remove = False # to track only one remove
  # Iterating until left < right -->
  # Even length: the last i vs i+1 are both equal
  # Odd length: the last i is unique so we do not care
  while left < right:
    if A[left] == A[right]:
      left += 1
      right -= 1
    elif A[left+1] == A[right] and not remove:
      remove = True
      left += 1
    elif A[right-1] == A[left] and not remove:
      remove = True
      right -= 1
    else:
      return False
  if remove:
    return True
  else:
    return False

def create_palindrome_2(A):
  n = len(A) 
  for i in range(n):
     mid = n//2
     if n%2 != 0 and i != mid: # ODD LENGTH STRING
       if A[i] != A[-i-1]:
         possible1 = A[:i]+A[i+1:]
         j = n-i-1
         possible2 = A[:j]+A[j+1:]
         if (possible1 == possible1[::-1]) or (possible2 == possible2[::-1]):
           return True
         else:
           return False
     elif n%2 == 0: # EVEN LENGTH STRING
       if A[i] != A[-i-1]:         
         possible1 = A[:i]+A[i+1:]
         j = n-i-1
         possible2 = A[:j]+A[j+1:]
         if (possible1 == possible1[::-1]) or (possible2 == possible2[::-1]):
           return True
         else:
           return False
  return False
 
print(create_palindrome("abcdcbea"))
# True
print(create_palindrome("abccba"))
# False
print(create_palindrome("abccaa"))
# False

print(create_palindrome_2("abcdcbea"))
# True
print(create_palindrome_2("abccba"))
# False
print(create_palindrome_2("abccaa"))
# False
