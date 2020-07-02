# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        
        # Logic 1: Level Order Iterative Way
        if not root:
            return []
        
        stack = [root] # to record nodes visited
        result = [] # to store results level by level
        n = len(stack)
        
        while stack:
            result = [[]] + result
            n = len(stack)
            while n:
                current = stack.pop(0)
                result[0].append(current.val)
                if current.left:
                    stack.append(current.left)
                if current.right:
                    stack.append(current.right)
                n -= 1 
        return result
