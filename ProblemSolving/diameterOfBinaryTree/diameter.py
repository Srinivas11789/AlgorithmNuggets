# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        # Very close modification of HEIGHT of the node - 100 pass - Recursive Method
        def height(node):
            
            if not node:
                return 0
            else:
                left = height(node.left)
                right = height(node.right)
                
                # While calculating height just cal a diameter
                self.dia = max(self.dia, left+right+1)
                
                return 1+max(left, right)
        
        self.dia = 0
        height(root)
        if self.dia > 0:
            return self.dia-1
        else:
            return 0
        
        """
        # Recursive Method - 100 pass - A littel modification of height calculation
        def height(node):
            
            # NUll condition handle
            if not node:
                return 0
            
            # Reset left and right
            left = 0
            right = 0
            
            # Both left and right existence initially and then have only left and only right
            if node.left and node.right:
                left, right = height(node.left)+1, height(node.right)+1
            elif node.left:
                left = height(node.left)+1
            elif node.right:
                right = height(node.right)+1
            if left+right > self.diameter:
                self.diameter = left+right
                
            # Return max of left and right
            return max(left,right)
            
        self.diameter = 0
        height(root)
        return self.diameter
        """
