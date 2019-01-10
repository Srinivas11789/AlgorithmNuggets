# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        self.uni_value = root.val
        self.result = True
        
        # Recursive traverse
        def traverse(node):
            
            if not node:
                return
            
            if node.val != self.uni_value:
                self.result = self.result and False
            
            if node.left:
                traverse(node.left)
            if node.right:
                traverse(node.right)
            
        traverse(root)
        return self.result
        
        
