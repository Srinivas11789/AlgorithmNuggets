# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        nodes = [root]
        result = []
        
        while 1:
            
            n = len(nodes)
            
            if n == 0:
                break
            
            result.append([])
            
            while n > 0:
                node = nodes.pop(0)
                result[-1].append(node.val)
                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)
                n -= 1
            
            if len(result)%2 == 0:
                result[-1] = result[-1][::-1]

        return result
        
    
 
