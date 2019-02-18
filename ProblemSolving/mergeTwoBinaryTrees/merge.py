# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        
        # 100 pass -95% runtime and 100% space
        # Recursive function to traverse the trees
        def traverse(node1, node2):
            
            # When both the nodes are present, change value to their sum
            if node1 and node2:
                node1.val = node1.val+node2.val
            
            # If both left are present recurse, else if node2 only present then replace node1 as node2
            if node1.left and node2.left:
                traverse(node1.left, node2.left)
            elif node2.left:
                node1.left = node2.left
            
            # If both right are present recurse, else if node2 only present then replace node1 as node2
            if node1.right and node2.right:
                traverse(node1.right, node2.right)
            elif node2.right:
                node1.right = node2.right
        
        # Null check for root node of both tree
        if not t1:
            return t2
        if not t2:
            return t1
        
        # Recursive call
        traverse(t1, t2)
        
        # Return the root of the first tree
        return t1
        
