# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        """
        #Recursive Solution
        def traverse(root):
            # Recursion
            if not root:
                return
            else:
                traverse(root.left)
                traverse(root.right)
                nodes.append(root.val)
        
        nodes = []
        traverse(root)
        return nodes
        """
    
        """
        # Hacky Solution - Iterative Solution
        if not root:
            return []
        nodes = []
        result = []
        nodes.append(root)
        while len(nodes) > 0:
            current = nodes.pop()
            result.append(current.val)
            if current.left:
                nodes.append(current.left)
            if current.right:
                nodes.append(current.right)

        return result[::-1]
        """
        
        # Proper Iterative
    
        
        
