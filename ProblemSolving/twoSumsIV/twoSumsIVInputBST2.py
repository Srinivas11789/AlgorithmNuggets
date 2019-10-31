# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        
        # 4 
        # [1, 2, 3] ==> 1,3
        
        s = set()
        
        def traverse(node):
            
            if node.val in s:
                return True
            
            s.add(k-node.val)
            
            left = right = False
            
            if node.left:
                left = traverse(node.left)
            if node.right:
                right = traverse(node.right)
        
            return left or right
        
        return traverse(root)
