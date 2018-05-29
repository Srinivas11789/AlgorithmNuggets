# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        
        """
        # Iterative
        if not root:
            return None
        
        dict_of_parents = {root:None}
        
        nodes = [root]
        
        # Level Order Traversal - until p or q is visited
        while p not in dict_of_parents or q not in dict_of_parents:
            node = nodes.pop()
            if node.left:
                dict_of_parents[node.left] = node
                nodes.append(node.left)
            if node.right:
                dict_of_parents[node.right] = node
                nodes.append(node.right)
        
        parents = set()
        
        while p:
            parents.add(p)
            p = dict_of_parents[p]
        
        while q not in parents:
            q = dict_of_parents[q]
        
        return q
        """
        
        # Recursive
        
        if root is None:
                return None
            
        if root == p or root == q:
                return root
            
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
            
        if left and right:
                return root
        elif left:
                return left
        elif right:
                return right
    
            
            
        
        
