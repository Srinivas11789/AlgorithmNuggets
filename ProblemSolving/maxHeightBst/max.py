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
        
        def height(node):
            if not node:
                return 0
            else:
                return 1+max(height(node.left),height(node.right))
        
        return height(root)
        

    """
    # Alternate - both 100 pass
    def height(node):
            if not node:
                return 0
            
            lh = height(node.left)
            rh = height(node.right)
            
            if lh > rh:
                return lh+1
            else:
                return rh+1
                        
        
        return height(root)
    """    
