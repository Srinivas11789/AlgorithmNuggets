"""
Write a function that reverses the digits a 32-bit signed integer, x. Assume that the environment can only store integers within the 32-bit signed integer range, [-2^31, 2^31 - 1]. The function returns 0 when the reversed integer overflows.

Example:
Input: 123
Output: 321
class Solution:
  def reverse(self, x):
    # Fill this in.

print(Solution().reverse(123))
# 321
print(Solution().reverse(2**31))
# 0
"""
import sys
class Solution:
  def reverse_hack(self, x):
    if x > (-2**31) and x < (2**31)-1:
        return int(str(x)[::-1]) 
    else:
        return 0
  
  # New Logic - learn more ways 
  def reverse(self, x):
    rev = 0
    #print(x)
    #i = 0
    while x:
      if x >= (2**31) or x <= (-2**31)-1:
          return 0
      #print("=============> "+str(i))
      pop = x%10
      #print(pop)
      x /= 10
      #print(x)
      rev = rev*10 + pop
      #print(rev)
      #i += 1
    return rev

print(Solution().reverse(123))
# 321
print(Solution().reverse(2**31))
# 0
 
