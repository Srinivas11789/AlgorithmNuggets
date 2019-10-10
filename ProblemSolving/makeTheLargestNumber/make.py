"""
Given a number of integers, combine them so it would create the largest number.

Example:
Input:  [17, 7, 2, 45, 72]
Output:  77245217
def largestNum(nums):
  # Fill this in.

print largestNum([17, 7, 2, 45, 72])
# 77245217
"""

def largestNum(nums):
  # Logic 1: BruteForce - 100 pass but might lead to timelimit exceeded 
  """
  import itertools
  string_arr = [str(i) for i in nums]
  maxi = 0
  for comb in itertools.permutations(string_arr, r=len(nums)):
    maxi = max(maxi, int("".join(comb)))
  return maxi
  """

  # Logic 2: Arranging sorted digit wise ( 1st, 2nd ... ) will solve this
  #nums = sorted(nums, key= lambda x: int(list(str(x))[0]), reverse=True)
  return "".join(sorted(map(str, nums), cmp=lambda x, y: cmp(x+y,y+x))[::-1]).lstrip('0') or '0'
  #return "".join([str(i) for i in nums])
  # for same first digits we need to check before applying
  """
  ans = ""
  i = 0
  while i < len(nums):
    nums[i] = str(nums[i])
    if i+1 < len(nums) and str(nums[i+1])[0] == nums[i][0]:
        nums[i+1] = str(nums[i+1])
        j = i + 1
        while j< len(nums) and str(nums[j])[0] == nums[i][0]:
            nums[j] = str(nums[j])
            j += 1
        temp = j
        j -= 1
        while int(nums[j]) > int(nums[j][0]*2):
            ans += nums[j]
            j -= 1
        for k in range(i, j+1):
            ans +=  nums[k]
        i = temp
    else:
        ans += nums[i]  
        i += 1
    
  return ans
  """
print largestNum([17, 7, 2, 45, 72])
print largestNum([3, 30, 34, 5, 9])
# 77245217
