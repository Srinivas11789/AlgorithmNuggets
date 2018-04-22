# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        
        if p and q:
            # check for values to be equal from root through the left and through the right
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return p is q # Similar to p==q
        
        """
        # works, but not sure how to handle the null character - think about it
        # Perform InOrder Traversal and verify the trees - (Left,Root,Right)
        tree = []
        def inOrder(node):
            if node:
                inOrder(node.left)
                tree.append(node.val)
                inOrder(node.right)
            
        
        inOrder(p)
        tree1 = tree
        tree = []
        inOrder(q)
        tree2 = tree
        print tree1,tree2
        if tree1 == tree2:
            return True
        else:
            return False
        """
        
            
        
