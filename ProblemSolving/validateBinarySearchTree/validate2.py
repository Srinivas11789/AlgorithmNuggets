# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # Logic 2:
        def traverse(node, left, right):
            if not node:
                return True
            if not left < node.val < right:
                return False
            return traverse(node.left, left, node.val) and traverse(node.right, node.val, right)
        
        return traverse(root, -float('inf'), float('inf'))
        
        # Logic 1: PreOrder traverse and compare
        
        """
        def traverse(node):
            if node:
                if node.left:
                    traverse(node.left)
                self.nodes.append(node.val)
                if node.right:
                    traverse(node.right)
        
        self.nodes = []
        traverse(root)
        print(set(self.nodes))
        if sorted(set(self.nodes)) == self.nodes:
            return True
        else:
            return False
        """
