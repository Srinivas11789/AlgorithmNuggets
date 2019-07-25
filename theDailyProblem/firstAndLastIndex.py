"""
Given a sorted array, A, with possibly duplicated elements, find the indices of the first and last occurrences of a target element, x. Return -1 if the target is not found.

Example:
Input: A = [1,3,3,5,7,8,9,9,9,15], target = 9
Output: [6,8]

Input: A = [100, 150, 150, 153], target = 150
Output: [1,2]

Input: A = [1,2,3,4,5,6,10], target = 9
Output: [-1, -1]
Here is a function signature example:

class Solution: 
  def getRange(self, arr, target):
    # Fill this in.
  
# Test program 
arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8] 
x = 2
print(Solution().getRange(arr, x))
# [1, 4]
"""

class Solution:
    def getRange(self, arr, target):
        
        # Logic 1: 2 pointer method - left and right pointer to converge - worst case O(N2)
        """
        left = 0
        right = len(arr)-1
        while left < len(arr) and arr[left] != target:
              left += 1
        if left == len(arr):
            left = -1
        while right > 0 and arr[right] != target:
              right -= 1
        if right == 0:
            right = -1
        return [left, right]
        """
        
        # Logic 2: 2 pointer O(N) Iteration
        left = 0
        left_range = -1
        right = len(arr)-1
        right_range = -1
        while left < right and (left_range == -1 or right_range == -1):
             if arr[left] == target and left_range == -1:
                   left_range = left
             if arr[right] == target and right_range == -1:
                    right_range = right
             if left_range == -1:
                 left += 1
             if right_range == -1:
                 right -= 1
        return [left_range, right_range]
                      
def main():
    s = Solution()
    arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
    x = 2
    print(s.getRange(arr, x) == [1,4])
    arr = [1,2,3,4,5,6,10]
    x = 9
    print(s.getRange(arr,x) == [-1, -1])
    A = [1,3,3,5,7,8,9,9,9,15]
    target = 9
    print(s.getRange(A, target) ==  [6, 8])
    A = [100, 150, 150, 153]
    target = 150
    print(s.getRange(A, target) == [1, 2])

main()
