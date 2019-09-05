# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        self.levelSums = {}
        self.max = -float('inf')
        self.max_level = 1

        # Depth First Search Logic
        def maxLevelSumUsingDFS(node, height):
            
            # Add height (level) key to a global dictionary
            if height not in self.levelSums:
                self.levelSums[height] = 0

            # Add value to sum of current level
            self.levelSums[height] += node.val

            """
            # Dont do this while it is being cooked
            # Set the maximum once obtained
            if self.levelSums[height] > self.max:
                self.max = self.levelSums[height] 
                self.max_level = height
            elif self.levelSums[height] == self.max: # Minimum height gets max height
                if height < self.max_level:
                    self.max_level = height
            """

            # Recurse or Traverse
            if node.left:
                maxLevelSumUsingDFS(node.left, height+1)
            if node.right:
                maxLevelSumUsingDFS(node.right, height+1)

        maxLevelSumUsingDFS(root, 1)

        # Do this after it is being cooked!
        self.max = max(self.levelSums.values())
        for key in sorted(self.levelSums.keys()):
            if self.levelSums[key] == self.max:
                return key
