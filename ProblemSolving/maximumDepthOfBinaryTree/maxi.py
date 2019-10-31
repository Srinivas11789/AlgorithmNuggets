# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        def depth(node):
            if not node:
                return 0
            else:
                return 1+max(depth(node.right), depth(node.left))
        
        return depth(root)
