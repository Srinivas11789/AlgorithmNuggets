# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        stack = [root]
        traversal = []
        while stack:
            curr = stack.pop(0)
            if not curr:
                continue
            traversal.append(curr.val)
            if curr.right:
                stack = [curr.right] + stack
            if curr.left:
                stack = [curr.left] + stack
        return traversal
