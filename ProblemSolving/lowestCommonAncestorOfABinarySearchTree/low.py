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
        
        # Logic: In a Binary search tree the arrangement is based on left being smaller than root and right being greater than root, for ancestor calculation from top down, when both pq are lesser than a ancestor then navigate left else navigate right.
        
        """
        # Recursive Solution - 100 pass
        def lca(node):
            
            if not node:
                return None
            else:
                # If children are smaller than main root, it should be somwehere in the left subtree
                if node.val > q.val and node.val > p.val:
                    return lca(node.left)
                elif node.val < q.val and node.val < p.val:
                    return lca(node.right)
                return node
        return lca(root)
        """
        
        # Iterative Solution - 100 pass
        if not root:
            return None
        
        node = root
        
        while node:
            if node.val > q.val and node.val > p.val:
                    node = node.left
            elif node.val < q.val and node.val < p.val:
                    node = node.right
            else:
                return node
        
        """
        # Post order traversal logic
        def traverse(node):
            if not node:
                return None
            else:
                left = traverse(node.left)
                right = traverse(node.right)
                if left == p.val and right == q.val:
                    result.append(node.val)
                return node.val
            
        
        result = []
        traverse(root)
        print result
        return result[0]
        """
            
