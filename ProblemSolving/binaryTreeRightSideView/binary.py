# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        # Logic 1:
        # * Perform level order traversal and get the last element on that level
        def traverse(node, level):
            if level not in levels:
                levels[level] = []
            levels[level].append(node.val)
            if node.left:
                traverse(node.left, level+1)
            if node.right:
                traverse(node.right, level+1)
            
        result = []
        levels = {}
        if not root:
            return []
        traverse(root, 0)
        for k,v in levels.items():
            result.append(v[-1])
        return result
