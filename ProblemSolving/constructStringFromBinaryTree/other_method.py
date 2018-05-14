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
        
        def preOrder(t):
        
            if not t:
                return ""
            
            result.append(str(t.val))
            
            # when t.left is null and t.right exists
            if t.right and not t.left:
                result.append("()(")
                preOrder(t.right)
                result.append(")")
            else:
                if t.left:
                    result.append("(")
                    preOrder(t.left)
                    result.append(")")
                if t.right:
                    result.append("(")
                    preOrder(t.right)
                    result.append(")")
            
        result = []
        preOrder(t)
        print result
        return "".join(result)
        
