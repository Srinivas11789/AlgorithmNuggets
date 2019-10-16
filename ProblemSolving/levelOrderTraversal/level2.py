# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        if not root:
            return []
        stack = [root]
        result = []
        while stack:
            result.append([])
            n = len(stack)
            while n:
                current = stack.pop(0)
                result[-1].append(current.val)
                if current.left:
                    stack.append(current.left)
                if current.right:
                    stack.append(current.right)
                n -= 1
        return result
