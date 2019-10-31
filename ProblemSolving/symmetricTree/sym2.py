# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        levels = {}
        
        def traverse(node, height):
            if height not in levels:
                levels[height] = []
            if node:
                traverse(node.left, height+1)
                levels[height].append(node.val)
                traverse(node.right, height+1)
            else:
                levels[height].append(None)
        
        traverse(root, 1)
        print(levels)
        for l in levels:
            if levels[l] == levels[l][::-1]:
                pass
            else:
                return False
        return True
