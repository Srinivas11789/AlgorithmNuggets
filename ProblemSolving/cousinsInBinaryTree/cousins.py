# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        
        # Iterative method - 100 pass 100% faster
        
        # * Level order search -> Find if they are cousins
        stack = [root]
        result = []
        
        while stack:
            n = len(stack)
            result.append([])
            while n > 0:
                current_node = stack.pop(0)
                result[-1].append(current_node.val)
                left = right = 0
                if current_node.left:
                    left = current_node.left.val
                    stack.append(current_node.left)
                if current_node.right:
                    right = current_node.right.val
                    stack.append(current_node.right)
                if left > 0 and right > 0:
                    if (left == x and right == y) or (left == y and right == x):
                        return False
                n -= 1

        for level in result:
            if x in level and y in level:
                return True
        return False
        
        
        
