# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def bstToGst(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        # Logic 1: 49% faster and 100% space
        # * Naive, find all the node values and sum of the bst
        # * Obtain these values in sorted form ( in order traversal from above?)
        # * Compute and replace the node values
        
        # Obtain all node values in sorted form
        self.node_vals = []
        def in_order_traverse(node):
            if node:
                if node.left:
                    in_order_traverse(node.left)
                self.node_vals.append(node.val)
                if node.right:
                    in_order_traverse(node.right)
            else:
                return
            
        def compute_and_replace(node):
            if node:
                if node.left:
                    compute_and_replace(node.left)
                # Compute
                for i in range(len(self.node_vals)):
                    if self.node_vals[i] >= node.val:
                        break
                #print(node.val, i)
                node.val = sum(self.node_vals[i:])
                if node.right:
                    compute_and_replace(node.right)
            else:
                return
        
        in_order_traverse(root)
        #print(self.node_vals, sum(self.node_vals), root.val)
        compute_and_replace(root)
        return root
            
        
