# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lcaDeepestLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        # Logic 1: Find height separate and iterate until height
        """
        def height(node):
            if not node:
                return -1
            else:
                return 1+max(height(node.left), height(node.right))
        
        def traverse(node, height):

                
        if not root:
            return None
        self.depth = height(root)
        ancestor = traverse(root, 0)
        return ancestor
        """
    
        # Logic 2: calculate the height as we traverse
        def traverse(node):
            
            # Null check
            if not node:
                return 0, None
            
            depth1, ancestor1 = traverse(node.left)
            depth2, ancestor2 = traverse(node.right)
            
            if depth1 > depth2:
                return depth1+1, ancestor1
            elif depth1 < depth2:
                return depth2+1, ancestor2
            
            return depth1+1 ,node
        
        return traverse(root)[1]
        
            
        
