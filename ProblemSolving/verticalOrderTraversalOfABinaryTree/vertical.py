# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        self.cols = {}
        self.levels = {}
        
        def traverseByLevel(node, level, r, c):
            
            if not node:
                return
            
            if c not in self.cols:
                self.cols[c] = []
            if c not in self.levels:
                self.levels[c] = []

            if self.levels[c] and self.levels[c][-1] >= level:
                i = len(self.levels[c])-1
                while i >= 0 and self.levels[c][i] > level:
                    i -= 1
                while i >= 0 and self.levels[c][i] == level and self.cols[c][i] > node.val:
                    i -= 1     
                self.levels[c] = self.levels[c][:i+1] + [level] + self.levels[c][i+1:]
                self.cols[c] = self.cols[c][:i+1] + [node.val] + self.cols[c][i+1:]
            else:
                self.cols[c].append(node.val)
                self.levels[c].append(level)
            
            if node.left:
                traverseByLevel(node.left, level+1, r+1, c-1)
            if node.right:
                traverseByLevel(node.right, level+1, r+1, c+1)
                
        
        traverseByLevel(root, 0, 0, 0)
        
        result = []
        for k in sorted(self.cols.keys()):
            result.append(self.cols[k])
        
        return result
