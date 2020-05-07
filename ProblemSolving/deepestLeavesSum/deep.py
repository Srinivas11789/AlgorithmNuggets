# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        # Logic 1: 88% faster - 100 pass
        # * Record all the leaves in the tree with their heights in a dictionary
        # * Track the maximum and return their sum
        
        def heightForLeaves(node, height):
            # null check
            if not node:
                return
            # traverse tree
            if node.left:
                heightForLeaves(node.left, height+1)
            if node.right:
                heightForLeaves(node.right, height+1)
            # Check for leaf
            if not node.left and not node.right:
                if height not in self.leaf_heights:
                     self.leaf_heights[height] = []
                self.leaf_heights[height].append(node.val)
                if height > self.max_height:
                    self.max_height = height
        
        self.leaf_heights = {} # height: [leaves]
        self.max_height = 0 # track maximum
        heightForLeaves(root, 0)
        return sum(self.leaf_heights[self.max_height])
        
        # Logic 2: 
        # * BFS
        # * Return the farthest level sum
