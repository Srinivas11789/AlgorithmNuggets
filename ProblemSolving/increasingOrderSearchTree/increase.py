# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # 1st attempt with recursive inorder sorting and tree construction - 100 pass on go 
        # Inorder to sort the tree 
        def sortTree(node):
            if not node:
                return
            else:
                # Left first to sort it ascending
                if node.left:
                    sortTree(node.left)
                    
                # Current node @here
                # Create a new result tree when the tree is empty else iterate through the right
                if self.tree:
                    self.tree.right = TreeNode(node.val)
                    self.tree = self.tree.right
                else:
                    self.tree = TreeNode(node.val)
                    self.head = self.tree
                # Right last 
                if node.right:
                    sortTree(node.right)
                    
        # New inreasing order tree construction
        if not root:
            return []
        else:
            # New inreasing order tree construction
            self.tree = None
            # Maintaint the reference for the head node or root node
            self.head = None
            # Function call
            sortTree(root)
        return self.head
            
            
