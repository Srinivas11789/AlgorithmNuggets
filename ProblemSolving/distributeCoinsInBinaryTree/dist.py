# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distributeCoins(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        # Reference from lee215 at https://leetcode.com/problems/distribute-coins-in-binary-tree/discuss/221930/JavaC%2B%2BPython-Recursive-Solution
        
        # DFS method to find the distance to the root from both the left and right subtree 
        
        # Global result
        self.result = 0
        
        # DFS recursive method
        def dfs(node):
            
            # Null node check
            if not node:
                return 0
            
            # Left and Right values
            left = dfs(node.left)
            right = dfs(node.right)
            
            # Add left and right values as we progress to the parent to the result
            self.result += abs(left) + abs(right)
            
            # For each node, return everything except 1 for itself
            return node.val + left + right - 1
        
        # recursive call
        dfs(root)
        
        return self.result
            
        
