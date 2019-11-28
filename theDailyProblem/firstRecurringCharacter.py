"""
Given a string, return the first recurring letter that appears. If there are no recurring letters, return None.

Example:
Input: qwertty
Output: t

Input: qwerty
Output: None
Here's some starter code:

def first_recurring_char(s):
  # Fill this in.
  
print(first_recurring_char('qwertty'))
# t

print(first_recurring_char('qwerty'))
# None
"""

def first_recurring_char(s):
  
  # O(N) Iteration with Extra space
  freq = {}
  for i in range(len(s)):
    if s[i] not in freq:
      freq[s[i]] = 1
    else:
      return s[i]
  return None

print(first_recurring_char('qwertty'))
# t

print(first_recurring_char('qwerty'))
# None
