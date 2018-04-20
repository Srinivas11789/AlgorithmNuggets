# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        def pre_order(node):
            print node
            if node and node.val:
                result.append(str(node.val))
                if node.left:
                    result.append("(")
                    pre_order(node.left)
                    result.append(")")
                if node.right:
                    result.append("(")
                    pre_order(node.right)
                    result.append(")")
            else:
                result.append("()")
        
        # Order matters, watch the order of execution while writing a problem
        result = []
        pre_order(t)
        return "".join(result)
        
