# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        def new_tree(node):
    
            if node.left:   
                left_children = new_tree(node.left)
            else:
                left_children = []
            
            if node.right:
                right_children = new_tree(node.right)
            else:
                right_children = []
            
            if 1 not in left_children:
                node.left = None
            
            if 1 not in right_children:
                node.right = None

            children = [node.val if node else None] + left_children + right_children

            #print children

            return children
        
        new_tree(root)
        return root

      
