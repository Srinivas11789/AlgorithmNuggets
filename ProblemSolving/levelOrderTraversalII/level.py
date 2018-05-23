# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        # Logic 1: Recursive Method
        
        # * Finding Height of the tree
        def height(node):
            if node is None:
                return 0
            else:
                return 1+max(height(node.left),height(node.right))
            
        # * Traversing nodes by each level
        def current_level(node, i, nodes):
            if node is None:
                return 
            if i == 1:
                nodes.append(node.val)
                #print node.val,
            elif i > 1:
                current_level(node.left, i-1, nodes)
                current_level(node.right, i-1, nodes)
            return nodes
        
        # * Traversing nodes by all level
        def all_levels(node):
            h = height(node)
            all_level = []
            for i in range(1,h+1):
                nodes = []
                all_level.append(current_level(node,i,nodes))
            return all_level
        
        return all_levels(root)[::-1]
       
        """
        # Logic 2: Iterative Method
        # * Iterate through the array as we progress through the tree
        if not root:
            return []
        traversal = [[root]]
        for level in traversal:
            nodes = []
            for node in level:
                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)
            if nodes:
                traversal.append(nodes)
        return [[node.val for node in level] for level in traversal][::-1]
        """
        
