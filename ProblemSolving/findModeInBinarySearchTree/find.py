# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        # Using extra space logic
        # * a dictionary with all the values
        self.freq = {}
        
        def traverse(node):
            # Null node handle
            if not node:
                return
            
            if node.val not in self.freq:
                self.freq[node.val] = 1
            else:
                self.freq[node.val] += 1
            
            if node.left:
                traverse(node.left)
            if node.right:
                traverse(node.right)
        
        if not root:
            return []
        
        traverse(root)
        
        result = []
        mode = max(self.freq.values())
        for value, count in self.freq.items():
            if count == mode:
                result.append(value)
        return result
            
        
