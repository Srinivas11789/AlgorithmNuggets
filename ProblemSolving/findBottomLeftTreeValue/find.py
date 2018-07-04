# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        # Breath First Traversal - level order search
        
        nodes = [root]
        levels = []
        
        while nodes:
            levels.append([])
            n = len(nodes)
            while n:
                cur = nodes.pop(0)
                levels[-1].append(cur.val)
                if cur.left:
                    nodes.append(cur.left)
                if cur.right:
                    nodes.append(cur.right)
                n -= 1
        
        return levels[-1][0]
                
        
        
