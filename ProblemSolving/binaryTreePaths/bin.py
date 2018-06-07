# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """

        def preOrder(node, paths):
            if not node:
                return 
            else:
                if not node.left and not node.right:
                    result.append("->".join(paths+[str(node.val)]))
                if node.left:
                    preOrder(node.left, paths+[str(node.val)])
                if node.right:
                    preOrder(node.right, paths+[str(node.val)])
                
        paths = []
        result = []
        
        if root and not root.left and not root.right:
            return [str(root.val)]
        
        preOrder(root, paths)
        print result

        return result
        
