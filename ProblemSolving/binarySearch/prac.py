# # Practice

def binarySearch(nums, target):
  left, right = 0, len(nums)-1
  while left < right:
    mid = left + len(nums[left:right])//2
    print(left, mid, right)
    if nums[mid] == target or nums[left] == target or nums[right] == target:
      return True
    elif nums[mid] > target:
      right = mid
    elif nums[mid] < target:
      left = mid

  return False

nums = [1,2,3,4,5,6,7,8,9]
for i in range(0, 10):
    print(binarySearch(nums, i)) 
