# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def traverse(node):
                
            # traverse to compute
            left_path = 0
            right_path = 0
            if node.left:
                left_path = 1 + traverse(node.left)
            if node.right:
                right_path = 1 + traverse(node.right)
            
            # bottom up path calculation
            
            # for passing through current node calulation
            max_path = (left_path + right_path)
            if max_path > self.max_path:
                self.max_path = max_path
                
            # for upper level max path calulation
            return max(left_path, right_path)
        
        self.max_path = 0
        traverse(root)
        return self.max_path
