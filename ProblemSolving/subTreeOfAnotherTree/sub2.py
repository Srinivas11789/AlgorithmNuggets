# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        # Logic 1: until matched once, compare everyone that is equal to subtree node separtely traversing them with another function.

        def checkSubtree(main, sub):
            
            if not main and not sub:
                return True
            
            if (main and not sub) or (sub and not main):
                return False
            
            if main.val != sub.val:
                return False
            
            left = checkSubtree(main.left, sub.left)
            right = checkSubtree(main.right, sub.right)

            return left and right
        
        def traverse(node):
            
            if not node:
                return
            
            if subRoot.val == node.val and not self.matched:
                self.matched = checkSubtree(node, subRoot)
                
            traverse(node.left)
            traverse(node.right)
            
        self.matched = False
        traverse(root)
        return self.matched
    
