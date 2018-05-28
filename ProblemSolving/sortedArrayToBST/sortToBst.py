# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        
        # Logic: 100 pass
        # Converting a binary search tree from a sorted list can be done by
        # 1. Find the root
        # 2. Recursively add the left and the right nodes to the root
        
        # Null check for nums list
        if not nums:
            return None
        
        # Find the middle element to select the root
        mid = len(nums)//2
        
        # Create a node with the middle element
        root = TreeNode(nums[mid])
        
        # Recursively set the left and right of the root by calling left and right array to mid
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root
        
