"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
You must do this in-place without making a copy of the array.
Minimize the total number of operations.

Here is a starting point:

class Solution:
  def moveZeros(self, nums):
    # Fill this in.

nums = [0, 0, 0, 2, 0, 1, 3, 4, 0, 0]
Solution().moveZeros(nums)
print(nums)
# [2, 1, 3, 4, 0, 0, 0, 0, 0, 0]
"""

class Solution:

    # O(N) and 1 pointer method    
    def moveZeros2(nums):
        zero = None
        for i in range(len(nums)):
            if nums[i] == 0:
                if zero is None:
                    zero = i
            else:
                nums[zero], nums[i] = nums[i], nums[zero]
                zero += 1
        return nums

def main():
    nums = [
            [0, 0, 0, 2, 0, 1, 3, 4, 0, 0],
            [ 0, 1, 0, 3, 12]
           ]
    for num in nums:
        Solution.moveZeros2(num)
        print(num)

main()
