# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
        
        # Logic 1: 2*O(N) == O(N) over each of the tree and check if the difference exists
        def traverseToSet(node):
            if not node:
                return
            
            if self.search:
                if target-node.val in self.tree1:
                    self.twoSum = self.twoSum or True
            else:
                self.tree1.add(node.val)
            
            if node.left:
                traverseToSet(node.left)
            if node.right:
                traverseToSet(node.right)
        
        self.tree1 = set()
        self.twoSum = False
        self.search = False
        traverseToSet(root1)
        self.search = True
        traverseToSet(root2)
        return self.twoSum
        
        # Logic 2: Traverse one tree and Search another tree for difference
