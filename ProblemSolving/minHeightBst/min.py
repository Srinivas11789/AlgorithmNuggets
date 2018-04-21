# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
    
        # When height is with respect to the edges return -1 if node is None, when height is the count of nodes return 0 when node is None
        # The extra condition of elif here is when the min height is reached or there is difference between left and the right subtree, to return the height of the left right
    
        def height(node):
            if not node:
                return 0
            elif node.left == None or node.right == None:
                return 1+height(node.left)+height(node.right)
            else:
                return 1+min(height(node.left),height(node.right))
        
        return height(root)
        
        
