# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        
        # Each subtree visited we move through, each subtree's root will be node
        def trim(node):
            # Reaching the depth of a BST
            if not node:
                return None
            # Range should be within L - R, hence if node is less than L, trim the right
            elif node.val < L:
                return trim(node.right)
            # Range should be within L - R, hence if node is greater than R, trim the left
            elif node.val > R:
                return trim(node.left)
            # Else, trim both the sides
            else:
                node.left = trim(node.left)
                node.right = trim(node.right)
                return node
        
        return trim(root)
        
            
        
        
