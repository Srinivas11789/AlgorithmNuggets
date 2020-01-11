# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        
        # Logic 1: Use globals to track minimum and then recurse - 100 pass - 46% faster
        def traverse(node):
            if not node:
                return
            if self.mini == None or abs(target-node.val) < self.mini:
                self.mini = abs(target-node.val)
                self.closest = node.val
            #print(self.mini)
            if node.left:
                traverse(node.left)
            if node.right:
                traverse(node.right)
        
        self.mini = None
        self.closest = root.val
        traverse(root)
        return self.closest
