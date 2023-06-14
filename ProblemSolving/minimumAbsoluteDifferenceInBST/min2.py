# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:

        self.min_abs_diff = float('inf')

        # assuming root and immediate node is the abs diff (but there can be right --> left subtrees that come close)
        def traverse(node):

            if node.left:
                self.min_abs_diff = min(self.min_abs_diff, abs(node.val - node.left.val))
                traverse(node.left)
            
            if node.right:
                self.min_abs_diff = min(self.min_abs_diff, abs(node.val - node.right.val))
                traverse(node.right)

        self.arrange = []

        # Use inorder to get the sorted version of tree and compute absolute as they are already arranged
        def inOrder(node):

            if node.left:
                inOrder(node.left)
            if self.arrange:
                self.min_abs_diff = min(self.min_abs_diff, abs(self.arrange[-1]-node.val))
            self.arrange.append(node.val)
            if node.right:
                inOrder(node.right)
    
        inOrder(root)
        return self.min_abs_diff 
