# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        # Logic: Create key based on p and q visied. Bottom up to verify key
        def findLca(node, p, q):
            
            if not node:
                return ""
            
            key = ""
            if node == p:
                key = "p"
            if node == q:
                key = "q"
            
            key += findLca(node.left, p, q)
            key += findLca(node.right, p, q)
                        
            if (key == "pq" or key == "qp") and self.lca == None:
                self.lca = node
            
            return key
        
        self.lca = None
        findLca(root, p, q)
        return self.lca

