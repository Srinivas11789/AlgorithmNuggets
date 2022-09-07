# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def traverse(node):
            
            oneLeft = oneRight = False
            
            if node.left:
                oneLeft = traverse(node.left)
            if node.right:
                oneRight = traverse(node.right)
            
            if oneLeft is False:
                node.left = None
            if oneRight is False:
                node.right = None
            
            final = oneLeft or oneRight
            
            if node.val == 1:
                final = final or True
            
            return final
        
        traverse(root)
        if root.val == 0 and not root.left and not root.right:
            root = None
        return root
