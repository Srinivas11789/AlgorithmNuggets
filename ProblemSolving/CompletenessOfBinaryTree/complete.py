# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        
        # Logic:
        # * Recursively calculate depth of each leaf node and add them into a list
        # * Traverse the list to ensure all the it has precedence left-most
        
        # List of depth of leaf nodes
        self.depth_of_leaf = []
        
        # Depth recursive function
        def depths(node, depth):
            
            # Record depth at leaf
            if not node:
                self.depth_of_leaf.append(depth)
            else:   
                # Traverse for left and right depth
                depths(node.left, depth+1)
                depths(node.right, depth+1)
        
        # Trigger
        depths(root, 0)
        
        # Traverse for left most precedence
        # * Ensure there is not change on the right once it reduces
        # * Ensure there is not change more than once
        
        left_most = self.depth_of_leaf[0]
        print self.depth_of_leaf
        low = 0
        
        for i in range(len(self.depth_of_leaf)):
            if self.depth_of_leaf[i] > left_most:
                return False
            elif self.depth_of_leaf[i] < left_most:
                    left_most = self.depth_of_leaf[i]
                    low += 1
        if low > 1:
            return False
        else:
            return True
            
                
        
                    
                
        
