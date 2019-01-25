# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        
        # Null check
        if not root:
            return 0
        
        # global sum
        self.sum = 0
        
        # Brute force - traverse all nodes to look at their value 
        def traverse(node):
            
            if node.val >= L and node.val <= R:
                self.sum += node.val
            
            if node.left:
                traverse(node.left)
            
            if node.right:
                traverse(node.right)
        
        # Function utilizing BST property - a little faster (avoiding unwanted traversals)
        def traverse2(node):
            
            print node.val
            
            if node.val >= L and node.val <= R:
                self.sum += node.val
            
            # Traverse left only when node value is greater than Left
            if node.val > L and node.left:
                traverse(node.left)
            
            if node.val < R and node.right:
                traverse(node.right) 
            
        
        traverse2(root)
        
        return self.sum
        
