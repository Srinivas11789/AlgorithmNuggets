# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        def inOrder(node, order):
            
            if node.left:
                inOrder(node.left, order)
            
            order += [node.val]
                
            if node.right:
                inOrder(node.right, order)
            
            return order
            
        
        order = inOrder(root, [])
        #print(order)
        
        return order[k-1]
