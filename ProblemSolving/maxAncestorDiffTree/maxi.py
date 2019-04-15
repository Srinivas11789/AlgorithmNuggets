# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxAncestorDiff(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        # Logic1: Literally follow the instructions ( No shortcuts ) - 100 pass 10% 100%
        # * At every node, maintain the hierarchy and check differences with all ancestors
        
        def ancestorDiff(node, hierarchy):
            
            for ancestor in hierarchy:
                if abs(ancestor.val - node.val) > self.maxDiff:
                    self.maxDiff = abs(ancestor.val - node.val)

            if node.left:
                ancestorDiff(node.left, hierarchy+[node])
            if node.right:
                ancestorDiff(node.right, hierarchy+[node])
                
        
        self.maxDiff = 0
        ancestorDiff(root, [])
        return self.maxDiff

