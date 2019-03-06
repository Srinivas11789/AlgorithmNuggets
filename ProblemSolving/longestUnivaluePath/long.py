# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        # Logic
        # * Tweak the logic to work for every subtree as the current node == root
        # * At every subtree the univalue path through it should be maximum then return
        self.max_univalue = 0
        
        def univalue_traverse(node): 
            
            if not node:
                return 0
            
            left_univalue = univalue_traverse(node.left)
            right_univalue = univalue_traverse(node.right)
            
            if node.left and node.val == node.left.val:
                left_univalue += 1
            else:
                left_univalue = 0
             
            if node.right and node.val == node.right.val:
                    right_univalue += 1
            else:
                right_univalue = 0

            subtree_univalue = left_univalue + right_univalue
                
            self.max_univalue = max(self.max_univalue, subtree_univalue)
                
            return max(left_univalue, right_univalue)
    
        univalue_traverse(root)
        return self.max_univalue
        
        """
        # The below logic would work for vertical paths. The example2 shows horizontal univalue path which this logic doesnt work for.
        # Logic:
        # * Try Depth first search as it may traverse the possible longest path
        # * Track the same value occurrences and update max depth
        
        self.max_univalue = 0
        
        def univalue_traverse(node, parent, univalue):
            
            # Update univalue path
            if node.val == parent:
                univalue += 1
            
            # Track the maximum univalue path
            self.max_univalue = max(univalue, self.max_univalue)
            
            # Left Node
            if node.left:
                univalue_traverse(node.left, node.val, univalue)
            
            # Right Node
            if node.right:
                univalue_traverse(node.right, node.val, univalue)
        
        if not root:
            return 0
        
        univalue_traverse(root, 0, 0)
        return self.max_univalue
        """
