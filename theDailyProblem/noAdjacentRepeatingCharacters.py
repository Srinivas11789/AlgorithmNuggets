"""
Given a string, rearrange the string so that no character next to each other are the same. If no such arrangement is possible, then return None.

Example:
Input: abbccc
Output: cbcbca
def rearrangeString(s):
  # Fill this in.

print rearrangeString('abbccc')
# cbcabc
"""

def rearrangeString(s):
  # Logic 1: O(N) arrangement 
  s = list(s)
  for i in range(len(s)):
    if i+1 < len(s) and s[i+1] == s[i]:
      j = i+1
      while s[j] == s[i] and s[i-1] == s[i]:
          j += 1
      if j == len(s):
         s[i], s[0] = s[0], s[i]
      else:
         s[i], s[j] = s[j], s[i]
  return s

print rearrangeString('abbccc')
# cbcabc
