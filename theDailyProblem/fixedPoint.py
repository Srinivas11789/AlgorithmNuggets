"""
A fixed point in a list is where the value is equal to its index. So for example the list [-5, 1, 3, 4], 1 is a fixed point in the list since the index and value is the same. Find a fixed point (there can be many, just return 1) in a sorted list of distinct elements, or return None if it doesn't exist.

Here is a starting point:

def find_fixed_point(nums):
  # Fill this in.

print find_fixed_point([-5, 1, 3, 4])
# 1

Can you do this in sublinear time?
"""

# Linear time with O(N) would be a very obvious case - But we want to do sublinear time less than O(N)

# Logic1
# Binary search for the help?
# 0, 1, 2, 3, 4, 5

def find_fixed_point(nums):
  left = 0
  right = len(nums)
  fixed_point = None
  while left < right:
    mid = left+(right-left)//2
    target = nums[mid]
    if mid < target:
        right = mid
    else:
        left = mid
    if right-left == 1:
      if nums[left] == left:
        fixed_point = left
      elif nums[right] == right:
        fixed_point = right
      break  
    #print(left, right, target)
  return fixed_point

print find_fixed_point([-5, 1, 3, 4])
print find_fixed_point([-5, 0, 2, 4, 5, 8])
