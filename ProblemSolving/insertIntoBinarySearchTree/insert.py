# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        
        # Recursive Solution - Insert a Node
        def recurse_insert(node, val):
            
            # Null node
            if not node:
                return
            
            # Guaranteed the node wont exist already so check for only smaller or greater than
            # * Left - recurse for left node existence 
            # * else, add the left node
            if val < node.val:
                if node.left:
                    recurse_insert(node.left, val)
                else:
                    node.left = TreeNode(val)
            else:
            # * Right - recurse for right node existence 
            # * else, add the right node
                if node.right:
                    recurse_insert(node.right, val)
                else:
                    node.right = TreeNode(val)
                    
        def iterative_insert(node, val):
            
            # stack to traverse 
            stack = [node]
            
            while stack:
                current_node = stack.pop(0)
                
                # Left and Right traverse
                if val < current_node.val:
                    if current_node.left:
                        stack.append(current_node.left)
                    else:
                        current_node.left = TreeNode(val)
                        return
                else:
                    if current_node.right:
                        stack.append(current_node.right)
                    else:
                        current_node.right = TreeNode(val)
                        return
                    
        # Function call
        recurse_insert(root, val)
        #iterative_insert(root, val)
        return root
        
