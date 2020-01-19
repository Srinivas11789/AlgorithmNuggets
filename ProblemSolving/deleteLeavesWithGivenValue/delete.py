# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def removeLeafNodes(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode
        """
        
        # Logic 1: traverse and delete all leaf nodes with target - 100 pass - 28ms 100% faster
        def traverse(node, parent, side):
            
            # Traverse to reach the leaf node ( left and right )
            # ( Imagine traversing forward until a leaf is reached )
            if node.left:
                traverse(node.left, node, "left")
            if node.right:
                traverse(node.right, node, "right")
            
            # After traversing on left and right sides, if the node becomes a leaf then do this  
            # ( Imagine traversing backwards to each parents until the root )
            if not node.left and not node.right:
                if node.val == target: 
                    if side == "center" and not parent: # Handle root node case ( no parent )
                        node = None
                    elif side == "left": # tracking the sides is used to delete resp node
                        parent.left = None
                    elif side == "right":  # tracking the sides is used to delete resp node
                        parent.right = None
            return node
                    
        return traverse(root, None, "center")
