# Pending...
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def height(node):
            
            if node is None:
                return 0
            else:
                return 1+max(height(node.left), height(node.right))
        
        def balance(node):
            
            if node is None:
                return result
            else:
                if node.left:
                        balance(node.left)
                if node.right:
                        balance(node.right)
                if abs(height(node.left)-height(node.right)) <= 1:
                    return True
                else:
                    return False
        
        if not root:
            return True

        return balance(root)
        
