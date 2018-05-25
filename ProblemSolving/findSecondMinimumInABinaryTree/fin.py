# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        # A general traversal to retrieve all the nodes
        def traverse(node):
            if not node:
                return None
            else:
                nodes.append(node.val)
                traverse(node.left)
                traverse(node.right)
                
        nodes = []
        traverse(root)
        nodes = list(set(nodes))
        nodes.sort()
        print nodes
        if len(nodes) >= 2:
            return nodes[1]
        else:
            return -1
