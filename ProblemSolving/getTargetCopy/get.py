# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        
        # Logic 1: traverse cloned to find the same node with same children
        def traverse(node):
            
            if not node:
                return
        
            if node.val == target.val:
                left = False
                right = False
                if node.left and target.left and node.left.val == target.left.val:
                    left = True
                if node.right and target.right and node.right.val == target.right.val:
                    right = True
                if not node.left and not target.left:
                    left = True
                if not node.right and not target.right:
                    right = True
                if left and right:
                    self.node = node
        
            # traversal
            if node.left:
                traverse(node.left)
            if node.right:
                traverse(node.right)
                
            return
        
        # Logic 2: traverse both the trees in parallel to find the exact node
        def dualTraverse(tree1, tree2):
            
            if tree1 and tree1 == target:
                return tree2
            
            if not tree1:
                return None
            
            l = None
            r = None
            if tree1.left:
                l = dualTraverse(tree1.left, tree2.left)
            if tree1.right:
                r = dualTraverse(tree1.right, tree2.right)
            
            if l:
                return l
            elif r:
                return r
            else:
                return None
        
        # logic 1 call
        
        #self.node = None
        #traverse(cloned)
        #return self.node
        
        # logic 2 call
        return dualTraverse(original, cloned)
