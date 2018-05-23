# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        
        def average(l):
            return sum(l)/float(len(l))
        
        
        # Iterative Mode 
        if root is None:
            return []
        
        all_nodes = [[root]]
        
        for level in all_nodes:
            nodes = []
            for node in level:
                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)
            if nodes:
                all_nodes.append(nodes)
            
        return [average([node.val for node in level]) for level in all_nodes]

        
        
