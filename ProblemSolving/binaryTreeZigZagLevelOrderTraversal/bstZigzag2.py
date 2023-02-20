# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return 
        stack = [root]
        zigZag = []

        while stack:
            n = len(stack)
            zigZag.append([]) # insert new level
            pos = len(zigZag)-1
            while n:
                curr = stack.pop(0)
                if pos%2 == 0:
                    zigZag[-1].append(curr.val)
                else:
                    zigZag[-1] = [curr.val] + zigZag[-1]
                if curr.left:
                    stack.append(curr.left)
                if curr.right:
                    stack.append(curr.right)
                n -= 1

        return zigZag
