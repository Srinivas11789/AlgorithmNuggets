"""
Given two strings, find if there is a one-to-one mapping of characters between the two strings.

Example
Input: abc, def
Output: True # a -> d, b -> e, c -> f

Input: aab, def
Ouput: False # a can't map to d and e 
Here's some starter code:

def has_character_map(str1, str2):
  # Fill this in.

print(has_character_map('abc', 'def'))
# True
print(has_character_map('aac', 'def'))
# False
"""

def has_character_map(str1, str2):
  # Logic 1: 100 pass --> Using extra space --> a dictionary
  """
  result = {}
  for i, j in zip(str1, str2):
    if i not in result:
      result[i] = j
    else:
      if result[i] == j:
        pass
      else:
        return False
  return True
  """
  
  # Logic 2: Using no extra space and O(N) Iteration  

print(has_character_map('abc', 'def'))
# True
print(has_character_map('aac', 'def'))
# False
