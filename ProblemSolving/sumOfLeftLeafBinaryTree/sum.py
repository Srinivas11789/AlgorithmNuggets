# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 100 pass - Iterative - Sum of all the left leaf nodes
        # Logic:
        # 1. Traverse the tree - moving through all the nodes 
        # 2. If a left node is found with left and right of the left node null, then add the node to sum
        
        if not root:
            return 0
        
        nodes = [root]
        sumi = 0
        
        while nodes:
            node = nodes.pop(0)
            if node.left:
                if node.left.left is None and node.left.right is None:
                    sumi += node.left.val
                nodes.append(node.left)
            if node.right:
                nodes.append(node.right)
        return sumi

        
        """
        # 100 pass - Recursive method
        def sumLeft(node):
            if not node:
                return 
            
            if node.left:
                if node.left.left is None and node.left.right is None:
                    self.sumi += node.left.val
            
            sumLeft(node.left)
            sumLeft(node.right)
            
        self.sumi = 0
        sumLeft(root)
        return self.sumi
        """
        
        """
        # Logic to add all the left nodes.. Question is add all the left leaf nodes
        if not root:
            return 0
        
        nodes = [root]
        sumi = 0
        
        while nodes:
            node = nodes.pop(0)
            if node.left:
                sumi += node.left.val
                nodes.append(node.left)
            if node.right:
                nodes.append(node.right)
        return sumi
        """
            
