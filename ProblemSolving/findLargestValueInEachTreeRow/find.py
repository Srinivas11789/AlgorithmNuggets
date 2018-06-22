# 100 pass

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        # Breath First Search and Max - Iterative
        
        if not root:
            return []
        
        nodes = [root]
        result = []
        answer = []
        
        while nodes:
            result.append([])
            n = len(nodes)
            while n:
                node = nodes.pop(0)
                result[-1].append(node.val)
                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)
                n -= 1
            if len(result) > 0:
                answer.append(max(result[-1]))
        
        return answer
