# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def divide(arr):
            
            if not arr:
                return
            
            mid = len(arr)//2
            left = mid-1
            right = mid+1
            
            root = TreeNode(arr[mid])
            
            root.left = divide(arr[:mid])
            root.right = divide(arr[mid+1:])
            
            return root
        
        return divide(nums)
